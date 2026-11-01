from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
import time

from app.db.session import get_db
from app.models import User, LecturerProfile, StudentProfile, InstitutionConfig
from app.core.security import verify_password, get_password_hash, create_access_token
from app.api.deps import get_current_user, require_roles
from app.schemas.auth import (
    LoginRequest,
    LoginResponse,
    UserProfile,
    TenantInfo,
    AdminCreateRequest
)

router = APIRouter(prefix="/auth", tags=["Authentication & Tenant"])

def build_user_profile(user: User) -> UserProfile:
    """Helper to assemble a comprehensive UserProfile including relational academic details."""
    profile_data = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "department": user.department,
        "avatar": user.avatar or "/assets/images/thumbs/leave-request-img2.png",
        "permissions": user.permissions or [],
        "is_root": user.is_root,
        "program": None,
        "matric_number": None,
        "staff_id": None,
        "rank": None,
        "level": None,
        "cgpa": None,
    }

    if user.student_profile:
        sp = user.student_profile
        profile_data["matric_number"] = sp.matric_number
        profile_data["level"] = sp.level
        profile_data["program"] = sp.program
        profile_data["faculty"] = sp.faculty
        profile_data["cgpa"] = sp.cgpa
        profile_data["admission_year"] = sp.admission_year
        profile_data["status"] = sp.status
        profile_data["phone"] = getattr(sp, "phone", None)
        profile_data["address"] = getattr(sp, "address", None)
        profile_data["guardian_name"] = getattr(sp, "guardian_name", None)
        profile_data["guardian_phone"] = getattr(sp, "guardian_phone", None)
        profile_data["guardian_email"] = getattr(sp, "guardian_email", None)
        profile_data["hall_of_residence"] = getattr(sp, "hall_of_residence", None)
        profile_data["bio"] = getattr(sp, "bio", None)
        profile_data["blood_group"] = getattr(sp, "blood_group", None)
        profile_data["emergency_contact"] = getattr(sp, "emergency_contact", None)
        profile_data["date_of_birth"] = getattr(sp, "date_of_birth", None)
        profile_data["gender"] = getattr(sp, "gender", None)

    if user.lecturer_profile:
        profile_data["staff_id"] = user.lecturer_profile.staff_id
        profile_data["rank"] = user.lecturer_profile.rank

    return UserProfile(**profile_data)

@router.get("/tenant-info", response_model=TenantInfo)
def get_tenant_info(db: Session = Depends(get_db)):
    """Returns co-branding and academic session config from database."""
    inst = db.query(InstitutionConfig).filter_by(config_key="primary").first()
    if not inst:
        return TenantInfo(
            institution_name="Apex Metropolitan University",
            institution_code="AMU-EDU",
            portal_subtitle="Intelligent Academic Portal & SIS",
            academic_session="2026/2027 Academic Session",
            current_semester="First Semester (Fall)",
            support_email="helpdesk@amu.edu",
            status="operational"
        )
    return TenantInfo(
        institution_name=inst.institution_name,
        institution_code=f"{inst.short_code}-EDU",
        portal_subtitle=inst.portal_subtitle,
        academic_session=inst.academic_session,
        current_semester=inst.current_semester,
        support_email=inst.support_email,
        status="operational"
    )

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate user with email/matric/staffId and verify bcrypt password from database."""
    # Retrieve single-tenant institution configuration for authentic co-branded messaging
    inst = db.query(InstitutionConfig).filter_by(config_key="primary").first()
    inst_name = inst.institution_name if inst and inst.institution_name else "University"
    support_email = inst.support_email if inst and inst.support_email else "helpdesk@campus.edu"

    identifier = payload.identifier.strip()
    if not identifier:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Please enter your Matriculation Number, Staff ID, or {inst_name} email address."
        )
    
    # 1. Search by primary email
    user = db.query(User).filter(User.email.ilike(identifier)).first()

    # 2. Search by matric number in StudentProfile
    if not user:
        student = db.query(StudentProfile).filter(StudentProfile.matric_number.ilike(identifier)).first()
        if student:
            user = student.user

    # 3. Search by staff ID in LecturerProfile
    if not user:
        lecturer = db.query(LecturerProfile).filter(LecturerProfile.staff_id.ilike(identifier)).first()
        if lecturer:
            user = lecturer.user

    # 4. Search by exact User ID (e.g. STU-2026-089, FAC-104, ADM-001)
    if not user:
        user = db.query(User).filter(User.id.ilike(identifier)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"User account not found in the {inst_name} directory matching '{identifier}'. Please verify your Matriculation Number, Staff ID, or university email."
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"This {inst_name} account is currently suspended. Please contact the Academic Registrar's Office for clearance."
        )

    # Strictly verify password against stored bcrypt hash in database
    if not payload.password or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Incorrect password for this {inst_name} account. Please verify your password or contact the IT Support Desk ({support_email})."
        )

    profile = build_user_profile(user)
    token = create_access_token(subject=user.id, role=user.role)

    return LoginResponse(
        access_token=token,
        token_type="bearer",
        user=profile
    )

@router.get("/me", response_model=UserProfile)
def get_current_stakeholder_profile(current_user: User = Depends(get_current_user)):
    """Retrieve live authenticated stakeholder profile from database session."""
    return build_user_profile(current_user)

@router.post("/quick-login/{role}", response_model=LoginResponse)
def quick_login(role: str, db: Session = Depends(get_db)):
    """Development shortcut for instant stakeholder impersonation from the database."""
    role_norm = role.lower().strip()
    if role_norm == "teacher":
        role_norm = "lecturer"

    user = db.query(User).filter_by(role=role_norm).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No provisioned user found with role '{role}' in database"
        )
    
    profile = build_user_profile(user)
    token = create_access_token(subject=user.id, role=user.role)
    return LoginResponse(
        access_token=token,
        token_type="bearer",
        user=profile
    )

@router.get("/admins")
def list_admins(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["super-admin", "admin"]))
):
    """Retrieve provisioned university administrators from database."""
    admins = db.query(User).filter(User.role.in_(["super-admin", "admin"])).all()
    results = []
    for a in admins:
        results.append({
            "id": a.id,
            "name": a.name,
            "email": a.email,
            "staffId": a.id,
            "role": a.role,
            "scope": "Platform Owner" if a.is_root else "Campus Operations",
            "department": a.department or "Administration",
            "status": "Active" if a.is_active else "Suspended",
            "dateCreated": a.created_at.strftime("%d %b %Y") if a.created_at else "01 Jan 2026",
            "isRoot": a.is_root,
            "permissions": a.permissions or [],
        })
    return results

@router.post("/admins")
def create_admin(
    payload: AdminCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["super-admin"]))
):
    """Provision a new delegated university administrator in the database."""
    existing = db.query(User).filter_by(email=payload.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Administrator with this email already exists.")

    admin_count = db.query(User).filter(User.role.in_(["super-admin", "admin"])).count()
    new_id = f"ADM-{str(admin_count + 1).zfill(3)}"

    new_user = User(
        id=new_id,
        name=payload.name,
        email=payload.email,
        hashed_password=get_password_hash(payload.password or "CampusPass@2026"),
        role="admin",
        department=payload.department or "Academic Administration",
        is_root=False,
        is_active=True,
        permissions=payload.permissions or ["curriculum"]
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "staffId": payload.staffId or new_user.id,
        "role": new_user.role,
        "scope": payload.scope or "Academic Operations",
        "department": new_user.department,
        "status": "Active",
        "dateCreated": new_user.created_at.strftime("%d %b %Y"),
        "isRoot": False,
        "permissions": new_user.permissions,
    }

@router.delete("/admins/{admin_id}")
def delete_admin(
    admin_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["super-admin"]))
):
    """Revoke and delete a university administrator from database."""
    user = db.query(User).filter_by(id=admin_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Admin not found.")
    if user.is_root or user.role == "super-admin":
        raise HTTPException(status_code=400, detail="Cannot delete root Super Administrator.")
    
    db.delete(user)
    db.commit()
    return {"status": "success", "message": f"Administrator {admin_id} access revoked."}
