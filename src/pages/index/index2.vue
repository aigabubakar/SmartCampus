<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navabar />
    
    <div class="dashboard-main-body">

      <!-- ================= Student Academic Portal Header ================= -->
      <div class="card border-0 radius-16 shadow-1 mb-24 overflow-hidden" style="background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 60%, #3b82f6 100%);">
        <div class="card-body p-24 text-white">
          <div class="d-flex flex-wrap align-items-center justify-content-between gap-20">
            
            <!-- Left: Student Info & Academic Standing -->
            <div class="d-flex align-items-center gap-16">
              <img 
                :src="studentUser?.avatar || '/assets/images/thumbs/user-img1.png'" 
                alt="Student Profile" 
                class="w-64-px h-64-px rounded-circle bg-white p-2 shadow-sm flex-shrink-0 object-fit-cover border border-2 border-white"
              >
              <div>
                <div class="d-flex align-items-center gap-10 flex-wrap">
                  <h4 class="fw-bold mb-0 text-white">Welcome back, {{ studentUser?.name || 'Sophia Chen' }}</h4>
                  <span class="badge badge-translucent text-white px-10 py-4 radius-8 text-xs font-monospace">
                    {{ studentUser?.matricNumber || 'SCI/2026/0491' }}
                  </span>
                  <span class="badge bg-success-500 text-white px-10 py-4 radius-8 text-xs fw-bold">
                    Good Academic Standing (CGPA: 3.82)
                  </span>
                </div>
                <p class="text-white text-opacity-80 text-sm mb-0 mt-6">
                  {{ studentUser?.program || 'B.Sc. Computer Science' }} • {{ institution.institutionName || institution.name || 'Apex Metropolitan University' }} • {{ institution.academicSession || institution.currentAcademicYear || '2026/2027 Academic Session' }}
                </p>
              </div>
            </div>

            <!-- Right: Examination Hall Pass Quick Button -->
            <div class="d-flex align-items-center gap-12 flex-wrap">
              <button 
                type="button" 
                class="btn btn-light radius-10 px-16 py-10 text-sm fw-bold d-flex align-items-center gap-8 shadow-sm"
                style="background-color: #ffffff !important; color: #111827 !important; border: 1px solid #ffffff !important;"
                data-bs-toggle="modal"
                data-bs-target="#studentExamPassModal"
              >
                <i class="ri-shield-check-fill text-lg text-primary-600"></i>
                <span style="color: #111827 !important;">View Exam Clearance Pass</span>
              </button>
            </div>

          </div>
        </div>
      </div>

      <div class="mt-24">
        <div class="row gy-4">
          <!-- Student Profile & Academic Gauge -->
          <div class="col-xxl-6">
            <StudentProfile />
          </div>

          <!-- Attendance Compliance & 75% Threshold -->
          <div class="col-xxl-6">
            <AttendanceChart />
          </div>

          <!-- Today's Lecture Timetable -->
          <div class="col-xxl-4 col-lg-6">
            <TodaysClass />
          </div>

          <!-- Semester Exam & Assessment Results -->
          <div class="col-xxl-8">
            <ExamResults />
          </div>

          <!-- Academic Calendar -->
          <div class="col-xxl-4 col-lg-6">
            <Calendar />
          </div>

          <!-- Leave Status -->
          <div class="col-xxl-4 col-lg-6">
            <LeaveStatus />
          </div>

          <!-- Notice Board & Circulars -->
          <div class="col-xxl-4 col-lg-6">
            <NoticeBoard />
          </div>

          <!-- Upcoming Events -->
          <div class="col-xxl-4 col-lg-6">
            <UpcomingEvents />
          </div>
        </div>
      </div>
    </div>
    
    <Footer />
  </main>

  <!-- Digital Examination Hall Pass Modal -->
  <StudentExamPassModal />

</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useInstitutionStore } from '@/stores/institution.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navabar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';

import StudentProfile from '@/components/index/index2/StudentProfile.vue';
import AttendanceChart from '@/components/index/index2/AttendanceChart.vue';
import TodaysClass from '@/components/index/index2/TodaysClass.vue';
import ExamResults from '@/components/index/index2/ExamResults.vue';
import Calendar from '@/components/index/index2/Calendar.vue';
import LeaveStatus from '@/components/index/index2/LeaveStatus.vue';
import NoticeBoard from '@/components/index/index2/NoticeBoard.vue';
import UpcomingEvents from '@/components/index/index2/UpcomingEvents.vue';
import StudentExamPassModal from '@/components/index/index2/StudentExamPassModal.vue';

export default {
  name: "Index2",
  components: {
    Sidebar,
    Navabar,
    Footer,
    StudentProfile,
    AttendanceChart,
    TodaysClass,
    ExamResults,
    Calendar,
    LeaveStatus,
    NoticeBoard,
    UpcomingEvents,
    StudentExamPassModal
  },
  setup() {
    const authStore = useAuthStore();
    const institution = useInstitutionStore();

    const studentUser = computed(() => authStore.currentUser);

    return {
      authStore,
      institution,
      studentUser
    };
  }
}
</script>
