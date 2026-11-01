<template>
  <Transition name="fade">
    <div
      v-if="authStore.isWarningModalOpen && authStore.isAuthenticated"
      class="session-timeout-overlay position-fixed top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center"
      style="z-index: 999999; background: rgba(15, 23, 42, 0.7); backdrop-filter: blur(4px);"
    >
      <div class="card border-0 shadow-lg radius-16 overflow-hidden max-w-440-px w-100 mx-16 animate-scale-in">
        <!-- Top Status Bar -->
        <div class="bg-warning-50 border-bottom border-warning-200 py-16 px-24 d-flex align-items-center gap-12">
          <div class="w-40-px h-40-px rounded-circle bg-warning-100 text-warning-main d-flex align-items-center justify-content-center flex-shrink-0">
            <i class="ri-timer-line text-xl"></i>
          </div>
          <div>
            <h6 class="text-sm fw-bold text-neutral-900 mb-0">Inactivity Security Warning</h6>
            <span class="text-xxs text-warning-700 fw-semibold">Institutional Session Protection</span>
          </div>
        </div>

        <!-- Body Content -->
        <div class="card-body p-24 text-center">
          <div class="my-16">
            <div class="countdown-badge mx-auto d-inline-flex align-items-center justify-content-center bg-warning-100 text-warning-800 rounded-circle fw-bold text-xxl mb-12" style="width: 72px; height: 72px;">
              {{ authStore.secondsRemaining }}s
            </div>
            <h5 class="fw-bold text-neutral-900 mb-8 h6">Are you still working?</h5>
            <p class="text-xs text-secondary-light mb-0 line-height-1-5">
              Your session has been inactive for almost 15 minutes. To safeguard student records and university data, you will be logged out in 
              <span class="fw-bold text-warning-700">{{ authStore.secondsRemaining }} seconds</span>.
            </p>
          </div>

          <div class="d-flex align-items-center gap-12 mt-24">
            <button
              type="button"
              class="btn btn-outline-neutral-300 text-neutral-700 text-xs fw-semibold py-10 px-16 rounded-8 flex-grow-1 hover-bg-neutral-100"
              @click="handleManualLogout"
            >
              <i class="ri-logout-box-r-line me-1"></i> Log Out Now
            </button>
            <button
              type="button"
              class="btn btn-primary-600 text-xs fw-semibold py-10 px-20 rounded-8 flex-grow-1 shadow-sm d-flex align-items-center justify-content-center gap-6"
              @click="handleStaySignedIn"
            >
              <i class="ri-shield-check-line"></i> Stay Signed In
            </button>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script>
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';

export default {
  name: 'SessionTimeoutModal',
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();

    const handleStaySignedIn = () => {
      authStore.extendSession();
    };

    const handleManualLogout = () => {
      authStore.logout();
      router.push('/login');
    };

    return {
      authStore,
      handleStaySignedIn,
      handleManualLogout
    };
  }
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.animate-scale-in {
  animation: modalScaleIn 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes modalScaleIn {
  from {
    transform: scale(0.95);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}
</style>
