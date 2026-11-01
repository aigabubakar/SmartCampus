import { createRouter, createWebHistory } from 'vue-router'
import { useToastStore } from '@/stores/toast.js'

// Error Pages
import AccessDenied from './pages/error/AccessDenied.vue'

// Dashboards
import DashboardDispatcher from './pages/index/DashboardDispatcher.vue'
import Index1 from './pages/index/index1.vue'
import Index2 from './pages/index/index2.vue'
import Index3 from './pages/index/index3.vue'
import Index4 from './pages/index/index4.vue'
import Index5 from './pages/index/index5.vue'

// Students
import AddNewStudent from './pages/students/addNewStudent.vue'
import StudentList from './pages/students/studentList.vue'
import SuspendedStudent from './pages/students/suspendedStudent.vue'
import StudentCategory from './pages/students/studentCategory.vue'
import EditStudent from './pages/students/editStudent.vue'
import StudentDetails from './pages/students/studentDetails.vue'

// Teachers
import AddNewTeacher from './pages/teachers/addNewTeacher.vue'
import TeacherList from './pages/teachers/teacherList.vue'
import EditTeacher from './pages/teachers/editTeacher.vue'
import TeacherDetails from './pages/teachers/teacherDetails.vue'
import TeacherTimetable from './pages/teachers/teacherTimetable.vue'

// Guardians
import AddNewGuardian from './pages/guardians/addNewGuardian.vue'
import GuardianList from './pages/guardians/guardianList.vue'
import EditGuardian from './pages/guardians/editGuardian.vue'
import GuardianDetails from './pages/guardians/guardianDetails.vue'

// Class/Section
import SectionList from './pages/class/sectionList.vue'
import SubjectList from './pages/class/subjectList.vue'
import ClassList from './pages/class/classList.vue'
import ClassRoomList from './pages/class/classRoomList.vue'

// Examinations
import ExamList from './pages/examination/examList.vue'
import ExamScheduleList from './pages/examination/examScheduleList.vue'
import ExamResultList from './pages/examination/examResult.vue'

// Fees
import FeesCollectionList from './pages/fees/feesCollection.vue'
import FeesTypeList from './pages/fees/feesType.vue'
import FeesGroupList from './pages/fees/feesGroup.vue'
import FeesDiscountList from './pages/fees/feesDiscount.vue'

// Attendance & Leaves
import StudentAttendance from './pages/attendance/StudentAttendance.vue'
import TeacherAttendance from './pages/attendance/TeacherAttendance.vue'
import EmployeeAttendance from './pages/attendance/EmployeeAttendance.vue'
import LeaveTypes from './pages/leaves/LeaveTypes.vue'
import LeaveRequest from './pages/leaves/LeaveRequest.vue'

// Library & Certificates
import Certificate from './pages/certificate/Certificate.vue'
import BooksList from './pages/library/BooksList.vue'
import MembersList from './pages/library/MembersList.vue'
import MemberDetails from './pages/library/MemberDetails.vue'
import IssueReturn from './pages/library/IssueReturn.vue'

// Accounts
import IncomeHead from './pages/accounts/IncomeHead.vue'
import IncomeList from './pages/accounts/IncomeList.vue'
import ExpenseHead from './pages/accounts/ExpenseHead.vue'
import ExpenseList from './pages/accounts/ExpenseList.vue'
import Transaction from './pages/accounts/Transaction.vue'

// HRM & Staff Management
import EmployeeList from './pages/hrm/EmployeeList.vue'
import EmployeeDetails from './pages/hrm/EmployeeDetails.vue'
import AddEmployee from './pages/hrm/AddEmployee.vue'
import Payroll from './pages/hrm/Payroll.vue'
import Designation from './pages/hrm/Designation.vue'
import Department from './pages/hrm/Department.vue'

// Campus Operations & Governance
import NoticeBoard from './pages/noticeBoard/NoticeBoard.vue'
import Event from './pages/event/Event.vue'
import Message from './pages/message/Message.vue'
import SubscriptionPlan from './pages/subscriptionPlan/SubscriptionPlan.vue'
import RoleAccess from './pages/roleAccess/RoleAccess.vue'
import AssignRole from './pages/assignRole/AssignRole.vue'

// Settings
import GeneralSettings from './pages/settings/General.vue'
import NotificationSettings from './pages/settings/Notification.vue'
import CurrenciesSettings from './pages/settings/Currencies.vue'
import LanguagesSettings from './pages/settings/Languages.vue'

// Authentication
import LoginPage from './pages/authentication/Login.vue'
import RegisterPage from './pages/authentication/Register.vue'
import LockScreen from './pages/authentication/LockScreen.vue'
import ProfileDispatcher from './pages/profile/ProfileDispatcher.vue'

// Role definitions
const ROLE_SUPER_ADMIN = 'super-admin'
const ROLE_ADMIN = 'admin'
const ROLE_LECTURER = 'lecturer'
const ROLE_TEACHER = 'teacher'
const ROLE_STUDENT = 'student'
const ROLE_GUARDIAN = 'guardian'

const ROLES_ANY_ADMIN = [ROLE_SUPER_ADMIN, ROLE_ADMIN]
const ROLES_FACULTY_AND_ADMIN = [ROLE_SUPER_ADMIN, ROLE_ADMIN, ROLE_LECTURER, ROLE_TEACHER]
const ROLES_STUDENT_AND_ADMIN = [ROLE_SUPER_ADMIN, ROLE_ADMIN, ROLE_STUDENT]
const ROLES_ACADEMIC_AND_ADMIN = [ROLE_SUPER_ADMIN, ROLE_ADMIN, ROLE_LECTURER, ROLE_TEACHER, ROLE_STUDENT]
const ROLES_ALL_CAMPUS = [ROLE_SUPER_ADMIN, ROLE_ADMIN, ROLE_LECTURER, ROLE_TEACHER, ROLE_STUDENT, ROLE_GUARDIAN, 'parent']

// Routes
const routes = [
    // Entry & Authentication
    { path: '/', component: LoginPage, meta: { guestOnly: true } },
    { path: '/login', component: LoginPage, meta: { guestOnly: true } },
    { path: '/register', component: RegisterPage, meta: { guestOnly: true } },
    { path: '/lock-screen', component: LockScreen, meta: { requiresAuth: true, title: 'Workstation Locked' } },

    // Security & Access Denied
    { path: '/403', component: AccessDenied, meta: { requiresAuth: true, title: '403 Forbidden' } },

    // Dashboards & Profile
    { path: '/profile', component: ProfileDispatcher, meta: { requiresAuth: true, title: 'My Academic Dossier' } },
    { path: '/dashboard', component: DashboardDispatcher, meta: { requiresAuth: true, title: 'Campus Dashboard' } },
    { path: '/student-dashboard', component: Index2, meta: { requiresAuth: true, roles: ROLES_STUDENT_AND_ADMIN, title: 'Student Portal' } },
    { path: '/lecturer-dashboard', component: Index3, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecturer Console' } },
    { path: '/teacher-dashboard', component: Index3, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecturer Console' } },
    { path: '/admin-dashboard', component: Index1, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Executive Dashboard' } },
    { path: '/index-2', component: Index2, meta: { requiresAuth: true, roles: ROLES_STUDENT_AND_ADMIN } },
    { path: '/index-3', component: Index3, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN } },
    { path: '/index-4', component: Index4, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN, ROLE_ADMIN, ROLE_GUARDIAN, 'parent'] } },
    { path: '/index-5', component: Index5, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN } },

    // ================= 1. PLATFORM OWNER & SUPER ADMIN ONLY =================
    { path: '/role-access', component: RoleAccess, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN], title: 'Super Admin Governance' } },
    { path: '/assign-role-plan', component: AssignRole, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN], title: 'Role Assignment' } },
    { path: '/general', component: GeneralSettings, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN], title: 'Campus CMS & System Configuration' } },
    { path: '/notification', component: NotificationSettings, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN], title: 'Notification Channels' } },
    { path: '/currencies', component: CurrenciesSettings, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN], title: 'Currencies & FX' } },
    { path: '/languages', component: LanguagesSettings, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN], title: 'Localization & Languages' } },
    { path: '/subscription-plan', component: SubscriptionPlan, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN], title: 'Subscription & Tenant Licensing' } },

    // ================= 3. HRM & EMPLOYEE OPERATIONS (ADMINS ONLY) =================
    { path: '/employee-list', component: EmployeeList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Employee Directory' } },
    { path: '/employee-details', component: EmployeeDetails, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Employee Dossier' } },
    { path: '/add-new-employee', component: AddEmployee, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Add Employee' } },
    { path: '/payroll', component: Payroll, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Payroll' } },
    { path: '/designation', component: Designation, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Designations' } },
    { path: '/department', component: Department, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Departments' } },
    { path: '/employee-attendance', component: EmployeeAttendance, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Employee Attendance' } },

    // ================= 4. ACCOUNTS & FINANCIAL LEDGERS (ADMINS ONLY) =================
    { path: '/income-head', component: IncomeHead, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Income Heads' } },
    { path: '/income-list', component: IncomeList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Income List' } },
    { path: '/expense-head', component: ExpenseHead, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Expense Heads' } },
    { path: '/expense-list', component: ExpenseList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Expense List' } },
    { path: '/transaction', component: Transaction, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Transactions' } },

    // ================= 5. BURSARY & FEES STRUCTURES =================
    { path: '/fees-type', component: FeesTypeList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Fees Types' } },
    { path: '/fees-group', component: FeesGroupList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Fees Groups' } },
    { path: '/fees-discount', component: FeesDiscountList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Fees Discounts' } },
    { path: '/fees-collect', component: FeesCollectionList, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN, ROLE_ADMIN, ROLE_GUARDIAN, 'parent'], title: 'Fees Collection' } },
    { path: '/fees-collection', component: FeesCollectionList, meta: { requiresAuth: true, roles: ROLES_ALL_CAMPUS, title: 'Tuition & Bursary Ledger' } },

    // ================= 6. STUDENTS ADMINISTRATION & PORTAL =================
    { path: '/add-new-student', component: AddNewStudent, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Add Student' } },
    { path: '/student-list', component: StudentList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Student Directory' } },
    { path: '/suspended-student', component: SuspendedStudent, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Suspended Students' } },
    { path: '/student-category', component: StudentCategory, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Student Categories' } },
    { path: '/edit-student', component: EditStudent, meta: { requiresAuth: true, roles: ROLES_STUDENT_AND_ADMIN, title: 'Edit Student Academic Dossier' } },
    { path: '/student-details', component: StudentDetails, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN, ROLE_ADMIN, ROLE_STUDENT], title: 'Student Dossier' } },

    // ================= 7. ACADEMIC STAFF & LECTURERS =================
    { path: '/add-new-lecturer', component: AddNewTeacher, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Appoint Lecturer' } },
    { path: '/lecturer-list', component: TeacherList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Lecturers Directory' } },
    { path: '/edit-lecturer', component: EditTeacher, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Edit Lecturer' } },
    { path: '/lecturer-details', component: TeacherDetails, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecturer Academic Dossier' } },
    { path: '/lecture-timetable', component: TeacherTimetable, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecture Timetable' } },
    { path: '/lecturer-attendance', component: TeacherAttendance, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecture Attendance Marker' } },

    // Legacy teacher routes (retained as functional aliases)
    { path: '/add-new-teacher', component: AddNewTeacher, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Appoint Lecturer' } },
    { path: '/teacher-list', component: TeacherList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Lecturers Directory' } },
    { path: '/edit-teacher', component: EditTeacher, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Edit Lecturer' } },
    { path: '/teacher-details', component: TeacherDetails, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecturer Academic Dossier' } },
    { path: '/teacher-timetable', component: TeacherTimetable, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecture Timetable' } },
    { path: '/teacher-attendance', component: TeacherAttendance, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecture Attendance Marker' } },

    // ================= 8. GUARDIANS ADMINISTRATION & PORTAL =================
    { path: '/add-new-guardian', component: AddNewGuardian, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Add Guardian' } },
    { path: '/guardian-list', component: GuardianList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Guardian Directory' } },
    { path: '/edit-guardian', component: EditGuardian, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Edit Guardian' } },
    { path: '/guardian-details', component: GuardianDetails, meta: { requiresAuth: true, roles: [ROLE_SUPER_ADMIN, ROLE_ADMIN, ROLE_GUARDIAN, 'parent'], title: 'Guardian Profile' } },

    // ================= 9. CLASS & CURRICULUM =================
    { path: '/section-list', component: SectionList, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Class Sections' } },
    { path: '/subject-list', component: SubjectList, meta: { requiresAuth: true, roles: ROLES_ACADEMIC_AND_ADMIN, title: 'Course Modules' } },
    { path: '/class-list', component: ClassList, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Class Rooms' } },
    { path: '/class-room-list', component: ClassRoomList, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Lecture Halls' } },

    // ================= 10. EXAMINATIONS & RESULTS =================
    { path: '/exam', component: ExamList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Examinations' } },
    { path: '/exam-schedule', component: ExamScheduleList, meta: { requiresAuth: true, roles: ROLES_ACADEMIC_AND_ADMIN, title: 'Exam Timetable' } },
    { path: '/exam-result', component: ExamResultList, meta: { requiresAuth: true, roles: ROLES_ALL_CAMPUS, title: 'Assessments & Grades' } },

    // ================= 11. ATTENDANCE & LEAVES =================
    { path: '/student-attendance', component: StudentAttendance, meta: { requiresAuth: true, roles: ROLES_ALL_CAMPUS, title: 'Attendance Record' } },
    { path: '/leave-types', component: LeaveTypes, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Leave Types' } },
    { path: '/leave-request', component: LeaveRequest, meta: { requiresAuth: true, roles: ROLES_FACULTY_AND_ADMIN, title: 'Leave Requests' } },

    // ================= 12. DIGITAL LIBRARY & CERTIFICATES =================
    { path: '/certificate', component: Certificate, meta: { requiresAuth: true, roles: ROLES_STUDENT_AND_ADMIN, title: 'Certificates' } },
    { path: '/books-list', component: BooksList, meta: { requiresAuth: true, roles: ROLES_ACADEMIC_AND_ADMIN, title: 'Digital Library' } },
    { path: '/members-list', component: MembersList, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Library Members' } },
    { path: '/member-details', component: MemberDetails, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Member Details' } },
    { path: '/issue-return', component: IssueReturn, meta: { requiresAuth: true, roles: ROLES_ANY_ADMIN, title: 'Issue & Return' } },

    // ================= 13. CAMPUS-WIDE NOTICES & ENGAGEMENT =================
    { path: '/notice-board', component: NoticeBoard, meta: { requiresAuth: true, roles: ROLES_ALL_CAMPUS, title: 'Notice Board & Circulars' } },
    { path: '/event', component: Event, meta: { requiresAuth: true, roles: ROLES_ALL_CAMPUS, title: 'Events' } },
    { path: '/message', component: Message, meta: { requiresAuth: true, roles: ROLES_ALL_CAMPUS, title: 'Messages' } },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

function isValidJwt(token) {
    if (!token || typeof token !== 'string') return false;
    if (token.startsWith('demo_jwt_token_')) return false;
    const parts = token.split('.');
    return parts.length === 3 && parts.every((p) => p.length > 0);
}

function clearSessionStorage() {
    localStorage.removeItem('campus_user');
    localStorage.removeItem('campus_token');
    localStorage.removeItem('campus_role');
    localStorage.removeItem('campus_last_active');
    localStorage.removeItem('campus_screen_locked');
    localStorage.removeItem('campus_locked_redirect');
}

function getActiveUserRole() {
    const directRole = localStorage.getItem('campus_role');
    if (directRole) return directRole;

    try {
        const storedUser = localStorage.getItem('campus_user');
        if (storedUser) {
            const parsed = JSON.parse(storedUser);
            if (parsed.role) return parsed.role;
        }
    } catch {
        // fallback
    }
    return null;
}

// Navigation Guard: Protect internal portal pages and enforce strict RBAC
router.beforeEach((to, from, next) => {
    // Explicit session reset / logout query parameter support
    if (to.query.logout === '1' || to.query.reset === '1') {
        clearSessionStorage();
    }

    const rawToken = localStorage.getItem('campus_token');
    let isAuthenticated = isValidJwt(rawToken);

    // If stored token is invalid or a legacy dummy token, purge immediately
    if (rawToken && !isAuthenticated) {
        clearSessionStorage();
    }

    const isAuthRoute = to.path === '/' || to.path === '/login' || to.path === '/register';

    // ================= SESSION INACTIVITY CHECK (15-MINUTE TIMEOUT) =================
    if (isAuthenticated) {
        const lastActive = Number(localStorage.getItem('campus_last_active') || 0)
        const SESSION_TIMEOUT_MS = 15 * 60 * 1000 // 15 minutes
        const isExpired = lastActive > 0 && (Date.now() - lastActive) >= SESSION_TIMEOUT_MS

        if (isExpired) {
            // Clear expired session credentials
            localStorage.removeItem('campus_user')
            localStorage.removeItem('campus_token')
            localStorage.removeItem('campus_role')
            localStorage.removeItem('campus_last_active')
            localStorage.removeItem('campus_screen_locked')
            localStorage.removeItem('campus_locked_redirect')
            isAuthenticated = false

            try {
                const toastStore = useToastStore()
                toastStore.warning(
                    'Your session expired due to 15 minutes of inactivity. Please re-authenticate to continue.',
                    'Session Expired'
                )
            } catch {
                // Ignore if store not yet hydrated
            }

            return next({ path: '/login', query: { reason: 'inactivity', redirect: to.fullPath } })
        }
    }

    const currentRole = getActiveUserRole()
    const isLocked = localStorage.getItem('campus_screen_locked') === 'true'

    // ================= WORKSTATION LOCK SCREEN ENFORCEMENT =================
    // If workstation is locked and user is authenticated:
    if (isAuthenticated && isLocked) {
        if (to.path !== '/lock-screen') {
            return next({ path: '/lock-screen' })
        }
        return next()
    }

    // Unauthenticated user attempting to access lock screen -> redirect to login
    if (!isAuthenticated && to.path === '/lock-screen') {
        return next({ path: '/login' })
    }

    // Authenticated user who is NOT locked attempting to access lock screen -> redirect to dashboard
    if (isAuthenticated && !isLocked && to.path === '/lock-screen') {
        return next('/dashboard')
    }

    // Unauthenticated user trying to access any route other than login/register
    if (!isAuthenticated && !isAuthRoute) {
        return next({ path: '/login', query: { redirect: to.fullPath } })
    }

    // Authenticated user trying to visit login/register/root -> redirect to dashboard
    if (isAuthenticated && isAuthRoute) {
        return next('/dashboard')
    }

    // ================= STRICT RBAC ROLE CLEARANCE CHECK =================
    if (isAuthenticated && to.meta && to.meta.roles) {
        const allowedRoles = to.meta.roles

        if (!currentRole || !allowedRoles.includes(currentRole)) {
            // Trigger feedback toast informing the user about the security interception
            try {
                const toastStore = useToastStore()
                toastStore.error(
                    `Access Denied: Your account role (${(currentRole || 'GUEST').toUpperCase()}) does not possess clearance for ${to.path}.`,
                    '403 Forbidden'
                )
            } catch {
                // Ignore if store not yet hydrated
            }

            // Redirect to 403 Forbidden Access Denied page
            return next('/403')
        }
    }

    next()
})

router.afterEach((to) => {
    // Record user activity timestamp on route navigation
    try {
        if (localStorage.getItem('campus_token')) {
            localStorage.setItem('campus_last_active', String(Date.now()))
        }
    } catch {}

    let institutionName = 'SmartCampus'
    try {
        const stored = localStorage.getItem('campus_institution_config')
        if (stored) {
            const parsed = JSON.parse(stored)
            if (parsed.name) institutionName = parsed.name
        }
    } catch {
        // fallback
    }

    const routeTitleMap = {
        '/': 'Portal Sign-In',
        '/login': 'Portal Sign-In',
        '/register': 'Institutional Registration',
        '/lock-screen': 'Workstation Locked',
        '/profile': 'My Academic Dossier',
        '/dashboard': 'Campus Intelligence & Dashboard',
        '/student-dashboard': 'Student Portal',
        '/lecturer-dashboard': 'Lecturer Console',
        '/role-access': 'Super Admin — Administrator Governance',
        '/assign-role-plan': 'Super Admin — Staff Role Delegation',
        '/general': 'Super Admin — Campus CMS & System Configuration',
        '/student-list': 'Student Directory',
        '/add-new-student': 'Student Admission',
        '/student-details': 'Student Academic Dossier',
        '/lecturer-list': 'Academic Staff & Lecturers Directory',
        '/teacher-list': 'Academic Staff & Lecturers Directory',
        '/lecturer-details': 'Lecturer Academic Dossier',
        '/teacher-details': 'Lecturer Academic Dossier',
        '/lecture-timetable': 'Lecture Timetable & Schedule',
        '/teacher-timetable': 'Lecture Timetable & Schedule',
        '/lecturer-attendance': 'Lecture Attendance Marker',
        '/teacher-attendance': 'Lecture Attendance Marker',
        '/exam-list': 'Examinations & Assessments',
        '/fees-collection': 'Institutional Bursary & Tuition',
        '/403': '403 Forbidden — Security Clearance Required'
    }

    const pageTitle = to.meta?.title || routeTitleMap[to.path] || 'Academic Portal'
    document.title = `${pageTitle} — ${institutionName}`
})

export default router