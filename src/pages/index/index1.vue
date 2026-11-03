<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navabar />
    
    <div class="dashboard-main-body">

      <!-- ================= Campus Executive Intelligence Header ================= -->
      <div class="card border-0 radius-16 shadow-1 mb-24 overflow-hidden" style="background: linear-gradient(135deg, #134e48 0%, #25A194 60%, #0d9488 100%);">
        <div class="card-body p-24 text-white">
          <div class="d-flex flex-wrap align-items-center justify-content-between gap-20">
            
            <!-- Left: University Brand & Session Context -->
            <div class="d-flex align-items-center gap-16">
              <img 
                :src="institution.crestUrl" 
                alt="University Crest" 
                class="w-64-px h-64-px rounded-circle bg-white p-4 shadow-sm flex-shrink-0 object-fit-contain"
              >
              <div>
                <div class="d-flex align-items-center gap-10 flex-wrap">
                  <h4 class="fw-bold mb-0 text-white">{{ institution.institutionName || institution.name || 'Apex Metropolitan University' }}</h4>
                  <span class="badge badge-translucent text-white px-10 py-4 radius-8 text-xs fw-semibold">
                    {{ institution.academicSession || institution.currentAcademicYear || '2026/2027 Academic Session' }} • {{ institution.currentSemester || 'First Semester (Fall)' }}
                  </span>
                  <span class="badge bg-emerald-600 text-white px-10 py-4 radius-8 text-xs fw-bold d-inline-flex align-items-center gap-4">
                    <span class="w-8-px h-8-px rounded-circle bg-white d-inline-block"></span>
                    Accredited Campus
                  </span>
                </div>
                <p class="text-white text-opacity-80 text-sm mb-0 mt-6 font-italic">
                  "{{ institution.motto || 'Excellence, Integrity & Innovation' }}" • University Academic Portal & Student Information System
                </p>
              </div>
            </div>

            <!-- Right: Quick Actions & Role Scope -->
            <div class="d-flex align-items-center gap-12 flex-wrap">
              <div class="bg-black bg-opacity-20 px-16 py-10 radius-12 border border-white border-opacity-10 text-end">
                <span class="text-white text-opacity-70 text-xs d-block">Operator Scope</span>
                <span class="fw-bold text-sm text-white text-capitalize">
                  {{ currentUser?.role?.replace('-', ' ') || 'Executive Admin' }}
                </span>
              </div>
              <router-link 
                v-if="auth.isSuperAdmin"
                to="/general" 
                class="btn btn-light radius-10 px-16 py-10 text-sm fw-bold d-flex align-items-center gap-6 shadow-sm"
                style="background-color: #ffffff !important; color: #111827 !important; border: 1px solid #ffffff !important;"
              >
                <i class="ri-settings-3-fill text-lg text-primary-600"></i>
                <span style="color: #111827 !important;">Campus CMS</span>
              </router-link>
            </div>

          </div>
        </div>
      </div>

      <!-- ================= University Executive Briefing Strip ================= -->
      <div class="alert alert-neutral border border-neutral-300 radius-12 bg-white shadow-1 py-12 px-20 mb-24">
        <div class="d-flex flex-wrap align-items-center justify-content-between gap-16">
          <div class="d-flex align-items-center gap-10">
            <span class="badge bg-primary-600 text-white text-xs px-8 py-4 radius-6 fw-bold">
              REGISTRY BRIEFING
            </span>
            <span class="fw-bold text-neutral-800 text-sm">Harmattan Semester Senate Operations:</span>
            <span class="text-secondary-light text-xs">Course registration open • Continuous assessment submission window active.</span>
          </div>
          <div class="d-flex align-items-center gap-20 text-xs">
            <span class="d-flex align-items-center gap-6 text-neutral-700 fw-semibold">
              <i class="ri-calendar-check-line text-primary-600"></i>
              Week 8 of 16
            </span>
            <span class="d-flex align-items-center gap-6 text-neutral-700 fw-semibold">
              <i class="ri-user-follow-line text-success-600"></i>
              91.4% Fee Cleared
            </span>
            <span class="d-flex align-items-center gap-6 text-neutral-700 fw-semibold">
              <i class="ri-shield-check-line text-primary-600"></i>
              Senate Compliance Active
            </span>
          </div>
        </div>
      </div>

      <!-- ================= Academic Standing & Early Advisory Banner ================= -->
      <div class="card border border-danger-subtle radius-16 shadow-1 mb-24 overflow-hidden bg-danger-50 bg-opacity-30">
        <div class="card-body p-20">
          <div class="d-flex flex-wrap align-items-center justify-content-between gap-16">
            <div class="d-flex align-items-center gap-16">
              <div class="w-48-px h-48-px rounded-circle bg-danger-100 text-danger-600 d-flex align-items-center justify-content-center text-2xl flex-shrink-0">
                <iconify-icon icon="solar:shield-warning-bold"></iconify-icon>
              </div>
              <div>
                <div class="d-flex align-items-center gap-8 flex-wrap">
                  <h6 class="fw-bold text-neutral-900 mb-0">Academic Standing & Retention Watchlist</h6>
                  <span class="badge bg-danger-600 text-white px-8 py-2 radius-6 text-xs fw-bold">
                    28 Students Flagged
                  </span>
                  <span class="text-secondary-light text-xs">
                    Harmattan Mid-Semester Senate Audit
                  </span>
                </div>
                <p class="text-neutral-700 text-xs mb-0 mt-4">
                  Registry attendance audits flagged <strong>14 students below the 75% examination eligibility requirement</strong> and <strong>14 students on academic probation watch (CGPA &lt; 1.50)</strong>. Faculty adviser review is required prior to examination pass clearance.
                </p>
              </div>
            </div>

            <button 
              type="button" 
              class="btn btn-danger radius-10 px-18 py-10 text-xs fw-bold d-flex align-items-center gap-8 shadow-sm text-white"
              data-bs-toggle="modal" 
              data-bs-target="#aiRiskDossierModal"
            >
              <iconify-icon icon="solar:eye-bold" class="text-sm"></iconify-icon>
              Review Retention Dossier
            </button>
          </div>
        </div>
      </div>

      <!-- ================= KPI Operational Metrics ================= -->
      <div class="mt-8">
        <div class="row gy-4">
          
          <!-- 6 Higher-Ed KPIs -->
          <div class="col-xxl-8">
            <div class="row gy-4">
              <div class="col-xxl-4 col-sm-6" v-for="(widget, index) in widgets" :key="index">
                <Widget 
                  :title="widget.title" 
                  :subtitle="widget.subtitle"
                  :count="widget.count" 
                  :icon="widget.icon" 
                  :gradientBg="widget.gradientBg"
                  :iconColor="widget.iconColor"
                  :badge="widget.badge"
                  :badgeClass="widget.badgeClass"
                  :trendValue="widget.trendValue"
                  :trendIsPositive="widget.trendIsPositive"
                  :trendLabel="widget.trendLabel"
                  :to="widget.to"
                  :modalTarget="widget.modalTarget"
                  :isHighlighted="widget.isHighlighted"
                />
              </div>
            </div>
          </div>

          <!-- Student Attendance & Exam Disqualification Threshold -->
          <div class="col-xxl-4">
             <StuAttendees />
          </div>

          <!-- Academic Revenue & Institutional Despatches -->
          <div class="col-12">
            <div class="row gy-4">
               <div class="col-xxl-8">
                  <div class="row gy-4">
                     <div class="col-12">
                        <RevenueStatic />
                     </div>
                     <div class="col-md-6">
                        <NoticeBoard />
                     </div>
                     <div class="col-md-6">
                        <LeaveRequests />
                     </div>
                  </div>
               </div>
               <div class="col-xxl-4">
                  <Calendar />
               </div>
            </div>
          </div>

          <!-- Community Demographics & Income -->
          <div class="col-xxl-4 col-lg-6">
             <UserOverview />
          </div>
          <div class="col-xxl-8 col-lg-6">
             <IncomeVsExpense />
          </div>

          <!-- Faculty Chairs & Honour Roll -->
          <div class="col-xxl-4 col-lg-6">
             <TopTeachers />
          </div>
          <div class="col-xxl-4 col-lg-6">
             <NewAdmissions />
          </div>
          <div class="col-xxl-4">
             <TopStudent />
          </div>

        </div>
      </div>
    </div>
    
    <Footer />
  </main>
  
  <!-- AI Early Warning Interactive Dossier Modal -->
  <AiRiskDossierModal />

</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useInstitutionStore } from '@/stores/institution';
import { useAuthStore } from '@/stores/auth';
import { telemetryApi } from '@/services/api.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navabar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import Widget from '@/components/index/index1/Widget.vue';
import StuAttendees from '@/components/index/index1/StuAttendees.vue';
import RevenueStatic from '@/components/index/index1/RevenueStatic.vue';
import NoticeBoard from '@/components/index/index1/NoticeBoard.vue';
import LeaveRequests from '@/components/index/index1/LeaveRequests.vue';
import Calendar from '@/components/index/index1/Calendar.vue';
import UserOverview from '@/components/index/index1/UserOverview.vue';
import IncomeVsExpense from '@/components/index/index1/IncomeVsExpense.vue';
import TopTeachers from '@/components/index/index1/TopTeachers.vue';
import NewAdmissions from '@/components/index/index1/NewAdmissions.vue';
import TopStudent from '@/components/index/index1/TopStudent.vue';
import AiRiskDossierModal from '@/components/index/index1/AiRiskDossierModal.vue';

export default {
  name: "Index1",
  components: {
    Sidebar,
    Navabar,
    Footer,
    Widget,
    StuAttendees,
    RevenueStatic,
    NoticeBoard,
    LeaveRequests,
    Calendar,
    UserOverview,
    IncomeVsExpense,
    TopTeachers,
    NewAdmissions,
    TopStudent,
    AiRiskDossierModal
  },
  setup() {
    const institution = useInstitutionStore();
    const auth = useAuthStore();
    const currentUser = computed(() => auth.currentUser);

    const widgets = ref([
      { 
        title: 'Total Enrolled Students', 
        subtitle: '11,400 Undergrad • 3,420 Postgrad',
        count: '14,820', 
        icon: 'solar:users-group-two-rounded-bold', 
        gradientBg: 'gradient-bg-end-1', 
        iconColor: 'bg-primary-600',
        badge: 'Accredited',
        badgeClass: 'bg-primary-50 text-primary-700',
        trendValue: '+3.8%',
        trendIsPositive: true,
        trendLabel: 'vs Last Session',
        to: '/student-list'
      },
      { 
        title: 'Academic Faculty & Staff', 
        subtitle: '412 Professors • 430 Lecturers',
        count: '842', 
        icon: 'solar:square-academic-cap-bold', 
        gradientBg: 'gradient-bg-end-2', 
        iconColor: 'bg-blue-600',
        badge: 'Active Roster',
        badgeClass: 'bg-blue-50 text-blue-700',
        trendValue: '1:17.6',
        trendIsPositive: true,
        trendLabel: 'Staff-to-Student Ratio',
        to: '/teacher-list'
      },
      { 
        title: 'Active Course Sections', 
        subtitle: 'Across 8 Accredited Faculties',
        count: '318', 
        icon: 'solar:book-bookmark-bold', 
        gradientBg: 'gradient-bg-end-3', 
        iconColor: 'bg-purple-600',
        badge: 'Harmattan',
        badgeClass: 'bg-purple-50 text-purple-700',
        trendValue: '100%',
        trendIsPositive: true,
        trendLabel: 'Timetable Assigned',
        to: '/class-list'
      },
      { 
        title: 'Bursary Fee Collection', 
        subtitle: '$4.2M Collected • $396K Pending',
        count: '91.4%', 
        icon: 'solar:wallet-money-bold', 
        gradientBg: 'gradient-bg-end-4', 
        iconColor: 'bg-warning-600',
        badge: 'Bursary Target Met',
        badgeClass: 'bg-warning-50 text-warning-800',
        trendValue: '+4.2%',
        trendIsPositive: true,
        trendLabel: 'Ahead of Schedule',
        to: '/fees-collection'
      },
      { 
        title: 'Academic Retention Watchlist', 
        subtitle: 'Attendance deficit & probation watch',
        count: '28 Flagged', 
        icon: 'solar:shield-warning-bold', 
        gradientBg: 'gradient-bg-end-5', 
        iconColor: 'bg-danger-600',
        badge: 'Advisory Required',
        badgeClass: 'bg-danger-subtle text-danger-700',
        trendValue: '14 Exam Holds',
        trendIsPositive: false,
        trendLabel: 'Attendance < 75%',
        modalTarget: '#aiRiskDossierModal',
        isHighlighted: true
      },
      { 
        title: 'Campus System Health', 
        subtitle: 'Biometric Turnstiles & SIS Synced',
        count: '99.9%', 
        icon: 'solar:server-bold', 
        gradientBg: 'gradient-bg-end-6', 
        iconColor: 'bg-cyan-600',
        badge: 'Optimal',
        badgeClass: 'bg-success-subtle text-success-700',
        trendValue: '12ms',
        trendIsPositive: true,
        trendLabel: 'API Response P95'
      }
    ]);

    onMounted(async () => {
      try {
        const res = await telemetryApi.getOverview();
        if (res && res.kpis) {
          const k = res.kpis;
          widgets.value[0].count = Number(k.totalStudents).toLocaleString();
          widgets.value[0].subtitle = `${Number(k.undergrad).toLocaleString()} Undergrad • ${Number(k.postgrad).toLocaleString()} Postgrad`;
          widgets.value[1].count = Number(k.academicFaculty).toLocaleString();
          widgets.value[2].count = Number(k.activeCourses).toLocaleString();
          widgets.value[3].count = `${k.tuitionCollectionRate}%`;
          widgets.value[4].count = `${k.atRiskStudentsCount} Flagged`;
          widgets.value[5].count = `${k.systemUptime}%`;
          widgets.value[5].trendValue = `${k.apiLatencyMs}ms`;
        }
      } catch (err) {
        // Fall back to defaults
      }
    });

    return {
      institution,
      auth,
      currentUser,
      widgets
    };
  }
}
</script>