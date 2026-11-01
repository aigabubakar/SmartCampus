from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File
from sqlalchemy import or_
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional, Any
from pathlib import Path
import base64
import uuid
import re

from app.db.session import get_db
from app.models import User, StudentProfile, CourseEnrollment, ExamGrade, AttendanceRecord
from app.core.security import get_password_hash
from app.api.deps import get_current_user, require_roles

router = APIRouter(prefix="/students", tags=["Student Academic Dossiers"])

def get_avatar_upload_directories() -> List[Path]:
    """Returns canonical directories where avatars must be written (both project public and backend public)."""
    dirs = []
    # 1. Project root public directory (where Vite serves assets)
    cur = Path(__file__).resolve()
    for parent in cur.parents:
        if (parent / "package.json").is_file():
            main_pub = parent / "public" / "uploads" / "avatars"
            main_pub.mkdir(parents=True, exist_ok=True)
            dirs.append(main_pub)
            break

    # 2. Backend public directory as backup/fallback
    backend_pub = Path(__file__).resolve().parent.parent.parent.parent / "public" / "uploads" / "avatars"
    backend_pub.mkdir(parents=True, exist_ok=True)
    if backend_pub not in dirs:
        dirs.append(backend_pub)

    return dirs

def save_avatar_image(avatar_str: str, user_id: str) -> str:
    """If avatar_str is a base64 data URL, decodes and saves it to public/uploads/avatars."""
    if not avatar_str or not avatar_str.startswith("data:image/"):
        return avatar_str

    try:
        match = re.match(r"^data:image/([a-zA-Z0-9\+]+);base64,(.+)$", avatar_str)
        if not match:
            return avatar_str

        ext = match.group(1).lower()
        if ext in ["jpeg", "jpg"]:
            ext = "jpg"
        elif ext == "png":
            ext = "png"
        elif ext == "webp":
            ext = "webp"
        else:
            ext = "jpg"

        b64_data = match.group(2)
        raw_bytes = base64.b64decode(b64_data)

        clean_user = re.sub(r"[^a-zA-Z0-9_-]", "_", user_id)
        filename = f"avatar_{clean_user}_{uuid.uuid4().hex[:8]}.{ext}"

        # Write to all target upload directories so both Vite and FastAPI serve it without 404
        for target_dir in get_avatar_upload_directories():
            target_path = target_dir / filename
            with open(target_path, "wb") as f:
                f.write(raw_bytes)

        return f"/uploads/avatars/{filename}"
    except Exception as e:
        print(f"[SmartCampus API] Error saving base64 avatar: {e}")
        return avatar_str

class StudentOut(BaseModel):
    id: int
    userId: str
    name: str
    email: str
    matricNumber: str
    level: str
    program: str
    faculty: str
    department: str
    cgpa: float
    admissionYear: str
    status: str
    avatar: Optional[str] = None
    guardianName: Optional[str] = None
    guardianPhone: Optional[str] = None
    guardianEmail: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    dateOfBirth: Optional[str] = None
    gender: Optional[str] = None
    bloodGroup: Optional[str] = None
    emergencyContact: Optional[str] = None
    hallOfResidence: Optional[str] = None
    bio: Optional[str] = None

    class Config:
        from_attributes = True

class StudentDossier(StudentOut):
    registeredCourses: List[dict] = []
    grades: List[dict] = []
    attendanceStats: dict = {}

class StudentCreateRequest(BaseModel):
    name: str
    email: str
    matricNumber: str
    level: str = "100 Level"
    program: str = "B.Sc Computer Science"
    faculty: str = "Faculty of Computing & Information Technology"
    department: str = "Department of Computer Science & AI"
    admissionYear: str = "2026"
    guardianName: Optional[str] = None
    guardianPhone: Optional[str] = None
    guardianEmail: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = "CampusPass@2026"

class StudentUpdateRequest(BaseModel):
    name: Optional[str] = None
    avatar: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    guardianName: Optional[str] = None
    guardianPhone: Optional[str] = None
    guardianEmail: Optional[str] = None
    dateOfBirth: Optional[str] = None
    gender: Optional[str] = None
    bloodGroup: Optional[str] = None
    emergencyContact: Optional[str] = None
    hallOfResidence: Optional[str] = None
    bio: Optional[str] = None
    # Institutional attributes (Administrators only):
    level: Optional[str] = None
    program: Optional[str] = None
    faculty: Optional[str] = None
    department: Optional[str] = None
    status: Optional[str] = None

def assemble_student_dossier(s: StudentProfile) -> StudentDossier:
    courses = []
    for enr in s.enrollments:
        c = enr.course
        courses.append({
            "code": c.code,
            "title": c.title,
            "units": c.credit_units,
            "semester": c.semester,
            "lecturer": c.lecturer.user.name if c.lecturer and c.lecturer.user else "Unassigned",
        })

    grades = []
    for g in s.grades:
        grades.append({
            "courseCode": g.course.code,
            "courseTitle": g.course.title,
            "caScore": g.ca_score,
            "examScore": g.exam_score,
            "totalScore": g.total_score,
            "letterGrade": g.letter_grade,
            "gradePoint": g.grade_point,
            "senateApproved": g.approved_by_senate
        })

    total_att = len(s.attendance_records)
    present_att = len([a for a in s.attendance_records if a.status == "present"])
    att_percent = round((present_att / total_att * 100), 1) if total_att > 0 else 100.0

    return StudentDossier(
        id=s.id,
        userId=s.user.id,
        name=s.user.name,
        email=s.user.email,
        matricNumber=s.matric_number,
        level=s.level,
        program=s.program,
        faculty=s.faculty,
        department=s.department,
        cgpa=s.cgpa,
        admissionYear=s.admission_year,
        status=s.status,
        avatar=s.user.avatar,
        guardianName=s.guardian_name,
        guardianPhone=s.guardian_phone,
        guardianEmail=getattr(s, "guardian_email", None),
        phone=getattr(s, "phone", None),
        address=getattr(s, "address", None),
        dateOfBirth=getattr(s, "date_of_birth", None),
        gender=getattr(s, "gender", None),
        bloodGroup=getattr(s, "blood_group", None),
        emergencyContact=getattr(s, "emergency_contact", None),
        hallOfResidence=getattr(s, "hall_of_residence", None),
        bio=getattr(s, "bio", None),
        registeredCourses=courses,
        grades=grades,
        attendanceStats={
            "totalLectures": total_att,
            "attended": present_att,
            "percentage": att_percent,
            "status": "Good Standing" if att_percent >= 75.0 else "Attendance Warning"
        }
    )

def find_student_profile(identifier: str, db: Session) -> Optional[StudentProfile]:
    s = None
    if identifier.isdigit():
        s = db.query(StudentProfile).filter_by(id=int(identifier)).first()
    if not s:
        s = db.query(StudentProfile).filter_by(user_id=identifier).first()
    if not s:
        s = db.query(StudentProfile).filter_by(matric_number=identifier).first()
    return s

@router.get("", response_model=List[StudentOut])
def list_students(
    level: Optional[str] = None,
    department: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Retrieve enrolled students from database."""
    query = db.query(StudentProfile)
    if level:
        query = query.filter(StudentProfile.level.ilike(f"%{level}%"))
    if department:
        query = query.filter(StudentProfile.department.ilike(f"%{department}%"))
    if search:
        query = query.join(User).filter(
            or_(
                User.name.ilike(f"%{search}%"),
                User.email.ilike(f"%{search}%"),
                StudentProfile.matric_number.ilike(f"%{search}%")
            )
        )
    
    students = query.all()
    results = []
    for s in students:
        results.append(StudentOut(
            id=s.id,
            userId=s.user.id,
            name=s.user.name,
            email=s.user.email,
            matricNumber=s.matric_number,
            level=s.level,
            program=s.program,
            faculty=s.faculty,
            department=s.department,
            cgpa=s.cgpa,
            admissionYear=s.admission_year,
            status=s.status,
            avatar=s.user.avatar,
            guardianName=s.guardian_name,
            guardianPhone=s.guardian_phone,
            guardianEmail=getattr(s, "guardian_email", None),
            phone=getattr(s, "phone", None),
            address=getattr(s, "address", None),
            dateOfBirth=getattr(s, "date_of_birth", None),
            gender=getattr(s, "gender", None),
            bloodGroup=getattr(s, "blood_group", None),
            emergencyContact=getattr(s, "emergency_contact", None),
            hallOfResidence=getattr(s, "hall_of_residence", None),
            bio=getattr(s, "bio", None),
        ))
    return results

@router.get("/me", response_model=StudentDossier)
def get_my_student_dossier(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Retrieve authenticated student's academic dossier."""
    if not current_user.student_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Authenticated stakeholder does not possess a student profile dossier."
        )
    return assemble_student_dossier(current_user.student_profile)

@router.put("/me", response_model=StudentDossier)
def update_my_student_profile(
    payload: StudentUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update authenticated student's own personal and contact profile."""
    if not current_user.student_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Authenticated stakeholder does not possess a student profile dossier."
        )
    
    s = current_user.student_profile
    user = current_user

    # Update User attributes
    if payload.name is not None and payload.name.strip():
        user.name = payload.name.strip()
    if payload.avatar is not None and payload.avatar.strip():
        user.avatar = save_avatar_image(payload.avatar.strip(), user.id)

    # Update Student Profile attributes
    if payload.phone is not None:
        s.phone = payload.phone.strip()
    if payload.address is not None:
        s.address = payload.address.strip()
    if payload.guardianName is not None:
        s.guardian_name = payload.guardianName.strip()
    if payload.guardianPhone is not None:
        s.guardian_phone = payload.guardianPhone.strip()
    if payload.guardianEmail is not None:
        s.guardian_email = payload.guardianEmail.strip()
    if payload.dateOfBirth is not None:
        s.date_of_birth = payload.dateOfBirth.strip()
    if payload.gender is not None:
        s.gender = payload.gender.strip()
    if payload.bloodGroup is not None:
        s.blood_group = payload.bloodGroup.strip()
    if payload.emergencyContact is not None:
        s.emergency_contact = payload.emergencyContact.strip()
    if payload.hallOfResidence is not None:
        s.hall_of_residence = payload.hallOfResidence.strip()
    if payload.bio is not None:
        s.bio = payload.bio.strip()

    db.commit()
    db.refresh(s)
    db.refresh(user)

    return assemble_student_dossier(s)

@router.get("/{identifier:path}", response_model=StudentDossier)
def get_student_dossier(identifier: str, db: Session = Depends(get_db)):
    """Retrieve complete academic dossier for a student by ID, User ID, or Matric Number."""
    s = find_student_profile(identifier, db)
    if not s:
        raise HTTPException(status_code=404, detail="Student academic dossier not found.")

    return assemble_student_dossier(s)

@router.put("/{identifier:path}", response_model=StudentDossier)
def update_student_profile(
    identifier: str,
    payload: StudentUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update a student's profile.
    - Students may only update their own record and personal/contact fields.
    - Administrators have authority to update institutional fields (status, program, level, faculty).
    """
    if identifier.lower() == "me":
        if not current_user.student_profile:
            raise HTTPException(status_code=404, detail="Student profile not found.")
        s = current_user.student_profile
    else:
        s = find_student_profile(identifier, db)

    if not s:
        raise HTTPException(status_code=404, detail=f"Student record '{identifier}' not found.")

    is_self = (current_user.id == s.user_id) or (
        current_user.student_profile and current_user.student_profile.matric_number == s.matric_number
    )
    is_admin = current_user.role in ["super-admin", "admin"]

    if not is_self and not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access Denied: You do not possess clearance to modify another student's academic dossier."
        )

    # Update User model attributes
    if payload.name is not None and payload.name.strip():
        s.user.name = payload.name.strip()
    if payload.avatar is not None and payload.avatar.strip():
        s.user.avatar = save_avatar_image(payload.avatar.strip(), s.user.id)

    # Update personal/contact profile attributes
    if payload.phone is not None:
        s.phone = payload.phone.strip()
    if payload.address is not None:
        s.address = payload.address.strip()
    if payload.guardianName is not None:
        s.guardian_name = payload.guardianName.strip()
    if payload.guardianPhone is not None:
        s.guardian_phone = payload.guardianPhone.strip()
    if payload.guardianEmail is not None:
        s.guardian_email = payload.guardianEmail.strip()
    if payload.dateOfBirth is not None:
        s.date_of_birth = payload.dateOfBirth.strip()
    if payload.gender is not None:
        s.gender = payload.gender.strip()
    if payload.bloodGroup is not None:
        s.blood_group = payload.bloodGroup.strip()
    if payload.emergencyContact is not None:
        s.emergency_contact = payload.emergencyContact.strip()
    if payload.hallOfResidence is not None:
        s.hall_of_residence = payload.hallOfResidence.strip()
    if payload.bio is not None:
        s.bio = payload.bio.strip()

    # Institutional locks: Only administrators can update academic credentials
    if is_admin:
        if payload.level is not None:
            s.level = payload.level.strip()
        if payload.program is not None:
            s.program = payload.program.strip()
        if payload.faculty is not None:
            s.faculty = payload.faculty.strip()
        if payload.department is not None:
            s.department = payload.department.strip()
        if payload.status is not None:
            s.status = payload.status.strip()

    db.commit()
    db.refresh(s)
    db.refresh(s.user)

    return assemble_student_dossier(s)

@router.post("/{identifier:path}/avatar")
async def upload_student_avatar(
    identifier: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Upload and set student scholar photograph."""
    if identifier.lower() == "me":
        if not current_user.student_profile:
            raise HTTPException(status_code=404, detail="Student profile not found.")
        s = current_user.student_profile
    else:
        s = find_student_profile(identifier, db)

    if not s:
        raise HTTPException(status_code=404, detail=f"Student record '{identifier}' not found.")

    is_self = (current_user.id == s.user_id) or (
        current_user.student_profile and current_user.student_profile.matric_number == s.matric_number
    )
    is_admin = current_user.role in ["super-admin", "admin"]

    if not is_self and not is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access Denied: You do not possess clearance to modify another student's photograph."
        )

    contents = await file.read()
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Image size exceeds maximum limit (5MB).")

    ext = file.filename.split(".")[-1].lower() if file.filename and "." in file.filename else "jpg"
    if ext not in ["jpg", "jpeg", "png", "webp"]:
        raise HTTPException(status_code=400, detail="Invalid image format. Permitted formats: JPG, PNG, WebP.")

    clean_user = re.sub(r"[^a-zA-Z0-9_-]", "_", s.user.id)
    filename = f"avatar_{clean_user}_{uuid.uuid4().hex[:8]}.{ext}"

    for target_dir in get_avatar_upload_directories():
        target_path = target_dir / filename
        with open(target_path, "wb") as f:
            f.write(contents)

    s.user.avatar = f"/uploads/avatars/{filename}"
    db.commit()
    db.refresh(s.user)

    return {
        "status": "success",
        "avatarUrl": s.user.avatar,
        "message": "Student photograph uploaded and persisted successfully."
    }

@router.post("", response_model=StudentOut)
def enroll_student(
    payload: StudentCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["super-admin", "admin"]))
):
    """Enroll and admit a new student into the university database."""
    existing_user = db.query(User).filter_by(email=payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    existing_matric = db.query(StudentProfile).filter_by(matric_number=payload.matricNumber).first()
    if existing_matric:
        raise HTTPException(status_code=400, detail="Student with this matric number already exists.")

    student_count = db.query(StudentProfile).count()
    user_id = f"STU-2026-{str(student_count + 101)}"

    user = User(
        id=user_id,
        name=payload.name,
        email=payload.email,
        hashed_password=get_password_hash(payload.password or "CampusPass@2026"),
        role="student",
        department=payload.department,
        avatar="/assets/images/thumbs/user-img1.png",
        permissions=["student_portal"]
    )
    db.add(user)
    db.flush()

    student = StudentProfile(
        user_id=user.id,
        matric_number=payload.matricNumber,
        level=payload.level,
        program=payload.program,
        faculty=payload.faculty,
        department=payload.department,
        cgpa=0.0,
        admission_year=payload.admissionYear,
        guardian_name=payload.guardianName,
        guardian_phone=payload.guardianPhone,
        guardian_email=payload.guardianEmail,
        phone=payload.phone or "+1 (555) 234-8901",
        address=payload.address or "Plot 14, Academic Hills, University City",
        status="Active"
    )
    db.add(student)
    db.commit()
    db.refresh(student)

    return StudentOut(
        id=student.id,
        userId=user.id,
        name=user.name,
        email=user.email,
        matricNumber=student.matric_number,
        level=student.level,
        program=student.program,
        faculty=student.faculty,
        department=student.department,
        cgpa=student.cgpa,
        admissionYear=student.admission_year,
        status=student.status,
        avatar=user.avatar,
        guardianName=student.guardian_name,
        guardianPhone=student.guardian_phone,
        guardianEmail=student.guardian_email,
        phone=student.phone,
        address=student.address,
        dateOfBirth=student.date_of_birth,
        gender=student.gender,
        bloodGroup=student.blood_group,
        emergencyContact=student.emergency_contact,
        hallOfResidence=student.hall_of_residence,
        bio=student.bio
    )
