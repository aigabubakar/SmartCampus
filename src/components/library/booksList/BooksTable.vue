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
                <th scope="col">Subject</th>
                <th scope="col">Book Name</th>
                <th scope="col">Publisher</th>
                <th scope="col">Author</th>
                <th scope="col">Number</th>
                <th scope="col">Rack No</th>
                <th scope="col">Qty</th>
                <th scope="col">Available</th>
                <th scope="col">Price</th>
                <th scope="col">Exam Date</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(book, index) in books" :key="book.id">
                <td>
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="book.selected">
                    <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                  </div>
                </td>
                <td>{{ book.subject }}</td>
                <td>{{ book.bookName }}</td>
                <td>{{ book.publisher }}</td>
                <td>{{ book.author }}</td>
                <td>{{ book.number }}</td>
                <td>{{ book.rackNo }}</td>
                <td>{{ book.qty }}</td>
                <td>{{ book.available }}</td>
                <td>${{ book.price }}</td>
                <td>{{ book.examDate }}</td>
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
                          @click="$emit('edit-book', book)">
                          <i class="ri-edit-2-line"></i>
                          Edit
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button" @click="openDeleteModal(book)">
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
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this book?</h6>
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
  name: "BooksTable",
  emits: ['edit-book'],
  setup() {
    const deleteId = ref(null);

    const books = ref([
      { id: 1, subject: 'Art', bookName: 'The Little Prince', publisher: 'Devon Lane', author: 'Darrell Steward', number: 101, rackNo: '1234', qty: 60, available: 20, price: 250, examDate: '05 Jun 2015', selected: false },
      { id: 2, subject: 'Mathematics', bookName: 'Advanced Algebra', publisher: 'Penguin Books', author: 'Jane Cooper', number: 102, rackNo: '5678', qty: 40, available: 18, price: 300, examDate: '10 Jul 2016', selected: false },
      { id: 3, subject: 'Science', bookName: 'Physics for Beginners', publisher: 'HarperCollins', author: 'Guy Hawkins', number: 103, rackNo: '8790', qty: 55, available: 30, price: 280, examDate: '15 Mar 2017', selected: false },
      { id: 4, subject: 'History', bookName: 'World Wars', publisher: 'Oxford Press', author: 'Leslie Alexander', number: 104, rackNo: '3210', qty: 35, available: 12, price: 200, examDate: '21 Sep 2018', selected: false },
      { id: 5, subject: 'Geography', bookName: 'Earth & Beyond', publisher: 'Macmillan', author: 'Robert Fox', number: 105, rackNo: '4311', qty: 45, available: 10, price: 310, examDate: '08 Jan 2019', selected: false },
      { id: 6, subject: 'Biology', bookName: 'Human Anatomy', publisher: 'Cambridge House', author: 'Annette Black', number: 106, rackNo: '2915', qty: 70, available: 35, price: 400, examDate: '11 Dec 2020', selected: false },
      { id: 7, subject: 'Economics', bookName: 'Money & Markets', publisher: 'Random House', author: 'Esther Howard', number: 107, rackNo: '3425', qty: 50, available: 28, price: 270, examDate: '19 Mar 2021', selected: false },
      { id: 8, subject: 'Computer Science', bookName: 'JavaScript Essentials', publisher: 'TechWorld', author: 'Kathryn Murphy', number: 108, rackNo: '5320', qty: 80, available: 60, price: 500, examDate: '05 Apr 2022', selected: false },
      { id: 9, subject: 'English', bookName: "Shakespeare's Works", publisher: 'Vintage Books', author: 'Courtney Henry', number: 109, rackNo: '1567', qty: 65, available: 45, price: 350, examDate: '12 May 2023', selected: false },
      { id: 10, subject: 'Chemistry', bookName: 'Organic Compounds', publisher: 'Scholastic', author: 'Wade Warren', number: 110, rackNo: '4879', qty: 75, available: 55, price: 420, examDate: '10 Feb 2024', selected: false },
    ]);

    const toggleAll = () => {
      const allSelected = books.value.every(book => book.selected);
      books.value.forEach(book => {
        book.selected = !allSelected;
      });
    };

    const openDeleteModal = (book) => {
      deleteId.value = book.id;
      const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
      modal.show();
    };

    const confirmDelete = () => {
      if (deleteId.value) {
        books.value = books.value.filter(book => book.id !== deleteId.value);
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
            columnDefs: [{ orderable: false, targets: [0, 11] }]
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
      books,
      toggleAll,
      openDeleteModal,
      confirmDelete
    };
  }
}
</script>
