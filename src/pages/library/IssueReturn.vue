<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-add-sidebar="openAddSidebar" />

        <div class="mt-24">
          <IssueReturnTable />
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- Add Issue Return Sidebar -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isAddSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add Book Issue</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleAddSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-6">
            <div class="">
              <label for="libraryCardNo" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Library Card No</label>
              <input type="text" class="form-control" id="libraryCardNo" placeholder="Enter Library Card No" v-model="addForm.cardNo">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="memberClass" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
              <input type="text" class="form-control" id="memberClass" placeholder="Enter Class" v-model="addForm.class">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="memberSection" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section</label>
              <input type="text" class="form-control" id="memberSection" placeholder="Enter Section" v-model="addForm.section">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="memberStudent" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Student</label>
              <select id="memberStudent" class="form-control form-select" v-model="addForm.student">
                <option value="" selected disabled>Select Student</option>
                <option value="Regular">Regular</option>
                <option value="Irregular">Irregular</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectSubject" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Select Subject</label>
              <select id="selectSubject" class="form-control form-select" v-model="addForm.subject">
                <option value="" selected disabled>Select a Subject</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Science">Science</option>
                <option value="English">English</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectBook" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Book</label>
              <select id="selectBook" class="form-control form-select" v-model="addForm.book">
                <option value="" selected disabled>Select a book</option>
                <option value="English">English</option>
                <option value="Mathematics">Mathematics</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="issueDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Issue Date</label>
              <input type="date" class="form-control" id="issueDate" v-model="addForm.issueDate">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="returnDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Return Date</label>
              <input type="date" class="form-control" id="returnDate" v-model="addForm.returnDate">
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

    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active': isAddSidebarOpen }" @click="closeSidebar"></div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/library/issueReturn/Breadcrumb.vue';
import IssueReturnTable from '@/components/library/issueReturn/IssueReturnTable.vue';

export default {
  name: "IssueReturn",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    IssueReturnTable
  },
  setup() {
    const isAddSidebarOpen = ref(false);

    const addForm = ref({
      cardNo: '',
      class: '',
      section: '',
      student: '',
      subject: '',
      book: '',
      issueDate: '',
      returnDate: ''
    });

    const openAddSidebar = () => {
      isAddSidebarOpen.value = true;
    };

    const closeSidebar = () => {
      isAddSidebarOpen.value = false;
    };

    const handleAddSubmit = () => {
      console.log('Add Issue Return:', addForm.value);
      // Here you would typically make an API call to add the issue return
      closeSidebar();
    };

    return {
      isAddSidebarOpen,
      addForm,
      openAddSidebar,
      closeSidebar,
      handleAddSubmit
    };
  }
}
</script>

<style scoped>
.my-sidebar.active {
  transform: translateX(0);
}

.overlay.active {
  visibility: visible;
  opacity: 1;
}
</style>
