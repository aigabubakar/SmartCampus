<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navabar />
    
    <div class="dashboard-main-body">

      <!-- ================= Faculty Teaching Console Header ================= -->
      <div class="card border-0 radius-16 shadow-1 mb-24 overflow-hidden" style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 60%, #4338ca 100%);">
        <div class="card-body p-24 text-white">
          <div class="d-flex flex-wrap align-items-center justify-content-between gap-20">
            
            <!-- Left: Faculty Info -->
            <div class="d-flex align-items-center gap-16">
              <img 
                :src="teacherUser?.avatar || '/assets/images/users/user1.png'" 
                alt="Faculty Member" 
                class="w-64-px h-64-px rounded-circle bg-white p-2 shadow-sm flex-shrink-0 object-fit-cover border border-2 border-white"
              >
              <div>
                <div class="d-flex align-items-center gap-10 flex-wrap">
                  <h4 class="fw-bold mb-0 text-white">{{ teacherUser?.name || 'Prof. Alistair Finch' }}</h4>
                  <span class="badge badge-translucent text-white px-10 py-4 radius-8 text-xs fw-semibold">
                    {{ institution.academicSession || institution.currentAcademicYear || '2026/2027 Academic Session' }} • {{ institution.currentSemester || 'First Semester (Fall)' }}
                  </span>
                  <span class="badge bg-purple-500 text-white px-10 py-4 radius-8 text-xs fw-bold">
                    Academic Faculty & Lecturer Console
                  </span>
                </div>
                <p class="text-white text-opacity-80 text-sm mb-0 mt-6">
                  {{ teacherUser?.department || 'Department of Computer Science' }} • {{ institution.institutionName || institution.name || 'Apex Metropolitan University' }}
                </p>
              </div>
            </div>

            <!-- Right: Quick Action -->
            <div class="d-flex align-items-center gap-12 flex-wrap">
              <router-link 
                to="/lecture-timetable" 
                class="btn btn-light radius-10 px-16 py-10 text-sm fw-bold text-neutral-900 d-flex align-items-center gap-8 shadow-sm"
              >
                <iconify-icon icon="solar:calendar-bold" class="text-lg text-primary-600"></iconify-icon>
                View Lecture Schedule
              </router-link>
            </div>

          </div>
        </div>
      </div>

      <div class="mt-24">
        <div class="row gy-4">
          <!-- Teacher Profile & Teaching Load -->
          <div class="col-xxl-7">
            <TeacherProfile />
          </div>

          <!-- Lecture Attendance Stats -->
          <div class="col-xxl-5">
            <AttendanceStats />
          </div>

          <!-- Student Gradebook & Scoring -->
          <div class="col-xxl-8">
            <StudentMarks />
          </div>

          <!-- Academic Calendar -->
          <div class="col-xxl-4 col-lg-6">
            <Calendar />
          </div>

          <!-- Notice Board -->
          <div class="col-xxl-4 col-lg-6">
            <NoticeBoard />
          </div>

          <!-- Upcoming Events -->
          <div class="col-xxl-4 col-lg-6">
            <UpcomingEvents />
          </div>

          <!-- Leave Status -->
          <div class="col-xxl-4">
            <LeaveStatus />
          </div>

        </div>
      </div>
    </div>
    
    <Footer />
  </main>
</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useInstitutionStore } from '@/stores/institution.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navabar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';

import TeacherProfile from '@/components/index/index3/TeacherProfile.vue';
import AttendanceStats from '@/components/index/index3/AttendanceStats.vue';
import NoticeBoard from '@/components/index/index3/NoticeBoard.vue';
import UpcomingEvents from '@/components/index/index3/UpcomingEvents.vue';
import Calendar from '@/components/index/index3/Calendar.vue';
import StudentMarks from '@/components/index/index3/StudentMarks.vue';
import LeaveStatus from '@/components/index/index3/LeaveStatus.vue';

export default {
  name: "Index3",
  components: {
    Sidebar,
    Navabar,
    Footer,
    TeacherProfile,
    AttendanceStats,
    NoticeBoard,
    UpcomingEvents,
    Calendar,
    StudentMarks,
    LeaveStatus
  },
  setup() {
    const authStore = useAuthStore();
    const institution = useInstitutionStore();

    const teacherUser = computed(() => authStore.currentUser);

    return {
      authStore,
      institution,
      teacherUser
    };
  }
}
</script>
