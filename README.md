# SmartCampus — Intelligent University Academic Portal & Student Information System (SIS)

**SmartCampus** is a single-tenant enterprise-grade academic operating system and university management platform. Built with a modern, high-performance architecture, it provides role-differentiated experiences for students, faculty, and university executives.

[![Frontend](https://img.shields.io/badge/Frontend-Vue%203%20%7C%20Vite%20%7C%20Pinia-42b883.svg)](https://vuejs.org/)
[![Backend](https://img.shields.io/badge/Backend-FastAPI%20%7C%20Python%203.11+-009688.svg)](https://fastapi.tiangolo.com/)
[![Database](https://img.shields.io/badge/Database-SQLite%20%2F%20SQLAlchemy-003B57.svg)](https://www.sqlite.org/)
[![Platform](https://img.shields.io/badge/Platform-StackHubs%20Technologies-10b981.svg)](https://stackhubs.com.ng)

---

## 🏛️ System Architecture & Personas

SmartCampus is engineered with strict **Role-Based Access Control (RBAC)** and a dynamic dashboard dispatcher that instantly directs authenticated users to their tailored workspace:

### 1. Student Academic Portal
* **Personalized Academic Dossier**: View and update profile, state of origin, emergency contacts, hall of residence, and upload verifiable academic portrait photographs.
* **Digital Examination Clearance Pass**: Verifiable digital exam pass with QR code, ensuring student attendance clears the Senate threshold (minimum 75%) and tuition status is validated.
* **Course Registration & Study Timetable**: Interactive semester course schedule and lecture hall assignments.
* **Continuous Assessment & Exam Gradebook**: Real-time transcript tracking, CAT/Exam score breakdowns, and CGPA calculations on a 5.0 grading scale.

### 2. Faculty Teaching Console
* **Teaching Roster & Timetables**: View assigned course modules, lecture times, and student rosters.
* **Lecture Attendance Marker**: Take daily lecture attendance and monitor at-risk attendance flags.
* **Grade Submission & CAT Scoring**: Submit continuous assessment marks directly to the department board.
* **Academic Leave Requests**: Submit duty and research leave applications for Dean approval.

### 3. Executive Administration Dashboard
* **Institutional Executive Intelligence**: Real-time campus KPIs, student enrolment demographics, fee collection ledgers, and academic calendar timelines.
* **Campus CMS & Branding**: Configure university name, crest, portal subtitles, motto, active academic session, and semester dates.
* **Security & Governance**: Institutional role assignment, user status toggles, and workstation lock screen protection.

---

## 🚀 Tech Stack

### Frontend
* **Framework**: Vue 3 (Composition API & `<script setup>`)
* **Build Tool**: Vite
* **State Management**: Pinia (Reactive Institutional & Auth Stores)
* **Routing**: Vue Router 4 (Dynamic Role-Differentiated Dispatcher & Navigation Guards)
* **Icons**: Iconify + Remix Icons
* **Charts**: ApexCharts

### Backend
* **API Framework**: FastAPI (Asynchronous Python)
* **ORM & Database**: SQLAlchemy with SQLite (migratable to PostgreSQL)
* **Authentication**: OAuth2 Password Flow with JWT Bearer tokens and PBKDF2-SHA256 password hashing
* **Validation**: Pydantic v2 schemas

---

## 🛠️ Quickstart Guide

### Prerequisites
* **Node.js** (v18.x or higher)
* **Python** (v3.10 or higher)

---

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment (optional but recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database seeder (initializes users, students, courses, and configs)
python app/scripts/seed_db.py

# Launch FastAPI server
python run.py
```
* Backend API documentation will be accessible at: `http://127.0.0.1:8000/docs`
* API endpoint base: `http://127.0.0.1:8000/api/v1`

---

### 2. Frontend Setup

From the root directory:

```bash
# Install frontend dependencies
npm install

# Start Vite development server
npm run dev
```
* Frontend application will be live at: `http://localhost:5173/`

---

### 3. Production Build

```bash
# Compile and optimize frontend assets for deployment
npm run build
```

---

## 🧪 Automated Test Suites

SmartCampus comes with comprehensive test coverage for backend security and profile persistence:

```bash
# Run security, JWT auth, and RBAC endpoint test suite (25/25 checks)
python scratch/test_backend_api.py

# Run student profile setup and photograph persistence test suite
python scratch/test_student_profile_persistence.py
```

---

## 🔐 Demo Credentials

| Role | Username / Identifier | Password | Access Scope |
| :--- | :--- | :--- | :--- |
| **Student** | `SCI/2026/0491` | `student123` | Student Academic Portal |
| **Lecturer** | `prof.finch@campus.edu` | `teacher123` | Faculty Teaching Console |
| **Admin** | `admin.vance@campus.edu` | `admin123` | Administrative Suite |
| **Super Admin** | `superadmin@campus.edu` | `super123` | Full Campus CMS & Governance |

---

## 📄 License & Attribution

* **Architecture & Development**: [StackHubs Technologies](https://stackhubs.com.ng)
* **Platform**: SmartCampus Academic Operating System
* **Website**: [https://stackhubs.com.ng](https://stackhubs.com.ng)
