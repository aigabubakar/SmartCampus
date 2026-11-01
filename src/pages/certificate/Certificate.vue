<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-add-sidebar="openAddSidebar" />

        <div class="mt-24">
          <CertificateTable @view-certificate="openViewModal" @edit-certificate="openEditSidebar" />
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- Add Sidebar -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isAddSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add New Certificate</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleAddSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-6">
            <div class="">
              <label for="certificateName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Certificate Name</label>
              <input type="text" class="form-control" id="certificateName" placeholder="Enter certificate name" v-model="addForm.certificateName">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectClass" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
              <select id="selectClass" class="form-control form-select" v-model="addForm.class">
                <option value="" selected disabled>Select Class</option>
                <option value="One">One</option>
                <option value="Two">Two</option>
                <option value="Three">Three</option>
                <option value="Four">Four</option>
                <option value="Five">Five</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectSection" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section</label>
              <select id="selectSection" class="form-control form-select" v-model="addForm.section">
                <option value="" selected disabled>Select Section</option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="C">C</option>
                <option value="D">D</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectStudent" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Student</label>
              <select id="selectStudent" class="form-control form-select" v-model="addForm.student">
                <option value="" selected disabled>Select Student</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Date</label>
              <input type="date" class="form-control" id="selectDate" v-model="addForm.date">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="footerLeftText" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Footer Left Text</label>
              <input type="text" class="form-control" id="footerLeftText" placeholder="Enter Footer Left Text" v-model="addForm.footerLeftText">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="footerRightText" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Footer Right Text</label>
              <input type="text" class="form-control" id="footerRightText" placeholder="Enter Footer Right Text" v-model="addForm.footerRightText">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Student Photo <span class="text-danger-600">*</span></label>
              <input type="file" class="form-control" @change="handleFileUpload">
            </div>
          </div>
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
              <button type="reset" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="closeSidebar">
                Cancel
              </button>
              <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
                Save
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>

    <!-- Edit Sidebar -->
    <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isEditSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Certificate</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleEditSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-6">
            <div class="">
              <label for="certificateNameEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Certificate Name</label>
              <input type="text" class="form-control" id="certificateNameEdit" placeholder="Enter certificate name" v-model="editForm.certificateName">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectClassEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
              <select id="selectClassEdit" class="form-control form-select" v-model="editForm.class">
                <option value="" selected disabled>Select Class</option>
                <option value="One">One</option>
                <option value="Two">Two</option>
                <option value="Three">Three</option>
                <option value="Four">Four</option>
                <option value="Five">Five</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectSectionEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section</label>
              <select id="selectSectionEdit" class="form-control form-select" v-model="editForm.section">
                <option value="" selected disabled>Select Section</option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="C">C</option>
                <option value="D">D</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectStudentEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Student</label>
              <select id="selectStudentEdit" class="form-control form-select" v-model="editForm.student">
                <option value="" selected disabled>Select Student</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectDateEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Date</label>
              <input type="date" class="form-control" id="selectDateEdit" v-model="editForm.date">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="footerLeftTextEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Footer Left Text</label>
              <input type="text" class="form-control" id="footerLeftTextEdit" placeholder="Enter Footer Left Text" v-model="editForm.footerLeftText">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="footerRightTextEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Footer Right Text</label>
              <input type="text" class="form-control" id="footerRightTextEdit" placeholder="Enter Footer Right Text" v-model="editForm.footerRightText">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Student Photo <span class="text-danger-600">*</span></label>
              <input type="file" class="form-control" @change="handleFileUpload">
            </div>
          </div>
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
              <button type="reset" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="closeSidebar">
                Cancel
              </button>
              <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
                Save
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>

    <!-- View Certificate Modal -->
    <div class="modal fade" id="viewCertificateModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content bg-transparent border-0">
          <div class="p-0 text-end mb-16">
            <button type="button" class="btn-close invert" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body p-0">
            <img src="@/assets/images/thumbs/certificate-img.png" alt="Certificate Image" class="w-100">
          </div>
        </div>
      </div>
    </div>

    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active': isSidebarOpen }" @click="closeSidebar"></div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/certificate/Breadcrumb.vue';
import CertificateTable from '@/components/certificate/CertificateTable.vue';

export default {
  name: "Certificate",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    CertificateTable
  },
  setup() {
    const isAddSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);
    
    const addForm = ref({
      certificateName: '',
      class: '',
      section: '',
      student: '',
      date: '',
      footerLeftText: '',
      footerRightText: '',
      studentPhoto: null
    });

    const editForm = ref({
      certificateName: '',
      class: '',
      section: '',
      student: '',
      date: '',
      footerLeftText: '',
      footerRightText: '',
      studentPhoto: null
    });

    const isSidebarOpen = computed(() => isAddSidebarOpen.value || isEditSidebarOpen.value);

    const openAddSidebar = () => {
      isAddSidebarOpen.value = true;
    };

    const openEditSidebar = (certificate) => {
      editForm.value = { ...certificate };
      isEditSidebarOpen.value = true;
    };

    const openViewModal = (certificate) => {
      const modal = new bootstrap.Modal(document.getElementById('viewCertificateModal'));
      modal.show();
    };

    const closeSidebar = () => {
      isAddSidebarOpen.value = false;
      isEditSidebarOpen.value = false;
    };

    const handleFileUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        console.log('File uploaded:', file.name);
      }
    };

    const handleAddSubmit = () => {
      console.log('Add Certificate:', addForm.value);
      // Here you would typically make an API call to add the certificate
      closeSidebar();
    };

    const handleEditSubmit = () => {
      console.log('Edit Certificate:', editForm.value);
      // Here you would typically make an API call to update the certificate
      closeSidebar();
    };

    return {
      isAddSidebarOpen,
      isEditSidebarOpen,
      isSidebarOpen,
      addForm,
      editForm,
      openAddSidebar,
      openEditSidebar,
      openViewModal,
      closeSidebar,
      handleFileUpload,
      handleAddSubmit,
      handleEditSubmit
    };
  }
}
</script>

<style scoped>
.my-sidebar.active,
.edit-sidebar.active {
  transform: translateX(0);
}

.overlay.active {
  visibility: visible;
  opacity: 1;
}
</style>
