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
                <th scope="col">Card No</th>
                <th scope="col">Issue To</th>
                <th scope="col">Class</th>
                <th scope="col">Book Name</th>
                <th scope="col">Number</th>
                <th scope="col">Issue Date</th>
                <th scope="col">Return Date</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(issue, index) in issueReturns" :key="issue.id">
                <td>
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="issue.selected">
                    <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                  </div>
                </td>
                <td>{{ issue.cardNo }}</td>
                <td>{{ issue.issueTo }}</td>
                <td>{{ issue.class }}</td>
                <td>{{ issue.bookName }}</td>
                <td>{{ issue.number }}</td>
                <td>{{ issue.issueDate }}</td>
                <td>{{ issue.returnDate }}</td>
                <td>
                  <div class="btn-group">
                    <button type="button" class="text-primary-light text-xl" data-bs-toggle="dropdown"
                      data-bs-display="static" aria-expanded="false">
                      <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                    </button>
                    <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button" @click="openReturnModal(issue)">
                          <i class="ri-arrow-go-back-line"></i>Book Return
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

  <!-- Return Book Modal -->
  <div class="modal fade" id="returnModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-sm modal-dialog modal-dialog-centered max-w-340-px">
      <div class="modal-content radius-16 bg-base">
        <div class="modal-body pt-32 px-36 pb-24 text-center">
          <span class="mb-16 fs-1 line-height-1 text-primary-600">
            <i class="ri-book-open-line"></i>
          </span>
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to Return this book?</h6>
          <div class="d-flex align-items-center justify-content-center gap-3 mt-24">
            <button type="reset"
              class="flex-grow-1 border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-24 py-11 radius-8"
              data-bs-dismiss="modal">
              No
            </button>
            <button type="button"
              class="flex-grow-1 btn btn-primary-600 border border-primary-600 text-md px-16 py-12 radius-8"
              data-bs-dismiss="modal" @click="confirmReturn">
              Yes Return
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
  name: "IssueReturnTable",
  setup() {
    const returnId = ref(null);

    const issueReturns = ref([
      { id: 1, cardNo: '12563', issueTo: 'Jon Dev', class: 'Class 1 (A)', bookName: 'The Little Prince', number: 101, issueDate: '01 Jun 2015', returnDate: '01 Feb 2015', selected: false },
      { id: 2, cardNo: '12874', issueTo: 'Sarah Khan', class: 'Class 2 (B)', bookName: 'To Kill a Mockingbird', number: 102, issueDate: '10 Jul 2016', returnDate: '25 Jul 2016', selected: false },
      { id: 3, cardNo: '13345', issueTo: 'Michael Lee', class: 'Class 3 (C)', bookName: '1984', number: 103, issueDate: '12 Mar 2017', returnDate: '02 Apr 2017', selected: false },
      { id: 4, cardNo: '14122', issueTo: 'Emma Watson', class: 'Class 4 (A)', bookName: 'Pride and Prejudice', number: 104, issueDate: '05 Aug 2018', returnDate: '28 Aug 2018', selected: false },
      { id: 5, cardNo: '14567', issueTo: 'David Miller', class: 'Class 5 (C)', bookName: 'The Great Gatsby', number: 105, issueDate: '11 Nov 2018', returnDate: '05 Dec 2018', selected: false },
      { id: 6, cardNo: '15231', issueTo: 'Olivia Brown', class: 'Class 6 (B)', bookName: 'The Hobbit', number: 106, issueDate: '22 May 2019', returnDate: '10 Jun 2019', selected: false },
      { id: 7, cardNo: '15890', issueTo: 'Lucas Smith', class: 'Class 7 (A)', bookName: 'Jane Eyre', number: 107, issueDate: '03 Apr 2020', returnDate: '20 Apr 2020', selected: false },
      { id: 8, cardNo: '16324', issueTo: 'Ella Johnson', class: 'Class 8 (B)', bookName: 'The Alchemist', number: 108, issueDate: '09 Oct 2021', returnDate: '28 Oct 2021', selected: false },
      { id: 9, cardNo: '17215', issueTo: 'Noah Wilson', class: 'Class 9 (C)', bookName: 'Brave New World', number: 109, issueDate: '05 Jan 2022', returnDate: '28 Jan 2022', selected: false },
      { id: 10, cardNo: '18009', issueTo: 'Sophia Davis', class: 'Class 10 (A)', bookName: "Harry Potter and the Sorcerer's Stone", number: 110, issueDate: '15 Mar 2023', returnDate: '10 Apr 2023', selected: false },
    ]);

    const toggleAll = () => {
      const allSelected = issueReturns.value.every(issue => issue.selected);
      issueReturns.value.forEach(issue => {
        issue.selected = !allSelected;
      });
    };

    const openReturnModal = (issue) => {
      returnId.value = issue.id;
      const modal = new bootstrap.Modal(document.getElementById('returnModal'));
      modal.show();
    };

    const confirmReturn = () => {
      if (returnId.value) {
        issueReturns.value = issueReturns.value.filter(issue => issue.id !== returnId.value);
        returnId.value = null;
        console.log('Book returned successfully');
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
      issueReturns,
      toggleAll,
      openReturnModal,
      confirmReturn
    };
  }
}
</script>
