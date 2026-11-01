<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div>
      <h4 class="fw-bold mb-2 text-primary-light">Official Notice Board & Circulars</h4>
      <p class="text-secondary-light text-xs mb-0">
        {{ institution.name }} • Centralized Senate, Registry, Academic Planning & Faculty Dispatches
      </p>
    </div>
    <div class="d-flex align-items-center gap-12">
      <button 
        v-if="canManageNotices"
        type="button" 
        class="my-sidebar-btn btn btn-primary-600 btn-sm radius-8 px-16 py-8 d-flex align-items-center gap-6 text-xs fw-semibold text-white shadow-sm" 
        @click="$emit('open-add-sidebar')"
      >
        <iconify-icon icon="solar:pen-new-square-bold" class="text-base"></iconify-icon>
        Publish New Circular
      </button>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useInstitutionStore } from '@/stores/institution.js';

export default {
  name: "Breadcrumb",
  emits: ['open-add-sidebar'],
  setup() {
    const authStore = useAuthStore();
    const institution = useInstitutionStore();

    const canManageNotices = computed(() => authStore.isAdmin || authStore.isSuperAdmin);

    return {
      institution,
      canManageNotices
    };
  }
}
</script>
