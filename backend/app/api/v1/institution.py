from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from app.db.session import get_db
from app.models.user import User
from app.models.institution import InstitutionConfig
from app.api.deps import require_roles

router = APIRouter(prefix="/institution", tags=["Institution CMS"])

def inst_to_dict(inst: InstitutionConfig) -> Dict[str, Any]:
    return {
        "institutionName": inst.institution_name,
        "name": inst.institution_name,
        "motto": getattr(inst, "motto", "Excellence, Integrity & Innovation") or "Excellence, Integrity & Innovation",
        "shortCode": inst.short_code,
        "portalSubtitle": inst.portal_subtitle,
        "campusLocation": inst.campus_location,
        "logoUrl": inst.logo_url,
        "logoDarkUrl": inst.logo_dark_url,
        "crestUrl": inst.crest_url,
        "supportEmail": inst.support_email,
        "supportPhone": inst.support_phone,
        "physicalAddress": inst.physical_address,
        "websiteUrl": inst.website_url,
        "academicSession": inst.academic_session,
        "currentAcademicYear": inst.academic_session,
        "currentSemester": inst.current_semester,
        "semesterStartDate": inst.semester_start_date,
        "semesterEndDate": inst.semester_end_date,
        "courseRegistrationOpen": inst.course_registration_open,
        "examPeriodActive": inst.exam_period_active,
        "gradeSubmissionDeadline": inst.grade_submission_deadline,
        "modules": inst.modules or {},
        "ai": inst.ai or {},
        "ssoEnabled": inst.sso_enabled,
        "sessionTimeoutMinutes": inst.session_timeout_minutes,
        "maintenanceMode": inst.maintenance_mode,
    }

@router.get("/config")
def get_config(db: Session = Depends(get_db)):
    """Retrieve live institutional configuration from database."""
    inst = db.query(InstitutionConfig).filter_by(config_key="primary").first()
    if not inst:
        # Create default record
        inst = InstitutionConfig(config_key="primary")
        db.add(inst)
        db.commit()
        db.refresh(inst)
    return inst_to_dict(inst)

@router.put("/config")
def update_config(
    payload: Dict[str, Any],
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(["super-admin", "admin"]))
):
    """Update and persist live institutional CMS settings to the database."""
    inst = db.query(InstitutionConfig).filter_by(config_key="primary").first()
    if not inst:
        inst = InstitutionConfig(config_key="primary")
        db.add(inst)

    if "institutionName" in payload:
        inst.institution_name = payload["institutionName"]
    elif "name" in payload:
        inst.institution_name = payload["name"]
    if "motto" in payload:
        inst.motto = payload["motto"]
    if "shortCode" in payload:
        inst.short_code = payload["shortCode"]
    if "portalSubtitle" in payload:
        inst.portal_subtitle = payload["portalSubtitle"]
    if "campusLocation" in payload:
        inst.campus_location = payload["campusLocation"]
    if "logoUrl" in payload:
        inst.logo_url = payload["logoUrl"]
    if "logoDarkUrl" in payload:
        inst.logo_dark_url = payload["logoDarkUrl"]
    if "crestUrl" in payload:
        inst.crest_url = payload["crestUrl"]
    if "supportEmail" in payload:
        inst.support_email = payload["supportEmail"]
    if "supportPhone" in payload:
        inst.support_phone = payload["supportPhone"]
    if "physicalAddress" in payload:
        inst.physical_address = payload["physicalAddress"]
    if "websiteUrl" in payload:
        inst.website_url = payload["websiteUrl"]
    if "academicSession" in payload:
        inst.academic_session = payload["academicSession"]
    if "currentSemester" in payload:
        inst.current_semester = payload["currentSemester"]
    if "semesterStartDate" in payload:
        inst.semester_start_date = payload["semesterStartDate"]
    if "semesterEndDate" in payload:
        inst.semester_end_date = payload["semesterEndDate"]
    if "courseRegistrationOpen" in payload:
        inst.course_registration_open = payload["courseRegistrationOpen"]
    if "examPeriodActive" in payload:
        inst.exam_period_active = payload["examPeriodActive"]
    if "gradeSubmissionDeadline" in payload:
        inst.grade_submission_deadline = payload["gradeSubmissionDeadline"]
    if "modules" in payload:
        inst.modules = payload["modules"]
    if "ai" in payload:
        inst.ai = payload["ai"]
    if "ssoEnabled" in payload:
        inst.sso_enabled = payload["ssoEnabled"]
    if "sessionTimeoutMinutes" in payload:
        inst.session_timeout_minutes = payload["sessionTimeoutMinutes"]
    if "maintenanceMode" in payload:
        inst.maintenance_mode = payload["maintenanceMode"]

    db.commit()
    db.refresh(inst)
    return {
        "status": "success",
        "message": "Institutional configuration updated in database",
        "config": inst_to_dict(inst)
    }
