<template>
  <div v-if="isAuthorized">
    <!-- Overlay for sidebars -->
    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300"></div>

    <Sidebar />

    <main class="dashboard-main">
      <Navbar />

      <div class="dashboard-main-body">
        <Breadcrumb />
        <NotificationForm />
      </div>

      <Footer />
    </main>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';

// Page Components
import Breadcrumb from '@/components/settings/notification/Breadcrumb.vue';
import NotificationForm from '@/components/settings/notification/NotificationForm.vue';

export default {
  name: "NotificationSettings",
  components: {
    Sidebar,
    Navbar,
    Footer,
    Breadcrumb,
    NotificationForm
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isAuthorized = computed(() => authStore.isSuperAdmin);

    onMounted(() => {
      if (!isAuthorized.value) {
        toastStore.error(
          'Security Interception: Notification Channels Configuration is restricted to the Super Administrator.',
          '403 Forbidden'
        );
        router.replace('/403');
      }
    });

    return {
      isAuthorized
    };
  }
}
</script>
