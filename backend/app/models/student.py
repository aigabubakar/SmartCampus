from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class StudentProfile(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(50), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    matric_number = Column(String(50), unique=True, index=True, nullable=False)
    level = Column(String(50), default="300 Level")
    program = Column(String(255), default="B.Sc Computer Science")
    faculty = Column(String(255), default="Faculty of Computing & Information Systems")
    department = Column(String(255), default="Department of Computer Science")
    cgpa = Column(Float, default=3.85)
    admission_year = Column(String(10), default="2023")
    guardian_name = Column(String(255), nullable=True, default="Eleanor Vance-Chen")
    guardian_phone = Column(String(50), nullable=True, default="+1 (555) 304-9912")
    guardian_email = Column(String(255), nullable=True, default="eleanor.vance@family.org")
    phone = Column(String(50), nullable=True, default="+1 (555) 234-8901")
    address = Column(String(500), nullable=True, default="Plot 14, Academic Hills, University City")
    date_of_birth = Column(String(50), nullable=True, default="2003-05-14")
    gender = Column(String(20), nullable=True, default="Female")
    blood_group = Column(String(10), nullable=True, default="O+")
    emergency_contact = Column(String(255), nullable=True, default="+1 (555) 304-9912")
    hall_of_residence = Column(String(255), nullable=True, default="Queen Idia Hall, Block C, Room 14")
    bio = Column(String(1000), nullable=True, default="Undergraduate Scholar majoring in Computer Science with a focus on Distributed Systems and Software Architecture.")
    status = Column(String(50), default="Active")  # Active, Graduated, Suspended, Probation

    # Relationships
    user = relationship("User", back_populates="student_profile")
    enrollments = relationship("CourseEnrollment", back_populates="student", cascade="all, delete-orphan")
    grades = relationship("ExamGrade", back_populates="student", cascade="all, delete-orphan")
    attendance_records = relationship("AttendanceRecord", back_populates="student", cascade="all, delete-orphan")
