<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-add-sidebar="openAddSidebar" />

        <div class="mt-24">
          <div class="row gy-4">
            <div class="col-xxl-3 col-lg-4">
              <EventList @view-event="openViewModal" @edit-event="openEditSidebar" />
            </div>
            <div class="col-xxl-9 col-lg-8">
              <CalendarCard />
            </div>
          </div>
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- Add sidebar start -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isAddSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add New Event</h5>
        <button type="button" class="close-my-sidebar text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form action="#" class="p-20">
        <div class="row g-3">
          <div class="col-12">
            <label for="eventTitle" class="form-label fw-semibold text-primary-light text-sm mb-8">Event Title :</label>
            <input type="text" class="form-control radius-8" id="eventTitle" placeholder="Enter Event Title">
          </div>
          <div class="col-md-6">
            <label for="startDate" class="form-label fw-semibold text-primary-light text-sm mb-8">Start Date</label>
            <div class="position-relative">
              <input class="form-control radius-8 bg-base flatpickr-input" id="startDate" type="text" placeholder="03/12/2024, 10:30 AM" readonly="readonly">
              <span class="position-absolute end-0 top-50 translate-middle-y me-12 line-height-1">
                <iconify-icon icon="solar:calendar-linear" class="icon text-lg"></iconify-icon>
              </span>
            </div>
          </div>
          <div class="col-md-6">
            <label for="endDate" class="form-label fw-semibold text-primary-light text-sm mb-8">End Date </label>
            <div class="position-relative">
              <input class="form-control radius-8 bg-base flatpickr-input" id="endDate" type="text" placeholder="03/12/2024, 2:30 PM" readonly="readonly">
              <span class="position-absolute end-0 top-50 translate-middle-y me-12 line-height-1">
                <iconify-icon icon="solar:calendar-linear" class="icon text-lg"></iconify-icon>
              </span>
            </div>
          </div>
          <div class="col-12">
            <label class="form-label fw-semibold text-primary-light text-sm mb-8">Label </label>
            <div class="d-flex align-items-center flex-wrap gap-28">
              <div v-for="label in labels" :key="label.id" class="form-check d-flex align-items-center gap-2" :class="label.checkClass">
                <input class="form-check-input" type="radio" name="label" :id="label.id">
                <label class="form-check-label line-height-1 fw-medium text-secondary-light text-sm d-flex align-items-center gap-1" :for="label.id">
                  <span class="w-8-px h-8-px rounded-circle" :class="label.colorClass"></span>
                  {{ label.text }}
                </label>
              </div>
            </div>
          </div>

          <div class="col-12">
            <label for="desc" class="form-label fw-semibold text-primary-light text-sm mb-8">Description</label>
            <textarea class="form-control" id="desc" rows="4" cols="50" placeholder="Write some text"></textarea>
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
    <!-- Add sidebar end -->

    <!-- Edit sidebar start -->
    <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isEditSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Event </h5>
        <button type="button" class="close-edit-sidebar text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form action="#" class="p-20">
        <div class="row g-3">
          <div class="col-12">
            <label for="eventTitleEdit" class="form-label fw-semibold text-primary-light text-sm mb-8">Event Title :</label>
            <input type="text" class="form-control radius-8" id="eventTitleEdit" placeholder="Enter Event Title" v-model="editForm.title">
          </div>
          <!-- Date inputs omitted for brevity, similar structure to add form -->
           <div class="col-md-6">
            <label for="startDateEdit" class="form-label fw-semibold text-primary-light text-sm mb-8">Start Date</label>
            <div class="position-relative">
              <input class="form-control radius-8 bg-base flatpickr-input" id="startDateEdit" type="text" placeholder="03/12/2024, 10:30 AM" readonly="readonly">
              <span class="position-absolute end-0 top-50 translate-middle-y me-12 line-height-1">
                <iconify-icon icon="solar:calendar-linear" class="icon text-lg"></iconify-icon>
              </span>
            </div>
          </div>
           <div class="col-md-6">
            <label for="endDateEdit" class="form-label fw-semibold text-primary-light text-sm mb-8">End Date </label>
            <div class="position-relative">
              <input class="form-control radius-8 bg-base flatpickr-input" id="endDateEdit" type="text" placeholder="03/12/2024, 2:30 PM" readonly="readonly">
              <span class="position-absolute end-0 top-50 translate-middle-y me-12 line-height-1">
                <iconify-icon icon="solar:calendar-linear" class="icon text-lg"></iconify-icon>
              </span>
            </div>
          </div>
          
           <div class="col-12">
            <label class="form-label fw-semibold text-primary-light text-sm mb-8">Label </label>
            <div class="d-flex align-items-center flex-wrap gap-28">
              <div v-for="label in labels" :key="label.id + 'Edit'" class="form-check d-flex align-items-center gap-2" :class="label.checkClass">
                <input class="form-check-input" type="radio" name="labelEdit" :id="label.id + 'Edit'" :checked="editForm.label === label.text">
                <label class="form-check-label line-height-1 fw-medium text-secondary-light text-sm d-flex align-items-center gap-1" :for="label.id + 'Edit'">
                  <span class="w-8-px h-8-px rounded-circle" :class="label.colorClass"></span>
                  {{ label.text }}
                </label>
              </div>
            </div>
          </div>

          <div class="col-12">
            <label for="descEdit" class="form-label fw-semibold text-primary-light text-sm mb-8">Description</label>
            <textarea class="form-control" id="descEdit" rows="4" cols="50" placeholder="Write some text" v-model="editForm.description"></textarea>
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
    <!-- Edit sidebar end -->

    <!-- Modal View Event -->
    <div class="modal fade" id="exampleModalView" tabindex="-1" aria-hidden="true" ref="viewModalRef">
        <div class="modal-dialog modal-lg modal-dialog modal-dialog-centered">
            <div class="modal-content radius-16 bg-base">
                <div class="modal-header py-16 px-24 border border-top-0 border-start-0 border-end-0">
                    <span class="modal-title fs-5 d-block" id="exampleModalViewLabel">View Details</span>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body p-24" v-if="selectedEvent">
                    <div class="mb-12">
                        <span class="text-secondary-light txt-sm fw-medium">Title</span>
                        <h6 class="text-primary-light fw-semibold text-md mb-0 mt-4">{{ selectedEvent.title }}</h6>
                    </div>
                    <div class="mb-12">
                        <span class="text-secondary-light txt-sm fw-medium">Start Date</span>
                        <h6 class="text-primary-light fw-semibold text-md mb-0 mt-4">{{ selectedEvent.date }}, 10:30AM</h6>
                    </div>
                    <div class="mb-12">
                        <span class="text-secondary-light txt-sm fw-medium">End Date</span>
                        <h6 class="text-primary-light fw-semibold text-md mb-0 mt-4">{{ selectedEvent.date }}, 2:30AM</h6>
                    </div>
                    <div class="mb-12">
                        <span class="text-secondary-light txt-sm fw-medium">Description</span>
                        <h6 class="text-primary-light fw-semibold text-md mb-0 mt-4">{{ selectedEvent.description }}</h6>
                    </div>
                    <div class="mb-12">
                        <span class="text-secondary-light txt-sm fw-medium">Label</span>
                        <h6 class="text-primary-light fw-semibold text-md mb-0 mt-4 d-flex align-items-center gap-2">
                            <span class="w-8-px h-8-px rounded-circle" :class="selectedEvent.colorClass"></span>
                            {{ selectedEvent.label }}
                        </h6>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Overlay -->
    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active': isSidebarOpen }" @click="closeSidebar"></div>

  </div>
</template>

<script>
import { ref, computed, onMounted, nextTick } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/event/Breadcrumb.vue';
import EventList from '@/components/event/EventList.vue';
import CalendarCard from '@/components/event/CalendarCard.vue';

export default {
  name: "Event",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    EventList,
    CalendarCard
  },
  setup() {
    const isAddSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);
    const selectedEvent = ref(null);
    const editForm = ref({ title: '', description: '', label: '' });

    const labels = [
        { id: 'Personal', text: 'Personal', colorClass: 'bg-success-600', checkClass: 'checked-success' },
        { id: 'Business', text: 'Business', colorClass: 'bg-primary-600', checkClass: 'checked-primary' },
        { id: 'Family', text: 'Family', colorClass: 'bg-warning-600', checkClass: 'checked-warning' },
        { id: 'Important', text: 'Important', colorClass: 'bg-lilac-600', checkClass: 'checked-secondary' },
        { id: 'Holiday', text: 'Holiday', colorClass: 'bg-danger-600', checkClass: 'checked-danger' },
    ];

    const isSidebarOpen = computed(() => isAddSidebarOpen.value || isEditSidebarOpen.value);

    const openAddSidebar = () => {
      isAddSidebarOpen.value = true;
      initDatePickers();
    };

    const openEditSidebar = (event) => {
      editForm.value = { ...event };
      isEditSidebarOpen.value = true;
      initDatePickers();
    };

    const openViewModal = (event) => {
      selectedEvent.value = event;
      const modal = new window.bootstrap.Modal(document.getElementById('exampleModalView'));
      modal.show();
    };

    const closeSidebar = () => {
      isAddSidebarOpen.value = false;
      isEditSidebarOpen.value = false;
    };

    const initDatePickers = async () => {
        await nextTick();
        if (typeof flatpickr !== 'undefined') {
             flatpickr(".flatpickr-input", {
                enableTime: true,
                dateFormat: "d/m/Y H:i",
            });
        }
    };

    return {
      isAddSidebarOpen,
      isEditSidebarOpen,
      isSidebarOpen,
      editForm,
      selectedEvent,
      labels,
      openAddSidebar,
      openEditSidebar,
      openViewModal,
      closeSidebar
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
