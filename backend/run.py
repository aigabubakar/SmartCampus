import sys
from pathlib import Path
import uvicorn

# Ensure the backend directory is in sys.path regardless of current working directory
backend_dir = Path(__file__).resolve().parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

if __name__ == "__main__":
    print("==================================================")
    print("Starting SmartCampus AI OS Backend API Server")
    print(f"Backend Directory: {backend_dir}")
    print("API Documentation: http://127.0.0.1:8000/docs")
    print("Health Check:      http://127.0.0.1:8000/health")
    print("==================================================")
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        app_dir=str(backend_dir),
        reload_dirs=[str(backend_dir / "app")]
    )
