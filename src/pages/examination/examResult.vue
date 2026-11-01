<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />
      <div class="mt-24">
         <ExamResultTable @viewResult="viewResult" />
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
import Breadcrumb from '@/components/examination/examResult/Breadcrumb.vue';
import ExamResultTable from '@/components/examination/examResult/ExamResultTable.vue';

export default {
  name: "ExamResultList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    ExamResultTable
  },
  setup() {
      const viewResult = (result) => {
          // Placeholder for view functionality, could open a modal or navigate to detail page
          console.log('View result:', result);
          alert(`Viewing result for ${result.name}`);
      };

      return {
          viewResult
      };
  }
}
</script>
