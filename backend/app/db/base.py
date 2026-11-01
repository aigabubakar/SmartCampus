# Import all the models, so that Base has them before being imported by Alembic or database table initializer
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.institution import InstitutionConfig  # noqa
from app.models.lecturer import LecturerProfile  # noqa
from app.models.student import StudentProfile  # noqa
from app.models.academic import Course, CourseEnrollment  # noqa
from app.models.attendance import AttendanceRecord  # noqa
from app.models.grade import ExamGrade  # noqa
from app.models.notice import CampusNotice  # noqa
from app.models.telemetry import StudentRiskRecord  # noqa
