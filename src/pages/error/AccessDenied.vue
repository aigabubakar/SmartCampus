<template>
  <div class="access-denied-wrapper min-vh-100 d-flex align-items-center justify-content-center p-24 bg-neutral-100">
    <div class="card border-0 shadow-lg radius-20 max-w-560-px w-100 overflow-hidden text-center p-32 p-sm-48 bg-white">
      
      <!-- Shield / Security Icon -->
      <div class="mx-auto mb-24 w-88-px h-88-px rounded-circle bg-danger-50 border border-danger-200 d-flex align-items-center justify-content-center text-danger-600">
        <iconify-icon icon="solar:shield-cross-bold" class="text-5xl"></iconify-icon>
      </div>

      <!-- Institutional Heading -->
      <span class="badge bg-danger-100 text-danger-800 text-xs px-12 py-6 radius-8 fw-bold text-uppercase letter-spacing-1 mb-12 d-inline-block">
        Security Clearance Violation (HTTP 403)
      </span>
      <h3 class="fw-bold text-neutral-900 mb-8">Restricted Institutional Access</h3>
      <p class="text-secondary-light text-sm mb-24 line-height-1-6">
        The sector you attempted to reach is protected by university Role-Based Access Control (RBAC). Your active credentials do not have administrative clearance to view or alter this sector.
      </p>

      <!-- Active User Context Card -->
      <div class="p-16 radius-12 bg-neutral-50 border border-neutral-200 text-start mb-28">
        <div class="d-flex align-items-center justify-content-between mb-8">
          <span class="text-xxs text-secondary-light fw-bold text-uppercase">Current Session</span>
          <span class="badge radius-6 text-xxs px-8 py-2 text-capitalize fw-bold" :class="roleBadgeClass">
            {{ userRole }}
          </span>
        </div>
        <div class="d-flex align-items-center gap-12">
          <img 
            :src="userAvatar" 
            alt="User" 
            class="w-40-px h-40-px rounded-circle object-fit-cover border border-neutral-300"
          >
          <div>
            <h6 class="text-sm fw-bold text-neutral-900 mb-0">{{ userName }}</h6>
            <span class="text-xs text-secondary-light">{{ userIdentifier }}</span>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="d-flex flex-column flex-sm-row align-items-center justify-content-center gap-12">
        <button 
          type="button" 
          class="btn btn-outline-neutral-300 btn-sm radius-10 px-20 py-10 text-xs fw-semibold text-neutral-700 w-100 w-sm-auto"
          @click="goBack"
        >
          <iconify-icon icon="solar:arrow-left-linear" class="text-sm me-4"></iconify-icon>
          Previous Page
        </button>
        <button 
          type="button" 
          class="btn btn-primary-600 btn-sm radius-10 px-24 py-10 text-xs fw-bold text-white shadow-sm w-100 w-sm-auto"
          @click="goToAuthorizedDashboard"
        >
          <iconify-icon icon="solar:home-smile-bold" class="text-sm me-4"></iconify-icon>
          Return to My Portal
        </button>
      </div>

    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';

export default {
  name: 'AccessDenied',
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();

    const currentUser = computed(() => authStore.currentUser);
    const userRole = computed(() => authStore.currentRole || 'Guest');
    const userName = computed(() => currentUser.value?.name || 'Authenticated User');
    const userIdentifier = computed(() => currentUser.value?.matricNumber || currentUser.value?.staffId || currentUser.value?.email || 'N/A');
    const userAvatar = computed(() => currentUser.value?.avatar || '/assets/images/users/user1.png');

    const roleBadgeClass = computed(() => {
      switch (userRole.value) {
        case 'student':
          return 'bg-blue-50 text-blue-700 border border-blue-200';
        case 'teacher':
          return 'bg-purple-50 text-purple-700 border border-purple-200';
        case 'guardian':
          return 'bg-warning-50 text-warning-800 border border-warning-200';
        case 'admin':
        case 'super-admin':
          return 'bg-danger-50 text-danger-700 border border-danger-200';
        default:
          return 'bg-neutral-200 text-neutral-700';
      }
    });

    const goBack = () => {
      if (window.history.length > 1) {
        router.back();
      } else {
        router.push('/dashboard');
      }
    };

    const goToAuthorizedDashboard = () => {
      router.push('/dashboard');
    };

    return {
      userRole,
      userName,
      userIdentifier,
      userAvatar,
      roleBadgeClass,
      goBack,
      goToAuthorizedDashboard
    };
  }
};
</script>

<style scoped>
.max-w-560-px {
  max-width: 560px;
}
.w-88-px {
  width: 88px;
}
.h-88-px {
  height: 88px;
}
.radius-20 {
  border-radius: 20px;
}
.text-xxs {
  font-size: 0.6875rem;
}
</style>
