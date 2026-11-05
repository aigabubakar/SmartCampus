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
              <button 
                type="button" 
                class="btn btn-sm radius-8 px-16 py-8 fw-semibold transition-2"
                :class="enrollmentStore.activeTab === 'registration' ? 'bg-primary-600 text-white shadow-sm' : 'text-secondary-light bg-transparent'"
                @click="enrollmentStore.activeTab = 'registration'"
              >
                <i class="ri-file-edit-line me-4"></i> Course Registration
              </button>
              <button 
                type="button" 
                class="btn btn-sm radius-8 px-16 py-8 fw-semibold transition-2"
                :class="enrollmentStore.activeTab === 'slip' ? 'bg-primary-600 text-white shadow-sm' : 'text-secondary-light bg-transparent'"
                @click="handleViewSlip"
              >
                <i class="ri-file-text-line me-4"></i> Official Course Slip
              </button>
            </div>
          </div>
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
        <!-- Tab 1: Registration Workspace -->
        <div v-if="enrollmentStore.activeTab === 'registration'">
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
    InterDepartmentalModal
  },
  setup() {
    const enrollmentStore = useEnrollmentStore();

    onMounted(async () => {
      try {
        await enrollmentStore.fetchAudit();
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
