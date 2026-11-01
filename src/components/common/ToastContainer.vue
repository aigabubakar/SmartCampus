<template>
  <div class="toast-container-wrapper" aria-live="polite" aria-atomic="true">
    <transition-group name="toast-slide" tag="div" class="d-flex flex-column gap-12">
      <div
        v-for="toast in toasts"
        :key="toast.id"
        class="custom-toast-card p-14 rounded-12 shadow-lg bg-white border border-neutral-200 position-relative overflow-hidden"
        :class="`toast-${toast.type}`"
        role="alert"
        @mouseenter="pauseToast(toast)"
        @mouseleave="resumeToast(toast)"
      >
        <div class="d-flex align-items-start gap-12">
          <!-- Icon -->
          <div
            class="toast-icon-badge flex-shrink-0 rounded-circle d-flex align-items-center justify-content-center text-lg"
            :class="badgeClass(toast.type)"
          >
            <iconify-icon :icon="toast.icon"></iconify-icon>
          </div>

          <!-- Content -->
          <div class="flex-grow-1 pe-12">
            <h6 class="text-xs fw-bold mb-2 text-neutral-900 text-uppercase letter-spacing-05">
              {{ toast.title }}
            </h6>
            <p class="text-xs text-secondary-light mb-0 line-height-1-4">
              {{ toast.message }}
            </p>
          </div>

          <!-- Close Button -->
          <button
            type="button"
            class="btn-close-toast text-secondary-light hover-text-neutral-900 p-0 border-0 bg-transparent flex-shrink-0 cursor-pointer"
            aria-label="Close"
            @click="removeToast(toast.id)"
          >
            <i class="ri-close-line text-lg"></i>
          </button>
        </div>

        <!-- Linear Progress Bar -->
        <div
          v-if="toast.duration > 0"
          class="toast-progress-bar"
          :class="progressClass(toast.type)"
          :style="{ animationDuration: `${toast.duration}ms`, animationPlayState: toast.paused ? 'paused' : 'running' }"
        ></div>
      </div>
    </transition-group>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: 'ToastContainer',
  setup() {
    const toastStore = useToastStore();
    const toasts = computed(() => toastStore.toasts);

    const removeToast = (id) => {
      toastStore.remove(id);
    };

    const pauseToast = (toast) => {
      if (toast.timer) {
        clearTimeout(toast.timer);
        toast.paused = true;
        const elapsed = Date.now() - toast.startTime;
        toast.remainingTime = Math.max(0, toast.duration - elapsed);
      }
    };

    const resumeToast = (toast) => {
      if (toast.paused && toast.remainingTime > 0) {
        toast.paused = false;
        toast.startTime = Date.now();
        toast.timer = setTimeout(() => {
          toastStore.remove(toast.id);
        }, toast.remainingTime);
      }
    };

    const badgeClass = (type) => {
      switch (type) {
        case 'success':
          return 'bg-success-50 text-success-600 border border-success-200';
        case 'error':
          return 'bg-danger-50 text-danger-600 border border-danger-200';
        case 'warning':
          return 'bg-warning-50 text-warning-700 border border-warning-200';
        case 'info':
        default:
          return 'bg-primary-50 text-primary-600 border border-primary-200';
      }
    };

    const progressClass = (type) => {
      switch (type) {
        case 'success':
          return 'bg-success-600';
        case 'error':
          return 'bg-danger-600';
        case 'warning':
          return 'bg-warning-500';
        case 'info':
        default:
          return 'bg-primary-600';
      }
    };

    return {
      toasts,
      removeToast,
      pauseToast,
      resumeToast,
      badgeClass,
      progressClass
    };
  }
};
</script>

<style scoped>
.toast-container-wrapper {
  position: fixed;
  top: 24px;
  right: 24px;
  z-index: 999999;
  max-width: 380px;
  width: calc(100% - 48px);
  pointer-events: none;
}

.custom-toast-card {
  pointer-events: auto;
  border-left: 4px solid transparent !important;
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.98) !important;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.custom-toast-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.12) !important;
}

.toast-success {
  border-left-color: #10b981 !important;
}

.toast-error {
  border-left-color: #ef4444 !important;
}

.toast-warning {
  border-left-color: #f59e0b !important;
}

.toast-info {
  border-left-color: #25A194 !important;
}

.toast-icon-badge {
  width: 36px;
  height: 36px;
}

.btn-close-toast {
  transition: color 0.15s ease;
  line-height: 1;
}

.toast-progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 3px;
  width: 100%;
  animation-name: toastProgress;
  animation-timing-function: linear;
  animation-fill-mode: forwards;
}

@keyframes toastProgress {
  from {
    width: 100%;
  }
  to {
    width: 0%;
  }
}

/* Animations */
.toast-slide-enter-active,
.toast-slide-leave-active {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.toast-slide-enter-from {
  opacity: 0;
  transform: translateX(60px) scale(0.95);
}

.toast-slide-leave-to {
  opacity: 0;
  transform: translateX(40px) scale(0.9);
}
</style>
