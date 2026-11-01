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
                <th scope="col">Join Date</th>
                <th scope="col">Card No</th>
                <th scope="col">Student Name</th>
                <th scope="col">Class</th>
                <th scope="col">Phone Number</th>
                <th scope="col">Book Issue</th>
                <th scope="col">Issue Date</th>
                <th scope="col">Return Date</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(member, index) in members" :key="member.id">
                <td>
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="member.selected">
                    <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                  </div>
                </td>
                <td>{{ member.joinDate }}</td>
                <td>{{ member.cardNo }}</td>
                <td>{{ member.studentName }}</td>
                <td>{{ member.class }}</td>
                <td>{{ member.phoneNumber }}</td>
                <td>{{ member.bookIssue }}</td>
                <td>{{ member.issueDate }}</td>
                <td>{{ member.returnDate }}</td>
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
                          @click="$emit('view-member', member)">
                          <i class="ri-eye-line"></i>
                          View
                        </button>
                      </li>
                      <li>
                        <button type="button"
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          @click="$emit('edit-member', member)">
                          <i class="ri-edit-2-line"></i>
                          Edit
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button"
                          @click="$emit('issue-book', member)">
                          <i class="ri-book-open-line"></i>
                          Issue Book
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button" @click="openDeleteModal(member)">
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
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this member?</h6>
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
  name: "MembersTable",
  emits: ['view-member', 'edit-member', 'issue-book'],
  setup() {
    const deleteId = ref(null);

    const members = ref([
      { id: 1, joinDate: '05 Jun 2015', cardNo: '12563', studentName: 'Jon Dev', class: 'Class 1 (A)', phoneNumber: '(+33)6 55 56 56 33', bookIssue: 2, issueDate: '01 Jun 2015', returnDate: '01 Feb 2015', selected: false },
      { id: 2, joinDate: '15 Jan 2016', cardNo: '12890', studentName: 'Emily Johnson', class: 'Class 2 (B)', phoneNumber: '(+1) 205 555 7821', bookIssue: 3, issueDate: '12 Jan 2016', returnDate: '20 Jan 2016', selected: false },
      { id: 3, joinDate: '10 Feb 2017', cardNo: '14250', studentName: 'Michael Brown', class: 'Class 3 (C)', phoneNumber: '(+44) 745 987 3210', bookIssue: 1, issueDate: '05 Feb 2017', returnDate: '15 Feb 2017', selected: false },
      { id: 4, joinDate: '22 Mar 2018', cardNo: '15642', studentName: 'Sarah Lee', class: 'Class 4 (A)', phoneNumber: '(+49) 178 556 9876', bookIssue: 4, issueDate: '15 Mar 2018', returnDate: '25 Mar 2018', selected: false },
      { id: 5, joinDate: '09 Apr 2019', cardNo: '16580', studentName: 'William Smith', class: 'Class 5 (B)', phoneNumber: '(+91) 98765 43210', bookIssue: 2, issueDate: '05 Apr 2019', returnDate: '10 Apr 2019', selected: false },
      { id: 6, joinDate: '20 May 2020', cardNo: '17690', studentName: 'Olivia White', class: 'Class 6 (C)', phoneNumber: '(+971) 55 432 7890', bookIssue: 3, issueDate: '18 May 2020', returnDate: '28 May 2020', selected: false },
      { id: 7, joinDate: '01 Jun 2021', cardNo: '18950', studentName: 'James Wilson', class: 'Class 7 (A)', phoneNumber: '(+92) 333 456 7890', bookIssue: 5, issueDate: '25 May 2021', returnDate: '05 Jun 2021', selected: false },
      { id: 8, joinDate: '17 Jul 2022', cardNo: '19560', studentName: 'Emma Garcia', class: 'Class 8 (B)', phoneNumber: '(+880) 1712 567 890', bookIssue: 1, issueDate: '10 Jul 2022', returnDate: '20 Jul 2022', selected: false },
      { id: 9, joinDate: '08 Aug 2023', cardNo: '20540', studentName: 'Liam Martinez', class: 'Class 9 (A)', phoneNumber: '(+880) 1785 112 223', bookIssue: 2, issueDate: '01 Aug 2023', returnDate: '12 Aug 2023', selected: false },
      { id: 10, joinDate: '02 Sep 2024', cardNo: '21500', studentName: 'Noah Anderson', class: 'Class 10 (C)', phoneNumber: '(+880) 1990 998 877', bookIssue: 6, issueDate: '28 Aug 2024', returnDate: '10 Sep 2024', selected: false },
    ]);

    const toggleAll = () => {
      const allSelected = members.value.every(member => member.selected);
      members.value.forEach(member => {
        member.selected = !allSelected;
      });
    };

    const openDeleteModal = (member) => {
      deleteId.value = member.id;
      const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
      modal.show();
    };

    const confirmDelete = () => {
      if (deleteId.value) {
        members.value = members.value.filter(member => member.id !== deleteId.value);
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
            columnDefs: [{ orderable: false, targets: [0, 9] }]
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
      members,
      toggleAll,
      openDeleteModal,
      confirmDelete
    };
  }
}
</script>
