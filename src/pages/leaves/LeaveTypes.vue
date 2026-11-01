<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @open-add-sidebar="openAddSidebar" />
      <div class="mt-24">
        <LeaveTypeTable @open-edit-sidebar="openEditSidebar" />
      </div>
    </div>
    <Footer />
  </main>
  
  <ThemeCustomizer />

  <!-- Add Sidebar -->
  <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isAddSidebarOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
      <h5 class="text-lg mb-0">Add New Leave Type</h5>
      <button type="button" class="close-my-sidebar text-danger-600 text-lg d-flex" @click="closeSidebar">
        <i class="ri-close-large-line"></i>
      </button>
    </div>
    <form action="#" class="d-flex flex-column p-20">
      <div class="row g-3">
        <div class="col-sm-12">
          <div class="">
            <label for="leaveTypeName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Leave Type Name</label>
            <input type="text" class="form-control" id="leaveTypeName" placeholder="Enter Leave Type name">
          </div>
        </div>
        <div class="col-sm-12">
          <div class="">
            <label for="leaveStatus" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
            <select id="leaveStatus" class="form-control form-select">
              <option value="" selected disabled>Select Status</option>
              <option value="Active">Active</option>
              <option value="Inactive">Inactive</option>
            </select>
          </div>
        </div>
        <div class="col-12">
          <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
            <button type="button" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="closeSidebar">
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
      <h5 class="text-lg mb-0">Edit Leave Type</h5>
      <button type="button" class="close-edit-sidebar text-danger-600 text-lg d-flex" @click="closeSidebar">
        <i class="ri-close-large-line"></i>
      </button>
    </div>
    <form action="#" class="d-flex flex-column p-20">
      <div class="row g-3">
        <div class="col-sm-12">
          <div class="">
            <label for="editLeaveTypeName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Leave Type Name</label>
            <input type="text" class="form-control" id="editLeaveTypeName" placeholder="Enter Leave Type name" v-model="editForm.name">
          </div>
        </div>
        <div class="col-sm-12">
          <div class="">
            <label for="editLeaveStatus" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
            <select id="editLeaveStatus" class="form-control form-select" v-model="editForm.status">
              <option value="Active">Active</option>
              <option value="Inactive">Inactive</option>
            </select>
          </div>
        </div>
        <div class="col-12">
          <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
            <button type="button" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="closeSidebar">
              Cancel
            </button>
            <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8">
              Update
            </button>
          </div>
        </div>
      </div>
    </form>
  </div>
  
  <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active': isSidebarOpen }" @click="closeSidebar"></div>

</template>

<script>
import { ref, computed } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/leaves/leaveTypes/Breadcrumb.vue';
import LeaveTypeTable from '@/components/leaves/leaveTypes/LeaveTypeTable.vue';

export default {
  name: "LeaveTypes",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    LeaveTypeTable
  },
  setup() {
    const isAddSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);
    const editForm = ref({ name: '', status: '' });
    
    // Computed property to check if any sidebar is open to toggle overlay
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

    return {
      isAddSidebarOpen,
      isEditSidebarOpen,
      isSidebarOpen,
      editForm,
      openAddSidebar,
      openEditSidebar,
      closeSidebar
    };
  }
}
</script>
