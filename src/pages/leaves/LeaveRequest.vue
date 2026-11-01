<template>
  <div>
    <Sidebar />
    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb />

        <div class="mt-24">
          <LeaveRequestTable @view-request="openViewSidebar" />
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- View Sidebar -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isViewSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">View Leave Request</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <div class="p-20">
        <div class="d-flex flex-column gap-28">
          <div class="d-flex flex-column gap-8">
            <div class="d-flex gap-4">
              <span class="fw-semibold text-sm text-secondary-light w-110-px">Apply Date</span>
              <span class="fw-normal text-sm text-primary-light">: {{ selectedRequest.applyDate }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-sm text-secondary-light w-110-px">Name</span>
              <span class="fw-normal text-sm text-primary-light">: {{ selectedRequest.name }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-sm text-secondary-light w-110-px">User type</span>
              <span class="fw-normal text-sm text-primary-light">: {{ selectedRequest.userType }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-sm text-secondary-light w-110-px">Leave Type</span>
              <span class="fw-normal text-sm text-primary-light">: {{ selectedRequest.leaveType }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-sm text-secondary-light w-110-px">Date</span>
              <span class="fw-normal text-sm text-primary-light">: {{ selectedRequest.date }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-sm text-secondary-light w-110-px">Duration</span>
              <span class="fw-normal text-sm text-primary-light">: {{ selectedRequest.duration }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-sm text-secondary-light w-110-px">Reasons</span>
              <span class="fw-normal text-sm text-primary-light">: {{ selectedRequest.reason }}</span>
            </div>
          </div>
          <div class="">
            <h5 class="text-md mb-0">Update Status</h5>
            <div class="d-flex align-items-center flex-wrap gap-28 mt-16">
              <div class="form-check checked-primary d-flex align-items-center gap-2">
                <input class="form-check-input" type="radio" name="status" id="pending" value="Pending" v-model="statusForm.status">
                <label class="form-check-label" for="pending">Pending</label>
              </div>
              <div class="form-check checked-primary d-flex align-items-center gap-2">
                <input class="form-check-input" type="radio" name="status" id="approved" value="Approved" v-model="statusForm.status">
                <label class="form-check-label" for="approved">Approved</label>
              </div>
              <div class="form-check checked-primary d-flex align-items-center gap-2">
                <input class="form-check-input" type="radio" name="status" id="rejected" value="Rejected" v-model="statusForm.status">
                <label class="form-check-label" for="rejected">Rejected</label>
              </div>
            </div>
          </div>
          <form @submit.prevent="handleSubmit">
            <div class="">
              <label for="note" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Leave Note</label>
              <textarea class="form-control" id="note" placeholder="Enter note..." v-model="statusForm.note"></textarea>
            </div>
            <div class="d-flex align-items-center justify-content-center gap-3 mt-24">
              <button type="button"
                class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8"
                @click="closeSidebar">
                Cancel
              </button>
              <button type="submit"
                class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
                Save
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active': isViewSidebarOpen }" @click="closeSidebar"></div>
  </div>
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/leaves/leaveRequest/Breadcrumb.vue';
import LeaveRequestTable from '@/components/leaves/leaveRequest/LeaveRequestTable.vue';

export default {
  name: "LeaveRequest",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    LeaveRequestTable
  },
  setup() {
    const isViewSidebarOpen = ref(false);
    const selectedRequest = ref({
      applyDate: '',
      name: '',
      userType: '',
      leaveType: '',
      date: '',
      duration: '',
      reason: ''
    });
    const statusForm = ref({
      status: '',
      note: ''
    });

    const openViewSidebar = (request) => {
      selectedRequest.value = { ...request };
      statusForm.value.status = request.status;
      statusForm.value.note = '';
      isViewSidebarOpen.value = true;
    };

    const closeSidebar = () => {
      isViewSidebarOpen.value = false;
    };

    const handleSubmit = () => {
      console.log('Status Update:', statusForm.value);
      // Here you would typically make an API call to update the status
      closeSidebar();
    };

    return {
      isViewSidebarOpen,
      selectedRequest,
      statusForm,
      openViewSidebar,
      closeSidebar,
      handleSubmit
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
