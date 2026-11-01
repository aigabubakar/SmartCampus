<template>
  <div class="card h-100">
    <div class="card-body p-0 dataTable-wrapper">
      <div class="d-flex align-items-center justify-content-between flex-wrap gap-16 px-20 py-12 border-bottom border-neutral-200">
        <div class="d-flex flex-wrap align-items-center gap-16">
          <!-- Export Dropdown -->
          <div class="dropdown">
            <button type="button"
              class="px-12 py-5-px border border-neutral-300 radius-8 d-flex align-items-center gap-20"
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
                <th scope="col">
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" @change="toggleAll">
                    <label class="form-check-label">S.L</label>
                  </div>
                </th>
                <th scope="col">Invoice</th>
                <th scope="col">Name</th>
                <th scope="col">Description</th>
                <th scope="col">Expense Head</th>
                <th scope="col">Payment Type</th>
                <th scope="col">Amount</th>
                <th scope="col">Date</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(expense, index) in expenses" :key="expense.id">
                <td>
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="expense.selected">
                    <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                  </div>
                </td>
                <td>{{ expense.invoice }}</td>
                <td>{{ expense.name }}</td>
                <td>{{ expense.description }}</td>
                <td>{{ expense.expenseHead }}</td>
                <td>{{ expense.paymentType }}</td>
                <td>{{ expense.amount }}</td>
                <td>{{ expense.date }}</td>
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
                          @click="$emit('edit-item', expense)">
                          <i class="ri-edit-2-line"></i>
                          Edit
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button" @click="openDeleteModal(expense.id)">
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
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this expense?</h6>
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
  name: "ExpenseListTable",
  emits: ['edit-item'],
  setup() {
    const deleteId = ref(null);

    const expenses = ref([
      { id: 2, invoice: '1002', name: 'Sports Fund', description: 'Football tournament registration fees', expenseHead: 'Utility Bills', paymentType: 'Online', amount: '$850', date: '05 Jan 2024', selected: false },
      { id: 3, invoice: '1003', name: 'Exam Fees', description: 'Mid-term exam fee collection', expenseHead: 'Maintenance', paymentType: 'Cash', amount: '$1,200', date: '10 Jan 2024', selected: false },
      { id: 4, invoice: '1004', name: 'Admission', description: 'Purchase of stationery items', expenseHead: 'Stationery', paymentType: 'Cash', amount: '$320', date: '15 Jan 2024', selected: false },
      { id: 5, invoice: '1005', name: 'Science Lab', description: 'New student admission fees', expenseHead: 'Transport', paymentType: 'Cash', amount: '$680', date: '18 Jan 2024', selected: false },
      { id: 6, invoice: '1006', name: 'Donation', description: 'Lab maintenance fund collection', expenseHead: 'Laboratory', paymentType: 'Cheque', amount: '$2,500', date: '22 Jan 2024', selected: false },
      { id: 7, invoice: '1007', name: 'Library Sale', description: 'Alumni donation for scholarship', expenseHead: 'Sports Equipment', paymentType: 'Online', amount: '$950', date: '25 Jan 2024', selected: false },
      { id: 8, invoice: '1008', name: 'Transport Fees', description: 'Sale of old library books', expenseHead: 'Library Books', paymentType: 'Bank Transfer', amount: '$1,800', date: '28 Jan 2024', selected: false },
      { id: 9, invoice: '1009', name: 'Event Income', description: 'Monthly bus service collection', expenseHead: 'Technology', paymentType: 'Cheque', amount: '$8,500', date: '02 Feb 2024', selected: false },
      { id: 10, invoice: '1010', name: 'Miscellaneous', description: 'Annual cultural program tickets', expenseHead: 'Event Expenses', paymentType: 'Cash', amount: '$3,200', date: '10 Feb 2024', selected: false },
    ]);

    const toggleAll = () => {
      const allSelected = expenses.value.every(expense => expense.selected);
      expenses.value.forEach(expense => {
        expense.selected = !allSelected;
      });
    };

    const openDeleteModal = (id) => {
      deleteId.value = id;
      const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
      modal.show();
    };

    const confirmDelete = () => {
      if (deleteId.value) {
        expenses.value = expenses.value.filter(expense => expense.id !== deleteId.value);
        deleteId.value = null;
        console.log('Expense deleted successfully');
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
            columnDefs: [{ orderable: false, targets: [0, 8] }]
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
      expenses,
      toggleAll,
      openDeleteModal,
      confirmDelete
    };
  }
}
</script>
