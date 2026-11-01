<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />

      <div class="mt-24">
        <GuardianTable />
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
import Breadcrumb from '@/components/guardians/guardianList/Breadcrumb.vue';
import GuardianTable from '@/components/guardians/guardianList/GuardianTable.vue';

export default {
  name: "GuardianList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    GuardianTable
  }
}
</script>
