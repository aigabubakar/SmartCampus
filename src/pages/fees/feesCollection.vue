<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="isAddSidebarOpen = true" />
      <div class="mt-24">
         <FeesCollectionTable @viewDetails="openPayslipModal" />
      </div>
    </div>
    <Footer />
  </main>
  
  <CollectFeesSidebar :isOpen="isAddSidebarOpen" @close="isAddSidebarOpen = false" />
  <PayslipModal :details="selectedPayslip" /> 
  <ThemeCustomizer />
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/fees/feesCollection/Breadcrumb.vue';
import FeesCollectionTable from '@/components/fees/feesCollection/FeesCollectionTable.vue';
import CollectFeesSidebar from '@/components/fees/feesCollection/CollectFeesSidebar.vue';
import PayslipModal from '@/components/fees/feesCollection/PayslipModal.vue';

export default {
  name: "FeesCollectionList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    FeesCollectionTable,
    CollectFeesSidebar,
    PayslipModal
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const selectedPayslip = ref(null);

      const openPayslipModal = (student) => {
          selectedPayslip.value = student;
          // Trigger Bootstrap modal manually if needed, or rely on data-bs attributes if mixed
          // Since the user's template used data-bs-toggle="modal", we need to make sure the modal ID matches
          // In FeedCollectionTable.vue, I used data-bs-target="#payslipModal", and in PayslipModal.vue id="payslipModal".
          // However, to make it dynamic with Vue, we usually want to set the data BEFORE the modal opens.
          // By the time the click event propagates to Bootstrap's handler, this function runs.
          // Ideally we might need to wait for next tick or just rely on reactivity updates being fast enough.
      };

      return {
          isAddSidebarOpen,
          selectedPayslip,
          openPayslipModal
      };
  }
}
</script>
