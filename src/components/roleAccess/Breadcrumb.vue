<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div>
      <h1 class="fw-bold mb-4 h5 text-primary-light">Administrator Governance & Delegation</h1>
      <div class="d-flex align-items-center gap-6 text-xs text-secondary-light">
        <router-link to="/dashboard" class="text-secondary-light hover-text-primary hover-underline">Dashboard</router-link>
        <span>/</span>
        <span class="text-secondary-light">Governance</span>
        <span>/</span>
        <span class="text-primary-600 fw-semibold">Admin Access Control</span>
      </div>
    </div>
    
    <div class="d-flex align-items-center gap-12 flex-wrap">
      <span class="badge bg-danger-50 text-danger-700 border border-danger-200 px-12 py-6 rounded-pill text-xs fw-semibold d-flex align-items-center gap-6">
        <i class="ri-shield-keyhole-line text-sm"></i>
        <span>Root Authority: Super Admin</span>
      </span>
      <router-link
        to="/general"
        class="btn btn-outline-neutral-300 text-neutral-700 btn-sm text-xs fw-semibold py-8 px-14 rounded-8 d-flex align-items-center gap-6 shadow-sm hover-bg-neutral-100"
      >
        <i class="ri-settings-5-line text-sm"></i>
        <span>Campus CMS & Config</span>
      </router-link>
      <button
        type="button"
        class="btn btn-primary-600 btn-sm text-xs fw-semibold py-8 px-16 rounded-8 d-flex align-items-center gap-6 shadow-sm"
        @click="$emit('open-add-sidebar')"
        :disabled="!authStore.canManageAdmins"
        :title="!authStore.canManageAdmins ? 'Only Super Admin can provision university administrators' : ''"
      >
        <i class="ri-user-add-line text-sm"></i>
        <span>Provision University Admin</span>
      </button>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth.js';

export default {
  name: "RoleAccessBreadcrumb",
  emits: ['open-add-sidebar'],
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  }
}
</script>
