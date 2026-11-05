<template>
  <div class="card border-0 shadow-1 radius-16 overflow-hidden ai-advisor-card mb-24">
    <div class="card-body p-20 p-md-24 position-relative">
      <!-- Ambient decorative glow -->
      <div class="ai-glow-orb position-absolute top-0 end-0"></div>

      <div class="d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-16 position-relative z-1">
        <div class="d-flex align-items-start gap-16">
          <!-- AI Brain Icon -->
          <div class="w-52-px h-52-px rounded-circle d-flex align-items-center justify-content-center flex-shrink-0 ai-icon-badge shadow-sm">
            <i class="ri-sparkling-2-fill text-2xl text-white"></i>
          </div>

          <div>
            <div class="d-flex flex-wrap align-items-center gap-8 mb-6">
              <span class="badge bg-primary-600 text-white text-xs px-10 py-3 radius-6 fw-semibold d-inline-flex align-items-center gap-6">
                <i class="ri-robot-2-line"></i> SmartAdvisor AI™
              </span>
              <span 
                class="badge text-xs px-10 py-3 radius-6 fw-bold"
                :class="enrollmentStore.hasMandatoryCarryovers ? 'bg-danger-100 text-danger-700 border border-danger-200' : 'bg-success-100 text-success-700 border border-success-200'"
              >
                <i :class="enrollmentStore.hasMandatoryCarryovers ? 'ri-error-warning-line' : 'ri-checkbox-circle-line'" class="me-4"></i>
                {{ enrollmentStore.aiAdvisory?.badgeText || (enrollmentStore.hasMandatoryCarryovers ? 'Carryover Priority Active' : 'Clean Standing') }}
              </span>
              <span class="text-secondary-light text-xs">
                Senate Regulation 4.2 Automated Compliance Engine
              </span>
            </div>

            <h5 class="text-lg fw-bold text-neutral-900 mb-6">
              {{ enrollmentStore.aiAdvisory?.headline || 'AI Academic Advisory Assessment' }}
            </h5>

            <p class="text-neutral-700 text-sm mb-8 line-height-1-5 max-w-850-px">
              {{ enrollmentStore.aiAdvisory?.directive }}
            </p>

            <div class="d-flex flex-wrap align-items-center gap-12 text-xs text-secondary-light">
              <span class="d-inline-flex align-items-center gap-6 bg-base px-10 py-4 radius-6 border border-neutral-200">
                <i class="ri-user-star-line text-primary-600"></i>
                <strong>Scholar:</strong> {{ enrollmentStore.student?.name }} ({{ enrollmentStore.student?.matricNumber }})
              </span>
              <span class="d-inline-flex align-items-center gap-6 bg-base px-10 py-4 radius-6 border border-neutral-200">
                <i class="ri-award-line text-warning-600"></i>
                <strong>Academic Standing:</strong> {{ enrollmentStore.student?.cgpa?.toFixed(2) }} CGPA
              </span>
              <span class="d-inline-flex align-items-center gap-6 bg-base px-10 py-4 radius-6 border border-neutral-200">
                <i class="ri-speed-up-line text-info-600"></i>
                <strong>Pacing Recommendation:</strong> {{ enrollmentStore.aiAdvisory?.workloadRecommendation }}
              </span>
            </div>
          </div>
        </div>

        <!-- Quick Action Trigger -->
        <div class="d-flex flex-column align-items-lg-end gap-8 flex-shrink-0">
          <button 
            type="button" 
            class="btn btn-outline-primary btn-sm radius-8 d-inline-flex align-items-center gap-6 px-16 py-8"
            :disabled="enrollmentStore.isLoading"
            @click="handleRefreshAudit"
          >
            <i class="ri-refresh-line" :class="{ 'spin-anim': enrollmentStore.isLoading }"></i>
            {{ enrollmentStore.isLoading ? 'Re-Auditing...' : 'Sync Transcript' }}
          </button>
          <span class="text-xxs text-secondary-light">
            Active: {{ enrollmentStore.session }} • {{ enrollmentStore.semester }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: 'AiAdvisorBanner',
  setup() {
    const enrollmentStore = useEnrollmentStore();

    const handleRefreshAudit = async () => {
      await enrollmentStore.fetchAudit();
    };

    return {
      enrollmentStore,
      handleRefreshAudit
    };
  }
};
</script>

<style scoped>
.ai-advisor-card {
  background: linear-gradient(135deg, rgba(72, 127, 255, 0.08) 0%, rgba(139, 92, 246, 0.05) 100%);
  border: 1px solid rgba(72, 127, 255, 0.2) !important;
}

.ai-icon-badge {
  background: linear-gradient(135deg, #487fff 0%, #7c3aed 100%);
}

.ai-glow-orb {
  width: 200px;
  height: 200px;
  background: radial-gradient(circle, rgba(124, 58, 237, 0.12) 0%, transparent 70%);
  pointer-events: none;
}

.max-w-850-px {
  max-width: 850px;
}

.spin-anim {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  100% {
    transform: rotate(360deg);
  }
}
</style>
