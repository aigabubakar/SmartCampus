from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.core.config import settings
from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.api.v1.auth import router as auth_router
from app.api.v1.institution import router as institution_router
from app.api.v1.telemetry import router as telemetry_router
from app.api.v1.notices import router as notices_router
from app.api.v1.lecturers import router as lecturers_router
from app.api.v1.students import router as students_router
from app.api.v1.courses import router as courses_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure tables exist in SQLite or Postgres
    try:
        Base.metadata.create_all(bind=engine)
        # Verify and migrate any missing student columns in SQLite
        from sqlalchemy import text
        with engine.connect() as conn:
            res = conn.execute(text("PRAGMA table_info(students)")).fetchall()
            existing_cols = {row[1] for row in res}
            new_columns = [
                ("phone", "VARCHAR(50) DEFAULT '+1 (555) 234-8901'"),
                ("address", "VARCHAR(500) DEFAULT 'Plot 14, Academic Hills, University City'"),
                ("date_of_birth", "VARCHAR(50) DEFAULT '2003-05-14'"),
                ("gender", "VARCHAR(20) DEFAULT 'Female'"),
                ("blood_group", "VARCHAR(10) DEFAULT 'O+'"),
                ("emergency_contact", "VARCHAR(255) DEFAULT '+1 (555) 304-9912'"),
                ("hall_of_residence", "VARCHAR(255) DEFAULT 'Queen Idia Hall, Block C, Room 14'"),
                ("bio", "VARCHAR(1000) DEFAULT 'Undergraduate Scholar majoring in Computer Science with a focus on Distributed Systems and Software Architecture.'"),
            ]
            for col_name, col_def in new_columns:
                if col_name not in existing_cols:
                    conn.execute(text(f"ALTER TABLE students ADD COLUMN {col_name} {col_def}"))
                    conn.commit()
        print("[SmartCampus API] Database tables and student profile schema verified.")
    except Exception as e:
        print(f"[SmartCampus API] Database initialization warning: {e}")
    yield
    # Shutdown

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="Smart Campus AI Operating System - Enterprise Backend API & Relational Database",
    version="1.2.0",
    lifespan=lifespan
)

# CORS middleware for Vite frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(auth_router, prefix=settings.API_V1_STR)
app.include_router(institution_router, prefix=settings.API_V1_STR)
app.include_router(telemetry_router, prefix=settings.API_V1_STR)
app.include_router(notices_router, prefix=settings.API_V1_STR)
app.include_router(lecturers_router, prefix=settings.API_V1_STR)
app.include_router(students_router, prefix=settings.API_V1_STR)
app.include_router(courses_router, prefix=settings.API_V1_STR)

# Mount static uploads directory for serving avatars and assets
from fastapi.staticfiles import StaticFiles
from pathlib import Path
uploads_dir = Path(__file__).resolve().parent.parent.parent / "public" / "uploads"
uploads_dir.mkdir(parents=True, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=str(uploads_dir)), name="uploads")

@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "database": "connected",
        "version": "1.2.0"
    }

if __name__ == "__main__":
    import uvicorn
    from pathlib import Path
    backend_dir = Path(__file__).resolve().parent.parent
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        app_dir=str(backend_dir),
        reload_dirs=[str(backend_dir / "app")]
    )
