<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="openAddSidebar" />
      <div class="mt-24">
         <SubjectTable @openEditSidebar="openEditSidebar" />
      </div>
    </div>
    <Footer />
  </main>
  
  <AddSubjectSidebar :isOpen="isAddSidebarOpen" @close="closeAddSidebar" />
  <EditSubjectSidebar :isOpen="isEditSidebarOpen" :subjectData="selectedSubject" @close="closeEditSidebar" />
  
  <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" 
       :class="{ 'active': isAddSidebarOpen || isEditSidebarOpen }" @click="closeAllSidebars"></div>
       
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/class/subjectList/Breadcrumb.vue';
import SubjectTable from '@/components/class/subjectList/SubjectTable.vue';
import AddSubjectSidebar from '@/components/class/subjectList/AddSubjectSidebar.vue';
import EditSubjectSidebar from '@/components/class/subjectList/EditSubjectSidebar.vue';
import { ref } from 'vue';

export default {
  name: "SubjectList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    SubjectTable,
    AddSubjectSidebar,
    EditSubjectSidebar
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const isEditSidebarOpen = ref(false);
      const selectedSubject = ref(null);

      const openAddSidebar = () => {
          isAddSidebarOpen.value = true;
      };

      const closeAddSidebar = () => {
          isAddSidebarOpen.value = false;
      };

      const openEditSidebar = (subject) => {
          selectedSubject.value = subject;
          isEditSidebarOpen.value = true;
      };

      const closeEditSidebar = () => {
          isEditSidebarOpen.value = false;
          selectedSubject.value = null;
      };
      
      const closeAllSidebars = () => {
          closeAddSidebar();
          closeEditSidebar();
      }

      return {
          isAddSidebarOpen,
          isEditSidebarOpen,
          selectedSubject,
          openAddSidebar,
          closeAddSidebar,
          openEditSidebar,
          closeEditSidebar,
          closeAllSidebars
      };
  }
}
</script>
