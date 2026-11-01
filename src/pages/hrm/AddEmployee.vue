<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb />
        <AddEmpForm />
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />
  </div>
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/hrm/addEmployee/Breadcrumb.vue';
import AddEmpForm from '@/components/hrm/addEmployee/AddEmpForm.vue';

export default {
  name: "AddEmployee",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    AddEmpForm
  },

}
</script>
