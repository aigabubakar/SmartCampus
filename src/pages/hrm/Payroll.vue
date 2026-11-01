<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-payment-sidebar="openPaymentSidebar" />

        <div class="mt-24">
          <PayrollTable @view-payslip="viewPayslip" />
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- Payment Sidebar -->
    <PaymentSidebar 
      :isOpen="isPaymentSidebarOpen" 
      @close="closePaymentSidebar"
      @submit="handlePaymentSubmit"
    />

    <!-- Overlay -->
    <div 
      class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 duration-300"
      :class="{ 'visibility-hidden opacity-0': !isPaymentSidebarOpen, 'active': isPaymentSidebarOpen }"
      @click="closePaymentSidebar"
    ></div>

    <!-- Payslip Modal -->
    <PayslipModal :employee="selectedEmployee" />
  </div>
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/hrm/payroll/Breadcrumb.vue';
import PayrollTable from '@/components/hrm/payroll/PayrollTable.vue';
import PaymentSidebar from '@/components/hrm/payroll/PaymentSidebar.vue';
import PayslipModal from '@/components/hrm/payroll/PayslipModal.vue';

export default {
  name: "Payroll",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    PayrollTable,
    PaymentSidebar,
    PayslipModal
  },
  setup() {
    const isPaymentSidebarOpen = ref(false);
    const selectedEmployee = ref({});

    const openPaymentSidebar = () => {
      isPaymentSidebarOpen.value = true;
    };

    const closePaymentSidebar = () => {
      isPaymentSidebarOpen.value = false;
    };

    const handlePaymentSubmit = (paymentData) => {
      console.log('Payment data received:', paymentData);
      // Add your payment submission logic here
      alert('Payment processed successfully!');
    };

    const viewPayslip = (employee) => {
      selectedEmployee.value = employee;
      // Trigger Bootstrap modal
      const modalElement = document.getElementById('payslipModal');
      if (modalElement) {
        if (window.bootstrap) {
          const modal = new window.bootstrap.Modal(modalElement);
          modal.show();
        } else {
          console.error('Bootstrap is not available');
        }
      }
    };

    return {
      isPaymentSidebarOpen,
      selectedEmployee,
      openPaymentSidebar,
      closePaymentSidebar,
      handlePaymentSubmit,
      viewPayslip
    };
  }
}
</script>

<style scoped>
.overlay.active {
  visibility: visible !important;
  opacity: 1 !important;
}

.my-sidebar.active-translate-0 {
  transform: translateX(0) !important;
}
</style>
