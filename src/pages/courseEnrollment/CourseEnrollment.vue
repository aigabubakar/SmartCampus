<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <!-- Breadcrumb / Header Area -->
      <div class="d-flex flex-wrap align-items-center justify-content-between gap-16 mb-24">
        <div>
          <h4 class="fw-bold mb-4 text-neutral-900 d-flex align-items-center gap-10">
            <i class="ri-survey-line text-primary-600"></i>
            AI-Powered Course Enrollment
          </h4>
          <span class="text-secondary-light text-sm">
            2026/2027 Academic Session • Senate Academic Regulations & SmartAdvisor AI™
          </span>
        </div>

        <!-- Navigation Tabs -->
        <div class="d-flex align-items-center gap-8 bg-neutral-100 p-4 radius-10">
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
            <i class="ri-file-text-line me-4"></i> Official Slip
          </button>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="enrollmentStore.isLoading" class="text-center py-48">
        <div class="spinner-border text-primary-600 mb-16" style="width: 3rem; height: 3rem;" role="status">
          <span class="visually-hidden">Loading Course Docket...</span>
        </div>
        <h6 class="text-neutral-800 fw-bold mb-4">SmartAdvisor AI is Auditing Your Academic Transcript...</h6>
        <p class="text-secondary-light text-xs">Checking prior level requirements, prerequisites, and credit unit limits.</p>
      </div>

      <!-- Main Content -->
      <div v-else>
        <!-- Tab 1: Registration Workspace -->
        <div v-if="enrollmentStore.activeTab === 'registration'">
          <!-- SmartAdvisor AI Directive Banner -->
          <AiAdvisorBanner />

          <div class="row g-24">
            <!-- Left: Courses (Carryovers + Current Level) -->
            <div class="col-xl-8 col-lg-7">
              <!-- Mandatory Carryovers Section -->
              <CarryoverCoursesSection />

              <!-- Current Level Courses Section -->
              <CurrentLevelCoursesSection />
            </div>

            <!-- Right: Sticky Credit Unit Meter Card -->
            <div class="col-xl-4 col-lg-5">
              <CreditUnitMeterCard />
            </div>
          </div>
        </div>

        <!-- Tab 2: Official Registration Slip -->
        <div v-else-if="enrollmentStore.activeTab === 'slip'">
          <CourseRegistrationSlip />
        </div>
      </div>
    </div>
    <Footer />
  </main>
  <ThemeCustomizer />
</template>

<script>
import { onMounted } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import AiAdvisorBanner from '@/components/courseEnrollment/AiAdvisorBanner.vue';
import CarryoverCoursesSection from '@/components/courseEnrollment/CarryoverCoursesSection.vue';
import CurrentLevelCoursesSection from '@/components/courseEnrollment/CurrentLevelCoursesSection.vue';
import CreditUnitMeterCard from '@/components/courseEnrollment/CreditUnitMeterCard.vue';
import CourseRegistrationSlip from '@/components/courseEnrollment/CourseRegistrationSlip.vue';
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: "CourseEnrollment",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    AiAdvisorBanner,
    CarryoverCoursesSection,
    CurrentLevelCoursesSection,
    CreditUnitMeterCard,
    CourseRegistrationSlip
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
