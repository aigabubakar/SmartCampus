<template>
  <div id="app">
    <router-view />
    <ToastContainer />
    <SessionTimeoutModal />
    <ThemeCustomizer :isGlobal="true" />
  </div>
</template>

<script>
import { computed, onMounted, onUnmounted } from 'vue';
import { useRoute } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useInstitutionStore } from '@/stores/institution.js';
import { systemApi } from '@/services/api.js';
import ToastContainer from '@/components/common/ToastContainer.vue';
import SessionTimeoutModal from '@/components/common/SessionTimeoutModal.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

export default {
  name: 'App',
  components: {
    ToastContainer,
    SessionTimeoutModal,
    ThemeCustomizer
  },
  setup() {
    const route = useRoute();
    const authStore = useAuthStore();
    const institutionStore = useInstitutionStore();
    const showLayout = computed(() => route.meta.layout !== false);

    let heartbeatTimer = null;

    const handleUserInteraction = () => {
      authStore.recordUserActivity();
    };

    const handleVisibilityChange = () => {
      if (!document.hidden) {
        authStore.checkInactivity();
      }
    };

    onMounted(async () => {
      // 1. Hydrate institutional CMS from backend
      try {
        await institutionStore.loadConfig();
      } catch (e) {
        // Fall back to local defaults
      }

      // 2. Health check & Session Verification
      try {
        await systemApi.checkHealth();
        if (authStore.isAuthenticated) {
          await authStore.verifySession();
        }
      } catch (e) {
        // Handled gracefully
      }

      // Activity events to keep session alive when user is actively interacting
      const activityEvents = ['mousemove', 'mousedown', 'keydown', 'scroll', 'touchstart', 'click'];
      activityEvents.forEach((event) => {
        window.addEventListener(event, handleUserInteraction, { passive: true });
      });

      // Visibility change: check session when user returns to this tab
      document.addEventListener('visibilitychange', handleVisibilityChange);

      // Heartbeat timer: runs every second to check inactivity and decrement warning countdown
      heartbeatTimer = setInterval(() => {
        authStore.checkInactivity();
      }, 1000);
    });

    onUnmounted(() => {
      const activityEvents = ['mousemove', 'mousedown', 'keydown', 'scroll', 'touchstart', 'click'];
      activityEvents.forEach((event) => {
        window.removeEventListener(event, handleUserInteraction);
      });

      document.removeEventListener('visibilitychange', handleVisibilityChange);

      if (heartbeatTimer) {
        clearInterval(heartbeatTimer);
        heartbeatTimer = null;
      }
    });

    return { showLayout };
  }
};
</script>
