from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import hashlib
from datetime import datetime

from app.db.session import get_db
from app.models import User, Course, StudentProfile, CourseEnrollment, ExamGrade, InstitutionConfig
from app.api.deps import get_current_user, require_roles

router = APIRouter(prefix="/enrollment", tags=["AI Course Enrollment & Registration"])

# Level rank mapping for hierarchy comparison
LEVEL_RANK = {
    "100 Level": 100,
    "200 Level": 200,
    "300 Level": 300,
    "400 Level": 400,
    "500 Level": 500,
    "Postgraduate": 600
}

def parse_level_rank(level_str: str) -> int:
    if not level_str:
        return 300
    for key, val in LEVEL_RANK.items():
        if key.lower() in level_str.lower():
            return val
    # Extract digits if any
    digits = "".join([c for c in level_str if c.isdigit()])
    if digits:
        return int(digits)
    return 300

# Schemas
class CourseItemOut(BaseModel):
    id: int
    code: str
    title: str
    creditUnits: int
    level: str
    semester: str
    category: str
    lecturerName: Optional[str] = None
    prerequisiteCode: Optional[str] = None
    prerequisitePassed: bool = True
    description: Optional[str] = None

class CarryoverItemOut(BaseModel):
    id: int
    code: str
    title: str
    creditUnits: int
    level: str
    semester: str
    category: str
    failedSession: str
    failedGrade: str
    failedScore: float
    autoEnrolled: bool = True
    locked: bool = True
    reason: str

class CreditPolicyOut(BaseModel):
    minUnits: int = 15
    maxUnits: int = 24
    carryoverUnits: int = 0
    advisableMaxUnits: int = 21
    underloadAllowedWithWaiver: bool = True
    underloadReasons: List[str] = [
        "Final Year / Graduating Clearance (Completing Remaining Degree Requirements)",
        "Academic Adviser Prescribed Workload Pacing (GPA Recovery & Counseling)",
        "Medical / Compassionate Concession (Senate Certified)",
        "Special Academic Accommodation / Approved Part-Time Load",
        "Senate Special Exemption"
    ]

class AiAdvisoryOut(BaseModel):
    status: str  # MANDATORY_CARRYOVER_ENFORCED | CLEAR_TO_ENROLL
    headline: str
    badgeText: str
    badgeColor: str
    directive: str
    workloadRecommendation: str
    recommendedCourseIds: List[int] = []

class StudentSummaryOut(BaseModel):
    id: int
    name: str
    matricNumber: str
    level: str
    program: str
    faculty: str
    department: str
    cgpa: float
    avatar: Optional[str] = None

class AdviserReviewOut(BaseModel):
    status: str  # DRAFT, PENDING_APPROVAL, APPROVED, DISAPPROVED
    isApproved: bool = False
    isDisapproved: bool = False
    isPending: bool = False
    adviserName: Optional[str] = None
    adviserRemarks: Optional[str] = None
    approvedAt: Optional[str] = None

class EnrollmentAuditResponse(BaseModel):
    student: StudentSummaryOut
    session: str
    semester: str
    hasMandatoryCarryovers: bool
    mandatoryCarryovers: List[CarryoverItemOut]
    availableCourses: List[CourseItemOut]
    currentEnrollments: List[Dict[str, Any]]
    creditPolicy: CreditPolicyOut
    aiAdvisory: AiAdvisoryOut
    registrationStatus: str = "DRAFT"  # DRAFT, PENDING_APPROVAL, APPROVED, DISAPPROVED
    adviserReview: Optional[AdviserReviewOut] = None

class CourseRegistrationRequest(BaseModel):
    session: str = "2026/2027"
    semester: str = "First Semester"
    courseIds: List[int]
    studentId: Optional[int] = None
    underloadReason: Optional[str] = None
    underloadNotes: Optional[str] = None

class AdviserReviewActionRequest(BaseModel):
    studentId: int
    session: str = "2026/2027"
    semester: str = "First Semester"
    remarks: Optional[str] = None

def get_target_student(db: Session, current_user: User, student_id: Optional[int] = None) -> StudentProfile:
    if current_user.role in ["super-admin", "admin", "lecturer"] and student_id:
        student = db.query(StudentProfile).filter_by(id=student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student profile not found")
        return student
    elif current_user.role == "student":
        student = db.query(StudentProfile).filter_by(user_id=current_user.id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student profile not found for authenticated user")
        return student
    elif current_user.role in ["super-admin", "admin", "lecturer"]:
        # Academic staff / level adviser inspecting course audit without explicit studentId:
        # Default to the first student in their department/assigned level, or the first active student
        student = None
        if current_user.department:
            student = db.query(StudentProfile).filter(StudentProfile.department.ilike(f"%{current_user.department}%")).first()
        if not student:
            student = db.query(StudentProfile).first()
        if not student:
            raise HTTPException(status_code=404, detail="No students available in system")
        return student
    else:
        raise HTTPException(status_code=403, detail="Unauthorized to access course enrollment")

def compute_unfulfilled_carryovers(db: Session, student: StudentProfile, target_semester: str = "First Semester"):
    """
    Scans student's historical grades:
    Finds courses with grade 'F' or score < 40 that have not been subsequently cleared with score >= 40.
    Identifies if they belong to previous levels or prior semesters.
    """
    student_rank = parse_level_rank(student.level)

    # All grades for student
    all_grades = db.query(ExamGrade).filter_by(student_id=student.id).all()
    
    # Check course success history
    passed_course_ids = set()
    failed_grade_map = {}

    for g in all_grades:
        if g.total_score >= 40.0 and g.letter_grade != "F":
            passed_course_ids.add(g.course_id)

    for g in all_grades:
        if (g.letter_grade == "F" or g.total_score < 40.0) and g.course_id not in passed_course_ids:
            # Most recent failure for this course
            failed_grade_map[g.course_id] = g

    carryover_items = []
    for course_id, g in failed_grade_map.items():
        course = db.query(Course).filter_by(id=course_id).first()
        if not course:
            continue
        
        course_rank = parse_level_rank(course.level)
        # Check if course matches current semester season (e.g. First Semester courses are retaken in First Semester)
        # and course level is strictly less than current level (or previous year of same level)
        is_previous_level = course_rank < student_rank or g.session != "2026/2027"

        if is_previous_level:
            carryover_items.append({
                "course": course,
                "grade": g,
                "failedSession": g.session,
                "failedGrade": g.letter_grade,
                "failedScore": g.total_score,
                "courseRank": course_rank
            })

    # Sort carryovers by lowest level first (100L before 200L)
    carryover_items.sort(key=lambda x: (x["courseRank"], x["course"].code))
    return carryover_items

@router.get("/audit", response_model=EnrollmentAuditResponse)
def audit_student_enrollment(
    student_id: Optional[int] = None,
    session: str = "2026/2027",
    semester: str = "First Semester",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Audits the student's transcript and enforces Senate regulations:
    Mandatory previous-level failed courses are flagged as auto-enrolled and locked.
    """
    student = get_target_student(db, current_user, student_id)
    student_rank = parse_level_rank(student.level)

    # 1. Detect unfulfilled carryovers
    carryovers_raw = compute_unfulfilled_carryovers(db, student, semester)
    mandatory_carryovers = []
    total_carryover_units = 0

    for item in carryovers_raw:
        c = item["course"]
        g = item["grade"]
        total_carryover_units += c.credit_units
        mandatory_carryovers.append(CarryoverItemOut(
            id=c.id,
            code=c.code,
            title=c.title,
            creditUnits=c.credit_units,
            level=c.level,
            semester=c.semester,
            category="Mandatory Carryover",
            failedSession=item["failedSession"],
            failedGrade=item["failedGrade"],
            failedScore=item["failedScore"],
            autoEnrolled=True,
            locked=True,
            reason=f"Senate Regulation 4.2: Unfulfilled {c.level} requirement must be pre-registered and cleared before current {student.level} courses."
        ))

    has_carryovers = len(mandatory_carryovers) > 0

    # 2. Available current-level courses
    current_courses = db.query(Course).filter(
        Course.level.ilike(f"%{student.level}%"),
        Course.semester.ilike(f"%{semester}%")
    ).all()

    # Pass check for prerequisites
    passed_course_codes = set()
    all_grades = db.query(ExamGrade).filter_by(student_id=student.id).all()
    for gr in all_grades:
        if gr.total_score >= 40.0 and gr.letter_grade != "F":
            if gr.course:
                passed_course_codes.add(gr.course.code)

    available_courses_out = []
    recommended_ids = [c.id for c in mandatory_carryovers]

    for c in current_courses:
        prereq_passed = True
        if c.prerequisite_course_code:
            prereq_passed = c.prerequisite_course_code in passed_course_codes

        lecturer_name = c.lecturer.user.name if c.lecturer and c.lecturer.user else "Faculty Board"

        available_courses_out.append(CourseItemOut(
            id=c.id,
            code=c.code,
            title=c.title,
            creditUnits=c.credit_units,
            level=c.level,
            semester=c.semester,
            category=c.category or ("Core Compulsory" if "core" in (c.category or "").lower() else "Elective"),
            lecturerName=lecturer_name,
            prerequisiteCode=c.prerequisite_course_code,
            prerequisitePassed=prereq_passed,
            description=c.description
        ))

        # Recommend core compulsory courses if prerequisite passed
        if (c.category == "Core Compulsory" or not c.category) and prereq_passed:
            recommended_ids.append(c.id)

    # 3. Existing enrollments for this session & semester
    existing_enrs = db.query(CourseEnrollment).filter_by(
        student_id=student.id,
        session=session,
        semester=semester
    ).all()

    current_enrollments_out = []
    reg_status = "DRAFT"
    adviser_review_out = None

    if existing_enrs:
        first_e = existing_enrs[0]
        st = getattr(first_e, "approval_status", "Pending Approval") or "Pending Approval"
        if "approved" in st.lower() and "dis" not in st.lower():
            reg_status = "APPROVED"
        elif "disapproved" in st.lower() or "reject" in st.lower():
            reg_status = "DISAPPROVED"
        else:
            reg_status = "PENDING_APPROVAL"

        adviser_review_out = AdviserReviewOut(
            status=reg_status,
            isApproved=(reg_status == "APPROVED"),
            isDisapproved=(reg_status == "DISAPPROVED"),
            isPending=(reg_status == "PENDING_APPROVAL"),
            adviserName=getattr(first_e, "adviser_name", None) or "Prof. Alistair Finch",
            adviserRemarks=getattr(first_e, "adviser_remarks", None),
            approvedAt=first_e.approved_at.isoformat() if getattr(first_e, "approved_at", None) else None
        )

        for enr in existing_enrs:
            if enr.course:
                current_enrollments_out.append({
                    "enrollmentId": enr.id,
                    "courseId": enr.course_id,
                    "code": enr.course.code,
                    "title": enr.course.title,
                    "creditUnits": enr.course.credit_units,
                    "level": enr.course.level,
                    "isCarryover": enr.is_carryover,
                    "autoEnrolled": enr.auto_enrolled_by_ai,
                    "registrationType": enr.registration_type,
                    "approvalStatus": getattr(enr, "approval_status", "Pending Approval") or "Pending Approval",
                    "adviserName": getattr(enr, "adviser_name", None),
                    "adviserRemarks": getattr(enr, "adviser_remarks", None),
                    "approvedAt": enr.approved_at.isoformat() if getattr(enr, "approved_at", None) else None,
                    "status": enr.status,
                    "enrolledAt": enr.enrolled_at.isoformat() if enr.enrolled_at else None
                })

    # 4. AI Advisory Synthesis
    cgpa = student.cgpa or 3.0
    if has_carryovers:
        carryover_codes = ", ".join([co.code for co in mandatory_carryovers])
        status = "MANDATORY_CARRYOVER_ENFORCED"
        headline = f"SmartAdvisor AI: {len(mandatory_carryovers)} Mandatory Carryover(s) Enforced"
        badgeText = "Carryover Priority Active"
        badgeColor = "danger"
        directive = (
            f"Regulation 4.2 Directive: Unfulfilled requirements from previous levels ({carryover_codes}) "
            f"have been automatically pre-registered into your semester docket and locked. "
            f"These {total_carryover_units} credit units take precedence. You may now select up to "
            f"{24 - total_carryover_units} additional units from your {student.level} courses."
        )
    else:
        status = "CLEAR_TO_ENROLL"
        headline = "SmartAdvisor AI: Clean Academic Standing"
        badgeText = "Clear to Enroll"
        badgeColor = "success"
        directive = (
            f"Transcript Verified: All previous-level prerequisites and requirements are satisfied. "
            f"You are authorized to register a full curriculum of {student.level} Core and Elective courses (15–24 units)."
        )

    # Workload pacing based on CGPA
    if cgpa >= 3.5:
        workload = f"Distinction Scholar (CGPA {cgpa:.2f}): Recommended load is 21–24 credit units including specialized electives."
    elif cgpa >= 2.5:
        workload = f"Good Academic Standing (CGPA {cgpa:.2f}): Recommended load is 18–21 credit units for balanced academic performance."
    else:
        workload = f"Academic Warning Alert (CGPA {cgpa:.2f} < 2.50): SmartAdvisor AI advises capping registration at 15–18 units to maximize grade recovery."

    ai_advisory = AiAdvisoryOut(
        status=status,
        headline=headline,
        badgeText=badgeText,
        badgeColor=badgeColor,
        directive=directive,
        workloadRecommendation=workload,
        recommendedCourseIds=recommended_ids
    )

    credit_policy = CreditPolicyOut(
        minUnits=15,
        maxUnits=24,
        carryoverUnits=total_carryover_units,
        advisableMaxUnits=24 - total_carryover_units
    )

    student_summary = StudentSummaryOut(
        id=student.id,
        name=student.user.name if student.user else "Enrolled Student",
        matricNumber=student.matric_number,
        level=student.level,
        program=student.program,
        faculty=student.faculty,
        department=student.department,
        cgpa=student.cgpa,
        avatar=student.user.avatar if student.user else None
    )

    return EnrollmentAuditResponse(
        student=student_summary,
        session=session,
        semester=semester,
        hasMandatoryCarryovers=has_carryovers,
        mandatoryCarryovers=mandatory_carryovers,
        availableCourses=available_courses_out,
        currentEnrollments=current_enrollments_out,
        creditPolicy=credit_policy,
        aiAdvisory=ai_advisory,
        registrationStatus=reg_status,
        adviserReview=adviser_review_out
    )

@router.post("/register")
def register_courses(
    payload: CourseRegistrationRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Submits course registration.
    AI RULE: Validates that all mandatory carryover courses are present in payload.courseIds.
    If any carryover is omitted, registration is strictly rejected with HTTP 422.
    """
    student = get_target_student(db, current_user, payload.studentId)
    
    # 1. Audit carryovers
    carryovers_raw = compute_unfulfilled_carryovers(db, student, payload.semester)
    mandatory_carryover_ids = {item["course"].id: item["course"] for item in carryovers_raw}

    # Verify that all mandatory carryovers are included
    missing_carryover_codes = []
    for co_id, co_course in mandatory_carryover_ids.items():
        if co_id not in payload.courseIds:
            missing_carryover_codes.append(f"{co_course.code} ({co_course.title})")

    if missing_carryover_codes:
        raise HTTPException(
            status_code=422,
            detail=(
                f"AI Academic Regulation Violation: You have {len(missing_carryover_codes)} mandatory carryover course(s) "
                f"[{', '.join(missing_carryover_codes)}] from previous levels. Per University Senate Academic Regulations, "
                f"failed previous-level courses MUST be registered first before current-level courses can be enrolled."
            )
        )

    # 2. Fetch all selected course objects
    selected_courses = db.query(Course).filter(Course.id.in_(payload.courseIds)).all()
    if len(selected_courses) != len(payload.courseIds):
        raise HTTPException(status_code=404, detail="One or more selected course IDs do not exist.")

    # 3. Credit Unit Limits Validation
    total_credit_units = sum(c.credit_units for c in selected_courses)
    if total_credit_units > 24:
        raise HTTPException(
            status_code=422,
            detail=f"Credit Limit Exceeded: Total requested credit units ({total_credit_units}) exceeds the Senate ceiling of 24 units."
        )

    is_underload = total_credit_units < 15
    underload_concession_ref = None
    if is_underload:
        if not payload.underloadReason:
            raise HTTPException(
                status_code=422,
                detail=(
                    f"Academic Underload Alert: Total selected load ({total_credit_units} Units) is below the required minimum of 15 units. "
                    f"To proceed with underload registration, an official justification reason "
                    f"(such as Final Year Clearance, Medical Exemption, or Academic Adviser Prescribed Pacing) must be selected."
                )
            )
        # Generate official Senate Underload Concession Reference
        ref_hash = hashlib.sha256(f"{student.matric_number}:{payload.session}:{payload.semester}:UNDERLOAD".encode()).hexdigest()[:6].upper()
        underload_concession_ref = f"AMU/SEN/UND-2026/{ref_hash}"

    # 4. Atomic Registration Persistence
    # Clear existing enrollments for this session and semester to allow updates/replacements
    db.query(CourseEnrollment).filter_by(
        student_id=student.id,
        session=payload.session,
        semester=payload.semester
    ).delete()

    created_enrollments = []
    for c in selected_courses:
        is_carryover = c.id in mandatory_carryover_ids
        auto_enrolled = is_carryover
        reg_type = "Carryover (Auto-Enrolled)" if is_carryover else (c.category or "Core Regular")

        enr = CourseEnrollment(
            student_id=student.id,
            course_id=c.id,
            session=payload.session,
            semester=payload.semester,
            status="Registered",
            is_carryover=is_carryover,
            auto_enrolled_by_ai=auto_enrolled,
            registration_type=reg_type,
            underload_concession=is_underload,
            underload_reason=payload.underloadReason if is_underload else None,
            concession_reference=underload_concession_ref if is_underload else None,
            approval_status="Pending Approval",
            adviser_remarks=None,
            adviser_name=None,
            approved_at=None
        )
        db.add(enr)
        created_enrollments.append(enr)

    db.commit()

    # Generate verification token
    verification_payload = f"{student.matric_number}:{payload.session}:{payload.semester}:{total_credit_units}:{datetime.utcnow().strftime('%Y%m%d%H%M')}"
    verification_hash = hashlib.sha256(verification_payload.encode()).hexdigest()[:16].upper()

    concession_data = None
    if is_underload:
        concession_data = {
            "isUnderload": True,
            "approved": True,
            "concessionReference": underload_concession_ref,
            "reason": payload.underloadReason,
            "notes": payload.underloadNotes,
            "approvedBy": "Senate Committee on Academic Policy & Accreditations"
        }

    return {
        "status": "success",
        "message": f"Successfully enrolled {len(created_enrollments)} courses ({total_credit_units} Credit Units) for {payload.session} - {payload.semester}." + (f" Approved under Senate Underload Concession [{underload_concession_ref}]." if is_underload else "") + " Course form submitted for Level Adviser review.",
        "student": {
            "name": student.user.name if student.user else "Student",
            "matricNumber": student.matric_number,
            "level": student.level
        },
        "totalCreditUnits": total_credit_units,
        "carryoverUnits": sum(c.credit_units for c in selected_courses if c.id in mandatory_carryover_ids),
        "coursesCount": len(created_enrollments),
        "approvalStatus": "Pending Approval",
        "isUnderload": is_underload,
        "underloadConcession": concession_data,
        "verificationHash": verification_hash,
        "enrolledAt": datetime.utcnow().isoformat()
    }

@router.get("/current")
def get_current_enrollments(
    student_id: Optional[int] = None,
    session: str = "2026/2027",
    semester: str = "First Semester",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Retrieve the student's active course enrollments."""
    student = get_target_student(db, current_user, student_id)
    enrollments = db.query(CourseEnrollment).filter_by(
        student_id=student.id,
        session=session,
        semester=semester
    ).all()

    results = []
    total_units = 0
    carryover_count = 0

    for enr in enrollments:
        if enr.course:
            total_units += enr.course.credit_units
            if enr.is_carryover:
                carryover_count += 1
            results.append({
                "enrollmentId": enr.id,
                "courseId": enr.course_id,
                "code": enr.course.code,
                "title": enr.course.title,
                "creditUnits": enr.course.credit_units,
                "level": enr.course.level,
                "category": enr.course.category or "Core",
                "isCarryover": enr.is_carryover,
                "autoEnrolled": enr.auto_enrolled_by_ai,
                "registrationType": enr.registration_type,
                "underloadConcession": getattr(enr, "underload_concession", False),
                "underloadReason": getattr(enr, "underload_reason", None),
                "concessionReference": getattr(enr, "concession_reference", None),
                "lecturer": enr.course.lecturer.user.name if enr.course.lecturer and enr.course.lecturer.user else "Faculty Board",
                "status": enr.status,
                "enrolledAt": enr.enrolled_at.isoformat() if enr.enrolled_at else None
            })

    return {
        "student": {
            "id": student.id,
            "name": student.user.name if student.user else "Student",
            "matricNumber": student.matric_number,
            "level": student.level,
            "program": student.program
        },
        "session": session,
        "semester": semester,
        "totalCreditUnits": total_units,
        "carryoverCount": carryover_count,
        "enrollments": results
    }

@router.get("/slip")
def get_registration_slip(
    student_id: Optional[int] = None,
    session: str = "2026/2027",
    semester: str = "First Semester",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Generates official verifiable course registration slip data."""
    student = get_target_student(db, current_user, student_id)
    inst = db.query(InstitutionConfig).filter_by(config_key="primary").first()

    enrollments = db.query(CourseEnrollment).filter_by(
        student_id=student.id,
        session=session,
        semester=semester
    ).all()

    courses = []
    total_units = 0
    carryover_units = 0
    core_units = 0
    elective_units = 0

    for enr in enrollments:
        if enr.course:
            units = enr.course.credit_units
            total_units += units
            if enr.is_carryover:
                carryover_units += units
            elif "elective" in (enr.course.category or "").lower():
                elective_units += units
            else:
                core_units += units

            courses.append({
                "code": enr.course.code,
                "title": enr.course.title,
                "creditUnits": units,
                "level": enr.course.level,
                "semester": enr.course.semester,
                "category": "Mandatory Carryover" if enr.is_carryover else (enr.course.category or "Core"),
                "isCarryover": enr.is_carryover,
                "lecturer": enr.course.lecturer.user.name if enr.course.lecturer and enr.course.lecturer.user else "Department Faculty Board",
                "status": enr.status
            })

    # Sort so carryovers appear first at the top of the slip
    courses.sort(key=lambda x: (0 if x["isCarryover"] else 1, x["code"]))

    verification_string = f"{student.matric_number}:{session}:{semester}:{total_units}"
    token = hashlib.sha256(verification_string.encode()).hexdigest()[:18].upper()

    has_underload = any(getattr(enr, "underload_concession", False) for enr in enrollments) or (total_units < 15 and len(enrollments) > 0)
    concession_data = None
    if has_underload:
        first_with_reason = next((enr for enr in enrollments if getattr(enr, "underload_reason", None)), None)
        reason = first_with_reason.underload_reason if first_with_reason and first_with_reason.underload_reason else "Final Year Clearance / Senate Approved Pacing"
        ref = (first_with_reason.concession_reference if first_with_reason and getattr(first_with_reason, "concession_reference", None) 
               else f"AMU/SEN/UND-2026/{token[:6]}")
        concession_data = {
            "isUnderload": True,
            "approved": True,
            "concessionReference": ref,
            "reason": reason,
            "approvedBy": "Senate Committee on Academic Policy & Accreditations",
            "regulatoryNotice": "Holder of this slip is authorized to undertake a reduced course load per Academic Regulation 4.6. Valid for examination clearance and degree certification."
        }

    # Level Adviser Approval Details
    first_enr = enrollments[0] if enrollments else None
    adviser_st = getattr(first_enr, "approval_status", "Pending Approval") if first_enr else "Pending Approval"
    adviser_name = getattr(first_enr, "adviser_name", None) or "Prof. Alistair Finch"
    adviser_remarks = getattr(first_enr, "adviser_remarks", None)
    approved_at_dt = getattr(first_enr, "approved_at", None)

    is_approved = bool(adviser_st and "approved" in adviser_st.lower() and "dis" not in adviser_st.lower())
    is_disapproved = bool(adviser_st and ("disapproved" in adviser_st.lower() or "reject" in adviser_st.lower()))
    is_pending = not is_approved and not is_disapproved

    adviser_approval_data = {
        "status": "Approved" if is_approved else ("Disapproved" if is_disapproved else "Pending Approval"),
        "isApproved": is_approved,
        "isDisapproved": is_disapproved,
        "isPending": is_pending,
        "adviserName": adviser_name,
        "adviserTitle": f"{student.level} Academic Course Adviser",
        "adviserRemarks": adviser_remarks,
        "approvedAt": approved_at_dt.strftime("%B %d, %Y - %H:%M UTC") if approved_at_dt else None
    }

    return {
        "institution": {
            "name": inst.institution_name if inst else "Apex Metropolitan University",
            "shortCode": inst.short_code if inst else "AMU",
            "crestUrl": inst.crest_url if inst else "/assets/images/logo-icon.png",
            "motto": getattr(inst, "motto", "Excellence, Integrity & Innovation"),
            "academicSession": session,
            "semester": semester
        },
        "student": {
            "name": student.user.name if student.user else "Sophia Chen",
            "matricNumber": student.matric_number,
            "level": student.level,
            "program": student.program,
            "faculty": student.faculty,
            "department": student.department,
            "cgpa": student.cgpa,
            "avatar": student.user.avatar if student.user else None
        },
        "summary": {
            "totalCourses": len(courses),
            "totalCreditUnits": total_units,
            "carryoverUnits": carryover_units,
            "coreUnits": core_units,
            "electiveUnits": elective_units,
            "maxAllowedUnits": 24,
            "minAllowedUnits": 15,
            "isUnderload": has_underload,
            "approvalStatus": adviser_approval_data["status"]
        },
        "underloadConcession": concession_data,
        "adviserApproval": adviser_approval_data,
        "courses": courses,
        "verificationToken": token,
        "generatedAt": datetime.utcnow().strftime("%B %d, %Y - %H:%M UTC")
    }

@router.delete("/drop/{course_id}")
def drop_course(
    course_id: int,
    student_id: Optional[int] = None,
    session: str = "2026/2027",
    semester: str = "First Semester",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Drops an enrolled elective or regular course.
    AI RULE: Strictly blocks dropping any mandatory carryover course!
    """
    student = get_target_student(db, current_user, student_id)
    
    enr = db.query(CourseEnrollment).filter_by(
        student_id=student.id,
        course_id=course_id,
        session=session,
        semester=semester
    ).first()

    if not enr:
        raise HTTPException(status_code=404, detail="Enrollment record not found for this course.")

    # Strictly protect mandatory carryovers
    if enr.is_carryover:
        course_code = enr.course.code if enr.course else f"Course #{course_id}"
        raise HTTPException(
            status_code=422,
            detail=(
                f"Senate Regulation Lock: Cannot drop mandatory carryover course [{course_code}]. "
                f"Academic regulations mandate that unfulfilled previous-level courses cannot be dropped until cleared and passed."
            )
        )

    course_title = enr.course.title if enr.course else "Course"
    db.delete(enr)
    db.commit()

    return {
        "status": "success",
        "message": f"Successfully dropped {course_title} from your {session} enrollment docket."
    }

@router.post("/reset")
def reset_enrollment_docket(
    session: str = "2026/2027",
    semester: str = "First Semester",
    student_id: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Resets the student's active semester registration:
    Clears fresh course enrollments while strictly preserving and locking mandatory carryovers!
    """
    student = get_target_student(db, current_user, student_id)
    
    # Clear current session enrollments
    db.query(CourseEnrollment).filter_by(
        student_id=student.id,
        session=session,
        semester=semester
    ).delete()

    # Automatically re-lock mandatory carryovers
    carryovers_raw = compute_unfulfilled_carryovers(db, student, semester)
    created_carryovers = []
    for item in carryovers_raw:
        c = item["course"]
        enr = CourseEnrollment(
            student_id=student.id,
            course_id=c.id,
            session=session,
            semester=semester,
            status="Registered",
            is_carryover=True,
            auto_enrolled_by_ai=True,
            registration_type="Carryover (Auto-Enrolled)"
        )
        db.add(enr)
        created_carryovers.append(c.code)
    db.commit()

    return {
        "status": "success",
        "message": f"Docket reset. {len(created_carryovers)} mandatory carryover(s) [{', '.join(created_carryovers)}] preserved. You can now add fresh courses.",
        "carryoversPreserved": created_carryovers
    }

@router.get("/all-courses")
def get_all_accredited_courses(
    level: Optional[str] = None,
    department: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """List all accredited university courses with category, units, level, and prerequisites."""
    query = db.query(Course)
    if level and level != "All Levels":
        query = query.filter(Course.level.ilike(f"%{level}%"))
    if department and department != "All Departments":
        query = query.filter(Course.department.ilike(f"%{department}%"))
    if search:
        s = f"%{search.strip()}%"
        query = query.filter(or_(Course.code.ilike(s), Course.title.ilike(s), Course.description.ilike(s)))
    
    courses = query.all()
    results = []
    for c in courses:
        results.append({
            "id": c.id,
            "code": c.code,
            "title": c.title,
            "creditUnits": c.credit_units,
            "level": c.level,
            "semester": c.semester,
            "department": c.department,
            "category": c.category or "Core Compulsory",
            "prerequisiteCode": c.prerequisite_course_code,
            "lecturerName": c.lecturer.user.name if c.lecturer and c.lecturer.user else "Faculty Board",
            "description": c.description
        })
    return results

# =====================================================================
# LEVEL ADVISER COURSE REGISTRATION APPROVAL & REVIEW ENDPOINTS
# =====================================================================

@router.get("/adviser/submissions")
def get_adviser_submissions(
    session: str = "2026/2027",
    semester: str = "First Semester",
    level: Optional[str] = "All Levels",
    status: Optional[str] = "All",
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Returns all student course registration submissions for Level Adviser review.
    Guarded for lecturers, faculty advisers, and academic administrators.
    """
    if current_user.role not in ["lecturer", "admin", "super-admin"]:
        raise HTTPException(status_code=403, detail="Unauthorized: Level Adviser role required.")

    query = db.query(StudentProfile).join(CourseEnrollment, CourseEnrollment.student_id == StudentProfile.id)\
        .filter(CourseEnrollment.session == session, CourseEnrollment.semester == semester)\
        .distinct()

    if level and level != "All Levels":
        query = query.filter(StudentProfile.level.ilike(f"%{level}%"))

    if search and search.strip():
        search_term = f"%{search.strip()}%"
        query = query.join(User, StudentProfile.user_id == User.id)\
            .filter(or_(
                StudentProfile.matric_number.ilike(search_term),
                User.name.ilike(search_term)
            ))

    students = query.all()
    submissions = []

    pending_count = 0
    approved_count = 0
    disapproved_count = 0

    for s in students:
        s_enrs = db.query(CourseEnrollment).filter_by(
            student_id=s.id,
            session=session,
            semester=semester
        ).all()
        if not s_enrs:
            continue

        total_units = sum(e.course.credit_units for e in s_enrs if e.course)
        carryover_units = sum(e.course.credit_units for e in s_enrs if e.course and e.is_carryover)
        has_carryovers = any(e.is_carryover for e in s_enrs)
        is_underload = any(getattr(e, "underload_concession", False) for e in s_enrs) or (total_units < 15)

        first_e = s_enrs[0]
        st = getattr(first_e, "approval_status", "Pending Approval") or "Pending Approval"
        if "approved" in st.lower() and "dis" not in st.lower():
            norm_status = "Approved"
            approved_count += 1
        elif "disapproved" in st.lower() or "reject" in st.lower():
            norm_status = "Disapproved"
            disapproved_count += 1
        else:
            norm_status = "Pending Approval"
            pending_count += 1

        # Status filter
        if status and status != "All":
            if status.lower() == "pending" and norm_status != "Pending Approval":
                continue
            elif status.lower() == "approved" and norm_status != "Approved":
                continue
            elif status.lower() in ["disapproved", "rejected"] and norm_status != "Disapproved":
                continue

        submissions.append({
            "studentId": s.id,
            "name": s.user.name if s.user else "Student",
            "matricNumber": s.matric_number,
            "level": s.level,
            "program": s.program,
            "department": s.department,
            "faculty": s.faculty,
            "cgpa": s.cgpa or 0.0,
            "avatar": s.user.avatar if s.user else None,
            "totalCreditUnits": total_units,
            "carryoverUnits": carryover_units,
            "hasCarryovers": has_carryovers,
            "coursesCount": len(s_enrs),
            "isUnderload": is_underload,
            "underloadReason": getattr(first_e, "underload_reason", None),
            "concessionReference": getattr(first_e, "concession_reference", None),
            "approvalStatus": norm_status,
            "adviserName": getattr(first_e, "adviser_name", None),
            "adviserRemarks": getattr(first_e, "adviser_remarks", None),
            "approvedAt": first_e.approved_at.isoformat() if getattr(first_e, "approved_at", None) else None,
            "enrolledAt": first_e.enrolled_at.isoformat() if first_e.enrolled_at else None
        })

    # Sort: Pending Approval first, then Disapproved, then Approved
    status_order = {"Pending Approval": 0, "Disapproved": 1, "Approved": 2}
    submissions.sort(key=lambda x: (status_order.get(x["approvalStatus"], 9), x["name"]))

    return {
        "session": session,
        "semester": semester,
        "summary": {
            "totalSubmissions": len(submissions),
            "pendingCount": pending_count,
            "approvedCount": approved_count,
            "disapprovedCount": disapproved_count
        },
        "submissions": submissions
    }

@router.get("/adviser/submission/{student_id}")
def get_adviser_submission_detail(
    student_id: int,
    session: str = "2026/2027",
    semester: str = "First Semester",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Returns complete student docket breakdown for deep Level Adviser evaluation.
    """
    if current_user.role not in ["lecturer", "admin", "super-admin"]:
        raise HTTPException(status_code=403, detail="Unauthorized: Level Adviser role required.")

    student = db.query(StudentProfile).filter_by(id=student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student profile not found")

    enrollments = db.query(CourseEnrollment).filter_by(
        student_id=student.id,
        session=session,
        semester=semester
    ).all()

    if not enrollments:
        raise HTTPException(status_code=404, detail="No active course registration found for this student.")

    # Audit carryovers
    carryovers_raw = compute_unfulfilled_carryovers(db, student, semester)
    mandatory_carryover_ids = {item["course"].id for item in carryovers_raw}

    courses = []
    total_units = 0
    carryover_units = 0

    for enr in enrollments:
        if enr.course:
            u = enr.course.credit_units
            total_units += u
            if enr.is_carryover:
                carryover_units += u
            courses.append({
                "enrollmentId": enr.id,
                "courseId": enr.course.id,
                "code": enr.course.code,
                "title": enr.course.title,
                "creditUnits": u,
                "level": enr.course.level,
                "category": enr.course.category or "Core",
                "isCarryover": enr.is_carryover,
                "registrationType": enr.registration_type,
                "lecturer": enr.course.lecturer.user.name if enr.course.lecturer and enr.course.lecturer.user else "Faculty Board"
            })

    courses.sort(key=lambda x: (0 if x["isCarryover"] else 1, x["code"]))

    first_enr = enrollments[0]
    st = getattr(first_enr, "approval_status", "Pending Approval") or "Pending Approval"
    if "approved" in st.lower() and "dis" not in st.lower():
        norm_status = "Approved"
    elif "disapproved" in st.lower() or "reject" in st.lower():
        norm_status = "Disapproved"
    else:
        norm_status = "Pending Approval"

    is_underload = any(getattr(e, "underload_concession", False) for e in enrollments) or (total_units < 15)

    return {
        "student": {
            "id": student.id,
            "name": student.user.name if student.user else "Student",
            "matricNumber": student.matric_number,
            "level": student.level,
            "program": student.program,
            "department": student.department,
            "faculty": student.faculty,
            "cgpa": student.cgpa,
            "avatar": student.user.avatar if student.user else None
        },
        "session": session,
        "semester": semester,
        "totalCreditUnits": total_units,
        "carryoverUnits": carryover_units,
        "coursesCount": len(courses),
        "isUnderload": is_underload,
        "underloadReason": getattr(first_enr, "underload_reason", None),
        "concessionReference": getattr(first_enr, "concession_reference", None),
        "approvalStatus": norm_status,
        "adviserName": getattr(first_enr, "adviser_name", None),
        "adviserRemarks": getattr(first_enr, "adviser_remarks", None),
        "approvedAt": first_enr.approved_at.isoformat() if getattr(first_enr, "approved_at", None) else None,
        "enrolledAt": first_enr.enrolled_at.isoformat() if first_enr.enrolled_at else None,
        "courses": courses,
        "mandatoryCarryoversPending": len(mandatory_carryover_ids - {c["courseId"] for c in courses if c["isCarryover"]})
    }

@router.post("/adviser/approve")
def approve_student_registration(
    payload: AdviserReviewActionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Approves a student's semester course registration docket.
    Signs registration with the Level Adviser's name and official timestamp.
    """
    if current_user.role not in ["lecturer", "admin", "super-admin"]:
        raise HTTPException(status_code=403, detail="Unauthorized: Level Adviser role required.")

    enrollments = db.query(CourseEnrollment).filter_by(
        student_id=payload.studentId,
        session=payload.session,
        semester=payload.semester
    ).all()

    if not enrollments:
        raise HTTPException(status_code=404, detail="No course enrollments found for this student in the specified session/semester.")

    adviser_name = current_user.name or "Prof. Alistair Finch"
    now = datetime.utcnow()
    remarks = payload.remarks or f"Approved and endorsed by Level Adviser {adviser_name}."

    for enr in enrollments:
        enr.approval_status = "Approved"
        enr.adviser_name = adviser_name
        enr.adviser_remarks = remarks
        enr.approved_at = now

    db.commit()

    student = db.query(StudentProfile).filter_by(id=payload.studentId).first()
    student_name = student.user.name if student and student.user else f"Student #{payload.studentId}"

    return {
        "status": "success",
        "message": f"Successfully approved and signed course registration for {student_name}.",
        "studentId": payload.studentId,
        "approvalStatus": "Approved",
        "adviserName": adviser_name,
        "adviserRemarks": remarks,
        "approvedAt": now.isoformat()
    }

@router.post("/adviser/reject")
def disapprove_student_registration(
    payload: AdviserReviewActionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Disapproves a student's course registration docket and sends it back for revision.
    Requires corrective remarks so the student knows what to change.
    """
    if current_user.role not in ["lecturer", "admin", "super-admin"]:
        raise HTTPException(status_code=403, detail="Unauthorized: Level Adviser role required.")

    if not payload.remarks or not payload.remarks.strip():
        raise HTTPException(
            status_code=422,
            detail="Disapproval feedback is required: Please specify the corrective adjustments needed by the student."
        )

    enrollments = db.query(CourseEnrollment).filter_by(
        student_id=payload.studentId,
        session=payload.session,
        semester=payload.semester
    ).all()

    if not enrollments:
        raise HTTPException(status_code=404, detail="No course enrollments found for this student in the specified session/semester.")

    adviser_name = current_user.name or "Prof. Alistair Finch"
    now = datetime.utcnow()

    for enr in enrollments:
        enr.approval_status = "Disapproved"
        enr.adviser_name = adviser_name
        enr.adviser_remarks = payload.remarks.strip()
        enr.approved_at = None

    db.commit()

    student = db.query(StudentProfile).filter_by(id=payload.studentId).first()
    student_name = student.user.name if student and student.user else f"Student #{payload.studentId}"

    return {
        "status": "success",
        "message": f"Course registration for {student_name} has been marked as Disapproved. The student has been notified to make required adjustments.",
        "studentId": payload.studentId,
        "approvalStatus": "Disapproved",
        "adviserName": adviser_name,
        "adviserRemarks": payload.remarks.strip(),
        "reviewedAt": now.isoformat()
    }
