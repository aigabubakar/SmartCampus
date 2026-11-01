<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navabar />

    <div class="dashboard-main-body">
      <Breadcrumb />
      <div class="mt-24">
        <SuspendedStudentTable />
      </div>
    </div>

    <Footer />
  </main>
  
  <SuspendModal />
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navabar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

// Suspended Student Components
import Breadcrumb from '@/components/students/suspendedStudent/Breadcrumb.vue';
import SuspendedStudentTable from '@/components/students/suspendedStudent/SuspendedStudentTable.vue';
import SuspendModal from '@/components/students/suspendedStudent/SuspendModal.vue';

export default {
  name: "SuspendedStudent",
  components: {
    Sidebar,
    Navabar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    SuspendedStudentTable,
    SuspendModal
  }
}
</script>
