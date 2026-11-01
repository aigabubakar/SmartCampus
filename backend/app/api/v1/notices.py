from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from app.db.session import get_db
from app.models.notice import CampusNotice

router = APIRouter(prefix="/notices", tags=["Institutional Notices & Circulars"])

class NoticeModel(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    sender: str
    audience: str  # 'all', 'students', 'faculty', 'guardians'
    priority: str  # 'Urgent', 'Important', 'Event', 'General'
    date: Optional[str] = None

    class Config:
        from_attributes = True

@router.get("", response_model=List[NoticeModel])
def get_notices(audience: Optional[str] = None, db: Session = Depends(get_db)):
    """Retrieve institutional notices from database, optionally filtered by audience"""
    query = db.query(CampusNotice).order_by(CampusNotice.id.desc())
    if audience and audience != "all":
        query = query.filter(CampusNotice.audience.in_(["all", audience]))
    
    notices = query.all()
    return notices

@router.post("", response_model=NoticeModel)
def create_notice(payload: NoticeModel, db: Session = Depends(get_db)):
    """Publish a new institutional notice / senate circular to the database"""
    notice = CampusNotice(
        title=payload.title,
        description=payload.description,
        sender=payload.sender or "Office of the Registrar",
        audience=payload.audience or "all",
        priority=payload.priority or "General",
        date=payload.date or "28 Oct 2026"
    )
    db.add(notice)
    db.commit()
    db.refresh(notice)
    return notice

@router.delete("/{notice_id}")
def delete_notice(notice_id: int, db: Session = Depends(get_db)):
    """Delete an institutional notice from database"""
    notice = db.query(CampusNotice).filter_by(id=notice_id).first()
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")
    db.delete(notice)
    db.commit()
    return {"status": "success", "message": f"Notice {notice_id} deleted"}
