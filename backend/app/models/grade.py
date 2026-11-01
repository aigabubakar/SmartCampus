from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class ExamGrade(Base):
    __tablename__ = "exam_grades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    session = Column(String(50), default="2026/2027")
    semester = Column(String(50), default="First Semester")
    ca_score = Column(Float, default=0.0)      # Continuous Assessment (max 30)
    exam_score = Column(Float, default=0.0)    # Examination (max 70)
    total_score = Column(Float, default=0.0)   # Total (max 100)
    letter_grade = Column(String(5), default="F")  # A, B, C, D, E, F
    grade_point = Column(Float, default=0.0)   # 5.0 (A) to 0.0 (F)
    approved_by_senate = Column(Boolean, default=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    student = relationship("StudentProfile", back_populates="grades")
    course = relationship("Course", back_populates="grades")
