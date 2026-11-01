<template>
  <div class="card h-100">
    <div class="card-body p-0 dataTable-wrapper">
      <div class="d-flex align-items-center justify-content-between flex-wrap gap-16 px-20 py-12 border-bottom border-neutral-200">
        <div class="d-flex flex-wrap align-items-center gap-16">
          <!-- Export Dropdown -->
          <div class="dropdown">
            <button type="button"
              class="px-12 py-5-px border border-neutral-300 radius-8 d-flex align-items-center gap-20 "
              data-bs-toggle="dropdown" aria-expanded="false">
              <span class="d-flex align-items-center gap-1 text-secondary-light text-sm">
                <i class="ri-file-upload-line text-md line-height-1"></i>
                Export
              </span>
              <span class="">
                <i class="ri-arrow-down-s-line"></i>
              </span>
            </button>
            <ul class="dropdown-menu p-12 border bg-base shadow">
              <li>
                <button type="button"
                  class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10">
                  <i class="ri-file-3-line"></i>
                  PDF
                </button>
              </li>
              <li>
                <button type="button"
                  class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10">
                  <i class="ri-file-excel-line"></i>
                  Excel
                </button>
              </li>
            </ul>
          </div>

          <!-- Search -->
          <form class="navbar-search dt-search m-0">
            <input type="text" class="dt-input bg-transparent radius-4" aria-controls="dataTable"
              name="search" placeholder="Search...">
            <iconify-icon icon="ion:search-outline" class="icon"></iconify-icon>
          </form>
        </div>

        <div class="d-flex align-items-center gap-8 text-secondary-light">
          <span class="">Rows per page:</span>
          <div class="dt-length">
            <select name="dataTable_length" aria-controls="dataTable" class="dt-input form-control form-select">
              <option value="5">5</option>
              <option value="10" selected>10</option>
              <option value="25">25</option>
              <option value="50">50</option>
              <option value="100">100</option>
            </select>
          </div>
        </div>
      </div>

      <div class="p-0">
        <div class="table-responsive">
          <table class="table bordered-table mb-0 data-table" id="dataTable">
            <thead>
              <tr>
                <th scope="col">S.L</th>
                <th scope="col">Apply Date</th>
                <th scope="col">Name</th>
                <th scope="col">User type</th>
                <th scope="col">Leave Type</th>
                <th scope="col">Date</th>
                <th scope="col">Duration</th>
                <th scope="col">Status</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(request, index) in leaveRequests" :key="index">
                <td>{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</td>
                <td>{{ request.applyDate }}</td>
                <td>{{ request.name }}</td>
                <td>{{ request.userType }}</td>
                <td><i :class="request.icon + ' me-1'"></i> {{ request.leaveType }}</td>
                <td>{{ request.date }}</td>
                <td>{{ request.duration }}</td>
                <td>
                  <span :class="getStatusClass(request.status)">
                    {{ request.status }}
                  </span>
                </td>
                <td>
                  <div class="btn-group">
                    <button type="button" class="text-primary-light text-xl" data-bs-toggle="dropdown"
                      data-bs-display="static" aria-expanded="false">
                      <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                    </button>
                    <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                      <li>
                        <button type="button"
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          @click="$emit('view-request', request)">
                          <i class="ri-eye-line"></i>
                          View Request
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button" @click="openDeleteModal(request)">
                          <i class="ri-delete-bin-6-line"></i>
                          Delete
                        </button>
                      </li>
                    </ul>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- Delete Modal -->
  <div class="modal fade" id="deleteModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-sm modal-dialog modal-dialog-centered max-w-340-px">
      <div class="modal-content radius-16 bg-base">
        <div class="modal-body pt-32 px-36 pb-24 text-center">
          <span class="mb-16 fs-1 line-height-1 text-danger">
            <iconify-icon icon="fluent:delete-24-regular" class="menu-icon"></iconify-icon>
          </span>
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this leave request?</h6>
          <div class="d-flex align-items-center justify-content-center gap-3 mt-24">
            <button type="reset"
              class="flex-grow-1 border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-24 py-11 radius-8"
              data-bs-dismiss="modal">
              Cancel
            </button>
            <button type="button"
              class="flex-grow-1 btn btn-primary-600 border border-primary-600 text-md px-16 py-12 radius-8" 
              data-bs-dismiss="modal" @click="confirmDelete">
              Yes, Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from 'vue';

export default {
  name: "LeaveRequestTable",
  emits: ['view-request'],
  setup() {
    const deleteId = ref(null);

    const leaveRequests = ref([
      { id: 1, applyDate: '07 May 2025', name: 'Jerome Bell', userType: 'Teacher', leaveType: 'Medical Leave', icon: 'ri-hospital-line', date: '07 May 2025 - 08 May 2025', duration: '1', status: 'Approved', reason: 'Doctor or hospital visits' },
      { id: 2, applyDate: '10 May 2025', name: 'Jane Cooper', userType: 'Student', leaveType: 'Casual Leave', icon: 'ri-sun-line', date: '10 May 2025 - 12 May 2025', duration: '2', status: 'Pending', reason: 'Personal reasons' },
      { id: 3, applyDate: '12 May 2025', name: 'Devon Lane', userType: 'Teacher', leaveType: 'Half Day Leave', icon: 'ri-time-line', date: '12 May 2025', duration: '0.5', status: 'Rejected', reason: 'Personal appointment' },
      { id: 4, applyDate: '13 May 2025', name: 'Cody Fisher', userType: 'Admin', leaveType: 'Vacation Leave', icon: 'ri-flight-takeoff-line', date: '13 May 2025 - 20 May 2025', duration: '7', status: 'Approved', reason: 'Family vacation' },
      { id: 5, applyDate: '14 May 2025', name: 'Theresa Webb', userType: 'Teacher', leaveType: 'Study Leave', icon: 'ri-book-open-line', date: '14 May 2025 - 16 May 2025', duration: '2', status: 'Pending', reason: 'Professional development' },
      { id: 6, applyDate: '15 May 2025', name: 'Darrell Steward', userType: 'Student', leaveType: 'Paid Leave', icon: 'ri-money-dollar-circle-line', date: '15 May 2025 - 17 May 2025', duration: '2', status: 'Approved', reason: 'Family event' },
      { id: 7, applyDate: '17 May 2025', name: 'Leslie Alexander', userType: 'Teacher', leaveType: 'Emergency Leave', icon: 'ri-alarm-warning-line', date: '17 May 2025 - 18 May 2025', duration: '1', status: 'Rejected', reason: 'Family emergency' },
      { id: 8, applyDate: '18 May 2025', name: 'Guy Hawkins', userType: 'Admin', leaveType: 'Maternity Leave', icon: 'ri-parent-line', date: '18 May 2025 - 28 May 2025', duration: '10', status: 'Approved', reason: 'Maternity' },
      { id: 9, applyDate: '19 May 2025', name: 'Brooklyn Simmons', userType: 'Teacher', leaveType: 'Paternity Leave', icon: 'ri-user-heart-line', date: '19 May 2025 - 24 May 2025', duration: '5', status: 'Pending', reason: 'Paternity' },
      { id: 10, applyDate: '20 May 2025', name: 'Kristin Watson', userType: 'Student', leaveType: 'Unpaid Leave', icon: 'ri-close-circle-line', date: '20 May 2025 - 21 May 2025', duration: '1', status: 'Rejected', reason: 'Personal reasons' },
    ]);

    const getStatusClass = (status) => {
      if (status === 'Approved') {
        return 'bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm';
      } else if (status === 'Pending') {
        return 'bg-warning-100 text-warning-600 px-24 py-4 radius-4 fw-medium text-sm';
      } else {
        return 'bg-danger-100 text-danger-600 px-24 py-4 radius-4 fw-medium text-sm';
      }
    };

    const openDeleteModal = (item) => {
      deleteId.value = item.id;
      const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
      modal.show();
    };

    const confirmDelete = () => {
      if (deleteId.value) {
        leaveRequests.value = leaveRequests.value.filter(lr => lr.id !== deleteId.value);
        deleteId.value = null;
      }
    };

    onMounted(async () => {
      await nextTick();
      if (typeof $ !== 'undefined' && $.fn.DataTable) {
        $('.data-table').each(function () {
          const $table = $(this);

          if ($table.hasClass('dataTable-initialized')) return;

          let tableInstance = $table.DataTable({
            pageLength: 10,
            columnDefs: [{ orderable: false, targets: [8] }]
          });

          $table.addClass('dataTable-initialized');

          $table.closest('.dataTable-wrapper').find('.dt-search .dt-input').on('keyup', function () {
            tableInstance.search(this.value).draw();
          });

          $table.closest('.dataTable-wrapper').find('.dt-length .dt-input').on('change', function () {
            const value = $(this).val();
            tableInstance.page.len(value).draw();
          });
        });
      }
    });

    return {
      leaveRequests,
      getStatusClass,
      openDeleteModal,
      confirmDelete
    };
  }
}
</script>
