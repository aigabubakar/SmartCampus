from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class LecturerProfile(Base):
    __tablename__ = "lecturers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(50), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    staff_id = Column(String(50), unique=True, index=True, nullable=False)
    rank = Column(String(100), default="Lecturer")  # Professor, Associate Professor, Senior Lecturer, etc.
    faculty = Column(String(255), default="Faculty of Computing & Information Systems")
    department = Column(String(255), default="Department of Computer Science")
    office_location = Column(String(255), default="Science & Engineering Complex, Block B, Room 304")
    research_focus = Column(String(500), nullable=True)
    phone = Column(String(50), nullable=True)
    highest_qualification = Column(String(100), default="Ph.D. in Computer Science")
    date_appointed = Column(String(50), default="2021-08-15")

    # Relationships
    user = relationship("User", back_populates="lecturer_profile")
    courses = relationship("Course", back_populates="lecturer")
