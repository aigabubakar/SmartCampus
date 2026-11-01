<template>
  <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-640-px w-100 duration-300 shadow-lg" :class="{ 'translate-x-full': !isOpen, 'active-translate-0': isOpen }">
    <div class="px-24 py-16 border-bottom d-flex align-items-center justify-content-between gap-16 bg-base">
      <div class="d-flex align-items-center gap-10">
        <div class="w-36-px h-36-px rounded-8 bg-primary-50 text-primary-600 d-flex align-items-center justify-content-center">
          <i class="ri-user-add-line text-lg"></i>
        </div>
        <div>
          <h5 class="text-sm fw-bold mb-0 text-primary-light">Provision University Administrator</h5>
          <span class="text-xxs text-secondary-light">Delegated staff operational access</span>
        </div>
      </div>
      <button type="button" class="btn p-0 border-0 text-neutral-400 text-hover-danger-600" @click="$emit('close')">
        <i class="ri-close-large-line text-lg"></i>
      </button>
    </div>

    <form @submit.prevent="handleProvision" class="d-flex flex-column p-24 gap-20">
      
      <!-- Basic Staff Identity -->
      <div>
        <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Administrator Full Name <span class="text-danger-600">*</span></label>
        <input type="text" class="form-control text-sm radius-8" placeholder="e.g. Dr. Arthur Pendelton" v-model="form.name" required />
      </div>

      <div class="row g-3">
        <div class="col-sm-7">
          <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Official University Email <span class="text-danger-600">*</span></label>
          <input type="email" class="form-control text-sm radius-8" placeholder="a.pendelton@campus.edu" v-model="form.email" required />
        </div>
        <div class="col-sm-5">
          <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Staff ID Number <span class="text-danger-600">*</span></label>
          <input type="text" class="form-control text-sm radius-8" placeholder="STAFF-ADM-24" v-model="form.staffId" required />
        </div>
      </div>

      <!-- Department Allocation -->
      <div>
        <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Assigned Department / Directorate <span class="text-danger-600">*</span></label>
        <select class="form-select text-sm radius-8" v-model="form.department" required>
          <option value="Vice Chancellor / Executive Office">Vice Chancellor / Executive Office</option>
          <option value="Academic Registrar Office">Academic Registrar Office</option>
          <option value="Faculty Dean Office">Faculty Dean Office</option>
          <option value="University Bursary & Collections">University Bursary & Collections</option>
          <option value="Undergraduate Admissions Board">Undergraduate Admissions Board</option>
          <option value="Human Resources & Payroll">Human Resources & Payroll</option>
          <option value="Main University Library">Main University Library</option>
        </select>
      </div>

      <!-- Operational Scope Level -->
      <div>
        <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Administrative Operational Scope <span class="text-danger-600">*</span></label>
        <select class="form-select text-sm radius-8" v-model="form.scope" required>
          <option value="Full Campus Operations">Full Campus Operations (All Departments)</option>
          <option value="Academic & Examinations">Academic & Examinations (Curricula, Exams, Grades)</option>
          <option value="Admissions & Student Affairs">Admissions & Student Affairs (Vetting, Registry)</option>
          <option value="Finance & Bursary">Finance & Bursary (Tuition, Accounts, Payroll)</option>
          <option value="Faculty & Staff HRM">Faculty & Staff HRM (Lecturers, Leaves)</option>
        </select>
        <span class="text-xxs text-secondary-light mt-4 d-block">
          Determines the primary operational sphere this administrator can manage.
        </span>
      </div>

      <!-- Granular Operational Permissions -->
      <div class="p-16 rounded-10 bg-neutral-50 border border-neutral-200">
        <label class="text-xs fw-bold text-primary-light mb-8 d-block">Granular Operational Entitlements</label>
        <div class="d-flex flex-column gap-10">
          
          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="permCurriculum" value="curriculum" v-model="form.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="permCurriculum">
              <strong>Modify Curricula & Course Catalogs:</strong> Can create and alter departments, degrees, and syllabus structures.
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="permGrading" value="grading_approvals" v-model="form.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="permGrading">
              <strong>Approve & Finalize Exam Results:</strong> Can sign off on faculty grading sheets and release student transcripts.
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="permAIOverride" value="ai_override" v-model="form.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="permAIOverride">
              <strong>AI Recommendation Overrides:</strong> Can review and override AI at-risk student flags and timetable suggestions.
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="permAdmissions" value="admissions" v-model="form.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="permAdmissions">
              <strong>Admissions Decision Authority:</strong> Can accept or reject student applicant credentials.
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="permFees" value="fee_structures" v-model="form.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="permFees">
              <strong>Tuition & Fee Management:</strong> Can configure fee structures, payment waivers, and audit ledgers.
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="permBroadcast" value="broadcasts" v-model="form.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="permBroadcast">
              <strong>Campus-Wide Emergency Broadcasts:</strong> Can publish official announcements to all portals.
            </label>
          </div>

        </div>
      </div>

      <!-- Action Buttons -->
      <div class="d-flex align-items-center justify-content-end gap-12 pt-16 border-top">
        <button type="button" class="btn btn-outline-neutral-300 text-xs fw-semibold py-10 px-18 rounded-8" @click="$emit('close')">
          Cancel
        </button>
        <button type="submit" class="btn btn-primary-600 text-xs fw-semibold py-10 px-24 rounded-8 d-flex align-items-center gap-6 shadow-sm">
          <i class="ri-check-line"></i>
          <span>Provision Administrator</span>
        </button>
      </div>

    </form>
  </div>
</template>

<script>
import { reactive } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: "RoleAddSidebar",
  props: {
    isOpen: {
      type: Boolean,
      default: false,
    },
  },
  emits: ['close'],
  setup(props, { emit }) {
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const form = reactive({
      name: '',
      email: '',
      staffId: '',
      department: 'Academic Registrar Office',
      scope: 'Academic & Examinations',
      permissions: ['curriculum', 'grading_approvals'],
    });

    const handleProvision = () => {
      try {
        const adminName = form.name;
        const staffId = form.staffId;
        const adminScope = form.scope;

        authStore.createUniversityAdmin({
          name: form.name,
          email: form.email,
          staffId: form.staffId,
          department: form.department,
          scope: form.scope,
          permissions: [...form.permissions],
        });

        toastStore.success(
          `Staff member ${adminName} (${staffId}) granted administrative credentials with ${adminScope} scope.`,
          'Administrator Provisioned'
        );

        // Reset form
        form.name = '';
        form.email = '';
        form.staffId = '';
        form.permissions = ['curriculum', 'grading_approvals'];

        emit('close');
      } catch (err) {
        toastStore.error(err.message, 'Provisioning Error');
      }
    };

    return {
      form,
      handleProvision,
    };
  },
};
</script>

<style scoped>
.max-w-640-px {
  max-width: 640px;
}
.text-xxs {
  font-size: 0.6875rem;
}
</style>
