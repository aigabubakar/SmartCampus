<template>
  <div class="card h-100 p-0">
    <div class="card-body p-24">
      <div class="mt-8">
        <div v-for="(event, index) in events" :key="index" class="event-item d-flex align-items-center justify-content-between gap-4 pb-16 mb-16 border border-start-0 border-end-0 border-top-0">
          <div class="">
            <div class="d-flex align-items-center gap-10">
              <span class="w-12-px h-12-px rounded-circle fw-medium" :class="event.colorClass"></span>
              <span class="text-secondary-light">{{ event.time }}</span>
            </div>
            <span class="text-primary-light fw-semibold text-md mt-4">{{ event.title }}</span>
          </div>
          <div class="dropdown">
            <button type="button" data-bs-toggle="dropdown" aria-expanded="false">
              <iconify-icon icon="entypo:dots-three-vertical" class="icon text-secondary-light"></iconify-icon>
            </button>
            <ul class="dropdown-menu p-12 border bg-base shadow">
              <li>
                <button type="button" class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10" @click="$emit('view-event', event)">
                  <iconify-icon icon="hugeicons:view" class="icon text-lg line-height-1"></iconify-icon>
                  View
                </button>
              </li>
              <li>
                <button type="button" class="edit-sidebar-btn dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10" @click="$emit('edit-event', event)">
                  <iconify-icon icon="lucide:edit" class="icon text-lg line-height-1"></iconify-icon>
                  Edit
                </button>
              </li>
              <li>
                <button type="button" class="delete-item dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-danger-100 text-hover-danger-600 d-flex align-items-center gap-10" @click="openDeleteModal(event)">
                  <iconify-icon icon="fluent:delete-24-regular" class="icon text-lg line-height-1"></iconify-icon>
                  Delete
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Modal Delete Event start -->
    <div class="modal fade" id="exampleModalDelete" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog modal-sm modal-dialog modal-dialog-centered max-w-340-px">
        <div class="modal-content radius-16 bg-base">
          <div class="modal-body pt-32 px-36 pb-24 text-center">
            <span class="mb-16 fs-1 line-height-1 text-danger">
              <iconify-icon icon="fluent:delete-24-regular" class="menu-icon"></iconify-icon>
            </span>
            <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this event?</h6>
            <div class="d-flex align-items-center justify-content-center gap-3 mt-24">
              <button type="reset" class="flex-grow-1 border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-24 py-11 radius-8" data-bs-dismiss="modal">
                Cancel
              </button>
              <button type="button" class="flex-grow-1 btn btn-primary-600 border border-primary-600 text-md px-16 py-12 radius-8" data-bs-dismiss="modal" @click="confirmDelete">
                Yes, Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Modal Delete Event end -->

  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: "EventList",
  emits: ['view-event', 'edit-event'],
  setup(props, { emit }) {
    const deleteEventRef = ref(null);
    const events = ref([
      { title: 'Design Conference', time: 'Today, 10:30 PM - 02:30 AM', colorClass: 'bg-warning-600', description: 'N/A', label: 'Business', date: '25 Jan 2024' },
      { title: 'Weekend Festival', time: 'Today, 10:30 PM - 02:30 AM', colorClass: 'bg-success-600', description: 'N/A', label: 'Personal', date: '26 Jan 2024' },
      { title: 'Design Conference', time: 'Today, 10:30 PM - 02:30 AM', colorClass: 'bg-info-600', description: 'N/A', label: 'Business', date: '27 Jan 2024' },
      { title: 'Ultra Europe 2019', time: 'Today, 10:30 PM - 02:30 AM', colorClass: 'bg-warning-600', description: 'N/A', label: 'Family', date: '28 Jan 2024' },
      { title: 'Design Conference', time: 'Today, 10:30 PM - 02:30 AM', colorClass: 'bg-warning-600', description: 'N/A', label: 'Business', date: '29 Jan 2024' },
    ]);

    const openDeleteModal = (event) => {
      deleteEventRef.value = event;
      const modal = new window.bootstrap.Modal(document.getElementById('exampleModalDelete'));
      modal.show();
    };

    const confirmDelete = () => {
      if (deleteEventRef.value) {
        events.value = events.value.filter(e => e !== deleteEventRef.value);
        deleteEventRef.value = null;
        console.log('Deleted successfully');
      }
    };

    return {
      events,
      openDeleteModal,
      confirmDelete
    };
  }
}
</script>
