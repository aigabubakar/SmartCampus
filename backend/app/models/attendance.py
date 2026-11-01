from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class AttendanceRecord(Base):
    __tablename__ = "attendance_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    lecturer_id = Column(Integer, ForeignKey("lecturers.id", ondelete="SET NULL"), nullable=True)
    lecture_date = Column(String(50), nullable=False)  # ISO Date YYYY-MM-DD
    status = Column(String(50), default="present")     # present, absent, late, excused
    notes = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    course = relationship("Course", back_populates="attendance_records")
    student = relationship("StudentProfile", back_populates="attendance_records")
