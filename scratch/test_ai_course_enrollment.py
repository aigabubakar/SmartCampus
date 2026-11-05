import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000/api/v1"

def run_tests():
    print("==================================================")
    print("TEST SUITE: AI Course Enrollment & Carryover Engine")
    print("==================================================")

    # 1. Login as Sophia Chen
    print("\n[Step 1] Authenticating as Sophia Chen (SCI/2026/0491)...")
    login_resp = requests.post(f"{BASE_URL}/auth/login", json={
        "identifier": "sophia.chen@student.campus.edu",
        "password": "CampusPass@2026"
    })
    assert login_resp.status_code == 200, f"Login failed: {login_resp.text}"
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    print(f"  [PASS] Logged in successfully. Token acquired.")

    # 2. Call AI Enrollment Audit
    print("\n[Step 2] Auditing academic transcript for carryovers...")
    audit_resp = requests.get(f"{BASE_URL}/enrollment/audit", headers=headers)
    assert audit_resp.status_code == 200, f"Audit failed: {audit_resp.text}"
    audit_data = audit_resp.json()

    print(f"  Student: {audit_data['student']['name']} ({audit_data['student']['matricNumber']}) - {audit_data['student']['level']}")
    print(f"  Has Mandatory Carryovers: {audit_data['hasMandatoryCarryovers']}")
    print(f"  AI Advisory Headline: {audit_data['aiAdvisory']['headline']}")
    print(f"  AI Directive: {audit_data['aiAdvisory']['directive']}")

    assert audit_data["hasMandatoryCarryovers"] is True, "Expected mandatory carryovers to be True"
    assert len(audit_data["mandatoryCarryovers"]) >= 1, "Expected at least 1 mandatory carryover"
    
    carryover = audit_data["mandatoryCarryovers"][0]
    print(f"  [PASS] Detected carryover: {carryover['code']} - {carryover['title']} ({carryover['creditUnits']} Units, Prior Grade: {carryover['failedGrade']})")
    assert carryover["autoEnrolled"] is True, "Carryover should be autoEnrolled=True"
    assert carryover["locked"] is True, "Carryover should be locked=True"
    mth201_id = carryover["id"]

    # 3. Test Tamper Attempt: Registering ONLY current level courses and omitting the carryover
    print("\n[Step 3] Testing tamper-proofing: Attempting registration without carryover...")
    current_courses = audit_data["availableCourses"]
    current_course_ids = [c["id"] for c in current_courses[:4]] # 4 current courses, omitting MTH 201

    tamper_resp = requests.post(
        f"{BASE_URL}/enrollment/register",
        headers=headers,
        json={
            "session": "2026/2027",
            "semester": "First Semester",
            "courseIds": current_course_ids
        }
    )
    print(f"  Tamper response status: {tamper_resp.status_code}")
    assert tamper_resp.status_code == 422, f"Expected 422 Unprocessable Entity, got: {tamper_resp.status_code}"
    err_detail = tamper_resp.json()["detail"]
    print(f"  [PASS] Backend correctly rejected registration with AI Directive: {err_detail}")
    assert "mandatory carryover" in err_detail.lower(), "Error message should cite mandatory carryovers"

    # 4. Compliant Enrollment Test: Including mandatory carryover + current level courses
    print("\n[Step 4] Submitting compliant enrollment (Carryover + 300 Level Core)...")
    compliant_course_ids = [mth201_id] + [c["id"] for c in current_courses[:5]]
    reg_resp = requests.post(
        f"{BASE_URL}/enrollment/register",
        headers=headers,
        json={
            "session": "2026/2027",
            "semester": "First Semester",
            "courseIds": compliant_course_ids
        }
    )
    assert reg_resp.status_code == 200, f"Registration failed: {reg_resp.text}"
    reg_data = reg_resp.json()
    print(f"  [PASS] Enrollment confirmed! Registered: {reg_data['coursesCount']} courses, {reg_data['totalCreditUnits']} Units (Carryover Units: {reg_data['carryoverUnits']})")
    print(f"  Verification Hash: {reg_data['verificationHash']}")

    # 5. Drop Protection Test: Attempting to drop mandatory carryover
    print("\n[Step 5] Testing Senate protection: Attempting to drop mandatory carryover...")
    drop_carryover_resp = requests.delete(f"{BASE_URL}/enrollment/drop/{mth201_id}", headers=headers)
    assert drop_carryover_resp.status_code == 422, f"Expected 422, got: {drop_carryover_resp.status_code}"
    print(f"  [PASS] Drop blocked as expected: {drop_carryover_resp.json()['detail']}")

    # 6. Official Registration Slip Test
    print("\n[Step 6] Fetching Official Course Registration Slip...")
    slip_resp = requests.get(f"{BASE_URL}/enrollment/slip", headers=headers)
    assert slip_resp.status_code == 200, f"Slip fetch failed: {slip_resp.text}"
    slip_data = slip_resp.json()
    print(f"  Institution: {slip_data['institution']['name']}")
    print(f"  Total Registered Units: {slip_data['summary']['totalCreditUnits']}")
    print(f"  Carryover Units: {slip_data['summary']['carryoverUnits']}")
    print(f"  Verification Token: {slip_data['verificationToken']}")
    print("  Courses Breakdown:")
    for c in slip_data["courses"]:
        tag = "[CARRYOVER]" if c["isCarryover"] else f"[{c['category']}]"
        print(f"    - {c['code']} {tag}: {c['title']} ({c['creditUnits']} Units)")
    print("  [PASS] Official slip generated with verification token and signature blocks.")

    print("\n==================================================")
    print("ALL AI ENROLLMENT & CARRYOVER TESTS PASSED (100%)!")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
