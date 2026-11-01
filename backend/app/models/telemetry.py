from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.base_class import Base

class StudentRiskRecord(Base):
    __tablename__ = "student_risk_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    matric_no = Column(String(50), nullable=False, index=True)
    initials = Column(String(10), nullable=True)
    department = Column(String(255), nullable=True)
    level = Column(String(50), default="300 Level")
    cgpa = Column(Float, default=2.0)
    risk_category = Column(String(50), nullable=False)  # attendance, probation, academic
    risk_vector = Column(String(500), nullable=False)
    flagged_course = Column(String(255), nullable=False)
    ai_confidence = Column(Integer, default=90)
    status = Column(String(100), default="Unaddressed")  # Unaddressed, Advisor Alerted, Under Supervision, Resolved
    created_at = Column(DateTime, default=datetime.utcnow)
