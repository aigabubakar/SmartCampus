<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="openAddSidebar" />
      <div class="mt-24">
         <ClassTable @openEditSidebar="openEditSidebar" />
      </div>
    </div>
    <Footer />
  </main>
  
  <AddClassSidebar :isOpen="isAddSidebarOpen" @close="closeAddSidebar" />
  <EditClassSidebar :isOpen="isEditSidebarOpen" :classData="selectedClass" @close="closeEditSidebar" />
  
  <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" 
       :class="{ 'active': isAddSidebarOpen || isEditSidebarOpen }" @click="closeAllSidebars"></div>
       
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/class/classList/Breadcrumb.vue';
import ClassTable from '@/components/class/classList/ClassTable.vue';
import AddClassSidebar from '@/components/class/classList/AddClassSidebar.vue';
import EditClassSidebar from '@/components/class/classList/EditClassSidebar.vue';
import { ref } from 'vue';

export default {
  name: "ClassList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    ClassTable,
    AddClassSidebar,
    EditClassSidebar
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const isEditSidebarOpen = ref(false);
      const selectedClass = ref(null);

      const openAddSidebar = () => {
          isAddSidebarOpen.value = true;
      };

      const closeAddSidebar = () => {
          isAddSidebarOpen.value = false;
      };

      const openEditSidebar = (cls) => {
          selectedClass.value = cls;
          isEditSidebarOpen.value = true;
      };

      const closeEditSidebar = () => {
          isEditSidebarOpen.value = false;
          selectedClass.value = null;
      };
      
      const closeAllSidebars = () => {
          closeAddSidebar();
          closeEditSidebar();
      }

      return {
          isAddSidebarOpen,
          isEditSidebarOpen,
          selectedClass,
          openAddSidebar,
          closeAddSidebar,
          openEditSidebar,
          closeEditSidebar,
          closeAllSidebars
      };
  }
}
</script>
