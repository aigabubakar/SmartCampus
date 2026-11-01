from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base_class import Base

class CampusNotice(Base):
    __tablename__ = "campus_notices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    description = Column(String(2000), nullable=False)
    sender = Column(String(255), default="Office of the Registrar")
    audience = Column(String(50), default="all")  # all, students, faculty, guardians
    priority = Column(String(50), default="General")  # Urgent, Important, Event, General
    date = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
