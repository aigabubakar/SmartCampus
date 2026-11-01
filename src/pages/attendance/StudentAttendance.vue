<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />
      <div class="mt-24">
         <StudentAttendanceTable />
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
import Breadcrumb from '@/components/attendance/studentAttendance/Breadcrumb.vue';
import StudentAttendanceTable from '@/components/attendance/studentAttendance/StudentAttendanceTable.vue';

export default {
  name: "StudentAttendance",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    StudentAttendanceTable
  }
}
</script>
