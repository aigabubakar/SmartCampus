<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />
      <TeacherTable />
    </div>
    <Footer />
  </main>
  <ThemeCustomizer />
  <DeleteModal />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/teachers/teacherList/Breadcrumb.vue';
import TeacherTable from '@/components/teachers/teacherList/TeacherTable.vue';
import DeleteModal from '@/components/teachers/teacherList/DeleteModal.vue';

export default {
  name: "TeacherList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    TeacherTable,
    DeleteModal
  }
}
</script>
