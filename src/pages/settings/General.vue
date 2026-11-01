<template>
  <div v-if="isAuthorized">
    <!-- Overlay for sidebars -->
    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300"></div>

    <Sidebar />

    <main class="dashboard-main">
      <Navbar />

      <div class="dashboard-main-body">
        <Breadcrumb />
        <GeneralForm />
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
import Breadcrumb from '@/components/settings/general/Breadcrumb.vue';
import GeneralForm from '@/components/settings/general/GeneralForm.vue';

export default {
  name: "GeneralSettings",
  components: {
    Sidebar,
    Navbar,
    Footer,
    Breadcrumb,
    GeneralForm
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isAuthorized = computed(() => authStore.isSuperAdmin);

    onMounted(() => {
      if (!isAuthorized.value) {
        toastStore.error(
          'Security Interception: Campus CMS and University System Configuration are strictly restricted to the Super Administrator.',
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
