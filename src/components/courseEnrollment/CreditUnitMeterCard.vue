<template>
  <div class="card border-0 shadow-1 radius-16 sticky-top" style="top: 24px;">
    <div class="card-body p-20 p-md-24">
      <div class="d-flex align-items-center justify-content-between gap-8 pb-16 border-bottom border-neutral-200">
        <div>
          <h6 class="text-md fw-bold text-neutral-900 mb-0">Credit Unit Load Meter</h6>
          <span class="text-secondary-light text-xs">Senate Policy: Min 15 • Max 24 Units</span>
        </div>
        <span 
          class="badge text-xs px-10 py-4 radius-6 fw-bold"
          :class="meterBadgeClass"
        >
          {{ meterBadgeText }}
        </span>
      </div>

      <!-- Real-time Progress Bar -->
      <div class="mt-20">
        <div class="d-flex align-items-center justify-content-between mb-8">
          <span class="text-xs text-secondary-light">Total Registered Load</span>
          <span class="text-sm fw-bold" :class="meterTextClass">
            {{ enrollmentStore.totalSelectedUnits }} / 24 <span class="text-xs fw-normal text-secondary-light">Units</span>
          </span>
        </div>

        <div class="progress" style="height: 10px; border-radius: 6px;">
          <!-- Carryover portion (Danger) -->
          <div 
            class="progress-bar bg-danger-600" 
            role="progressbar" 
            :style="{ width: `${carryoverPercentage}%` }"
            :aria-valuenow="enrollmentStore.carryoverUnits" 
            aria-valuemin="0" 
            aria-valuemax="24"
            v-tooltip="`Carryover Units: ${enrollmentStore.carryoverUnits}`"
          ></div>
          <!-- Current level portion (Primary) -->
          <div 
            class="progress-bar bg-primary-600" 
            role="progressbar" 
            :style="{ width: `${regularPercentage}%` }"
            :aria-valuenow="enrollmentStore.regularUnits" 
            aria-valuemin="0" 
            aria-valuemax="24"
            v-tooltip="`Current Level Units: ${enrollmentStore.regularUnits}`"
          ></div>
        </div>

        <div class="d-flex align-items-center justify-content-between mt-6 text-xxs text-secondary-light">
          <span>0 Min</span>
          <span class="text-warning-700 fw-semibold">15 Unit Threshold</span>
          <span class="text-danger-700 fw-semibold">24 Max Ceiling</span>
        </div>
      </div>

      <!-- Unit Accounting Breakdown -->
      <div class="mt-20 p-14 radius-10 bg-neutral-50 border border-neutral-200 d-flex flex-column gap-10">
        <div class="d-flex align-items-center justify-content-between text-xs">
          <span class="text-secondary-light d-flex align-items-center gap-6">
            <span class="w-8-px h-8-px rounded-circle bg-danger-600"></span>
            Mandatory Carryovers (Locked):
          </span>
          <strong class="text-danger-700 font-monospace">{{ enrollmentStore.carryoverUnits }} Units</strong>
        </div>

        <div class="d-flex align-items-center justify-content-between text-xs">
          <span class="text-secondary-light d-flex align-items-center gap-6">
            <span class="w-8-px h-8-px rounded-circle bg-primary-600"></span>
            Current Level Modules:
          </span>
          <strong class="text-primary-700 font-monospace">{{ enrollmentStore.regularUnits }} Units</strong>
        </div>

        <div class="d-flex align-items-center justify-content-between text-xs pt-8 border-top border-neutral-200">
          <span class="text-neutral-900 fw-bold">Total Semester Credit Units:</span>
          <strong class="text-neutral-900 font-monospace fs-6">{{ enrollmentStore.totalSelectedUnits }} Units</strong>
        </div>
      </div>

      <!-- Queued Courses Compact List -->
      <div class="mt-20">
        <h6 class="text-xs fw-bold text-neutral-800 text-uppercase mb-8">
          Queued Modules ({{ enrollmentStore.selectedCourses.length }})
        </h6>

        <div class="queued-courses-list d-flex flex-column gap-6 max-h-200-px overflow-y-auto pe-4">
          <div 
            v-for="c in enrollmentStore.selectedCourses" 
            :key="c.id"
            class="d-flex align-items-center justify-content-between p-8 radius-6 border border-neutral-100 bg-base text-xs"
          >
            <div class="d-flex align-items-center gap-6 min-w-0">
              <i 
                v-if="enrollmentStore.isCarryoverLocked(c.id)" 
                class="ri-lock-2-fill text-danger-600 flex-shrink-0"
                title="Mandatory Carryover Locked"
              ></i>
              <span class="fw-bold font-monospace" :class="enrollmentStore.isCarryoverLocked(c.id) ? 'text-danger-700' : 'text-primary-600'">
                {{ c.code }}
              </span>
              <span class="text-truncate text-secondary-light" style="max-width: 140px;">
                {{ c.title }}
              </span>
            </div>

            <div class="d-flex align-items-center gap-6 flex-shrink-0">
              <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-6 py-2 radius-4">
                {{ c.creditUnits }}u
              </span>
              <button 
                v-if="!enrollmentStore.isCarryoverLocked(c.id)"
                type="button" 
                class="btn p-0 text-danger-500 hover-text-danger-700 border-0 bg-transparent line-height-1"
                title="Remove course"
                @click="enrollmentStore.toggleCourse(c)"
              >
                <i class="ri-close-circle-line"></i>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Action Button -->
      <div class="mt-24">
        <button 
          type="button" 
          class="btn btn-primary w-100 py-12 radius-10 fw-bold d-flex align-items-center justify-content-center gap-8 shadow-sm"
          :disabled="!enrollmentStore.canSubmit || enrollmentStore.isSubmitting"
          @click="handleSubmit"
        >
          <span v-if="enrollmentStore.isSubmitting" class="spinner-border spinner-border-sm" role="status"></span>
          <i v-else class="ri-shield-check-fill text-lg"></i>
          <span>{{ enrollmentStore.isSubmitting ? 'Registering...' : 'Submit AI-Verified Registration' }}</span>
        </button>

        <p class="text-xxs text-center text-secondary-light mt-8 mb-0">
          <i class="ri-checkbox-circle-fill text-success-600 me-2"></i>
          Complies with 2026/2027 Senate Academic Regulations
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: 'CreditUnitMeterCard',
  setup() {
    const enrollmentStore = useEnrollmentStore();

    const carryoverPercentage = computed(() => {
      const units = enrollmentStore.carryoverUnits;
      return Math.min(100, (units / 24) * 100);
    });

    const regularPercentage = computed(() => {
      const units = enrollmentStore.regularUnits;
      return Math.min(100, (units / 24) * 100);
    });

    const meterBadgeClass = computed(() => {
      if (enrollmentStore.isOverload) return 'bg-danger-600 text-white';
      if (enrollmentStore.isUnderload) return 'bg-warning-100 text-warning-800 border border-warning-200';
      if (enrollmentStore.totalSelectedUnits >= 22) return 'bg-info-100 text-info-800 border border-info-200';
      return 'bg-success-100 text-success-700 border border-success-200';
    });

    const meterBadgeText = computed(() => {
      if (enrollmentStore.isOverload) return 'Overload Alert (>24)';
      if (enrollmentStore.isUnderload) return 'Underload (<15)';
      if (enrollmentStore.totalSelectedUnits >= 22) return 'Maximum Load';
      return 'Balanced Load';
    });

    const meterTextClass = computed(() => {
      if (enrollmentStore.isOverload) return 'text-danger-600';
      if (enrollmentStore.isUnderload) return 'text-warning-600';
      return 'text-success-600';
    });

    const handleSubmit = async () => {
      await enrollmentStore.submitRegistration();
    };

    return {
      enrollmentStore,
      carryoverPercentage,
      regularPercentage,
      meterBadgeClass,
      meterBadgeText,
      meterTextClass,
      handleSubmit
    };
  }
};
</script>

<style scoped>
.max-h-200-px {
  max-height: 200px;
}
</style>
