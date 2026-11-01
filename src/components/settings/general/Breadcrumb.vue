<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div>
      <h1 class="fw-bold mb-4 h5 text-primary-light">Campus CMS & System Configuration</h1>
      <div class="d-flex align-items-center gap-6 text-xs text-secondary-light">
        <router-link to="/dashboard" class="text-secondary-light hover-text-primary hover-underline">Dashboard</router-link>
        <span>/</span>
        <span class="text-secondary-light">Super Admin</span>
        <span>/</span>
        <span class="text-primary-600 fw-semibold">Campus CMS & System Configuration</span>
      </div>
    </div>
    
    <div class="d-flex align-items-center gap-10 flex-wrap">
      <span class="badge bg-purple-50 text-purple-700 border border-purple-200 px-12 py-6 rounded-pill text-xs fw-semibold d-flex align-items-center gap-6">
        <i class="ri-shield-keyhole-line text-sm"></i>
        <span>Super Admin Console</span>
      </span>
      <span class="badge bg-primary-50 text-primary-600 border border-primary-200 px-12 py-6 rounded-pill text-xs fw-medium d-flex align-items-center gap-6">
        <span class="w-8-px h-8-px rounded-circle bg-success-main"></span>
        {{ institution.institutionName }} ({{ institution.shortCode }})
      </span>
      <router-link 
        to="/role-access" 
        class="btn btn-outline-primary-600 btn-sm text-xs fw-semibold py-8 px-14 rounded-8 d-flex align-items-center gap-6 shadow-sm"
      >
        <i class="ri-shield-user-line text-sm"></i>
        <span>Admin Governance</span>
      </router-link>
    </div>
  </div>
</template>

<script>
import { useInstitutionStore } from '@/stores/institution.js';

export default {
  name: "GeneralBreadcrumb",
  setup() {
    const institution = useInstitutionStore();
    return { institution };
  }
}
</script>
