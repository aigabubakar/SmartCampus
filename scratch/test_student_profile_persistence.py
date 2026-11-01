import requests
import sqlite3

BASE_URL = "http://127.0.0.1:8000/api/v1"

def run_tests():
    print("==================================================")
    print("TEST SUITE: Student Profile Setup & Persistence")
    print("==================================================")

    # 1. Login as Student Sophia Chen
    login_res = requests.post(f"{BASE_URL}/auth/login", json={
        "identifier": "SCI/2026/0491",
        "password": "CampusPass@2026"
    })
    assert login_res.status_code == 200, f"Login failed: {login_res.text}"
    token = login_res.json()["access_token"]
    user = login_res.json()["user"]
    print(f"[PASS] Logged in as: {user['name']} ({user['matric_number']})")
    headers = {"Authorization": f"Bearer {token}"}

    # 2. GET /students/me
    me_res = requests.get(f"{BASE_URL}/students/me", headers=headers)
    assert me_res.status_code == 200, f"GET /students/me failed: {me_res.text}"
    dossier = me_res.json()
    assert dossier["matricNumber"] == "SCI/2026/0491"
    print(f"[PASS] GET /students/me returned dossier with phone: {dossier.get('phone')} and hall: {dossier.get('hallOfResidence')}")

    # 3. GET /students/{identifier}
    id_res = requests.get(f"{BASE_URL}/students/SCI/2026/0491", headers=headers)
    assert id_res.status_code == 200, f"GET /students/SCI/2026/0491 failed: {id_res.text}"
    assert id_res.json()["name"] == user["name"]
    print("[PASS] GET /students/SCI/2026/0491 matches")

    # 4. PUT /students/me - Update personal & guardian profile
    update_payload = {
        "name": "Sophia A. Chen",
        "phone": "+1 (555) 777-8899",
        "address": "42 Scholars Boulevard, Apex Campus, University City",
        "hallOfResidence": "Queen Idia Hall, Penthouse Suite 01",
        "guardianName": "Eleanor Vance-Chen, Ph.D.",
        "guardianPhone": "+1 (555) 304-9912",
        "guardianEmail": "eleanor.vance@chambers.org",
        "bio": "Honors Undergraduate Scholar specializing in Distributed Operating Systems and AI-driven Campus Infrastructure."
    }
    put_res = requests.put(f"{BASE_URL}/students/me", json=update_payload, headers=headers)
    assert put_res.status_code == 200, f"PUT /students/me failed: {put_res.text}"
    updated_dossier = put_res.json()
    assert updated_dossier["name"] == "Sophia A. Chen"
    assert updated_dossier["phone"] == "+1 (555) 777-8899"
    assert updated_dossier["address"] == "42 Scholars Boulevard, Apex Campus, University City"
    assert updated_dossier["hallOfResidence"] == "Queen Idia Hall, Penthouse Suite 01"
    assert updated_dossier["guardianName"] == "Eleanor Vance-Chen, Ph.D."
    assert updated_dossier["bio"] == update_payload["bio"]
    print("[PASS] PUT /students/me updated and returned matching dossier")

    # 5. Verify direct SQLite persistence
    conn = sqlite3.connect("backend/smartcampus.db")
    c = conn.cursor()
    c.execute("SELECT name FROM users WHERE id='STU-2026-089'")
    db_name = c.fetchone()[0]
    assert db_name == "Sophia A. Chen", f"Database user name not persisted: {db_name}"

    c.execute("SELECT phone, address, hall_of_residence, guardian_name, bio FROM students WHERE matric_number='SCI/2026/0491'")
    row = c.fetchone()
    assert row[0] == "+1 (555) 777-8899", f"Database phone mismatch: {row[0]}"
    assert row[1] == "42 Scholars Boulevard, Apex Campus, University City", f"Database address mismatch: {row[1]}"
    assert row[2] == "Queen Idia Hall, Penthouse Suite 01", f"Database hall mismatch: {row[2]}"
    assert row[3] == "Eleanor Vance-Chen, Ph.D.", f"Database guardian mismatch: {row[3]}"
    print("[PASS] Verified direct persistence in SQLite database tables ('users' & 'students')")
    conn.close()

    # 6. Verify security lock: Student cannot modify another student's record
    unauth_put = requests.put(f"{BASE_URL}/students/CSC/2023/1042", json={"name": "Hacked Student"}, headers=headers)
    assert unauth_put.status_code == 403, f"Expected 403 Forbidden, got: {unauth_put.status_code}"
    print("[PASS] Student blocked from editing another student's dossier (HTTP 403 Forbidden)")

    # 7. Verify security lock: Student cannot modify academic locks (e.g., program, status, level)
    tamper_put = requests.put(f"{BASE_URL}/students/me", json={
        "program": "Doctor of Philosophy in Computer Science",
        "status": "Graduated with Highest Honors",
        "level": "Postgraduate 900 Level"
    }, headers=headers)
    assert tamper_put.status_code == 200
    res_tamper = tamper_put.json()
    assert res_tamper["program"] == "B.Sc Computer Science", f"Academic program was modified by student! {res_tamper['program']}"
    assert res_tamper["level"] == "300 Level", f"Academic level was modified by student! {res_tamper['level']}"
    print("[PASS] Academic locks intact: Student unable to alter program or level")

    # 8. Verify avatar update with preset
    avatar_preset_put = requests.put(f"{BASE_URL}/students/me", json={
        "avatar": "/assets/images/thumbs/user-img2.png"
    }, headers=headers)
    assert avatar_preset_put.status_code == 200, f"Preset avatar failed: {avatar_preset_put.text}"
    assert avatar_preset_put.json()["avatar"] == "/assets/images/thumbs/user-img2.png"

    conn = sqlite3.connect("backend/smartcampus.db")
    c = conn.cursor()
    c.execute("SELECT avatar FROM users WHERE id='STU-2026-089'")
    db_avatar = c.fetchone()[0]
    assert db_avatar == "/assets/images/thumbs/user-img2.png", f"Database avatar mismatch: {db_avatar}"
    conn.close()
    print("[PASS] Preset scholar avatar saved and persisted to database")

    # 9. Verify Base64 photograph upload & persistence
    # 1x1 transparent PNG in base64
    sample_b64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="
    avatar_b64_put = requests.put(f"{BASE_URL}/students/me", json={
        "avatar": sample_b64
    }, headers=headers)
    assert avatar_b64_put.status_code == 200, f"Base64 avatar failed: {avatar_b64_put.text}"
    saved_avatar_path = avatar_b64_put.json()["avatar"]
    assert saved_avatar_path.startswith("/uploads/avatars/"), f"Unexpected avatar path: {saved_avatar_path}"

    conn = sqlite3.connect("backend/smartcampus.db")
    c = conn.cursor()
    c.execute("SELECT avatar FROM users WHERE id='STU-2026-089'")
    db_avatar = c.fetchone()[0]
    assert db_avatar == saved_avatar_path, f"Database avatar mismatch: {db_avatar}"
    conn.close()
    print(f"[PASS] Base64 photograph decoded, stored to disk ({saved_avatar_path}), and persisted to database")

    print("\nALL STUDENT PROFILE & PHOTOGRAPH TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()

