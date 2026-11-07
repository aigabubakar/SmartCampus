<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <!-- Institutional Academic Header -->
      <div class="card border-0 shadow-1 radius-16 mb-24 overflow-hidden">
        <div class="card-body p-20 p-md-24">
          <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-16">
            <!-- Student & Session Info -->
            <div>
              <div class="d-flex flex-wrap align-items-center gap-8 mb-6">
                <span class="badge bg-primary-600 text-white text-xs px-10 py-3 radius-6 fw-bold">
                  2026/2027 Academic Session
                </span>
                <span class="badge bg-neutral-100 text-neutral-800 text-xs px-10 py-3 radius-6 fw-semibold">
                  First Semester (Harmattan)
                </span>
                <span class="badge bg-success-50 text-success-700 border border-success-200 text-xs px-10 py-3 radius-6 fw-semibold d-inline-flex align-items-center gap-4">
                  <span class="w-6-px h-6-px rounded-circle bg-success-600"></span> Course Registration Active
                </span>
              </div>

              <h4 class="fw-bold mb-4 text-neutral-900 d-flex align-items-center gap-10">
                <i class="ri-survey-line text-primary-600"></i>
                Tertiary Course Enrollment & Registration Portal
              </h4>

              <div class="d-flex flex-wrap align-items-center gap-12 text-xs text-secondary-light">
                <span><strong>Enrolled Scholar:</strong> {{ enrollmentStore.student?.name }}</span>
                <span>•</span>
                <span><strong>Matric No:</strong> <span class="font-monospace text-neutral-900 fw-bold">{{ enrollmentStore.student?.matricNumber }}</span></span>
                <span>•</span>
                <span><strong>Academic Level:</strong> {{ enrollmentStore.student?.level }}</span>
                <span>•</span>
                <span><strong>Program:</strong> {{ enrollmentStore.student?.program }}</span>
                <span>•</span>
                <span><strong>CGPA:</strong> <span class="text-success-700 fw-bold">{{ enrollmentStore.student?.cgpa?.toFixed(2) }}</span></span>
              </div>
            </div>

            <!-- Workspace Mode Toggle Tabs -->
            <div class="d-flex align-items-center gap-8 bg-neutral-100 p-4 radius-10 flex-shrink-0">
              <!-- Adviser Tab (Visible to Lecturers & Admins) -->
              <button 
                v-if="enrollmentStore.isAdviserOrAdmin"
                type="button" 
                class="btn btn-sm radius-8 px-14 py-8 fw-semibold transition-2 d-inline-flex align-items-center gap-6"
                :class="enrollmentStore.activeTab === 'adviser' ? 'bg-primary-600 text-white shadow-sm' : 'text-secondary-light bg-transparent'"
                @click="enrollmentStore.activeTab = 'adviser'"
              >
                <i class="ri-shield-user-line"></i> 
                <span>Level Adviser Console</span>
                <span 
                  v-if="enrollmentStore.adviserSummary?.pendingCount > 0" 
                  class="badge bg-danger-600 text-white text-xxs px-6 py-2 rounded-pill fw-bold"
                >
                  {{ enrollmentStore.adviserSummary?.pendingCount }}
                </span>
              </button>

              <button 
                type="button" 
                class="btn btn-sm radius-8 px-14 py-8 fw-semibold transition-2"
                :class="enrollmentStore.activeTab === 'registration' ? 'bg-primary-600 text-white shadow-sm' : 'text-secondary-light bg-transparent'"
                @click="enrollmentStore.activeTab = 'registration'"
              >
                <i class="ri-file-edit-line me-4"></i> Course Registration
              </button>
              <button 
                type="button" 
                class="btn btn-sm radius-8 px-14 py-8 fw-semibold transition-2"
                :class="enrollmentStore.activeTab === 'slip' ? 'bg-primary-600 text-white shadow-sm' : 'text-secondary-light bg-transparent'"
                @click="handleViewSlip"
              >
                <i class="ri-file-text-line me-4"></i> Official Course Slip
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Live Student Registration Status Banner -->
      <div v-if="!enrollmentStore.isAdviserOrAdmin && enrollmentStore.currentEnrollments.length > 0" class="mb-24">
        <!-- 1. Approved -->
        <div v-if="enrollmentStore.isApprovedByAdviser" class="alert alert-success d-flex align-items-center justify-content-between p-16 radius-12 border-0 shadow-xs mb-0">
          <div class="d-flex align-items-center gap-12">
            <span class="badge bg-success-600 text-white rounded-circle p-8 flex-shrink-0">
              <i class="ri-shield-check-fill text-lg"></i>
            </span>
            <div>
              <h6 class="text-xs fw-bold text-success-900 mb-2">
                Course Registration Approved & Signed by Level Adviser
              </h6>
              <p class="text-xxs text-success-800 mb-0">
                Endorsed by <strong>{{ enrollmentStore.adviserReview?.adviserName || 'Prof. Alistair Finch' }}</strong>
                <span v-if="enrollmentStore.adviserReview?.adviserRemarks"> — Remarks: "{{ enrollmentStore.adviserReview?.adviserRemarks }}"</span>.
                Your Form 01 Course Registration Slip is cleared for examinations.
              </p>
            </div>
          </div>
          <button 
            type="button" 
            class="btn btn-success btn-xs radius-6 px-12 py-6 text-xxs fw-bold flex-shrink-0 ms-12"
            @click="handleViewSlip"
          >
            <i class="ri-printer-line me-2"></i> View Official Slip
          </button>
        </div>

        <!-- 2. Disapproved / Action Required -->
        <div v-else-if="enrollmentStore.isDisapprovedByAdviser" class="alert alert-danger d-flex align-items-center justify-content-between p-16 radius-12 border-0 shadow-xs mb-0">
          <div class="d-flex align-items-center gap-12">
            <span class="badge bg-danger-600 text-white rounded-circle p-8 flex-shrink-0">
              <i class="ri-alert-fill text-lg"></i>
            </span>
            <div>
              <h6 class="text-xs fw-bold text-danger-900 mb-2">
                Action Required: Level Adviser Disapproved Registration
              </h6>
              <p class="text-xxs text-danger-800 mb-0">
                <strong>Adviser Feedback:</strong> "{{ enrollmentStore.adviserReview?.adviserRemarks || 'Please review your course selection and re-submit.' }}"
                <br />
                Your registration docket has been unlocked. Make the requested course adjustments below and click <strong>"Re-Submit Registration"</strong>.
              </p>
            </div>
          </div>
          <button 
            type="button" 
            class="btn btn-danger btn-xs radius-6 px-12 py-6 text-xxs fw-bold flex-shrink-0 ms-12"
            @click="enrollmentStore.activeTab = 'registration'"
          >
            <i class="ri-edit-line me-2"></i> Fix Courses Below
          </button>
        </div>

        <!-- 3. Pending Review -->
        <div v-else-if="enrollmentStore.isPendingAdviserApproval" class="alert alert-warning d-flex align-items-center justify-content-between p-16 radius-12 border-0 shadow-xs mb-0">
          <div class="d-flex align-items-center gap-12">
            <span class="badge bg-warning-600 text-white rounded-circle p-8 flex-shrink-0">
              <i class="ri-time-fill text-lg"></i>
            </span>
            <div>
              <h6 class="text-xs fw-bold text-warning-900 mb-2">
                Registration Submitted • Awaiting Level Adviser Endorsement
              </h6>
              <p class="text-xxs text-warning-800 mb-0">
                Your course form has been submitted and is currently queued for audit by your Departmental Level Adviser (<strong>{{ enrollmentStore.adviserReview?.adviserName || 'Prof. Alistair Finch' }}</strong>).
              </p>
            </div>
          </div>
          <button 
            type="button" 
            class="btn btn-outline-warning btn-xs radius-6 px-12 py-6 text-xxs fw-bold text-neutral-900 flex-shrink-0 ms-12"
            @click="handleViewSlip"
          >
            <i class="ri-file-text-line me-2"></i> Preview Slip
          </button>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="enrollmentStore.isLoading" class="text-center py-48">
        <div class="spinner-border text-primary-600 mb-16" style="width: 3rem; height: 3rem;" role="status">
          <span class="visually-hidden">Auditing Academic Records...</span>
        </div>
        <h6 class="text-neutral-800 fw-bold mb-4">SmartAdvisor AI is Auditing Your Academic Records...</h6>
        <p class="text-secondary-light text-xs">Inspecting prior level requirements, unfulfilled carryovers, and degree prerequisites.</p>
      </div>

      <!-- Main Workspace -->
      <div v-else>
        <!-- Tab 0: Level Adviser Review & Approval Console (For Lecturers & Admins) -->
        <div v-if="enrollmentStore.activeTab === 'adviser'">
          <AdviserApprovalConsole />
        </div>

        <!-- Tab 1: Registration Workspace -->
        <div v-else-if="enrollmentStore.activeTab === 'registration'">
          <!-- SmartAdvisor AI Directive Banner -->
          <AiAdvisorBanner />

          <div class="row g-24">
            <!-- Left Column (col-xl-7): Course Catalogue - Browse & Add Fresh Courses -->
            <div class="col-xl-7 col-lg-7">
              <CourseCatalogueSection />
            </div>

            <!-- Right Column (col-xl-5): Active Registration Docket (Pre-enrolled carryover at top + fresh courses) -->
            <div class="col-xl-5 col-lg-5">
              <RegistrationDocketCard />
            </div>
          </div>
        </div>

        <!-- Tab 2: Official Registration Slip (Form 01) -->
        <div v-else-if="enrollmentStore.activeTab === 'slip'">
          <CourseRegistrationSlip />
        </div>
      </div>
    </div>
    <Footer />
  </main>

  <!-- Inter-Departmental Elective Modal -->
  <InterDepartmentalModal />

  <ThemeCustomizer />
</template>

<script>
import { onMounted } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import AiAdvisorBanner from '@/components/courseEnrollment/AiAdvisorBanner.vue';
import CourseCatalogueSection from '@/components/courseEnrollment/CourseCatalogueSection.vue';
import RegistrationDocketCard from '@/components/courseEnrollment/RegistrationDocketCard.vue';
import CourseRegistrationSlip from '@/components/courseEnrollment/CourseRegistrationSlip.vue';
import InterDepartmentalModal from '@/components/courseEnrollment/InterDepartmentalModal.vue';
import AdviserApprovalConsole from '@/components/courseEnrollment/AdviserApprovalConsole.vue';
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: "CourseEnrollment",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    AiAdvisorBanner,
    CourseCatalogueSection,
    RegistrationDocketCard,
    CourseRegistrationSlip,
    InterDepartmentalModal,
    AdviserApprovalConsole
  },
  setup() {
    const enrollmentStore = useEnrollmentStore();

    onMounted(async () => {
      try {
        await enrollmentStore.fetchAudit();
        if (enrollmentStore.isAdviserOrAdmin) {
          enrollmentStore.activeTab = 'adviser';
          await enrollmentStore.fetchAdviserSubmissions();
        }
      } catch (err) {
        console.error('Failed to load course enrollment audit:', err);
      }
    });

    const handleViewSlip = async () => {
      await enrollmentStore.fetchSlip();
      enrollmentStore.activeTab = 'slip';
    };

    return {
      enrollmentStore,
      handleViewSlip
    };
  }
};
</script>

<style scoped>
.transition-2 {
  transition: all 0.2s ease-in-out;
}
</style>
