<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openSidebar="openSidebar" />
      <div class="mt-24">
         <StudentCategoryTable />
      </div>
    </div>
    <Footer />
  </main>
  <ThemeCustomizer />
  <AddCategorySidebar :isOpen="isSidebarOpen" @close="closeSidebar" />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/students/studentCategory/Breadcrumb.vue';
import StudentCategoryTable from '@/components/students/studentCategory/StudentCategoryTable.vue';
import AddCategorySidebar from '@/components/students/studentCategory/AddCategorySidebar.vue';
import { ref } from 'vue';

export default {
  name: "StudentCategory",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    StudentCategoryTable,
    AddCategorySidebar
  },
  setup() {
    const isSidebarOpen = ref(false);

    const openSidebar = () => {
        isSidebarOpen.value = true;
    };

    const closeSidebar = () => {
        isSidebarOpen.value = false;
    };

    return {
        isSidebarOpen,
        openSidebar,
        closeSidebar
    };
  }
}
</script>
