from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional

from app.db.session import get_db
from app.models import User, LecturerProfile, Course
from app.core.security import get_password_hash
from app.api.deps import require_roles

router = APIRouter(prefix="/lecturers", tags=["Academic Faculty & Lecturers"])

class LecturerOut(BaseModel):
    id: int
    userId: str
    name: str
    email: str
    staffId: str
    rank: str
    faculty: str
    department: str
    officeLocation: str
    researchFocus: Optional[str] = None
    highestQualification: Optional[str] = None
    avatar: Optional[str] = None
    assignedCourses: List[str] = []

    class Config:
        from_attributes = True

class LecturerCreateRequest(BaseModel):
    name: str
    email: str
    rank: str = "Lecturer II"
    faculty: str = "Faculty of Computing & Information Technology"
    department: str = "Department of Computer Science & AI"
    officeLocation: str = "Science Complex, Block B, Room 201"
    researchFocus: Optional[str] = None
    highestQualification: str = "Ph.D."
    password: Optional[str] = "CampusPass@2026"

@router.get("", response_model=List[LecturerOut])
def list_lecturers(department: Optional[str] = None, db: Session = Depends(get_db)):
    """Retrieve all academic staff and lecturers from database."""
    query = db.query(LecturerProfile)
    if department:
        query = query.filter(LecturerProfile.department.ilike(f"%{department}%"))
    
    lecturers = query.all()
    results = []
    for l in lecturers:
        results.append(LecturerOut(
            id=l.id,
            userId=l.user.id,
            name=l.user.name,
            email=l.user.email,
            staffId=l.staff_id,
            rank=l.rank,
            faculty=l.faculty,
            department=l.department,
            officeLocation=l.office_location,
            researchFocus=l.research_focus,
            highestQualification=l.highest_qualification,
            avatar=l.user.avatar,
            assignedCourses=[f"{c.code}: {c.title}" for c in l.courses]
        ))
    return results

@router.get("/{identifier}", response_model=LecturerOut)
def get_lecturer_details(identifier: str, db: Session = Depends(get_db)):
    """Retrieve detailed dossier for a specific lecturer by ID, User ID, or Staff ID."""
    l = None
    if identifier.isdigit():
        l = db.query(LecturerProfile).filter_by(id=int(identifier)).first()
    if not l:
        l = db.query(LecturerProfile).filter_by(user_id=identifier).first()
    if not l:
        l = db.query(LecturerProfile).filter_by(staff_id=identifier).first()
    if not l:
        raise HTTPException(status_code=404, detail="Lecturer not found")
    
    return LecturerOut(
        id=l.id,
        userId=l.user.id,
        name=l.user.name,
        email=l.user.email,
        staffId=l.staff_id,
        rank=l.rank,
        faculty=l.faculty,
        department=l.department,
        officeLocation=l.office_location,
        researchFocus=l.research_focus,
        highestQualification=l.highest_qualification,
        avatar=l.user.avatar,
        assignedCourses=[f"{c.code}: {c.title}" for c in l.courses]
    )

@router.post("", response_model=LecturerOut)
def create_lecturer(
    payload: LecturerCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["super-admin", "admin"]))
):
    """Appoint and provision a new tertiary lecturer in the database."""
    existing_user = db.query(User).filter_by(email=payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists.")

    lecturer_count = db.query(LecturerProfile).count()
    user_id = f"FAC-{str(lecturer_count + 101)}"
    staff_id = f"STAFF-FAC-{str(lecturer_count + 101)}"

    user = User(
        id=user_id,
        name=payload.name,
        email=payload.email,
        hashed_password=get_password_hash(payload.password or "CampusPass@2026"),
        role="lecturer",
        department=payload.department,
        avatar="/assets/images/users/user1.png",
        permissions=["lecturer_dossier", "grading", "attendance"]
    )
    db.add(user)
    db.flush()

    lecturer = LecturerProfile(
        user_id=user.id,
        staff_id=staff_id,
        rank=payload.rank,
        faculty=payload.faculty,
        department=payload.department,
        office_location=payload.officeLocation,
        research_focus=payload.researchFocus,
        highest_qualification=payload.highestQualification
    )
    db.add(lecturer)
    db.commit()
    db.refresh(lecturer)

    return LecturerOut(
        id=lecturer.id,
        userId=user.id,
        name=user.name,
        email=user.email,
        staffId=lecturer.staff_id,
        rank=lecturer.rank,
        faculty=lecturer.faculty,
        department=lecturer.department,
        officeLocation=lecturer.office_location,
        researchFocus=lecturer.research_focus,
        highestQualification=lecturer.highest_qualification,
        avatar=user.avatar,
        assignedCourses=[]
    )
