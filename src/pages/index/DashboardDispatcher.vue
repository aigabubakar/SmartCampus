<template>
  <component :is="resolvedDashboard" />
</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth.js';

import Index1 from '@/pages/index/index1.vue';
import Index2 from '@/pages/index/index2.vue';
import Index3 from '@/pages/index/index3.vue';
import Index4 from '@/pages/index/index4.vue';

export default {
  name: 'DashboardDispatcher',
  components: {
    Index1,
    Index2,
    Index3,
    Index4
  },
  setup() {
    const authStore = useAuthStore();

    const resolvedDashboard = computed(() => {
      const role = authStore.currentRole || authStore.user?.role;

      switch (role) {
        case 'student':
          return Index2; // Student Academic Portal
        case 'lecturer':
        case 'teacher':
          return Index3; // Lecturer Teaching Console
        case 'guardian':
          return Index4; // Parent / Guardian Portal
        case 'admin':
        case 'super-admin':
        default:
          return Index1; // Executive Campus Intelligence Dashboard
      }
    });

    return {
      resolvedDashboard
    };
  }
};
</script>
