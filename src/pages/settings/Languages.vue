<template>
  <div v-if="isAuthorized">
    <!-- Overlay -->
    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" 
         :class="{ 'active': isSidebarOpen || isEditSidebarOpen }"
         @click="closeSidebars">
    </div>

    <Sidebar />

    <main class="dashboard-main">
      <Navbar />

      <div class="dashboard-main-body">
        <Breadcrumb @open-add-sidebar="openAddSidebar" />
        <LanguagesList @edit-language="openEditSidebar" @delete-language="openDeleteModal" />
      </div>

      <Footer />
    </main>

    <!-- Sidebars -->
    <AddLanguageSidebar :isActive="isSidebarOpen" @close="closeSidebars" @save="saveLanguage" />
    <EditLanguageSidebar :isActive="isEditSidebarOpen" :languageData="selectedLanguage" @close="closeSidebars" @update="updateLanguage" />

    <!-- Modals -->
    <DeleteLanguageModal @confirm-delete="deleteLanguage"/>

  </div>
</template>

<script>
import { onMounted, ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';

// Page Components
import Breadcrumb from '@/components/settings/languages/Breadcrumb.vue';
import LanguagesList from '@/components/settings/languages/LanguagesList.vue';
import AddLanguageSidebar from '@/components/settings/languages/AddLanguageSidebar.vue';
import EditLanguageSidebar from '@/components/settings/languages/EditLanguageSidebar.vue';
import DeleteLanguageModal from '@/components/settings/languages/DeleteLanguageModal.vue';

export default {
  name: "LanguagesSettings",
  components: {
    Sidebar,
    Navbar,
    Footer,
    Breadcrumb,
    LanguagesList,
    AddLanguageSidebar,
    EditLanguageSidebar,
    DeleteLanguageModal
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isAuthorized = computed(() => authStore.isSuperAdmin);

    onMounted(() => {
      if (!isAuthorized.value) {
        toastStore.error(
          'Security Interception: Localization & Languages Configuration is restricted to the Super Administrator.',
          '403 Forbidden'
        );
        router.replace('/403');
      }
    });

    const isSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);
    const selectedLanguage = ref(null);
    const languageToDelete = ref(null);

    const openAddSidebar = () => {
      isSidebarOpen.value = true;
      isEditSidebarOpen.value = false;
    };

    const openEditSidebar = (language) => {
      selectedLanguage.value = { ...language }; // Clone data
      isEditSidebarOpen.value = true;
      isSidebarOpen.value = false;
    };

    const closeSidebars = () => {
      isSidebarOpen.value = false;
      isEditSidebarOpen.value = false;
    };

    const saveLanguage = (data) => {
      console.log('Save language:', data);
      closeSidebars();
    };

    const updateLanguage = (data) => {
      console.log('Update language:', data);
      closeSidebars();
    };

    const openDeleteModal = (language) => {
        languageToDelete.value = language;
        // Trigger bootstrap modal
        const modalEl = document.getElementById('exampleModalDelete');
        if (modalEl && window.bootstrap) {
            const modal = new window.bootstrap.Modal(modalEl);
            modal.show();
        }
    };

    const deleteLanguage = () => {
        console.log('Delete language', languageToDelete.value);
        // Add delete logic here
         // Close modal manually
         const modalEl = document.getElementById('exampleModalDelete');
        if (modalEl && window.bootstrap) {
            const modal = window.bootstrap.Modal.getInstance(modalEl);
            if(modal) modal.hide();
        }
    }

    return {
      isAuthorized,
      isSidebarOpen,
      isEditSidebarOpen,
      selectedLanguage,
      openAddSidebar,
      openEditSidebar,
      closeSidebars,
      saveLanguage,
      updateLanguage,
      openDeleteModal,
      deleteLanguage
    };
  }
}
</script>
