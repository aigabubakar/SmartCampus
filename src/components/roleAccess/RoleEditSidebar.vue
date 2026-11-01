<template>
  <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-640-px w-100 duration-300 shadow-lg" :class="{ 'translate-x-full': !isOpen, 'active-translate-0': isOpen }">
    <div class="px-24 py-16 border-bottom d-flex align-items-center justify-content-between gap-16 bg-base">
      <div class="d-flex align-items-center gap-10">
        <div class="w-36-px h-36-px rounded-8 bg-blue-50 text-blue-600 d-flex align-items-center justify-content-center">
          <i class="ri-edit-2-line text-lg"></i>
        </div>
        <div>
          <h5 class="text-sm fw-bold mb-0 text-primary-light">Edit Administrator Entitlements</h5>
          <span class="text-xxs text-secondary-light">{{ localAdmin.name }} ({{ localAdmin.staffId }})</span>
        </div>
      </div>
      <button type="button" class="btn p-0 border-0 text-neutral-400 text-hover-danger-600" @click="$emit('close')">
        <i class="ri-close-large-line text-lg"></i>
      </button>
    </div>

    <!-- Root Protection Warning Banner -->
    <div v-if="localAdmin.isRoot" class="m-20 p-14 rounded-8 bg-danger-50 border border-danger-200 text-danger-700 text-xs d-flex align-items-start gap-10">
      <i class="ri-lock-2-line text-lg flex-shrink-0 mt-2"></i>
      <div>
        <strong class="d-block mb-2">Protected Developer Root Account</strong>
        <span>This account belongs to the platform vendor/developer and maintains immutable root ownership across all university subsystems.</span>
      </div>
    </div>

    <form @submit.prevent="handleUpdate" class="d-flex flex-column p-24 gap-20">
      
      <div>
        <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Administrator Full Name</label>
        <input type="text" class="form-control text-sm radius-8" v-model="localAdmin.name" :disabled="localAdmin.isRoot" required />
      </div>

      <div class="row g-3">
        <div class="col-sm-7">
          <label class="text-xs fw-semibold text-primary-light mb-6 d-block">University Email</label>
          <input type="email" class="form-control text-sm radius-8" v-model="localAdmin.email" :disabled="localAdmin.isRoot" required />
        </div>
        <div class="col-sm-5">
          <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Staff ID</label>
          <input type="text" class="form-control text-sm radius-8" v-model="localAdmin.staffId" :disabled="localAdmin.isRoot" required />
        </div>
      </div>

      <div>
        <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Department</label>
        <select class="form-select text-sm radius-8" v-model="localAdmin.department" :disabled="localAdmin.isRoot">
          <option value="Vice Chancellor / Executive Office">Vice Chancellor / Executive Office</option>
          <option value="Academic Registrar Office">Academic Registrar Office</option>
          <option value="Faculty Dean Office">Faculty Dean Office</option>
          <option value="University Bursary & Collections">University Bursary & Collections</option>
          <option value="Undergraduate Admissions Board">Undergraduate Admissions Board</option>
          <option value="Human Resources & Payroll">Human Resources & Payroll</option>
          <option value="Main University Library">Main University Library</option>
        </select>
      </div>

      <div>
        <label class="text-xs fw-semibold text-primary-light mb-6 d-block">Administrative Operational Scope</label>
        <select class="form-select text-sm radius-8" v-model="localAdmin.scope" :disabled="localAdmin.isRoot">
          <option value="Full Campus Operations">Full Campus Operations</option>
          <option value="Academic & Examinations">Academic & Examinations</option>
          <option value="Admissions & Student Affairs">Admissions & Student Affairs</option>
          <option value="Finance & Bursary">Finance & Bursary</option>
          <option value="Faculty & Staff HRM">Faculty & Staff HRM</option>
        </select>
      </div>

      <!-- Granular Permissions -->
      <div class="p-16 rounded-10 bg-neutral-50 border border-neutral-200" v-if="!localAdmin.isRoot">
        <label class="text-xs fw-bold text-primary-light mb-8 d-block">Configured Operational Permissions</label>
        <div class="d-flex flex-column gap-10">
          
          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="editPermCurriculum" value="curriculum" v-model="localAdmin.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="editPermCurriculum">
              Modify Curricula & Course Catalogs
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="editPermGrading" value="grading_approvals" v-model="localAdmin.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="editPermGrading">
              Approve & Release Semester Exam Grades
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="editPermAI" value="ai_override" v-model="localAdmin.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="editPermAI">
              AI Recommendation Overrides (Student Risk & Timetable Solvers)
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="editPermAdmissions" value="admissions" v-model="localAdmin.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="editPermAdmissions">
              Admissions Application Decisions
            </label>
          </div>

          <div class="form-check d-flex align-items-center gap-8 m-0">
            <input class="form-check-input border-neutral-400" type="checkbox" id="editPermFees" value="fee_structures" v-model="localAdmin.permissions" />
            <label class="form-check-label text-xs text-neutral-700 cursor-pointer" for="editPermFees">
              Tuition Fee Structures & Payment Waivers
            </label>
          </div>

        </div>
      </div>

      <div class="d-flex align-items-center justify-content-end gap-12 pt-16 border-top">
        <button type="button" class="btn btn-outline-neutral-300 text-xs fw-semibold py-10 px-18 rounded-8" @click="$emit('close')">
          Cancel
        </button>
        <button type="submit" class="btn btn-primary-600 text-xs fw-semibold py-10 px-24 rounded-8 d-flex align-items-center gap-6 shadow-sm" :disabled="localAdmin.isRoot">
          <i class="ri-save-line"></i>
          <span>Save Changes</span>
        </button>
      </div>

    </form>
  </div>
</template>

<script>
import { reactive, watch } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: "RoleEditSidebar",
  props: {
    isOpen: {
      type: Boolean,
      default: false,
    },
    role: {
      type: Object,
      default: null,
    },
  },
  emits: ['close'],
  setup(props, { emit }) {
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const localAdmin = reactive({
      id: '',
      name: '',
      email: '',
      staffId: '',
      department: '',
      scope: '',
      isRoot: false,
      permissions: [],
    });

    watch(
      () => props.role,
      (newVal) => {
        if (newVal) {
          localAdmin.id = newVal.id;
          localAdmin.name = newVal.name;
          localAdmin.email = newVal.email;
          localAdmin.staffId = newVal.staffId;
          localAdmin.department = newVal.department;
          localAdmin.scope = newVal.scope;
          localAdmin.isRoot = newVal.isRoot;
          localAdmin.permissions = [...(newVal.permissions || [])];
        }
      },
      { immediate: true }
    );

    const handleUpdate = () => {
      try {
        authStore.updateAdminUser(localAdmin.id, {
          name: localAdmin.name,
          email: localAdmin.email,
          staffId: localAdmin.staffId,
          department: localAdmin.department,
          scope: localAdmin.scope,
          permissions: [...localAdmin.permissions],
        });
        toastStore.success(
          `Updated administrative scope and operational entitlements for ${localAdmin.name}.`,
          'Governance Updated'
        );
        emit('close');
      } catch (err) {
        toastStore.error(err.message, 'Update Failed');
      }
    };

    return {
      localAdmin,
      handleUpdate,
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
