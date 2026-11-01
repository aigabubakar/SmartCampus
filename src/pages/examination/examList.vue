<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="openAddSidebar" />
      <div class="mt-24">
         <ExamTable @openEditSidebar="openEditSidebar" />
      </div>
    </div>
    <Footer />
  </main>
  
  <AddExamSidebar :isOpen="isAddSidebarOpen" @close="closeAddSidebar" />
  <EditExamSidebar :isOpen="isEditSidebarOpen" :examData="selectedExam" @close="closeEditSidebar" />
  
  <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" 
       :class="{ 'active': isAddSidebarOpen || isEditSidebarOpen }" @click="closeAllSidebars"></div>
       
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/examination/exam/Breadcrumb.vue';
import ExamTable from '@/components/examination/exam/ExamTable.vue';
import AddExamSidebar from '@/components/examination/exam/AddExamSidebar.vue';
import EditExamSidebar from '@/components/examination/exam/EditExamSidebar.vue';
import { ref } from 'vue';

export default {
  name: "ExamList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    ExamTable,
    AddExamSidebar,
    EditExamSidebar
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const isEditSidebarOpen = ref(false);
      const selectedExam = ref(null);

      const openAddSidebar = () => {
          isAddSidebarOpen.value = true;
      };

      const closeAddSidebar = () => {
          isAddSidebarOpen.value = false;
      };

      const openEditSidebar = (exam) => {
          selectedExam.value = exam;
          isEditSidebarOpen.value = true;
      };

      const closeEditSidebar = () => {
          isEditSidebarOpen.value = false;
          selectedExam.value = null;
      };
      
      const closeAllSidebars = () => {
          closeAddSidebar();
          closeEditSidebar();
      }

      return {
          isAddSidebarOpen,
          isEditSidebarOpen,
          selectedExam,
          openAddSidebar,
          closeAddSidebar,
          openEditSidebar,
          closeEditSidebar,
          closeAllSidebars
      };
  }
}
</script>
