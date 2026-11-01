<template>
  <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300"></div>
  <aside class="sidebar" style="z-index: 999">
    <button type="button" class="sidebar-close-btn">
      <iconify-icon icon="radix-icons:cross-2"></iconify-icon>
    </button>
    <div class="">
      <div class="sidebar-logo d-flex align-items-center justify-content-between">
        <router-link to="/dashboard" class="">
          <img :src="institution.logoUrl" alt="site logo" class="light-logo">
          <img :src="institution.logoDarkUrl" alt="site logo" class="dark-logo">
          <img :src="institution.crestUrl" alt="site logo" class="logo-icon">
        </router-link>
        <button type="button" class="text-xxl d-xl-flex d-none line-height-1 sidebar-toggle text-neutral-500"
          aria-label="Collapse Sidebar">
          <i class="ri-contract-left-line"></i>
        </button>
      </div>
    </div>
    <!-- User Info start -->
    <div class="mx-16 py-12">
      <div class="dropdown profile-dropdown">
        <button type="button"
          class="profile-dropdown__button d-flex align-items-center justify-content-between p-10 w-100 overflow-hidden bg-neutral-50 radius-12 "
          data-bs-toggle="dropdown" data-bs-display="static" aria-expanded="false">
          <span class="d-flex align-items-start gap-10">
            <img :src="currentUser?.avatar || '/assets/images/thumbs/leave-request-img2.png'" alt="Thumbnail"
              class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
            <span class="profile-dropdown__contents">
              <span class="h6 mb-0 text-md d-block text-primary-light">{{ currentUser?.name || 'Academic Admin' }}</span>
              <span class="text-secondary-light text-sm mb-0 d-block text-capitalize">{{ userRoleDisplay }}</span>
            </span>
          </span>
          <span class="profile-dropdown__icon pe-8 text-xl d-flex line-height-1">
            <i class="ri-arrow-right-s-line"></i>
          </span>
        </button>
        <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
          <li>
            <router-link :to="myProfileRoute"
              class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6">
              <i class="ri-user-3-line"></i>
              My Profile
            </router-link>
          </li>
          <li v-if="isSuperAdmin">
            <router-link to="/general"
              class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6">
              <i class="ri-settings-3-line"></i>
              Campus CMS & Config
            </router-link>
          </li>
          <li>
            <a href="javascript:void(0)" @click="handleLockScreen"
              class="dropdown-item rounded text-warning-700 bg-hover-warning-50 d-flex align-items-center gap-2 py-6 cursor-pointer">
              <i class="ri-lock-password-line"></i>
              Lock Screen
            </a>
          </li>
          <li>
            <a href="javascript:void(0)" @click="handleLogout"
              class="dropdown-item rounded text-danger-600 bg-hover-danger-50 d-flex align-items-center gap-2 py-6 cursor-pointer">
              <i class="ri-shut-down-line"></i>
              Log Out
            </a>
          </li>
        </ul>
      </div>
    </div>
    <!-- User Info end -->
    <div class="sidebar-menu-area">
      <ul class="sidebar-menu" id="sidebar-menu">
        <!-- ================= 1. STUDENT SPECIFIC NAVIGATION ================= -->
        <template v-if="isStudent">
          <li class="sidebar-menu-group-title text-neutral-400 text-xxs px-16 py-8 text-uppercase fw-bold letter-spacing-1">
            Student Academic Portal
          </li>
          <li>
            <router-link to="/dashboard">
              <i class="ri-dashboard-3-line"></i>
              <span>My Academic Portal</span>
            </router-link>
          </li>
          <li>
            <router-link to="/subject-list">
              <i class="ri-book-open-line"></i>
              <span>Enrolled Courses</span>
            </router-link>
          </li>
          <li>
            <router-link to="/exam-result">
              <i class="ri-award-line"></i>
              <span>Assessment & Exam Grades</span>
            </router-link>
          </li>
          <li>
            <router-link to="/student-attendance">
              <i class="ri-fingerprint-line"></i>
              <span>Attendance & Clearance Pass</span>
            </router-link>
          </li>
          <li>
            <router-link to="/fees-collection">
              <i class="ri-wallet-3-line"></i>
              <span>Bursary & Tuition Ledger</span>
            </router-link>
          </li>
          <li>
            <router-link to="/books-list">
              <i class="ri-book-read-line"></i>
              <span>Digital Library</span>
            </router-link>
          </li>
          <li>
            <router-link to="/notice-board">
              <i class="ri-notification-3-line"></i>
              <span>Campus Circulars</span>
            </router-link>
          </li>
          <li>
            <router-link to="/student-details">
              <i class="ri-user-settings-line"></i>
              <span>My Student Dossier</span>
            </router-link>
          </li>
        </template>

        <!-- ================= 2. ACADEMIC FACULTY & LECTURER SPECIFIC NAVIGATION ================= -->
        <template v-else-if="isLecturer">
          <li class="sidebar-menu-group-title text-neutral-400 text-xxs px-16 py-8 text-uppercase fw-bold letter-spacing-1">
            Academic Faculty & Lecturer Console
          </li>
          <li>
            <router-link to="/dashboard">
              <i class="ri-dashboard-3-line"></i>
              <span>Lecturer Dashboard</span>
            </router-link>
          </li>
          <li>
            <router-link to="/lecture-timetable">
              <i class="ri-calendar-event-line"></i>
              <span>Lecture Timetable & Schedule</span>
            </router-link>
          </li>
          <li>
            <router-link to="/subject-list">
              <i class="ri-book-read-line"></i>
              <span>Assigned Academic Courses</span>
            </router-link>
          </li>
          <li>
            <router-link to="/lecturer-attendance">
              <i class="ri-fingerprint-line"></i>
              <span>Lecture Attendance Marker</span>
            </router-link>
          </li>
          <li>
            <router-link to="/exam-result">
              <i class="ri-survey-line"></i>
              <span>Continuous Assessment & Grades</span>
            </router-link>
          </li>
          <li>
            <router-link to="/leave-request">
              <i class="ri-flight-takeoff-line"></i>
              <span>Academic Leave Application</span>
            </router-link>
          </li>
          <li>
            <router-link to="/notice-board">
              <i class="ri-notification-3-line"></i>
              <span>Senate & Faculty Circulars</span>
            </router-link>
          </li>
          <li>
            <router-link to="/lecturer-details">
              <i class="ri-user-3-line"></i>
              <span>My Lecturer Dossier</span>
            </router-link>
          </li>
        </template>

        <!-- ================= 3. GUARDIAN / PARENT SPECIFIC NAVIGATION ================= -->
        <template v-else-if="isGuardian">
          <li class="sidebar-menu-group-title text-neutral-400 text-xxs px-16 py-8 text-uppercase fw-bold letter-spacing-1">
            Guardian Academic Portal
          </li>
          <li>
            <router-link to="/dashboard">
              <i class="ri-dashboard-3-line"></i>
              <span>Ward Academic Overview</span>
            </router-link>
          </li>
          <li>
            <router-link to="/exam-result">
              <i class="ri-award-line"></i>
              <span>Assessment & Exam Grades</span>
            </router-link>
          </li>
          <li>
            <router-link to="/student-attendance">
              <i class="ri-fingerprint-line"></i>
              <span>Attendance Verification</span>
            </router-link>
          </li>
          <li>
            <router-link to="/fees-collection">
              <i class="ri-wallet-3-line"></i>
              <span>Tuition & Bursary Settlement</span>
            </router-link>
          </li>
          <li>
            <router-link to="/notice-board">
              <i class="ri-notification-3-line"></i>
              <span>Campus Circulars</span>
            </router-link>
          </li>
        </template>

        <!-- ================= 4. UNIVERSITY ADMIN & SUPER ADMIN NAVIGATION ================= -->
        <template v-else>
          <li class="sidebar-menu-group-title text-neutral-400 text-xxs px-16 py-8 text-uppercase fw-bold letter-spacing-1">
            Executive ERP Operations
          </li>
          <li>
            <router-link to="/dashboard">
              <i class="ri-home-4-line"></i>
              <span>Executive Dashboard</span>
            </router-link>
          </li>
        <li class="dropdown">
          <a href="javascript:void(0)">
            <i class="ri-graduation-cap-line"></i>
            <span>Students</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/add-new-student">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Add New Student
              </router-link>
            </li>
            <li>
              <router-link to="/student-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Student List
              </router-link>
            </li>
            <li>
              <router-link to="/suspended-student">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Suspend Student
              </router-link>
            </li>
            <li>
              <router-link to="/student-category">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Student Categories
              </router-link>
            </li>
            <li>
              <router-link to="/edit-student">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Edit Student
              </router-link>
            </li>
            <li>
              <router-link to="/student-details">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Student Details
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown">
          <a href="javascript:void(0)">
            <i class="ri-user-follow-line"></i>
            <span>Lecturers</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/add-new-lecturer">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Appoint / Add Lecturer
              </router-link>
            </li>
            <li>
              <router-link to="/lecturer-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Lecturers Directory
              </router-link>
            </li>
            <li>
              <router-link to="/edit-lecturer">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Edit Lecturer
              </router-link>
            </li>
            <li>
              <router-link to="/lecturer-details">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Lecturer Dossier
              </router-link>
            </li>
            <li>
              <router-link to="/lecture-timetable">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Lecture Timetable
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown">
          <a href="javascript:void(0)">
            <i class="ri-account-circle-line"></i>
            <span>Guardian</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/add-new-guardian">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Add New Guardians
              </router-link>
            </li>
            <li>
              <router-link to="/guardian-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Guardians List
              </router-link>
            </li>
            <li>
              <router-link to="/edit-guardian">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Edit Guardian
              </router-link>
            </li>
            <li>
              <router-link to="/guardian-details">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Guardian Details
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown">
          <a href="javascript:void(0)">
            <i class="ri-list-view"></i>
            <span>Classes</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/section-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Section
              </router-link>
            </li>
            <li>
              <router-link to="/subject-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Subjects
              </router-link>
            </li>
            <li>
              <router-link to="/class-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Class List
              </router-link>
            </li>
            <li>
              <router-link to="/class-room-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Class Room
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown" v-if="institution.isModuleEnabled('examination')">
          <a href="javascript:void(0)">
            <i class="ri-file-edit-line"></i>
            <span>Examinations</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/exam">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Exam
              </router-link>
            </li>
            <li>
              <router-link to="/exam-schedule">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Exam Schedule
              </router-link>
            </li>
            <li>
              <router-link to="/exam-result">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Exam Result
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown" v-if="institution.isModuleEnabled('feeCollections')">
          <a href="javascript:void(0)">
            <i class="ri-money-dollar-circle-line"></i>
            <span>Fees Collection</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/fees-collect">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Fees Collect
              </router-link>
            </li>
            <li>
              <router-link to="/fees-type">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Fees Type
              </router-link>
            </li>
            <li>
              <router-link to="/fees-group">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Fees Group
              </router-link>
            </li>
            <li>
              <router-link to="/fees-discount">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Fees Discount
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown" v-if="institution.isModuleEnabled('attendance')">
          <a href="javascript:void(0)">
            <i class="ri-calendar-check-line"></i>
            <span>Attendance</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/student-attendance">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Student Attendance
              </router-link>
            </li>
            <li>
              <router-link to="/lecturer-attendance">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Lecturer Attendance
              </router-link>
            </li>
            <li>
              <router-link to="/employee-attendance">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Employee Attendance
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown" v-if="institution.isModuleEnabled('leaves')">
          <a href="javascript:void(0)">
            <i class="ri-time-line"></i>
            <span>Leaves</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/leave-types">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Leave Types
              </router-link>
            </li>
            <li>
              <router-link to="/leave-request">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Leave Request
              </router-link>
            </li>
          </ul>
        </li>
        <li>
          <router-link to="/certificate">
            <i class="ri-home-4-line"></i>
            <span>Certificate </span>
          </router-link>
        </li>
        <li class="dropdown" v-if="institution.isModuleEnabled('library')">
          <a href="javascript:void(0)">
            <i class="ri-book-2-line"></i>
            <span>Library</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/books-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Books List
              </router-link>
            </li>
            <li>
              <router-link to="/members-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Members List
              </router-link>
            </li>
            <li>
              <router-link to="/member-details">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Members Details
              </router-link>
            </li>
            <li>
              <router-link to="/issue-return">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Issue Return
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown" v-if="institution.isModuleEnabled('accounts')">
          <a href="javascript:void(0)">
            <i class="ri-money-dollar-circle-line"></i>
            <span>Accounts</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/income-head">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Income Head
              </router-link>
            </li>
            <li>
              <router-link to="/income-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Income List
              </router-link>
            </li>
            <li>
              <router-link to="/expense-head">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Expense Head
              </router-link>
            </li>
            <li>
              <router-link to="/expense-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Expense List
              </router-link>
            </li>
            <li>
              <router-link to="/transaction">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Transaction
              </router-link>
            </li>
          </ul>
        </li>
        <li class="dropdown" v-if="institution.isModuleEnabled('hrm')">
          <a href="javascript:void(0)">
            <i class="ri-user-settings-line"></i>
            <span>HRM</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/employee-list">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Employee List
              </router-link>
            </li>
            <li>
              <router-link to="/employee-details">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Employee Details
              </router-link>
            </li>
            <li>
              <router-link to="/add-new-employee">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Add New Employee
              </router-link>
            </li>
            <li>
              <router-link to="/payroll">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Payroll
              </router-link>
            </li>
            <li>
              <router-link to="/designation">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Designation
              </router-link>
            </li>
            <li>
              <router-link to="/department">
                <i class="ri-circle-fill circle-icon w-auto"></i>
                Department
              </router-link>
            </li>
          </ul>
        </li>
        <li v-if="institution.isModuleEnabled('noticeBoard')">
          <router-link to="/notice-board">
            <i class="ri-booklet-line"></i>
            <span>Notice Board </span>
          </router-link>
        </li>
        <li>
          <router-link to="/event">
            <i class="ri-calendar-event-line"></i>
            <span>Event </span>
          </router-link>
        </li>
        <li>
          <router-link to="/message">
            <i class="ri-message-2-line"></i>
            <span>Message </span>
          </router-link>
        </li>
        <li class="dropdown">
          <a href="javascript:void(0)">
            <i class="ri-shield-check-line"></i>
            <span>Authentication</span>
          </a>
          <ul class="sidebar-submenu">
            <li>
              <router-link to="/login"><i class="ri-circle-fill circle-icon text-primary-600 w-auto"></i> Login</router-link>
            </li>
            <li>
              <router-link to="/register"><i class="ri-circle-fill circle-icon text-warning-main w-auto"></i> Register</router-link>
            </li>
          </ul>
        </li>

        <!-- ================= 5. SUPER ADMINISTRATOR & TENANT PLATFORM GOVERNANCE ================= -->
        <template v-if="isSuperAdmin">
          <li class="sidebar-menu-group-title text-primary-600 text-xxs px-16 py-8 text-uppercase fw-bold letter-spacing-1 d-flex align-items-center justify-content-between mt-16 border-top pt-16">
            <span>Super Admin Console</span>
            <span class="badge bg-primary-50 text-primary-700 border border-primary-200 text-xxs px-6 py-2 rounded-pill">Root</span>
          </li>
          <li>
            <router-link to="/role-access">
              <i class="ri-shield-user-line"></i>
              <span>Admin Governance</span>
            </router-link>
          </li>
          <li class="dropdown">
            <a href="javascript:void(0)">
              <i class="ri-settings-5-line"></i>
              <span>Campus CMS & Config</span>
            </a>
            <ul class="sidebar-submenu">
              <li>
                <router-link to="/general">
                  <i class="ri-circle-fill circle-icon text-primary-600 w-auto"></i>
                  Identity, Calendar & AI
                </router-link>
              </li>
              <li>
                <router-link to="/notification">
                  <i class="ri-circle-fill circle-icon w-auto"></i>
                  Notification Channels
                </router-link>
              </li>
              <li>
                <router-link to="/currencies">
                  <i class="ri-circle-fill circle-icon w-auto"></i>
                  Currencies & FX
                </router-link>
              </li>
              <li>
                <router-link to="/languages">
                  <i class="ri-circle-fill circle-icon w-auto"></i>
                  Localization & Languages
                </router-link>
              </li>
            </ul>
          </li>
          <li>
            <router-link to="/subscription-plan">
              <i class="ri-price-tag-3-line"></i>
              <span>Subscription Plan</span>
            </router-link>
          </li>
          <li>
            <router-link to="/assign-role-plan">
              <i class="ri-user-follow-line"></i>
              <span>Assign Role Plan</span>
            </router-link>
          </li>
        </template>
      </template>
      </ul>
    </div>
  </aside>
</template>

<script>
import { onMounted, watch, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useInstitutionStore } from '@/stores/institution.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: 'Sidebar',
  setup() {
    const route = useRoute();
    const router = useRouter();
    const authStore = useAuthStore();
    const institution = useInstitutionStore();
    const toastStore = useToastStore();

    const currentUser = computed(() => authStore.currentUser);
    const isStudent = computed(() => authStore.isStudent);
    const isLecturer = computed(() => authStore.isLecturer || authStore.isTeacher);
    const isTeacher = computed(() => authStore.isTeacher || authStore.isLecturer);
    const isGuardian = computed(() => authStore.isGuardian);
    const isAdmin = computed(() => authStore.isAdmin || authStore.isSuperAdmin);
    const isSuperAdmin = computed(() => authStore.isSuperAdmin);

    const userRoleDisplay = computed(() => {
      const role = currentUser.value?.role;
      if (role === 'teacher' || role === 'lecturer') return 'Lecturer';
      if (role === 'super-admin') return 'Super Admin';
      if (role === 'admin') return 'University Admin';
      if (role === 'student') return 'Student';
      if (role === 'guardian' || role === 'parent') return 'Guardian';
      return role?.replace('-', ' ') || 'Academic User';
    });

    const myProfileRoute = computed(() => {
      const role = authStore.currentRole || authStore.user?.role;
      if (role === 'lecturer' || role === 'teacher') return '/lecturer-details';
      if (role === 'admin' || role === 'super-admin') return '/employee-details';
      if (role === 'guardian' || role === 'parent') return '/guardian-details';
      return '/student-details';
    });

    const handleLogout = () => {
      authStore.logout();
      toastStore.info('Your active session has been securely closed.', 'Signed Out');
      router.push('/login');
    };

    const handleLockScreen = () => {
      authStore.lockScreen(route.fullPath);
      router.push('/lock-screen');
    };

    const checkAndSetActiveMenu = () => {
      // Use nextTick to ensure Vue Router has applied classes
      setTimeout(() => {
        const sidebarMenus = document.querySelectorAll('.sidebar-menu .dropdown > a');
        
        sidebarMenus.forEach((menu) => {
          const parent = menu.parentElement;
          const submenu = parent.querySelector('.sidebar-submenu');
          const submenuLinks = submenu ? submenu.querySelectorAll('a') : [];

          // Check if any submenu link has router-link-active or router-link-exact-active class
          let isActive = false;
          submenuLinks.forEach(link => {
            if (link.classList.contains('router-link-active') || 
                link.classList.contains('router-link-exact-active')) {
              isActive = true;
            }
          });

          // If active, open the menu
          if (isActive) {
            parent.classList.add('open');
            if(submenu) submenu.style.display = 'block';
          } else {
            parent.classList.remove('open');
            if(submenu) submenu.style.display = 'none';
          }
        });
      }, 50);
    };

    onMounted(() => {
      // Initial check for active menu
      checkAndSetActiveMenu();

      // Sidebar Menu Toggle
      const sidebarMenus = document.querySelectorAll('.sidebar-menu .dropdown > a');

      sidebarMenus.forEach((menu) => {
        const parent = menu.parentElement;
        const submenu = parent.querySelector('.sidebar-submenu');

        menu.addEventListener('click', function (e) {
          e.preventDefault();
          
          // Close other open menus
          document.querySelectorAll('.sidebar-menu .dropdown.open').forEach((openMenu) => {
            if (openMenu !== parent) {
              openMenu.classList.remove('open');
              const otherSubmenu = openMenu.querySelector('.sidebar-submenu');
              if (otherSubmenu) {
                otherSubmenu.style.display = 'none';
              }
            }
          });

          // Toggle current menu
          parent.classList.toggle('open');
          if (submenu) {
            if (parent.classList.contains('open')) {
              submenu.style.display = 'block';
            } else {
              submenu.style.display = 'none';
            }
          }
        });
      });


      // Sidebar Mobile Toggle - Handled by Navbar component
      // The toggle button click is handled in Navabar.vue
      const sidebarCloseBtn = document.querySelector('.sidebar-close-btn');
      const sidebar = document.querySelector('.sidebar');
      const overlay = document.querySelector('.overlay'); 

      if(sidebarCloseBtn) {
        sidebarCloseBtn.addEventListener('click', () => {
          sidebar.classList.remove('sidebar-open');
          sidebar.classList.remove('open');
          overlay.classList.remove('visibility-visible', 'opacity-100');
          overlay.classList.add('visibility-hidden', 'opacity-0');
        });
      }
      
      if(overlay) {
        overlay.addEventListener('click', () => {
          sidebar.classList.remove('sidebar-open');
          sidebar.classList.remove('open');
          overlay.classList.remove('visibility-visible', 'opacity-100');
          overlay.classList.add('visibility-hidden', 'opacity-0');
        });
      }

      // Sidebar Desktop Toggle
      const sidebarDesktopToggle = document.querySelector('.sidebar-toggle');
      if(sidebarDesktopToggle) {
        sidebarDesktopToggle.addEventListener('click', () => {
          const sidebar = document.querySelector('.sidebar');
          const main = document.querySelector('.dashboard-main');
          if(sidebar) sidebar.classList.toggle('active');
          if(main) main.classList.toggle('active');
          sidebarDesktopToggle.classList.toggle('active');
        });
      }
    });

    // Watch for route changes and update active menu
    watch(() => route.path, () => {
      checkAndSetActiveMenu();
    });

    return {
      currentUser,
      handleLogout,
      handleLockScreen,
      institution,
      isStudent,
      isLecturer,
      isTeacher,
      isGuardian,
      isAdmin,
      isSuperAdmin,
      userRoleDisplay,
      myProfileRoute
    };
  }
}
</script>
