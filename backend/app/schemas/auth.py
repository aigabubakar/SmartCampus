from pydantic import BaseModel
from typing import Optional, List, Any

class LoginRequest(BaseModel):
    identifier: str
    password: str
    audience: Optional[str] = "student"  # "student", "faculty", "admin", "super-admin"
    remember_device: Optional[bool] = True

class UserProfile(BaseModel):
    id: str
    name: str
    email: str
    role: str
    department: Optional[str] = None
    faculty: Optional[str] = None
    program: Optional[str] = None
    matric_number: Optional[str] = None
    staff_id: Optional[str] = None
    rank: Optional[str] = None
    level: Optional[str] = None
    cgpa: Optional[float] = None
    admission_year: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    guardian_name: Optional[str] = None
    guardian_phone: Optional[str] = None
    guardian_email: Optional[str] = None
    hall_of_residence: Optional[str] = None
    bio: Optional[str] = None
    blood_group: Optional[str] = None
    emergency_contact: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None
    status: Optional[str] = None
    avatar: Optional[str] = "/assets/images/thumbs/leave-request-img2.png"
    permissions: Optional[List[str]] = []
    is_root: Optional[bool] = False

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserProfile

class TenantInfo(BaseModel):
    institution_name: str
    institution_code: str
    portal_subtitle: str
    academic_session: str
    current_semester: str
    support_email: str
    status: str = "operational"

class AdminCreateRequest(BaseModel):
    name: str
    email: str
    staffId: Optional[str] = None
    scope: Optional[str] = "Academic Operations"
    department: Optional[str] = "Academic Administration"
    permissions: Optional[List[str]] = ["curriculum"]
    password: Optional[str] = "CampusPass@2026"
