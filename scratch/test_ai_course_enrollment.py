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

    # 5. Underload Test A: Attempting registration < 15 units WITHOUT underload justification
    print("\n[Step 5] Testing Underload Alert: Attempting registration (<15 units) without justification...")
    underload_course_ids = [mth201_id, current_courses[0]["id"]] # 3 units + 3 units = 6 units
    underload_fail_resp = requests.post(
        f"{BASE_URL}/enrollment/register",
        headers=headers,
        json={
            "session": "2026/2027",
            "semester": "First Semester",
            "courseIds": underload_course_ids
        }
    )
    assert underload_fail_resp.status_code == 422, f"Expected 422, got: {underload_fail_resp.status_code}"
    print(f"  [PASS] Underload blocked without justification: {underload_fail_resp.json()['detail']}")

    # 6. Underload Test B: Submitting registration < 15 units WITH Senate Underload Concession reason
    print("\n[Step 6] Testing Underload Concession Waiver: Registering 6 units with Senate justification...")
    underload_pass_resp = requests.post(
        f"{BASE_URL}/enrollment/register",
        headers=headers,
        json={
            "session": "2026/2027",
            "semester": "First Semester",
            "courseIds": underload_course_ids,
            "underloadReason": "Final Year / Graduating Clearance (Completing Remaining Degree Requirements)",
            "underloadNotes": "Approved by Level Adviser Prof. A. Finch for final semester graduation clearance."
        }
    )
    assert underload_pass_resp.status_code == 200, f"Expected 200 with concession, got: {underload_pass_resp.text}"
    underload_data = underload_pass_resp.json()
    assert underload_data["isUnderload"] is True, "Expected isUnderload=True"
    assert underload_data["underloadConcession"] is not None, "Expected underloadConcession object"
    concession_ref = underload_data["underloadConcession"]["concessionReference"]
    print(f"  [PASS] Underload concession granted! Senate Ref: {concession_ref}")
    print(f"  Reason: {underload_data['underloadConcession']['reason']}")

    # 7. Underload Slip Verification
    print("\n[Step 7] Checking Course Slip for Senate Underload Concession Seal...")
    underload_slip_resp = requests.get(f"{BASE_URL}/enrollment/slip", headers=headers)
    assert underload_slip_resp.status_code == 200
    underload_slip = underload_slip_resp.json()
    assert underload_slip["summary"]["isUnderload"] is True
    assert underload_slip["underloadConcession"] is not None
    assert underload_slip["underloadConcession"]["concessionReference"] == concession_ref
    print(f"  [PASS] Course Registration Slip stamped with: {underload_slip['underloadConcession']['concessionReference']}")
    print(f"  Regulatory Notice: {underload_slip['underloadConcession']['regulatoryNotice']}")

    # 8. Drop Protection Test: Attempting to drop mandatory carryover
    print("\n[Step 8] Testing Senate protection: Attempting to drop mandatory carryover...")
    drop_carryover_resp = requests.delete(f"{BASE_URL}/enrollment/drop/{mth201_id}", headers=headers)
    assert drop_carryover_resp.status_code == 422, f"Expected 422, got: {drop_carryover_resp.status_code}"
    print(f"  [PASS] Drop blocked as expected: {drop_carryover_resp.json()['detail']}")

    # 9. Restore Full Balanced Load (Carryover + 5 current courses = 17 Units)
    print("\n[Step 9] Restoring full balanced curriculum (Carryover + 5 fresh courses = 17 Units)...")
    full_load_ids = [mth201_id] + [c["id"] for c in current_courses[:5]]
    full_resp = requests.post(
        f"{BASE_URL}/enrollment/register",
        headers=headers,
        json={
            "session": "2026/2027",
            "semester": "First Semester",
            "courseIds": full_load_ids
        }
    )
    assert full_resp.status_code == 200
    print(f"  [PASS] Restored balanced registration: {full_resp.json()['totalCreditUnits']} Units.")

    print("\n==================================================")
    print("ALL AI ENROLLMENT & UNDERLOAD CONCESSION TESTS PASSED (100%)!")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
