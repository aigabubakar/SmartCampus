from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
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
    enrolled_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    student = relationship("StudentProfile", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
