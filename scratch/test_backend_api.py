import sys
from pathlib import Path

# Add backend directory to path
backend_path = Path(__file__).resolve().parent.parent / "backend"
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

from fastapi.testclient import TestClient
from app.main import app

def run_api_tests():
    print("==================================================")
    print("SmartCampus Security & Database API Test Suite")
    print("==================================================")

    client = TestClient(app)
    passed = 0
    total = 0

    def assert_test(name, condition, details=""):
        nonlocal passed, total
        total += 1
        if condition:
            passed += 1
            print(f"  [PASS] {name} {details}")
        else:
            print(f"  [FAIL] {name} {details}")
            raise AssertionError(f"Test failed: {name} - {details}")

    # 1. Health
    res = client.get("/health")
    assert_test("Health Check", res.status_code == 200 and res.json()["database"] == "connected", f"Status: {res.status_code}")

    # 2. Tenant Info
    res = client.get("/api/v1/auth/tenant-info")
    assert_test("Tenant Info", res.status_code == 200 and "Apex Metropolitan University" in res.json()["institution_name"])

    # 3. Database Authentication Verification (Strict Bcrypt Verification)
    # 3a. Login by Email
    res = client.post("/api/v1/auth/login", json={
        "identifier": "a.finch@campus.edu",
        "password": "CampusPass@2026"
    })
    assert_test("Database Login by Email", res.status_code == 200 and res.json()["user"]["name"] == "Prof. Alistair Finch")
    lecturer_token = res.json()["access_token"]
    assert_test("Lecturer JWT Token Generated", len(lecturer_token) > 20)

    # 3b. Login by Student Matriculation Number
    res = client.post("/api/v1/auth/login", json={
        "identifier": "SCI/2026/0491",
        "password": "CampusPass@2026"
    })
    assert_test("Database Login by Matriculation No", res.status_code == 200 and res.json()["user"]["matric_number"] == "SCI/2026/0491")
    student_token = res.json()["access_token"]

    # 3c. Login by Staff ID
    res = client.post("/api/v1/auth/login", json={
        "identifier": "STAFF-FAC-104",
        "password": "CampusPass@2026"
    })
    assert_test("Database Login by Staff ID", res.status_code == 200 and res.json()["user"]["staff_id"] == "STAFF-FAC-104")

    # 3d. Login as Super Admin
    res = client.post("/api/v1/auth/login", json={
        "identifier": "superadmin@devcompany.io",
        "password": "CampusPass@2026"
    })
    assert_test("Database Login by Super Admin", res.status_code == 200 and res.json()["user"]["role"] == "super-admin")
    super_admin_token = res.json()["access_token"]

    # 4. Strict Security Rejections (Security is NOT Undermined)
    # 4a. Wrong Password must be rejected with 401
    res = client.post("/api/v1/auth/login", json={
        "identifier": "a.finch@campus.edu",
        "password": "WrongPassword@999"
    })
    assert_test("Reject Incorrect Password", res.status_code == 401 and "Incorrect password" in res.json()["detail"])

    # 4b. Unknown identifier must be rejected with 401
    res = client.post("/api/v1/auth/login", json={
        "identifier": "hacker.unknown@external.net",
        "password": "CampusPass@2026"
    })
    assert_test("Reject Unknown Identifier", res.status_code == 401 and "account not found" in res.json()["detail"].lower())

    # 4c. Empty password must be rejected
    res = client.post("/api/v1/auth/login", json={
        "identifier": "a.finch@campus.edu",
        "password": ""
    })
    assert_test("Reject Empty Password", res.status_code == 401)

    # 5. Token Verification (/auth/me)
    # 5a. Valid Bearer Token
    res = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {lecturer_token}"})
    assert_test("Verify /auth/me with Valid Token", res.status_code == 200 and res.json()["role"] == "lecturer")

    # 5b. Missing Token must be rejected with 401
    res = client.get("/api/v1/auth/me")
    assert_test("Reject /auth/me without Token", res.status_code == 401)

    # 5c. Corrupt Token must be rejected with 401
    res = client.get("/api/v1/auth/me", headers={"Authorization": "Bearer fake.corrupted.token"})
    assert_test("Reject Corrupted JWT Token", res.status_code == 401)

    # 6. Role-Based Access Control (RBAC) Enforcement
    # 6a. Student cannot create new administrators (Must return 403 Forbidden)
    res = client.post("/api/v1/auth/admins", json={
        "name": "Unauthorized User",
        "email": "intruder@campus.edu"
    }, headers={"Authorization": f"Bearer {student_token}"})
    assert_test("RBAC: Student Blocked from Admin Provisioning (403)", res.status_code == 403)

    # 6b. Super Admin CAN create new administrators
    new_admin_email = f"test.admin.{int(total)}@campus.edu"
    res = client.post("/api/v1/auth/admins", json={
        "name": "Audit Delegated Admin",
        "email": new_admin_email,
        "department": "Examinations Board"
    }, headers={"Authorization": f"Bearer {super_admin_token}"})
    assert_test("RBAC: Super Admin Authorized for Admin Provisioning (200)", res.status_code == 200 and res.json()["email"] == new_admin_email)
    created_admin_id = res.json()["id"]

    # 6c. Super Admin can revoke administrator
    res = client.delete(f"/api/v1/auth/admins/{created_admin_id}", headers={"Authorization": f"Bearer {super_admin_token}"})
    assert_test("RBAC: Super Admin Revoke Admin Access", res.status_code == 200)

    # 6d. Student cannot trigger academic retention intervention
    res = client.post("/api/v1/telemetry/intervene", json={
        "studentId": 1,
        "action": "Remedial Tutoring Assigned"
    }, headers={"Authorization": f"Bearer {student_token}"})
    assert_test("RBAC: Student Blocked from Interventions (403)", res.status_code == 403)

    # 6e. Lecturer CAN trigger academic retention intervention
    res = client.post("/api/v1/telemetry/intervene", json={
        "studentId": 1,
        "action": "Remedial Tutoring Assigned"
    }, headers={"Authorization": f"Bearer {lecturer_token}"})
    assert_test("RBAC: Lecturer Authorized for Interventions (200)", res.status_code == 200 and "Remedial Tutoring Assigned" in res.json()["message"])

    # 7. Institution Configuration PUT requires Admin clearance
    res = client.put("/api/v1/institution/config", json={
        "portalSubtitle": "University Academic Portal & SIS"
    })
    assert_test("RBAC: Unauthenticated Blocked from Updating Config (401)", res.status_code == 401)

    res = client.put("/api/v1/institution/config", json={
        "portalSubtitle": "University Academic Portal & SIS"
    }, headers={"Authorization": f"Bearer {super_admin_token}"})
    assert_test("RBAC: Super Admin Authorized to Update Config (200)", res.status_code == 200)

    # 8. Course & Academic Dossiers
    res = client.get("/api/v1/courses")
    assert_test("List Courses", res.status_code == 200 and len(res.json()) >= 4)

    # 8b. Student blocked from submitting grades
    csc301_id = [c["id"] for c in res.json() if c["code"] == "CSC 301"][0]
    res = client.post(f"/api/v1/courses/{csc301_id}/grades", json={
        "session": "2026/2027",
        "semester": "First Semester",
        "grades": [{"studentId": 1, "caScore": 30.0, "examScore": 70.0}]
    }, headers={"Authorization": f"Bearer {student_token}"})
    assert_test("RBAC: Student Blocked from Submitting Grades (403)", res.status_code == 403)

    # 8c. Lecturer authorized to submit grades
    res = client.post(f"/api/v1/courses/{csc301_id}/grades", json={
        "session": "2026/2027",
        "semester": "First Semester",
        "grades": [{"studentId": 1, "caScore": 28.0, "examScore": 64.0}]
    }, headers={"Authorization": f"Bearer {lecturer_token}"})
    assert_test("RBAC: Lecturer Authorized to Submit Grades (200)", res.status_code == 200)

    # 9. List Admins requires admin clearance
    res = client.get("/api/v1/auth/admins", headers={"Authorization": f"Bearer {student_token}"})
    assert_test("RBAC: Student Blocked from Admin Directory (403)", res.status_code == 403)

    res = client.get("/api/v1/auth/admins", headers={"Authorization": f"Bearer {super_admin_token}"})
    assert_test("RBAC: Super Admin Access to Admin Directory (200)", res.status_code == 200 and len(res.json()) >= 2)

    print("==================================================")
    print(f"All {passed}/{total} Security & API Tests Passed Cleanly!")
    print("==================================================")

if __name__ == "__main__":
    run_api_tests()
