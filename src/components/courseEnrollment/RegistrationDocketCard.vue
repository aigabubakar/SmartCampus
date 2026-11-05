<template>
  <div class="card border-0 shadow-1 radius-16 sticky-top registration-docket-card" style="top: 24px;">
    <div class="card-body p-20 p-md-24">
      <!-- Header -->
      <div class="d-flex align-items-center justify-content-between gap-12 pb-16 border-bottom border-neutral-200">
        <div>
          <div class="d-flex align-items-center gap-8">
            <h6 class="text-md fw-bold text-neutral-900 mb-0">Active Registration Docket</h6>
            <span class="badge bg-neutral-900 text-white text-xxs px-8 py-2 rounded-pill fw-bold">
              {{ enrollmentStore.selectedCourses.length }} Modules
            </span>
          </div>
          <span class="text-secondary-light text-xs">Harmattan Semester • Official Course Form</span>
        </div>

        <span 
          class="badge text-xs px-10 py-4 radius-6 fw-bold"
          :class="statusBadgeClass"
        >
          {{ statusBadgeText }}
        </span>
      </div>

      <!-- Credit Progress Bar -->
      <div class="mt-16">
        <div class="d-flex align-items-center justify-content-between mb-6">
          <span class="text-xs text-secondary-light">Current Load Accounting</span>
          <span class="text-sm fw-bold" :class="loadTextClass">
            {{ enrollmentStore.totalSelectedUnits }} / 24 <span class="text-xs fw-normal text-secondary-light">Credit Units</span>
          </span>
        </div>

        <div class="progress" style="height: 10px; border-radius: 6px;">
          <!-- Carryover Units (Red) -->
          <div 
            class="progress-bar bg-danger-600" 
            role="progressbar" 
            :style="{ width: `${carryoverPercentage}%` }"
            :aria-valuenow="enrollmentStore.carryoverUnits" 
            aria-valuemin="0" 
            aria-valuemax="24"
            title="Carryover Units"
          ></div>
          <!-- Fresh Units Added by Student (Blue) -->
          <div 
            class="progress-bar bg-primary-600" 
            role="progressbar" 
            :style="{ width: `${regularPercentage}%` }"
            :aria-valuenow="enrollmentStore.regularUnits" 
            aria-valuemin="0" 
            aria-valuemax="24"
            title="Fresh Current-Level Units"
          ></div>
        </div>

        <div class="d-flex align-items-center justify-content-between mt-4 text-xxs text-secondary-light">
          <span>0 Min</span>
          <span class="text-warning-700 fw-semibold">15 Unit Threshold</span>
          <span class="text-danger-700 fw-semibold">24 Max Ceiling</span>
        </div>
      </div>

      <!-- Section A: Mandatory Carryovers (Pre-Enrolled First) -->
      <div class="mt-20">
        <div class="d-flex align-items-center justify-content-between mb-8">
          <span class="text-xxs text-uppercase fw-bold text-danger-700 d-inline-flex align-items-center gap-4">
            <i class="ri-lock-2-fill"></i> 1. Mandatory Carryovers (Enrolled First)
          </span>
          <span class="badge bg-danger-50 text-danger-700 border border-danger-200 text-xxs px-6 py-2 radius-4 fw-semibold">
            {{ enrollmentStore.mandatoryCarryovers.length }} Required ({{ enrollmentStore.carryoverUnits }}u)
          </span>
        </div>

        <!-- Carryover list -->
        <div v-if="enrollmentStore.mandatoryCarryovers.length > 0" class="d-flex flex-column gap-8">
          <div 
            v-for="co in enrollmentStore.mandatoryCarryovers" 
            :key="co.id"
            class="p-10 radius-8 border border-danger-200 bg-danger-50 bg-opacity-25 d-flex align-items-center justify-content-between gap-10"
          >
            <div class="d-flex align-items-center gap-8 min-w-0">
              <span class="badge bg-danger-600 text-white rounded-circle p-4 flex-shrink-0">
                <i class="ri-lock-2-fill text-xxs"></i>
              </span>
              <div class="min-w-0">
                <div class="d-flex align-items-center gap-6">
                  <span class="fw-bold font-monospace text-xs text-danger-800">{{ co.code }}</span>
                  <span class="badge bg-danger-100 text-danger-700 text-xxs px-6 py-1 radius-4">{{ co.creditUnits }} Units</span>
                </div>
                <span class="text-xxs text-secondary-light text-truncate d-block" style="max-width: 170px;">
                  {{ co.title }}
                </span>
              </div>
            </div>

            <span class="badge bg-danger-100 text-danger-700 text-xxs px-6 py-2 radius-4 flex-shrink-0 fw-bold">
              Locked (Senate)
            </span>
          </div>
        </div>
        <div v-else class="p-8 radius-8 bg-neutral-50 text-xxs text-secondary-light text-center">
          No pending carryovers. Clean standing.
        </div>
      </div>

      <!-- Section B: Fresh Courses Added by Student -->
      <div class="mt-20">
        <div class="d-flex align-items-center justify-content-between mb-8">
          <span class="text-xxs text-uppercase fw-bold text-primary-700 d-inline-flex align-items-center gap-4">
            <i class="ri-add-circle-fill"></i> 2. Fresh Courses Added by Student
          </span>
          <span class="badge bg-primary-50 text-primary-700 border border-primary-200 text-xxs px-6 py-2 radius-4 fw-semibold">
            {{ enrollmentStore.freshSelectedCourses.length }} Added ({{ enrollmentStore.regularUnits }}u)
          </span>
        </div>

        <!-- Fresh Courses List -->
        <div v-if="enrollmentStore.freshSelectedCourses.length > 0" class="d-flex flex-column gap-8 max-h-240-px overflow-y-auto pe-2">
          <div 
            v-for="c in enrollmentStore.freshSelectedCourses" 
            :key="c.id"
            class="p-10 radius-8 border border-neutral-200 bg-base d-flex align-items-center justify-content-between gap-10 docket-fresh-item"
          >
            <div class="d-flex align-items-center gap-8 min-w-0">
              <span class="badge bg-primary-100 text-primary-700 text-xxs px-6 py-2 radius-4 fw-bold">
                {{ c.creditUnits }}u
              </span>
              <div class="min-w-0">
                <div class="d-flex align-items-center gap-6">
                  <span class="fw-bold font-monospace text-xs text-neutral-900">{{ c.code }}</span>
                  <span class="badge bg-neutral-100 text-secondary-light text-xxs px-4 py-1 radius-4">
                    {{ c.category }}
                  </span>
                </div>
                <span class="text-xxs text-secondary-light text-truncate d-block" style="max-width: 170px;">
                  {{ c.title }}
                </span>
              </div>
            </div>

            <!-- Remove Button -->
            <button 
              type="button" 
              class="btn btn-outline-danger btn-xs radius-6 p-4 d-flex align-items-center justify-content-center flex-shrink-0"
              title="Remove course from docket"
              @click="enrollmentStore.removeCourse(c.id)"
            >
              <i class="ri-delete-bin-line text-xs"></i>
            </button>
          </div>
        </div>

        <!-- Empty State for Fresh Courses -->
        <div v-else class="p-16 radius-10 border border-dashed border-neutral-300 text-center bg-neutral-50">
          <i class="ri-folder-add-line text-2xl text-neutral-400 d-block mb-4"></i>
          <span class="d-block text-xs fw-semibold text-neutral-800 mb-2">No fresh courses added yet</span>
          <span class="d-block text-xxs text-secondary-light mb-8">
            Select fresh courses from the catalogue on the left to add them to your docket.
          </span>
          <button 
            type="button" 
            class="btn btn-outline-primary btn-xs radius-6 d-inline-flex align-items-center gap-4 px-10 py-4"
            @click="enrollmentStore.quickAddRecommendedCore"
          >
            <i class="ri-magic-line"></i> Quick Add Recommended Core
          </button>
        </div>
      </div>

      <!-- Section C: Academic Underload Concession Request (Appears when units < 15) -->
      <div v-if="enrollmentStore.isUnderload && enrollmentStore.selectedCourses.length > 0" class="mt-16 p-14 radius-12 bg-warning-50 border border-warning-300">
        <div class="d-flex align-items-start gap-8 mb-8">
          <i class="ri-alert-fill text-warning-700 text-lg flex-shrink-0 mt-2"></i>
          <div>
            <h6 class="text-xs fw-bold text-warning-900 mb-2">Senate Academic Underload Notice</h6>
            <p class="text-xxs text-warning-800 mb-0 leading-relaxed">
              Your selected load (<strong>{{ enrollmentStore.totalSelectedUnits }} Units</strong>) is below the standard 15-unit semester minimum. Per Senate Regulation 4.6, you must select an approved concession reason to submit this registration.
            </p>
          </div>
        </div>

        <div class="mt-10">
          <label class="form-label text-xxs fw-bold text-neutral-800 mb-4 d-flex align-items-center justify-content-between">
            <span>Select Underload Justification:</span>
            <span class="badge bg-warning-200 text-warning-900 text-xxs px-6 py-1 radius-4">Required</span>
          </label>
          <select 
            v-model="enrollmentStore.underloadReason"
            class="form-select form-select-sm text-xs radius-8 border-warning-400 bg-white shadow-none"
          >
            <option value="" disabled>-- Select Official Senate Reason --</option>
            <option 
              v-for="reason in enrollmentStore.underloadReasonsList" 
              :key="reason" 
              :value="reason"
            >
              {{ reason }}
            </option>
          </select>
        </div>

        <div class="mt-8">
          <label class="form-label text-xxs text-secondary-light mb-2">
            Adviser Endorsement Notes (Optional):
          </label>
          <input 
            type="text" 
            v-model="enrollmentStore.underloadNotes"
            placeholder="e.g., Approved for final semester degree completion"
            class="form-control form-control-sm text-xxs radius-8 border-warning-300 bg-white"
          />
        </div>

        <div v-if="enrollmentStore.underloadReason" class="mt-8 p-6 radius-6 bg-success-50 border border-success-200 d-flex align-items-center gap-6">
          <i class="ri-checkbox-circle-fill text-success-600 text-xs"></i>
          <span class="text-xxs text-success-800 fw-medium">
            Concession attached. Registration authorized for underload submission.
          </span>
        </div>
      </div>

      <!-- Docket Unit Accounting Breakdown -->
      <div class="mt-20 p-12 radius-10 bg-neutral-50 border border-neutral-200 text-xs d-flex flex-column gap-6">
        <div class="d-flex justify-content-between text-secondary-light">
          <span>Mandatory Carryovers:</span>
          <strong class="text-danger-700 font-monospace">{{ enrollmentStore.carryoverUnits }} Units</strong>
        </div>
        <div class="d-flex justify-content-between text-secondary-light">
          <span>Fresh Courses Added:</span>
          <strong class="text-primary-700 font-monospace">{{ enrollmentStore.regularUnits }} Units</strong>
        </div>
        <div class="d-flex justify-content-between pt-6 border-top border-neutral-200 text-neutral-900 fw-bold">
          <span>Total Docket Units:</span>
          <strong class="font-monospace fs-6" :class="loadTextClass">
            {{ enrollmentStore.totalSelectedUnits }} / 24 Units
          </strong>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="mt-20 d-flex flex-column gap-8">
        <button 
          type="button" 
          class="btn w-100 py-12 radius-10 fw-bold d-flex align-items-center justify-content-center gap-8 shadow-sm"
          :class="enrollmentStore.isUnderload ? 'btn-warning text-neutral-900' : 'btn-primary'"
          :disabled="!enrollmentStore.canSubmit || enrollmentStore.isSubmitting"
          @click="handleSubmit"
        >
          <span v-if="enrollmentStore.isSubmitting" class="spinner-border spinner-border-sm" role="status"></span>
          <i v-else-if="enrollmentStore.isUnderload" class="ri-shield-user-fill text-lg"></i>
          <i v-else class="ri-shield-check-fill text-lg"></i>
          <span>
            {{ enrollmentStore.isSubmitting 
                ? 'Submitting...' 
                : (enrollmentStore.isUnderload ? 'Submit with Underload Concession' : 'Finalize & Submit Course Form') 
            }}
          </span>
        </button>

        <div class="d-flex align-items-center justify-content-between gap-8">
          <button 
            v-if="enrollmentStore.freshSelectedCourses.length > 0"
            type="button" 
            class="btn btn-outline-secondary btn-xs radius-6 text-xxs w-100 py-6"
            @click="enrollmentStore.clearFreshCourses"
          >
            <i class="ri-refresh-line me-2"></i> Clear Fresh Courses
          </button>
          
          <button 
            type="button" 
            class="btn btn-outline-primary btn-xs radius-6 text-xxs w-100 py-6"
            @click="enrollmentStore.quickAddRecommendedCore"
          >
            <i class="ri-magic-line me-2"></i> Auto-Fill Core
          </button>
        </div>

        <p class="text-xxs text-center text-secondary-light mt-4 mb-0">
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
  name: 'RegistrationDocketCard',
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

    const statusBadgeClass = computed(() => {
      if (enrollmentStore.isOverload) return 'bg-danger-600 text-white';
      if (enrollmentStore.isUnderload) {
        return enrollmentStore.underloadReason 
          ? 'bg-warning-500 text-white shadow-xs' 
          : 'bg-warning-100 text-warning-800 border border-warning-200';
      }
      if (enrollmentStore.totalSelectedUnits >= 22) return 'bg-info-100 text-info-800 border border-info-200';
      return 'bg-success-100 text-success-700 border border-success-200';
    });

    const statusBadgeText = computed(() => {
      if (enrollmentStore.isOverload) return 'Overload Alert (>24)';
      if (enrollmentStore.isUnderload) {
        return enrollmentStore.underloadReason 
          ? 'Underload Concession Ready' 
          : 'Underload (<15)';
      }
      if (enrollmentStore.totalSelectedUnits >= 22) return 'Maximum Load';
      return 'Balanced Load';
    });

    const loadTextClass = computed(() => {
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
      statusBadgeClass,
      statusBadgeText,
      loadTextClass,
      handleSubmit
    };
  }
};
</script>

<style scoped>
.max-h-240-px {
  max-height: 240px;
}

.docket-fresh-item {
  transition: all 0.2s ease;
}

.docket-fresh-item:hover {
  background-color: rgba(72, 127, 255, 0.04);
  border-color: rgba(72, 127, 255, 0.4) !important;
}

.btn-xs {
  padding: 4px 8px;
  font-size: 0.75rem;
}
</style>
