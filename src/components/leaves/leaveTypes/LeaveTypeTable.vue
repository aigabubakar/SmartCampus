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
                  class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10"
                  data-bs-toggle="modal" data-bs-target="#exampleModalView">
                  <i class="ri-file-3-line"></i>
                  PDF
                </button>
              </li>
              <li>
                <button type="button"
                  class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10"
                  data-bs-toggle="modal" data-bs-target="#exampleModalEdit">
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
                <th scope="col">
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="selectAll" @change="toggleAll">
                    <label class="form-check-label">S.L</label>
                  </div>
                </th>
                <th scope="col">Leave Type</th>
                <th scope="col">Status</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(type, index) in leaveTypes" :key="index">
                <td>
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="selectedItems" :value="type.id">
                    <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                  </div>
                </td>
                <td>{{ type.name }}</td>
                <td>
                  <span :class="getStatusClass(type.status)">
                    {{ type.status }}
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
                          @click="$emit('open-edit-sidebar', type)">
                          <i class="ri-edit-2-line"></i>
                          Edit
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button" @click="openDeleteModal(type)">
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
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this leave type?</h6>
          <div class="d-flex align-items-center justify-content-center gap-3 mt-24">
            <button type="reset"
              class="flex-grow-1 border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-24 py-11 radius-8"
              data-bs-dismiss="modal">
              Cancel
            </button>
            <button type="button"
              class="flex-grow-1 btn btn-primary-600 border border-primary-600 text-md px-16 py-12 radius-8" data-bs-dismiss="modal" @click="confirmDelete">
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
  name: "LeaveTypeTable",
  emits: ['open-edit-sidebar'],
  setup() {
    const selectAll = ref(false);
    const selectedItems = ref([]);
    const deleteId = ref(null);

    const leaveTypes = ref([
      { id: 1, name: 'Medical Leave', status: 'Active' },
      { id: 2, name: 'Special Leave', status: 'Inactive' },
      { id: 3, name: 'Casual Leave', status: 'Active' },
      { id: 4, name: 'Maternity Leave', status: 'Inactive' },
      { id: 5, name: 'Paternity Leave', status: 'Active' },
      { id: 6, name: 'Sick Leave', status: 'Active' },
      { id: 7, name: 'Annual Leave', status: 'Active' },
      { id: 8, name: 'Compassionate Leave', status: 'Inactive' },
      { id: 9, name: 'Study Leave', status: 'Active' },
      { id: 10, name: 'Unpaid Leave', status: 'Inactive' },
      { id: 11, name: 'Annual Leave', status: 'Active' },
      { id: 12, name: 'Compassionate Leave', status: 'Inactive' },
    ]);

    const toggleAll = () => {
      if (selectAll.value) {
        selectedItems.value = leaveTypes.value.map(lt => lt.id);
      } else {
        selectedItems.value = [];
      }
    };

    const getStatusClass = (status) => {
      return status === 'Active'
        ? 'bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm'
        : 'bg-danger-100 text-danger-600 px-24 py-4 radius-4 fw-medium text-sm';
    };

    const openDeleteModal = (item) => {
      deleteId.value = item.id;
      const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
      modal.show();
    };

    const confirmDelete = () => {
      if (deleteId.value) {
        leaveTypes.value = leaveTypes.value.filter(lt => lt.id !== deleteId.value);
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
            columnDefs: [{ orderable: false, targets: [0, 3] }] 
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
      leaveTypes,
      selectAll,
      selectedItems,
      toggleAll,
      getStatusClass,
      openDeleteModal,
      confirmDelete
    };
  }
}
</script>
