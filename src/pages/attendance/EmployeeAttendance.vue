<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />
      <div class="mt-24">
         <EmployeeAttendanceTable />
      </div>
    </div>
    <Footer />
  </main>
  
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/attendance/employeeAttendance/Breadcrumb.vue';
import EmployeeAttendanceTable from '@/components/attendance/employeeAttendance/EmployeeAttendanceTable.vue';

export default {
  name: "EmployeeAttendance",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    EmployeeAttendanceTable
  }
}
</script>
