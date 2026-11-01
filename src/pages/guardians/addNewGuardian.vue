<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />

      <form action="#" class="mt-24">
        <div class="row gy-3">
            <div class="col-xl-12">
                <PersonalInfo />
            </div>
            <div class="col-xl-12">
                <LoginDetails />
            </div>
             <div class="col-12">
                <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
                    <button type="reset"
                        class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8">
                        Reset
                    </button>
                    <button type="submit"
                        class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8">
                        Save Changes
                    </button>
                </div>
            </div>
        </div>
      </form>
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
import Breadcrumb from '@/components/guardians/addNewGuardian/Breadcrumb.vue';
import PersonalInfo from '@/components/guardians/addNewGuardian/PersonalInfo.vue';
import LoginDetails from '@/components/guardians/addNewGuardian/LoginDetails.vue';


export default {
  name: "AddNewGuardian",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    PersonalInfo,
    LoginDetails
  }
}
</script>
