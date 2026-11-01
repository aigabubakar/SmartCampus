<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />

      <div class="mt-24">
        <div class="card h-100">
          <TimetableControls />
          <TimetableGrid />
        </div>
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
import Breadcrumb from '@/components/teachers/teacherTimetable/Breadcrumb.vue';
import TimetableControls from '@/components/teachers/teacherTimetable/TimetableControls.vue';
import TimetableGrid from '@/components/teachers/teacherTimetable/TimetableGrid.vue';

export default {
    name: "TeacherTimetable",
    components: {
        Sidebar,
        Navbar,
        Footer,
        ThemeCustomizer,
        Breadcrumb,
        TimetableControls,
        TimetableGrid
    }
}
</script>
