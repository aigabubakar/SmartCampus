from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from datetime import datetime
from app.db.base_class import Base

class InstitutionConfig(Base):
    __tablename__ = "institution_configs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    config_key = Column(String(50), unique=True, index=True, default="primary")
    institution_name = Column(String(255), default="Apex Metropolitan University")
    motto = Column(String(255), default="Excellence, Integrity & Innovation")
    short_code = Column(String(50), default="AMU")
    portal_subtitle = Column(String(255), default="Intelligent Academic Portal & SIS")
    campus_location = Column(String(255), default="Main Campus - University City")
    logo_url = Column(String(500), default="/assets/images/logo.png")
    logo_dark_url = Column(String(500), default="/assets/images/logo-light.png")
    crest_url = Column(String(500), default="/assets/images/logo-icon.png")
    support_email = Column(String(255), default="helpdesk@amu.edu")
    support_phone = Column(String(100), default="+1 (555) 019-4820")
    physical_address = Column(String(500), default="100 University Avenue, Tech Corridor, CA 94105")
    website_url = Column(String(255), default="https://amu.edu")

    # Academic Calendar
    academic_session = Column(String(100), default="2026/2027 Academic Session")
    current_semester = Column(String(100), default="First Semester (Fall)")
    semester_start_date = Column(String(50), default="2026-09-01")
    semester_end_date = Column(String(50), default="2027-01-22")
    course_registration_open = Column(Boolean, default=True)
    exam_period_active = Column(Boolean, default=False)
    grade_submission_deadline = Column(String(50), default="2027-02-05")

    # JSON configurations for feature flags and AI parameters
    modules = Column(JSON, default=lambda: {
        "aiAdvisory": True,
        "studentAdmissions": True,
        "attendance": True,
        "examination": True,
        "feeCollections": True,
        "library": True,
        "accounts": True,
        "hrm": True,
        "leaves": True,
        "noticeBoard": True
    })
    ai = Column(JSON, default=lambda: {
        "provider": "gemini-flash",
        "atRiskAttendanceThreshold": 75,
        "atRiskGpaThreshold": 2.50,
        "requireHumanInTheLoop": True,
        "aiProctoringSensitivity": "medium",
        "policyDirectives": "All academic insights must comply with the 2026/2027 University Academic Handbook."
    })

    sso_enabled = Column(Boolean, default=True)
    session_timeout_minutes = Column(Integer, default=60)
    maintenance_mode = Column(Boolean, default=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
