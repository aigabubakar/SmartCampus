from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), unique=True, index=True, nullable=False)  # e.g. "CSC 301"
    title = Column(String(255), nullable=False)                         # e.g. "Advanced Data Structures & Algorithms"
    credit_units = Column(Integer, default=3)
    level = Column(String(50), default="300 Level")
    semester = Column(String(50), default="First Semester")
    department = Column(String(255), default="Department of Computer Science & AI")
    faculty = Column(String(255), default="Faculty of Computing & Information Technology")
    description = Column(String(1000), nullable=True)
    category = Column(String(50), default="Core Compulsory")            # Core Compulsory, Required, Elective, General Studies
    prerequisite_course_code = Column(String(50), nullable=True)        # e.g. "CSC 201"
    lecturer_id = Column(Integer, ForeignKey("lecturers.id", ondelete="SET NULL"), nullable=True)

    # Relationships
    lecturer = relationship("LecturerProfile", back_populates="courses")
    enrollments = relationship("CourseEnrollment", back_populates="course", cascade="all, delete-orphan")
    grades = relationship("ExamGrade", back_populates="course", cascade="all, delete-orphan")
    attendance_records = relationship("AttendanceRecord", back_populates="course", cascade="all, delete-orphan")

class CourseEnrollment(Base):
    __tablename__ = "course_enrollments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    session = Column(String(50), default="2026/2027")
    semester = Column(String(50), default="First Semester")
    status = Column(String(50), default="Registered")  # Registered, Dropped, Completed
    is_carryover = Column(Boolean, default=False)
    auto_enrolled_by_ai = Column(Boolean, default=False)
    registration_type = Column(String(50), default="Core Regular")  # Carryover (Auto-Enrolled), Core Regular, Elective
    underload_concession = Column(Boolean, default=False)
    underload_reason = Column(String(255), nullable=True)
    concession_reference = Column(String(100), nullable=True)
    enrolled_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    student = relationship("StudentProfile", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
