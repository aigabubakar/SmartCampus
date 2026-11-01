<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />
      <div class="mt-24">
         <TeacherAttendanceTable />
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
import Breadcrumb from '@/components/attendance/teacherAttendance/Breadcrumb.vue';
import TeacherAttendanceTable from '@/components/attendance/teacherAttendance/TeacherAttendanceTable.vue';

export default {
  name: "TeacherAttendance",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    TeacherAttendanceTable
  }
}
</script>
