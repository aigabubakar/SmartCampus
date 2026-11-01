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
        <CurrenciesList @edit-currency="openEditSidebar" @delete-currency="openDeleteModal" />
      </div>

      <Footer />
    </main>

    <!-- Sidebars -->
    <AddCurrencySidebar :isActive="isSidebarOpen" @close="closeSidebars" @save="saveCurrency" />
    <EditCurrencySidebar :isActive="isEditSidebarOpen" :currencyData="selectedCurrency" @close="closeSidebars" @update="updateCurrency" />

    <!-- Modals -->
    <DeleteCurrencyModal @confirm-delete="deleteCurrency"/>

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
import Breadcrumb from '@/components/settings/currencies/Breadcrumb.vue';
import CurrenciesList from '@/components/settings/currencies/CurrenciesList.vue';
import AddCurrencySidebar from '@/components/settings/currencies/AddCurrencySidebar.vue';
import EditCurrencySidebar from '@/components/settings/currencies/EditCurrencySidebar.vue';
import DeleteCurrencyModal from '@/components/settings/currencies/DeleteCurrencyModal.vue';

export default {
  name: "CurrenciesSettings",
  components: {
    Sidebar,
    Navbar,
    Footer,
    Breadcrumb,
    CurrenciesList,
    AddCurrencySidebar,
    EditCurrencySidebar,
    DeleteCurrencyModal
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isAuthorized = computed(() => authStore.isSuperAdmin);

    onMounted(() => {
      if (!isAuthorized.value) {
        toastStore.error(
          'Security Interception: Currencies & FX Configuration is restricted to the Super Administrator.',
          '403 Forbidden'
        );
        router.replace('/403');
      }
    });

    const isSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);
    const selectedCurrency = ref(null);
    const currencyToDelete = ref(null);

    const openAddSidebar = () => {
      isSidebarOpen.value = true;
      isEditSidebarOpen.value = false;
    };

    const openEditSidebar = (currency) => {
      selectedCurrency.value = { ...currency }; // Clone data
      isEditSidebarOpen.value = true;
      isSidebarOpen.value = false;
    };

    const closeSidebars = () => {
      isSidebarOpen.value = false;
      isEditSidebarOpen.value = false;
    };

    const saveCurrency = (data) => {
      console.log('Save currency:', data);
      closeSidebars();
      // Add logic to save to API or store
    };

    const updateCurrency = (data) => {
      console.log('Update currency:', data);
      closeSidebars();
      // Add logic to update API or store
    };

    const openDeleteModal = (currency) => {
        currencyToDelete.value = currency;
        // Trigger bootstrap modal
        const modalEl = document.getElementById('exampleModalDelete');
        if (modalEl && window.bootstrap) {
            const modal = new window.bootstrap.Modal(modalEl);
            modal.show();
        }
    };

    const deleteCurrency = () => {
        console.log('Delete currency', currencyToDelete.value);
        // Add delete logic here
         // Close modal manually if needed
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
      selectedCurrency,
      openAddSidebar,
      openEditSidebar,
      closeSidebars,
      saveCurrency,
      updateCurrency,
      openDeleteModal,
      deleteCurrency
    };
  }
}
</script>
