<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navabar />
    
    <div class="dashboard-main-body">
      <Breadcrumb />

      <form action="#" class="mt-24">
        <div class="row gy-3">
          
          <!-- Personal Info -->
          <div class="col-lg-12">
            <PersonalInfo />
          </div>

          <!-- Parent & Guardian Info -->
          <div class="col-lg-12">
            <ParentGuardianInfo />
          </div>

          <!-- Medical Details -->
          <div class="col-lg-12">
            <MedicalDetails />
          </div>

          <!-- Bank Details -->
          <div class="col-lg-12">
            <BankDetails />
          </div>

          <!-- Previous School Details -->
          <div class="col-xxl-6">
            <PreviousSchoolDetails />
          </div>

          <!-- Address -->
          <div class="col-xxl-6">
            <AddressDetails />
          </div>

          <!-- Hostel Details -->
          <div class="col-xxl-6">
            <HostelDetails />
          </div>

          <!-- Upload Documents -->
          <div class="col-xxl-6">
            <UploadDocuments />
          </div>

          <!-- Student Details -->
          <div class="col-xl-12">
            <StudentDetails />
          </div>

          <!-- Login Details -->
          <div class="col-xl-12">
            <LoginDetails />
          </div>

          <!-- Action Buttons -->
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
              <button type="reset"
                class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8">
                Cancel
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
import Navabar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

// Add New Student Components
import Breadcrumb from '@/components/students/addNewStudent/Breadcrumb.vue';
import PersonalInfo from '@/components/students/addNewStudent/PersonalInfo.vue';
import ParentGuardianInfo from '@/components/students/addNewStudent/ParentGuardianInfo.vue';
import MedicalDetails from '@/components/students/addNewStudent/MedicalDetails.vue';
import BankDetails from '@/components/students/addNewStudent/BankDetails.vue';
import PreviousSchoolDetails from '@/components/students/addNewStudent/PreviousSchoolDetails.vue';
import AddressDetails from '@/components/students/addNewStudent/AddressDetails.vue';
import HostelDetails from '@/components/students/addNewStudent/HostelDetails.vue';
import UploadDocuments from '@/components/students/addNewStudent/UploadDocuments.vue';
import StudentDetails from '@/components/students/addNewStudent/StudentDetails.vue';
import LoginDetails from '@/components/students/addNewStudent/LoginDetails.vue';

export default {
  name: "AddNewStudent",
  components: {
    Sidebar,
    Navabar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    PersonalInfo,
    ParentGuardianInfo,
    MedicalDetails,
    BankDetails,
    PreviousSchoolDetails,
    AddressDetails,
    HostelDetails,
    UploadDocuments,
    StudentDetails,
    LoginDetails
  }
}
</script>
