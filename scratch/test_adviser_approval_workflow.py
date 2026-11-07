import requests
import json
import sys

BASE_URL = "http://127.0.0.1:8000/api/v1"

def print_section(title):
    print("\n" + "=" * 65)
    print(f" {title}")
    print("=" * 65)

def login(email, password):
    resp = requests.post(f"{BASE_URL}/auth/login", json={"identifier": email, "password": password})
    if resp.status_code != 200:
        raise Exception(f"Login failed for {email}: {resp.status_code} {resp.text}")
    data = resp.json()
    return data["access_token"], data["user"]

def main():
    print_section("E2E LEVEL ADVISER APPROVAL WORKFLOW TEST")

    # 1. Login as Student: Sophia Chen
    print("\n[Step 1] Logging in as Student Sophia Chen...")
    student_token, student_user = login("sophia.chen@student.campus.edu", "CampusPass@2026")
    student_headers = {"Authorization": f"Bearer {student_token}"}
    print(f"[OK] Student authenticated: {student_user['name']} (Role: {student_user['role']})")

    # 2. Audit Courses for Sophia
    print("\n[Step 2] Auditing Sophia's courses...")
    audit_resp = requests.get(f"{BASE_URL}/enrollment/audit", headers=student_headers)
    assert audit_resp.status_code == 200, f"Audit failed: {audit_resp.text}"
    audit = audit_resp.json()
    carryovers = audit.get("mandatoryCarryovers", [])
    fresh_courses = audit.get("availableCourses", [])
    print(f"[OK] Mandatory carryovers found: {[c['code'] for c in carryovers]}")
    print(f"[OK] Available current-level courses count: {len(fresh_courses)}")

    # Pick carryover courses (e.g. MTH 201) + 5 fresh courses (17 units total)
    selected_ids = [c["id"] for c in carryovers]
    for c in fresh_courses[:5]:
        if c["id"] not in selected_ids:
            selected_ids.append(c["id"])

    # 3. Student registers courses
    print(f"\n[Step 3] Submitting course registration ({len(selected_ids)} courses)...")
    reg_resp = requests.post(
        f"{BASE_URL}/enrollment/register",
        headers=student_headers,
        json={"courseIds": selected_ids, "session": "2026/2027", "semester": "First Semester"}
    )
    assert reg_resp.status_code == 200, f"Registration failed: {reg_resp.text}"
    reg_data = reg_resp.json()
    print(f"[OK] Registration submitted: status = {reg_data.get('approvalStatus')}")
    assert reg_data.get("approvalStatus") == "Pending Approval", "Approval status must be 'Pending Approval'"

    # 4. Verify student audit shows Pending Approval
    audit_resp = requests.get(f"{BASE_URL}/enrollment/audit", headers=student_headers)
    audit = audit_resp.json()
    print(f"[OK] Registration Status in Audit: {audit.get('registrationStatus')}")
    assert audit.get("registrationStatus") == "PENDING_APPROVAL"

    # 5. Login as Level Adviser: Prof. Alistair Finch
    print("\n[Step 4] Logging in as Level Adviser Prof. Alistair Finch...")
    adviser_token, adviser_user = login("a.finch@campus.edu", "CampusPass@2026")
    adviser_headers = {"Authorization": f"Bearer {adviser_token}"}
    print(f"[OK] Adviser authenticated: {adviser_user['name']} (Role: {adviser_user['role']})")

    # 6. Fetch Submissions for Adviser Console
    print("\n[Step 5] Adviser queries submission queue...")
    sub_resp = requests.get(f"{BASE_URL}/enrollment/adviser/submissions?session=2026/2027&semester=First+Semester", headers=adviser_headers)
    assert sub_resp.status_code == 200, f"Submissions query failed: {sub_resp.text}"
    submissions_data = sub_resp.json()
    summary = submissions_data.get("summary", {})
    submissions = submissions_data.get("submissions", [])
    print(f"[OK] Summary: Total={summary.get('totalSubmissions')}, Pending={summary.get('pendingCount')}, Approved={summary.get('approvedCount')}, Disapproved={summary.get('disapprovedCount')}")
    
    sophia_sub = next((s for s in submissions if s["matricNumber"] == "SCI/2026/0491"), None)
    assert sophia_sub is not None, "Sophia's submission must appear in adviser submissions!"
    print(f"[OK] Found Sophia's docket: ID={sophia_sub['studentId']}, Status={sophia_sub['approvalStatus']}, Units={sophia_sub['totalCreditUnits']}")

    # 7. Adviser inspects detailed docket
    print("\n[Step 6] Adviser fetches deep docket inspection...")
    detail_resp = requests.get(f"{BASE_URL}/enrollment/adviser/submission/{sophia_sub['studentId']}", headers=adviser_headers)
    assert detail_resp.status_code == 200, f"Detail fetch failed: {detail_resp.text}"
    detail = detail_resp.json()
    print(f"[OK] Detailed docket: Student={detail['student']['name']}, Courses count={len(detail['courses'])}, CGPA={detail['student']['cgpa']}")

    # 8. Adviser Disapproves Registration with Feedback
    print("\n[Step 7] Adviser disapproves registration with corrective feedback...")
    disapprove_resp = requests.post(
        f"{BASE_URL}/enrollment/adviser/reject",
        headers=adviser_headers,
        json={
            "studentId": sophia_sub["studentId"],
            "session": "2026/2027",
            "semester": "First Semester",
            "remarks": "Please review elective courses: Ensure you have taken CSC 309 before enrolling for advanced lab modules."
        }
    )
    assert disapprove_resp.status_code == 200, f"Disapproval failed: {disapprove_resp.text}"
    dis_res = disapprove_resp.json()
    print(f"[OK] Disapproval successful: status={dis_res.get('status')}, message={dis_res.get('message')}")

    # 9. Verify Sophia sees Disapproved status and remarks in audit
    print("\n[Step 8] Checking student perspective after disapproval...")
    audit_resp = requests.get(f"{BASE_URL}/enrollment/audit", headers=student_headers)
    audit = audit_resp.json()
    print(f"[OK] Student audit registrationStatus: {audit.get('registrationStatus')}")
    assert audit.get("registrationStatus") == "DISAPPROVED", "Status must be 'DISAPPROVED'"
    adviser_review = audit.get("adviserReview", {})
    print(f"[OK] Student sees remarks: \"{adviser_review.get('adviserRemarks')}\" by {adviser_review.get('adviserName')}")
    assert "review elective" in (adviser_review.get("adviserRemarks") or "")

    # 10. Student re-submits corrected registration
    print("\n[Step 9] Student re-submits registration...")
    re_sub_resp = requests.post(
        f"{BASE_URL}/enrollment/register",
        headers=student_headers,
        json={"courseIds": selected_ids, "session": "2026/2027", "semester": "First Semester"}
    )
    assert re_sub_resp.status_code == 200, f"Re-submission failed: {re_sub_resp.text}"
    print(f"[OK] Re-submission status: {re_sub_resp.json().get('approvalStatus')}")
    assert re_sub_resp.json().get("approvalStatus") == "Pending Approval"

    # 11. Adviser Approves Registration
    print("\n[Step 10] Adviser approves registration with endorsement remarks...")
    approve_resp = requests.post(
        f"{BASE_URL}/enrollment/adviser/approve",
        headers=adviser_headers,
        json={
            "studentId": sophia_sub["studentId"],
            "session": "2026/2027",
            "semester": "First Semester",
            "remarks": "Endorsed for 2026/2027 Harmattan Semester. Satisfies all prerequisite regulations."
        }
    )
    assert approve_resp.status_code == 200, f"Approval failed: {approve_resp.text}"
    app_res = approve_resp.json()
    print(f"[OK] Approval successful: status={app_res.get('status')}, endorsedBy={app_res.get('adviserName')}")

    # 12. Student fetches official Course Registration Slip
    print("\n[Step 11] Student checks official Course Registration Slip...")
    slip_resp = requests.get(f"{BASE_URL}/enrollment/slip", headers=student_headers)
    assert slip_resp.status_code == 200, f"Slip fetch failed: {slip_resp.text}"
    slip = slip_resp.json()
    adviser_app = slip.get("adviserApproval", {})
    print(f"[OK] Slip Adviser Approval: status={adviser_app.get('status')}, isApproved={adviser_app.get('isApproved')}")
    print(f"[OK] Signed by: {adviser_app.get('adviserName')}")
    print(f"[OK] Approval Timestamp: {adviser_app.get('approvedAt')}")
    print(f"[OK] Official Remarks: \"{adviser_app.get('adviserRemarks')}\"")
    assert adviser_app.get("isApproved") is True
    assert adviser_app.get("status") == "Approved"
    assert adviser_app.get("approvedAt") is not None
    assert "Endorsed for 2026/2027" in adviser_app.get("adviserRemarks")

    print_section("ALL LEVEL ADVISER APPROVAL & DISAPPROVAL TESTS PASSED 100%!")

if __name__ == "__main__":
    main()
