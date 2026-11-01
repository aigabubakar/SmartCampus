<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-add-sidebar="openAddSidebar" />

        <div class="mt-24">
          <EmployeeListTable @edit-item="openEditSidebar" />
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- Add Employee Sidebar -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isAddSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add Employee</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleAddSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-12">
            <div class="">
              <label for="employeeName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Employee Name</label>
              <input type="text" class="form-control" id="employeeName" placeholder="Enter Employee Name" v-model="addForm.name">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="employeeId" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Employee ID</label>
              <input type="text" class="form-control" id="employeeId" placeholder="Enter Employee ID" v-model="addForm.employeeId">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="subject" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Subject</label>
              <select id="subject" class="form-control form-select" v-model="addForm.subject">
                <option value="" selected disabled>Select subject</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Physics">Physics</option>
                <option value="Chemistry">Chemistry</option>
                <option value="Biology">Biology</option>
                <option value="English">English</option>
                <option value="Geography">Geography</option>
                <option value="History">History</option>
                <option value="Economics">Economics</option>
                <option value="ICT">ICT</option>
                <option value="Accounting">Accounting</option>
              </select>
            </div>
          </div>
          <div class="col-sm-12">
            <div class="">
              <label for="class" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
              <input type="text" class="form-control" id="class" placeholder="e.g., 1 (A), 2 (B)" v-model="addForm.class">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="email" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Email</label>
              <input type="email" class="form-control" id="email" placeholder="Enter Email" v-model="addForm.email">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="phone" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Phone Number</label>
              <input type="text" class="form-control" id="phone" placeholder="Enter Phone Number" v-model="addForm.phone">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="joinDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Join Date</label>
              <input type="date" class="form-control" id="joinDate" v-model="addForm.joinDate">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="statusAdd" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
              <select id="statusAdd" class="form-control form-select" v-model="addForm.status">
                <option value="" selected disabled>Select status</option>
                <option value="Active">Active</option>
                <option value="Inactive">Inactive</option>
              </select>
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

    <!-- Edit Employee Sidebar -->
    <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isEditSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Employee</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleEditSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-12">
            <div class="">
              <label for="employeeNameEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Employee Name</label>
              <input type="text" class="form-control" id="employeeNameEdit" placeholder="Enter Employee Name" v-model="editForm.name">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="employeeIdEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Employee ID</label>
              <input type="text" class="form-control" id="employeeIdEdit" placeholder="Enter Employee ID" v-model="editForm.employeeId" readonly>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="subjectEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Subject</label>
              <select id="subjectEdit" class="form-control form-select" v-model="editForm.subject">
                <option value="" selected disabled>Select subject</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Physics">Physics</option>
                <option value="Chemistry">Chemistry</option>
                <option value="Biology">Biology</option>
                <option value="English">English</option>
                <option value="Geography">Geography</option>
                <option value="History">History</option>
                <option value="Economics">Economics</option>
                <option value="ICT">ICT</option>
                <option value="Accounting">Accounting</option>
              </select>
            </div>
          </div>
          <div class="col-sm-12">
            <div class="">
              <label for="classEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
              <input type="text" class="form-control" id="classEdit" placeholder="e.g., 1 (A), 2 (B)" v-model="editForm.class">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="emailEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Email</label>
              <input type="email" class="form-control" id="emailEdit" placeholder="Enter Email" v-model="editForm.email">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="phoneEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Phone Number</label>
              <input type="text" class="form-control" id="phoneEdit" placeholder="Enter Phone Number" v-model="editForm.phone">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="joinDateEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Join Date</label>
              <input type="date" class="form-control" id="joinDateEdit" v-model="editForm.joinDate">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="statusEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
              <select id="statusEdit" class="form-control form-select" v-model="editForm.status">
                <option value="" selected disabled>Select status</option>
                <option value="Active">Active</option>
                <option value="Inactive">Inactive</option>
              </select>
            </div>
          </div>
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
              <button type="reset" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="closeSidebar">
                Cancel
              </button>
              <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
                Update
              </button>
            </div>
          </div>
        </div>
      </form>
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
import Breadcrumb from '@/components/hrm/employeeList/Breadcrumb.vue';
import EmployeeListTable from '@/components/hrm/employeeList/EmployeeListTable.vue';

export default {
  name: "EmployeeList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    EmployeeListTable
  },
  setup() {
    const isAddSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);

    const addForm = ref({
      name: '',
      employeeId: '',
      subject: '',
      class: '',
      email: '',
      phone: '',
      joinDate: '',
      status: ''
    });

    const editForm = ref({
      id: null,
      name: '',
      employeeId: '',
      subject: '',
      class: '',
      email: '',
      phone: '',
      joinDate: '',
      status: ''
    });

    const isSidebarOpen = computed(() => isAddSidebarOpen.value || isEditSidebarOpen.value);

    const openAddSidebar = () => {
      isAddSidebarOpen.value = true;
    };

    const openEditSidebar = (item) => {
      editForm.value = { ...item };
      isEditSidebarOpen.value = true;
    };

    const closeSidebar = () => {
      isAddSidebarOpen.value = false;
      isEditSidebarOpen.value = false;
    };

    const handleAddSubmit = () => {
      console.log('Add Employee:', addForm.value);
      // Here you would typically make an API call to add the employee
      closeSidebar();
    };

    const handleEditSubmit = () => {
      console.log('Edit Employee:', editForm.value);
      // Here you would typically make an API call to update the employee
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
      closeSidebar,
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
