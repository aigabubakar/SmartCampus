from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional

from app.db.session import get_db
from app.models import User, Course, LecturerProfile, StudentProfile, CourseEnrollment, AttendanceRecord, ExamGrade
from app.api.deps import require_roles

router = APIRouter(prefix="/courses", tags=["Academic Courses & Examination"])

class CourseOut(BaseModel):
    id: int
    code: str
    title: str
    creditUnits: int
    level: str
    semester: str
    department: str
    lecturerName: Optional[str] = None
    lecturerStaffId: Optional[str] = None
    enrolledStudentsCount: int = 0
    description: Optional[str] = None

    class Config:
        from_attributes = True

class AttendanceBatchItem(BaseModel):
    studentId: int
    status: str = "present"  # present, absent, late, excused
    notes: Optional[str] = None

class AttendanceBatchRequest(BaseModel):
    lectureDate: str  # YYYY-MM-DD
    lecturerId: Optional[int] = None
    records: List[AttendanceBatchItem]

class GradeSubmissionItem(BaseModel):
    studentId: int
    caScore: float    # Max 30
    examScore: float  # Max 70

class GradeSubmissionRequest(BaseModel):
    session: str = "2026/2027"
    semester: str = "First Semester"
    grades: List[GradeSubmissionItem]

def compute_grade(total: float):
    if total >= 70:
        return "A", 5.0
    elif total >= 60:
        return "B", 4.0
    elif total >= 50:
        return "C", 3.0
    elif total >= 45:
        return "D", 2.0
    elif total >= 40:
        return "E", 1.0
    else:
        return "F", 0.0

@router.get("", response_model=List[CourseOut])
def list_courses(level: Optional[str] = None, department: Optional[str] = None, db: Session = Depends(get_db)):
    """Retrieve accredited courses with lecturer details and student counts."""
    query = db.query(Course)
    if level:
        query = query.filter(Course.level.ilike(f"%{level}%"))
    if department:
        query = query.filter(Course.department.ilike(f"%{department}%"))

    courses = query.all()
    results = []
    for c in courses:
        results.append(CourseOut(
            id=c.id,
            code=c.code,
            title=c.title,
            creditUnits=c.credit_units,
            level=c.level,
            semester=c.semester,
            department=c.department,
            lecturerName=c.lecturer.user.name if c.lecturer else "Unassigned",
            lecturerStaffId=c.lecturer.staff_id if c.lecturer else None,
            enrolledStudentsCount=len(c.enrollments),
            description=c.description
        ))
    return results

@router.post("/{course_id}/attendance")
def record_batch_attendance(
    course_id: int,
    payload: AttendanceBatchRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["super-admin", "admin", "lecturer"]))
):
    """Record lecture attendance for a course cohort."""
    course = db.query(Course).filter_by(id=course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    created_records = []
    for item in payload.records:
        rec = AttendanceRecord(
            course_id=course_id,
            student_id=item.studentId,
            lecturer_id=payload.lecturerId or course.lecturer_id,
            lecture_date=payload.lectureDate,
            status=item.status,
            notes=item.notes
        )
        db.add(rec)
        created_records.append(rec)
    
    db.commit()
    return {
        "status": "success",
        "message": f"Successfully logged {len(created_records)} attendance records for {course.code} on {payload.lectureDate}"
    }

@router.post("/{course_id}/grades")
def submit_course_grades(
    course_id: int,
    payload: GradeSubmissionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["super-admin", "admin", "lecturer"]))
):
    """Submit Continuous Assessment & Examination scores for students in a course."""
    course = db.query(Course).filter_by(id=course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    updated_count = 0
    for item in payload.grades:
        total = round(item.caScore + item.examScore, 2)
        letter, point = compute_grade(total)

        grade_rec = db.query(ExamGrade).filter_by(
            course_id=course_id,
            student_id=item.studentId,
            session=payload.session,
            semester=payload.semester
        ).first()

        if grade_rec:
            grade_rec.ca_score = item.caScore
            grade_rec.exam_score = item.examScore
            grade_rec.total_score = total
            grade_rec.letter_grade = letter
            grade_rec.grade_point = point
        else:
            grade_rec = ExamGrade(
                course_id=course_id,
                student_id=item.studentId,
                session=payload.session,
                semester=payload.semester,
                ca_score=item.caScore,
                exam_score=item.examScore,
                total_score=total,
                letter_grade=letter,
                grade_point=point,
                approved_by_senate=False
            )
            db.add(grade_rec)
        updated_count += 1

    db.commit()
    return {
        "status": "success",
        "message": f"Submitted grades for {updated_count} students in {course.code} ({payload.session} - {payload.semester})"
    }
