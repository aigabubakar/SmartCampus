<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="openAddSidebar" />
      <div class="mt-24">
         <SectionTable @openEditSidebar="openEditSidebar" />
      </div>
    </div>
    <Footer />
  </main>
  
  <AddSectionSidebar :isOpen="isAddSidebarOpen" @close="closeAddSidebar" />
  <EditSectionSidebar :isOpen="isEditSidebarOpen" :sectionData="selectedSection" @close="closeEditSidebar" />
  
  <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" 
       :class="{ 'active': isAddSidebarOpen || isEditSidebarOpen }" @click="closeAllSidebars"></div>
       
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/class/sectionList/Breadcrumb.vue';
import SectionTable from '@/components/class/sectionList/SectionTable.vue';
import AddSectionSidebar from '@/components/class/sectionList/AddSectionSidebar.vue';
import EditSectionSidebar from '@/components/class/sectionList/EditSectionSidebar.vue';
import { ref } from 'vue';

export default {
  name: "SectionList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    SectionTable,
    AddSectionSidebar,
    EditSectionSidebar
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const isEditSidebarOpen = ref(false);
      const selectedSection = ref(null);

      const openAddSidebar = () => {
          isAddSidebarOpen.value = true;
      };

      const closeAddSidebar = () => {
          isAddSidebarOpen.value = false;
      };

      const openEditSidebar = (section) => {
          selectedSection.value = section;
          isEditSidebarOpen.value = true;
      };

      const closeEditSidebar = () => {
          isEditSidebarOpen.value = false;
          selectedSection.value = null;
      };
      
      const closeAllSidebars = () => {
          closeAddSidebar();
          closeEditSidebar();
      }

      return {
          isAddSidebarOpen,
          isEditSidebarOpen,
          selectedSection,
          openAddSidebar,
          closeAddSidebar,
          openEditSidebar,
          closeEditSidebar,
          closeAllSidebars
      };
  }
}
</script>
