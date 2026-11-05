<template>
  <div class="card border-0 shadow-1 radius-16 mb-24 carryover-section-card" :class="{ 'has-carryovers-border': enrollmentStore.hasMandatoryCarryovers }">
    <div class="card-body p-20 p-md-24">
      <div class="d-flex flex-wrap align-items-center justify-content-between gap-12 pb-16 border-bottom border-neutral-200">
        <div>
          <div class="d-flex align-items-center gap-8">
            <h6 class="text-md fw-bold text-neutral-900 mb-0">
              1. Mandatory Previous-Level Carryovers
            </h6>
            <span 
              class="badge text-xxs px-8 py-2 rounded-pill fw-bold"
              :class="enrollmentStore.hasMandatoryCarryovers ? 'bg-danger-600 text-white' : 'bg-success-600 text-white'"
            >
              {{ enrollmentStore.mandatoryCarryovers.length }} Required
            </span>
          </div>
          <span class="text-secondary-light text-xs">
            Senate Regulation 4.2: Unfulfilled courses from previous levels must be pre-registered and cleared first.
          </span>
        </div>

        <div v-if="enrollmentStore.hasMandatoryCarryovers" class="d-flex align-items-center gap-6">
          <span class="badge bg-danger-50 text-danger-700 border border-danger-200 text-xs px-10 py-4 radius-6 fw-semibold d-inline-flex align-items-center gap-6">
            <i class="ri-lock-2-fill text-danger-600"></i> Auto-Enrolled & Locked by AI
          </span>
        </div>
      </div>

      <!-- Active Carryovers List -->
      <div v-if="enrollmentStore.hasMandatoryCarryovers" class="mt-16 d-flex flex-column gap-12">
        <div 
          v-for="course in enrollmentStore.mandatoryCarryovers" 
          :key="course.id"
          class="carryover-item p-16 radius-12 border border-danger-200 bg-danger-50 bg-opacity-25 d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-16"
        >
          <div class="d-flex align-items-start gap-14">
            <!-- Locked Checkbox Simulation -->
            <div class="locked-check-box flex-shrink-0 mt-4 d-flex align-items-center justify-content-center bg-danger-600 text-white rounded-circle shadow-xs">
              <i class="ri-lock-2-fill text-xs"></i>
            </div>

            <div>
              <div class="d-flex flex-wrap align-items-center gap-8 mb-4">
                <span class="fw-bold text-danger-700 text-sm font-monospace">{{ course.code }}</span>
                <span class="badge bg-danger-100 text-danger-800 text-xxs px-8 py-2 radius-4 fw-bold">
                  {{ course.level }} Carryover
                </span>
                <span class="badge bg-neutral-200 text-neutral-800 text-xxs px-8 py-2 radius-4 fw-semibold">
                  {{ course.creditUnits }} Credit Units
                </span>
                <span class="badge bg-neutral-100 text-secondary-light text-xxs px-8 py-2 radius-4">
                  Failed: {{ course.failedSession }} • Grade: {{ course.failedGrade }} ({{ course.failedScore }}%)
                </span>
              </div>

              <h6 class="text-sm fw-bold text-neutral-900 mb-4">
                {{ course.title }}
              </h6>

              <p class="text-secondary-light text-xs mb-0">
                <i class="ri-information-line me-4 text-danger-600"></i>
                {{ course.reason }}
              </p>
            </div>
          </div>

          <!-- Unit contribution & status -->
          <div class="d-flex align-items-center justify-content-end gap-12 flex-shrink-0">
            <div class="text-end">
              <span class="d-block text-xxs text-secondary-light text-uppercase fw-semibold">Docket Priority</span>
              <span class="text-xs fw-bold text-danger-700 d-inline-flex align-items-center gap-4">
                <i class="ri-shield-keyhole-line"></i> Priority 1 (Locked)
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Zero Carryover Clean State -->
      <div v-else class="text-center py-24">
        <div class="w-48-px h-48-px rounded-circle bg-success-50 text-success-600 d-inline-flex align-items-center justify-content-center text-2xl mb-8">
          <i class="ri-checkbox-circle-line"></i>
        </div>
        <h6 class="text-sm fw-bold text-neutral-900 mb-2">Clean Academic Progression</h6>
        <p class="text-secondary-light text-xs mb-0">
          You have zero pending carryovers from previous levels. You have full degree progression clearance.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: 'CarryoverCoursesSection',
  setup() {
    const enrollmentStore = useEnrollmentStore();
    return {
      enrollmentStore
    };
  }
};
</script>

<style scoped>
.carryover-section-card.has-carryovers-border {
  border: 1px solid rgba(239, 68, 68, 0.35) !important;
}

.carryover-item {
  transition: all 0.2s ease-in-out;
}

.carryover-item:hover {
  background-color: rgba(239, 68, 68, 0.08);
  border-color: rgba(239, 68, 68, 0.5) !important;
}

.locked-check-box {
  width: 22px;
  height: 22px;
  cursor: not-allowed;
}
</style>
