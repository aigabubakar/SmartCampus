import sys
from pathlib import Path

# Add backend directory to path
backend_path = Path(__file__).resolve().parent.parent.parent
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.core.security import get_password_hash
from app.models.user import User
from app.models.institution import InstitutionConfig
from app.models.lecturer import LecturerProfile
from app.models.student import StudentProfile
from app.models.academic import Course, CourseEnrollment
from app.models.attendance import AttendanceRecord
from app.models.grade import ExamGrade
from app.models.notice import CampusNotice
from app.models.telemetry import StudentRiskRecord

def seed_database():
    print("==================================================")
    print("SmartCampus — Tertiary Academic Database Seeder")
    print("==================================================")

    # 1. Initialize tables
    print("[1/6] Creating database tables...")
    Base.metadata.create_all(bind=engine)
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

        # Migrate courses columns
        res_c = conn.execute(text("PRAGMA table_info(courses)")).fetchall()
        existing_c_cols = {row[1] for row in res_c}
        new_c_columns = [
            ("category", "VARCHAR(50) DEFAULT 'Core Compulsory'"),
            ("prerequisite_course_code", "VARCHAR(50) DEFAULT NULL"),
        ]
        for col_name, col_def in new_c_columns:
            if col_name not in existing_c_cols:
                conn.execute(text(f"ALTER TABLE courses ADD COLUMN {col_name} {col_def}"))
                conn.commit()

        # Migrate course_enrollments columns
        res_e = conn.execute(text("PRAGMA table_info(course_enrollments)")).fetchall()
        existing_e_cols = {row[1] for row in res_e}
        new_e_columns = [
            ("is_carryover", "BOOLEAN DEFAULT 0"),
            ("auto_enrolled_by_ai", "BOOLEAN DEFAULT 0"),
            ("registration_type", "VARCHAR(50) DEFAULT 'Core Regular'"),
            ("underload_concession", "BOOLEAN DEFAULT 0"),
            ("underload_reason", "VARCHAR(255) DEFAULT NULL"),
            ("concession_reference", "VARCHAR(100) DEFAULT NULL"),
        ]
        for col_name, col_def in new_e_columns:
            if col_name not in existing_e_cols:
                conn.execute(text(f"ALTER TABLE course_enrollments ADD COLUMN {col_name} {col_def}"))
                conn.commit()
    print("      Tables and academic schemas successfully created or verified.")

    db = SessionLocal()
    try:
        # 2. Institutional CMS Configuration
        print("[2/6] Seeding Institutional CMS Configuration...")
        existing_inst = db.query(InstitutionConfig).filter_by(config_key="primary").first()
        if not existing_inst:
            inst = InstitutionConfig(
                config_key="primary",
                institution_name="Apex Metropolitan University",
                short_code="AMU",
                portal_subtitle="University Academic Portal & SIS",
                campus_location="Main Campus - University City",
                logo_url="/assets/images/logo.png",
                logo_dark_url="/assets/images/logo-light.png",
                crest_url="/assets/images/logo-icon.png",
                support_email="helpdesk@amu.edu",
                support_phone="+1 (555) 019-4820",
                physical_address="100 University Avenue, Tech Corridor, CA 94105",
                website_url="https://amu.edu",
                academic_session="2026/2027 Academic Session",
                current_semester="First Semester (Fall)",
                semester_start_date="2026-09-01",
                semester_end_date="2027-01-22",
                course_registration_open=True,
                exam_period_active=False,
                grade_submission_deadline="2027-02-05",
                modules={
                    "aiAdvisory": True,
                    "studentAdmissions": True,
                    "attendance": True,
                    "examination": True,
                    "feeCollections": True,
                    "library": True,
                    "accounts": True,
                    "hrm": True,
                    "leaves": True,
                    "noticeBoard": True
                },
                ai={
                    "provider": "senate-policy-engine",
                    "atRiskAttendanceThreshold": 75,
                    "atRiskGpaThreshold": 1.50,
                    "requireHumanInTheLoop": True,
                    "aiProctoringSensitivity": "standard",
                    "policyDirectives": "All academic standing classifications and examination approvals are governed by the 2026/2027 Senate Regulations and Faculty Handbook. Examination eligibility mandates minimum 75% verified lecture attendance."
                }
            )
            db.add(inst)
            db.commit()
            print("      Created primary university configuration.")
        else:
            existing_inst.portal_subtitle = "University Academic Portal & SIS"
            existing_inst.ai = {
                "provider": "senate-policy-engine",
                "atRiskAttendanceThreshold": 75,
                "atRiskGpaThreshold": 1.50,
                "requireHumanInTheLoop": True,
                "aiProctoringSensitivity": "standard",
                "policyDirectives": "All academic standing classifications and examination approvals are governed by the 2026/2027 Senate Regulations and Faculty Handbook. Examination eligibility mandates minimum 75% verified lecture attendance."
            }
            db.commit()
            print("      Synchronized primary university configuration.")

        # 3. Tertiary Stakeholder Accounts & Profiles
        print("[3/6] Seeding Tertiary Stakeholders (Super Admin, Lecturers, Students)...")
        default_pw = get_password_hash("CampusPass@2026")

        users_data = [
            {
                "id": "ADM-001",
                "name": "System Super Administrator",
                "email": "superadmin@devcompany.io",
                "role": "super-admin",
                "is_root": True,
                "department": "Software Engineering & Managed Systems",
                "avatar": "/assets/images/thumbs/leave-request-img2.png",
                "permissions": ["all_access", "manage_admins", "system_cms", "ai_governance", "database_control"]
            },
            {
                "id": "ADM-002",
                "name": "Dr. Evelyn Vance",
                "email": "evelyn.vance@campus.edu",
                "role": "admin",
                "is_root": False,
                "department": "Vice Chancellor / Executive Office",
                "avatar": "/assets/images/thumbs/leave-request-img1.png",
                "permissions": ["curriculum", "admissions", "grading_approvals", "ai_override", "staff_management"]
            },
            {
                "id": "ADM-003",
                "name": "Marcus Holloway",
                "email": "m.holloway@campus.edu",
                "role": "admin",
                "is_root": False,
                "department": "Academic Registrar Office",
                "avatar": "/assets/images/thumbs/user-img1.png",
                "permissions": ["curriculum", "grading_approvals", "transcripts", "exam_schedules"]
            },
            {
                "id": "FAC-104",
                "name": "Prof. Alistair Finch",
                "email": "a.finch@campus.edu",
                "role": "lecturer",
                "is_root": False,
                "department": "Department of Computer Science",
                "avatar": "/assets/images/users/user1.png",
                "permissions": ["lecturer_dossier", "grading", "attendance", "course_materials"]
            },
            {
                "id": "FAC-108",
                "name": "Dr. Angela Davis",
                "email": "a.davis@campus.edu",
                "role": "lecturer",
                "is_root": False,
                "department": "Department of Software Engineering",
                "avatar": "/assets/images/thumbs/leave-request-img1.png",
                "permissions": ["lecturer_dossier", "grading", "attendance"]
            },
            {
                "id": "STU-2026-089",
                "name": "Sophia Chen",
                "email": "sophia.chen@student.campus.edu",
                "role": "student",
                "is_root": False,
                "department": "Faculty of Computing & Information Systems",
                "avatar": "/assets/images/thumbs/user-img1.png",
                "permissions": ["student_portal"]
            },
            {
                "id": "STU-2023-104",
                "name": "David Adeleke",
                "email": "d.adeleke@student.campus.edu",
                "role": "student",
                "is_root": False,
                "department": "Faculty of Computing & Information Systems",
                "avatar": "/assets/images/thumbs/user-img3.png",
                "permissions": ["student_portal"]
            },
            {
                "id": "STU-2024-048",
                "name": "Chidinma Okoye",
                "email": "c.okoye@student.campus.edu",
                "role": "student",
                "is_root": False,
                "department": "Faculty of Engineering",
                "avatar": "/assets/images/thumbs/user-img2.png",
                "permissions": ["student_portal"]
            },
            {
                "id": "GRD-502",
                "name": "Eleanor Vance-Chen",
                "email": "eleanor.vance@family.org",
                "role": "guardian",
                "is_root": False,
                "department": "Parent & Guardian Assembly",
                "avatar": "/assets/images/thumbs/user-img2.png",
                "permissions": ["guardian_portal"]
            },
            {
                "id": "LIB-034",
                "name": "Samuel Osei",
                "email": "samuel.osei@library.campus.edu",
                "role": "librarian",
                "is_root": False,
                "department": "Main University Library & Digital Archives",
                "avatar": "/assets/images/thumbs/user-img3.png",
                "permissions": ["library_control"]
            }
        ]

        for u in users_data:
            user = db.query(User).filter_by(id=u["id"]).first()
            if not user:
                user = User(
                    id=u["id"],
                    name=u["name"],
                    email=u["email"],
                    hashed_password=default_pw,
                    role=u["role"],
                    is_root=u["is_root"],
                    department=u["department"],
                    avatar=u["avatar"],
                    permissions=u["permissions"],
                    is_active=True
                )
                db.add(user)
            else:
                user.name = u["name"]
                user.email = u["email"]
                user.role = u["role"]
                user.is_root = u["is_root"]
                user.department = u["department"]
                user.avatar = u["avatar"]
                user.permissions = u["permissions"]
                user.hashed_password = default_pw
                user.is_active = True
        db.commit()

        # Seed Lecturer Profiles
        lecturer_finch = db.query(LecturerProfile).filter_by(user_id="FAC-104").first()
        if not lecturer_finch:
            lecturer_finch = LecturerProfile(
                user_id="FAC-104",
                staff_id="STAFF-FAC-104",
                rank="Professor of Computer Science",
                faculty="Faculty of Computing & Information Systems",
                department="Department of Computer Science",
                office_location="Science & Engineering Complex, Block B, Room 304",
                research_focus="Distributed Systems & High-Performance Computing",
                highest_qualification="Ph.D. in Computer Science (MIT)",
                date_appointed="2020-09-01"
            )
            db.add(lecturer_finch)
        else:
            lecturer_finch.rank = "Professor of Computer Science"
            lecturer_finch.faculty = "Faculty of Computing & Information Systems"
            lecturer_finch.department = "Department of Computer Science"
            lecturer_finch.research_focus = "Distributed Systems & High-Performance Computing"

        lecturer_davis = db.query(LecturerProfile).filter_by(user_id="FAC-108").first()
        if not lecturer_davis:
            lecturer_davis = LecturerProfile(
                user_id="FAC-108",
                staff_id="STAFF-FAC-108",
                rank="Senior Lecturer",
                faculty="Faculty of Computing & Information Systems",
                department="Department of Software Engineering",
                office_location="Science Complex, Block C, Room 112",
                research_focus="Distributed Systems & Formal Verification",
                highest_qualification="Ph.D. in Software Engineering",
                date_appointed="2022-01-10"
            )
            db.add(lecturer_davis)
        else:
            lecturer_davis.faculty = "Faculty of Computing & Information Systems"
            lecturer_davis.department = "Department of Software Engineering"
        db.commit()

        # Seed Student Profiles
        student_sophia = db.query(StudentProfile).filter_by(user_id="STU-2026-089").first()
        if not student_sophia:
            student_sophia = StudentProfile(
                user_id="STU-2026-089",
                matric_number="SCI/2026/0491",
                level="300 Level",
                program="B.Sc Computer Science",
                faculty="Faculty of Computing & Information Systems",
                department="Department of Computer Science",
                cgpa=3.85,
                admission_year="2023",
                guardian_name="Eleanor Vance-Chen",
                guardian_phone="+1 (555) 304-9912",
                guardian_email="eleanor.vance@family.org",
                status="Active"
            )
            db.add(student_sophia)
            student_sophia.program = "B.Sc Computer Science"
            student_sophia.faculty = "Faculty of Computing & Information Systems"
            student_sophia.department = "Department of Computer Science"
            if not getattr(student_sophia, "phone", None):
                student_sophia.phone = "+1 (555) 234-8901"
            if not getattr(student_sophia, "address", None):
                student_sophia.address = "Plot 14, Academic Hills, University City"
            if not getattr(student_sophia, "hall_of_residence", None):
                student_sophia.hall_of_residence = "Queen Idia Hall, Block C, Room 14"
            if not getattr(student_sophia, "bio", None):
                student_sophia.bio = "Undergraduate Scholar majoring in Computer Science with a focus on Distributed Systems and Software Architecture."

        student_david = db.query(StudentProfile).filter_by(user_id="STU-2023-104").first()
        if not student_david:
            student_david = StudentProfile(
                user_id="STU-2023-104",
                matric_number="CSC/2023/1042",
                level="300 Level",
                program="B.Sc Computer Science",
                faculty="Faculty of Computing & Information Systems",
                department="Department of Computer Science",
                cgpa=1.82,
                admission_year="2023",
                status="Active"
            )
            db.add(student_david)
        else:
            student_david.program = "B.Sc Computer Science"
            student_david.faculty = "Faculty of Computing & Information Systems"
            student_david.department = "Department of Computer Science"

        student_chidinma = db.query(StudentProfile).filter_by(user_id="STU-2024-048").first()
        if not student_chidinma:
            student_chidinma = StudentProfile(
                user_id="STU-2024-048",
                matric_number="MEE/2024/0488",
                level="200 Level",
                program="B.Eng Mechanical Engineering",
                faculty="Faculty of Engineering",
                department="Mechanical Engineering",
                cgpa=1.45,
                admission_year="2024",
                status="Active"
            )
            db.add(student_chidinma)
        db.commit()

        # 4. Courses & Enrollments
        print("[4/6] Seeding Accredited Courses and Enrollments...")
        courses_data = [
            # 100 Level Courses
            {
                "code": "CSC 101",
                "title": "Introduction to Computer Science & Problem Solving",
                "credit_units": 3,
                "level": "100 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Core Compulsory",
                "prerequisite_course_code": None,
                "lecturer_id": lecturer_finch.id,
                "description": "Foundations of computing, algorithmic thinking, number systems, and computational problem solving."
            },
            {
                "code": "MTH 101",
                "title": "Elementary Mathematics I (Algebra & Calculus)",
                "credit_units": 3,
                "level": "100 Level",
                "semester": "First Semester",
                "department": "Department of Mathematics",
                "category": "Core Compulsory",
                "prerequisite_course_code": None,
                "lecturer_id": None,
                "description": "Real numbers, set theory, functions, polynomial equations, differentiation and integration fundamentals."
            },
            {
                "code": "GST 101",
                "title": "Use of English & Academic Communication",
                "credit_units": 2,
                "level": "100 Level",
                "semester": "First Semester",
                "department": "General Studies Unit",
                "category": "General Studies",
                "prerequisite_course_code": None,
                "lecturer_id": None,
                "description": "Lexical competence, academic writing, critical reading, logical reasoning, and presentation skills."
            },

            # 200 Level Courses
            {
                "code": "CSC 201",
                "title": "Computer Programming I (Structured C & Systems)",
                "credit_units": 3,
                "level": "200 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Core Compulsory",
                "prerequisite_course_code": "CSC 101",
                "lecturer_id": lecturer_finch.id,
                "description": "Structured programming in C, pointers, memory allocation, file I/O, and data structure primitives."
            },
            {
                "code": "MTH 201",
                "title": "Mathematical Methods I (Linear Algebra & ODE)",
                "credit_units": 3,
                "level": "200 Level",
                "semester": "First Semester",
                "department": "Department of Mathematics",
                "category": "Core Compulsory",
                "prerequisite_course_code": "MTH 101",
                "lecturer_id": None,
                "description": "Matrix operations, eigenvalues, eigenvectors, systems of linear equations, and first-order differential equations."
            },
            {
                "code": "CSC 205",
                "title": "Foundations of Operating Systems & Assembly",
                "credit_units": 3,
                "level": "200 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Core Compulsory",
                "prerequisite_course_code": "CSC 101",
                "lecturer_id": lecturer_finch.id,
                "description": "Computer architecture, x86 assembly, interrupt handling, CPU registers, and low-level system calls."
            },
            {
                "code": "ENG 203",
                "title": "Applied Thermodynamics",
                "credit_units": 3,
                "level": "200 Level",
                "semester": "First Semester",
                "department": "Mechanical Engineering",
                "category": "Core Compulsory",
                "prerequisite_course_code": None,
                "lecturer_id": None,
                "description": "Laws of thermodynamics, entropy, power cycles, and heat engine efficiencies."
            },

            # 300 Level Courses (Current Level for Sophia & David)
            {
                "code": "CSC 301",
                "title": "Advanced Data Structures & Algorithms",
                "credit_units": 3,
                "level": "300 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Core Compulsory",
                "prerequisite_course_code": "CSC 201",
                "lecturer_id": lecturer_finch.id,
                "description": "Analysis of algorithms, balanced search trees, graph theory, NP-completeness, and dynamic programming."
            },
            {
                "code": "CSC 303",
                "title": "Operating Systems & Distributed Architecture",
                "credit_units": 3,
                "level": "300 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Core Compulsory",
                "prerequisite_course_code": "CSC 205",
                "lecturer_id": lecturer_finch.id,
                "description": "Kernel architecture, process synchronization, paging, distributed shared memory, and cluster scheduling."
            },
            {
                "code": "SEN 305",
                "title": "Software Architecture & Design Patterns",
                "credit_units": 2,
                "level": "300 Level",
                "semester": "First Semester",
                "department": "Department of Software Engineering",
                "category": "Core Compulsory",
                "prerequisite_course_code": None,
                "lecturer_id": lecturer_davis.id,
                "description": "Architectural styles, microservices, enterprise integration patterns, domain-driven design, and clean architecture."
            },
            {
                "code": "CSC 305",
                "title": "Database Systems & Information Architecture",
                "credit_units": 3,
                "level": "300 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Core Compulsory",
                "prerequisite_course_code": None,
                "lecturer_id": lecturer_davis.id,
                "description": "Relational calculus, query optimization, ACID transactions, NoSQL graph databases, and distributed sharding."
            },
            {
                "code": "CSC 307",
                "title": "Artificial Intelligence & Neural Networks",
                "credit_units": 3,
                "level": "300 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Elective",
                "prerequisite_course_code": "MTH 201",
                "lecturer_id": lecturer_finch.id,
                "description": "Heuristic search, knowledge representation, backpropagation neural networks, transformers, and automated reasoning."
            },
            {
                "code": "CSC 309",
                "title": "Compiler Construction & Formal Languages",
                "credit_units": 3,
                "level": "300 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Elective",
                "prerequisite_course_code": "CSC 201",
                "lecturer_id": lecturer_finch.id,
                "description": "Lexical analysis, LL/LR parsing tables, syntax-directed translation, symbol tables, and code generation."
            },
            {
                "code": "CSC 311",
                "title": "Computer Networks & Cloud Infrastructure",
                "credit_units": 3,
                "level": "300 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Elective",
                "prerequisite_course_code": None,
                "lecturer_id": lecturer_davis.id,
                "description": "TCP/IP socket architecture, software-defined networking, SDN controllers, cloud provisioning, and virtualization."
            },
            {
                "code": "CSC 313",
                "title": "Human-Computer Interaction & Cognitive Systems",
                "credit_units": 2,
                "level": "300 Level",
                "semester": "First Semester",
                "department": "Department of Computer Science",
                "category": "Elective",
                "prerequisite_course_code": None,
                "lecturer_id": None,
                "description": "Usability engineering, mental models, Fitts' law, accessibility guidelines, heuristics, and user experience metrics."
            }
        ]

        course_objs = {}
        for c in courses_data:
            course = db.query(Course).filter_by(code=c["code"]).first()
            if not course:
                course = Course(
                    code=c["code"],
                    title=c["title"],
                    credit_units=c["credit_units"],
                    level=c["level"],
                    semester=c["semester"],
                    department=c["department"],
                    category=c.get("category", "Core Compulsory"),
                    prerequisite_course_code=c.get("prerequisite_course_code"),
                    lecturer_id=c["lecturer_id"],
                    description=c["description"]
                )
                db.add(course)
                db.flush()
            else:
                course.title = c["title"]
                course.credit_units = c["credit_units"]
                course.level = c["level"]
                course.semester = c["semester"]
                course.department = c["department"]
                course.category = c.get("category", "Core Compulsory")
                course.prerequisite_course_code = c.get("prerequisite_course_code")
                course.description = c["description"]
                if c["lecturer_id"]:
                    course.lecturer_id = c["lecturer_id"]
            course_objs[c["code"]] = course
        db.commit()

        # Seed Transcripts and Historical Grades
        # 1. Sophia Chen (300 Level):
        # Passed 100L: CSC 101, MTH 101, GST 101
        # Passed 200L: CSC 201, CSC 205
        # FAILED CARRYOVER from 200L First Semester: MTH 201 (Grade F, 34/100, 3 Units)
        sophia_transcripts = [
            # 100 Level (Session 2024/2025)
            {"code": "CSC 101", "session": "2024/2025", "semester": "First Semester", "ca": 27.0, "exam": 58.0, "total": 85.0, "grade": "A", "gp": 5.0},
            {"code": "MTH 101", "session": "2024/2025", "semester": "First Semester", "ca": 25.0, "exam": 53.0, "total": 78.0, "grade": "A", "gp": 5.0},
            {"code": "GST 101", "session": "2024/2025", "semester": "First Semester", "ca": 28.0, "exam": 61.0, "total": 89.0, "grade": "A", "gp": 5.0},
            # 200 Level (Session 2025/2026)
            {"code": "CSC 201", "session": "2025/2026", "semester": "First Semester", "ca": 28.0, "exam": 60.0, "total": 88.0, "grade": "A", "gp": 5.0},
            {"code": "CSC 205", "session": "2025/2026", "semester": "First Semester", "ca": 26.0, "exam": 58.0, "total": 84.0, "grade": "A", "gp": 5.0},
            # *** THE MANDATORY CARRYOVER: MTH 201 failed in 200L ***
            {"code": "MTH 201", "session": "2025/2026", "semester": "First Semester", "ca": 12.0, "exam": 22.0, "total": 34.0, "grade": "F", "gp": 0.0},
        ]

        for tr in sophia_transcripts:
            c = course_objs.get(tr["code"])
            if c:
                g = db.query(ExamGrade).filter_by(student_id=student_sophia.id, course_id=c.id, session=tr["session"]).first()
                if not g:
                    db.add(ExamGrade(
                        student_id=student_sophia.id,
                        course_id=c.id,
                        session=tr["session"],
                        semester=tr["semester"],
                        ca_score=tr["ca"],
                        exam_score=tr["exam"],
                        total_score=tr["total"],
                        letter_grade=tr["grade"],
                        grade_point=tr["gp"],
                        approved_by_senate=True
                    ))
                else:
                    g.ca_score = tr["ca"]
                    g.exam_score = tr["exam"]
                    g.total_score = tr["total"]
                    g.letter_grade = tr["grade"]
                    g.grade_point = tr["gp"]
        db.commit()

        # 2. David Adeleke (300 Level - Warning):
        # Failed 200L carryovers: CSC 201 (Grade F) and MTH 201 (Grade F)
        david_transcripts = [
            {"code": "CSC 201", "session": "2025/2026", "semester": "First Semester", "ca": 11.0, "exam": 20.0, "total": 31.0, "grade": "F", "gp": 0.0},
            {"code": "MTH 201", "session": "2025/2026", "semester": "First Semester", "ca": 10.0, "exam": 18.0, "total": 28.0, "grade": "F", "gp": 0.0},
        ]
        for tr in david_transcripts:
            c = course_objs.get(tr["code"])
            if c:
                g = db.query(ExamGrade).filter_by(student_id=student_david.id, course_id=c.id, session=tr["session"]).first()
                if not g:
                    db.add(ExamGrade(
                        student_id=student_david.id,
                        course_id=c.id,
                        session=tr["session"],
                        semester=tr["semester"],
                        ca_score=tr["ca"],
                        exam_score=tr["exam"],
                        total_score=tr["total"],
                        letter_grade=tr["grade"],
                        grade_point=tr["gp"],
                        approved_by_senate=True
                    ))
        db.commit()

        # Attendance for Sophia & David
        att1 = db.query(AttendanceRecord).filter_by(student_id=student_sophia.id, course_id=course_objs["CSC 301"].id).first()
        if not att1:
            db.add(AttendanceRecord(
                course_id=course_objs["CSC 301"].id,
                student_id=student_sophia.id,
                lecturer_id=lecturer_finch.id,
                lecture_date="2026-10-28",
                status="present",
                notes="Participated actively in AVL trees discussion"
            ))
            db.add(AttendanceRecord(
                course_id=course_objs["CSC 301"].id,
                student_id=student_david.id,
                lecturer_id=lecturer_finch.id,
                lecture_date="2026-10-28",
                status="absent",
                notes="Unexcused absence"
            ))
        db.commit()

        # 5. Institutional Notices
        print("[5/6] Seeding Senate Circulars & Institutional Notices...")
        notices_data = [
            {
                "title": "Senate Approval of 2026/2027 Academic Calendar & Exam Schedule",
                "description": "The University Senate at its 348th Regular Session approved the official timeline for Harmattan Semester examinations commencing March 16, 2027.",
                "sender": "Office of the Registrar",
                "audience": "all",
                "priority": "Urgent",
                "date": "28 Oct 2026"
            },
            {
                "title": "National Accreditation Peer-Review Visit for Computing & Engineering",
                "description": "External accreditation panel from the National Universities Commission (NUC) is scheduled to evaluate computing laboratories, research facilities, and faculty credentials.",
                "sender": "Academic Planning Directorate",
                "audience": "faculty",
                "priority": "Important",
                "date": "27 Oct 2026"
            },
            {
                "title": "Final Notice: Harmattan Semester Course Registration & Tuition Settlement",
                "description": "Late course registration and bursary tuition clearance will permanently close at midnight on Friday. Biometric digital examination passes will only be generated for 100% cleared students.",
                "sender": "University Bursary",
                "audience": "students",
                "priority": "Urgent",
                "date": "25 Oct 2026"
            },
            {
                "title": "Annual University Research Exhibition & Tech Innovation Challenge 2026",
                "description": "Registration is now open for students and faculty research groups to present interdisciplinary research and software engineering projects at the Senate Exhibition Hall.",
                "sender": "Dean of Student Affairs",
                "audience": "all",
                "priority": "Event",
                "date": "22 Oct 2026"
            }
        ]

        for n in notices_data:
            existing = db.query(CampusNotice).filter_by(title=n["title"]).first()
            if not existing:
                db.add(CampusNotice(**n))
        db.commit()

        # 6. Academic Standing & Retention Watchlist Records
        print("[6/6] Seeding Academic Standing & Retention Watchlist Records...")
        telemetry_data = [
            {
                "name": "David Adeleke",
                "matric_no": "CSC/2023/1042",
                "initials": "DA",
                "department": "Computer Science",
                "level": "300 Level",
                "cgpa": 1.82,
                "risk_category": "attendance",
                "risk_vector": "Attendance 58% (< 75% Exam Threshold)",
                "flagged_course": "CSC 301 — Advanced Algorithms",
                "ai_confidence": 94,
                "status": "Unaddressed"
            },
            {
                "name": "Chidinma Okoye",
                "matric_no": "MEE/2024/0488",
                "initials": "CO",
                "department": "Mechanical Engineering",
                "level": "200 Level",
                "cgpa": 1.45,
                "risk_category": "probation",
                "risk_vector": "Probation Risk (CGPA 1.45 < 1.50)",
                "flagged_course": "ENG 203 — Applied Thermodynamics",
                "ai_confidence": 91,
                "status": "Unaddressed"
            },
            {
                "name": "Emmanuel Babatunde",
                "matric_no": "LAW/2022/0119",
                "initials": "EB",
                "department": "Faculty of Law",
                "level": "400 Level",
                "cgpa": 2.15,
                "risk_category": "academic",
                "risk_vector": "CAT 1 Score: 8/30 (Course Failure Risk)",
                "flagged_course": "PUL 401 — Law of Evidence",
                "ai_confidence": 87,
                "status": "Advisor Alerted"
            },
            {
                "name": "Fatima Al-Hassan",
                "matric_no": "BCH/2023/0754",
                "initials": "FA",
                "department": "Biochemistry",
                "level": "300 Level",
                "cgpa": 1.90,
                "risk_category": "attendance",
                "risk_vector": "Attendance 62% (< 75% Exam Threshold)",
                "flagged_course": "BCH 305 — Enzymology",
                "ai_confidence": 89,
                "status": "Unaddressed"
            },
            {
                "name": "Olumide Fashola",
                "matric_no": "ECN/2024/0932",
                "initials": "OF",
                "department": "Economics",
                "level": "200 Level",
                "cgpa": 1.38,
                "risk_category": "probation",
                "risk_vector": "Probation Risk (CGPA 1.38 < 1.50)",
                "flagged_course": "ECN 201 — Macroeconomic Theory",
                "ai_confidence": 96,
                "status": "Under Supervision"
            }
        ]

        for t in telemetry_data:
            rec = db.query(StudentRiskRecord).filter_by(matric_no=t["matric_no"]).first()
            if not rec:
                db.add(StudentRiskRecord(**t))
        db.commit()

        print("==================================================")
        print("Database Seeding Completed Successfully!")
        print(f"Users Count:       {db.query(User).count()}")
        print(f"Lecturers Count:   {db.query(LecturerProfile).count()}")
        print(f"Students Count:    {db.query(StudentProfile).count()}")
        print(f"Courses Count:     {db.query(Course).count()}")
        print(f"Notices Count:     {db.query(CampusNotice).count()}")
        print(f"Risk Alerts Count: {db.query(StudentRiskRecord).count()}")
        print("==================================================")

    except Exception as e:
        db.rollback()
        print(f"ERROR during seeding: {e}")
        raise e
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
