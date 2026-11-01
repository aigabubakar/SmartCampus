from sqlalchemy import Column, String, Boolean, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, index=True)  # super-admin, admin, lecturer, student, guardian, librarian
    department = Column(String(255), nullable=True)
    avatar = Column(String(500), nullable=True, default="/assets/images/thumbs/leave-request-img2.png")
    is_active = Column(Boolean, default=True)
    is_root = Column(Boolean, default=False)
    permissions = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    lecturer_profile = relationship("LecturerProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
    student_profile = relationship("StudentProfile", back_populates="user", uselist=False, cascade="all, delete-orphan")
