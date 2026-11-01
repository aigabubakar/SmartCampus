<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="openAddSidebar" />
      <div class="mt-24">
         <ExamScheduleTable @openEditSidebar="openEditSidebar" />
      </div>
    </div>
    <Footer />
  </main>
  
  <AddExamScheduleSidebar :isOpen="isAddSidebarOpen" @close="closeAddSidebar" />
  <EditExamScheduleSidebar :isOpen="isEditSidebarOpen" :scheduleData="selectedSchedule" @close="closeEditSidebar" />
  
  <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" 
       :class="{ 'active': isAddSidebarOpen || isEditSidebarOpen }" @click="closeAllSidebars"></div>
       
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/examination/examSchedule/Breadcrumb.vue';
import ExamScheduleTable from '@/components/examination/examSchedule/ExamScheduleTable.vue';
import AddExamScheduleSidebar from '@/components/examination/examSchedule/AddExamScheduleSidebar.vue';
import EditExamScheduleSidebar from '@/components/examination/examSchedule/EditExamScheduleSidebar.vue';
import { ref } from 'vue';

export default {
  name: "ExamScheduleList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    ExamScheduleTable,
    AddExamScheduleSidebar,
    EditExamScheduleSidebar
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const isEditSidebarOpen = ref(false);
      const selectedSchedule = ref(null);

      const openAddSidebar = () => {
          isAddSidebarOpen.value = true;
      };

      const closeAddSidebar = () => {
          isAddSidebarOpen.value = false;
      };

      const openEditSidebar = (schedule) => {
          selectedSchedule.value = schedule;
          isEditSidebarOpen.value = true;
      };

      const closeEditSidebar = () => {
          isEditSidebarOpen.value = false;
          selectedSchedule.value = null;
      };
      
      const closeAllSidebars = () => {
          closeAddSidebar();
          closeEditSidebar();
      }

      return {
          isAddSidebarOpen,
          isEditSidebarOpen,
          selectedSchedule,
          openAddSidebar,
          closeAddSidebar,
          openEditSidebar,
          closeEditSidebar,
          closeAllSidebars
      };
  }
}
</script>
