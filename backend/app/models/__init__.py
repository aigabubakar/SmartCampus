from app.models.user import User
from app.models.institution import InstitutionConfig
from app.models.lecturer import LecturerProfile
from app.models.student import StudentProfile
from app.models.academic import Course, CourseEnrollment
from app.models.attendance import AttendanceRecord
from app.models.grade import ExamGrade
from app.models.notice import CampusNotice
from app.models.telemetry import StudentRiskRecord

__all__ = [
    "User",
    "InstitutionConfig",
    "LecturerProfile",
    "StudentProfile",
    "Course",
    "CourseEnrollment",
    "AttendanceRecord",
    "ExamGrade",
    "CampusNotice",
    "StudentRiskRecord",
]
