<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navabar />

    <div class="dashboard-main-body">
      <Breadcrumb />
      <div class="mt-24">
        <StudentTable />
      </div>
    </div>

    <Footer />
  </main>
  
  <DeleteModal />
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navabar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

// Student List Components
import Breadcrumb from '@/components/students/studentList/Breadcrumb.vue';
import StudentTable from '@/components/students/studentList/StudentTable.vue';
import DeleteModal from '@/components/students/studentList/DeleteModal.vue';

export default {
  name: "StudentList",
  components: {
    Sidebar,
    Navabar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    StudentTable,
    DeleteModal
  }
}
</script>
