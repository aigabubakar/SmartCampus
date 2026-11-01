<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <!-- Breadcrumb -->
        <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
          <div class="">
            <h1 class="fw-semibold mb-4 h6 text-primary-light">Member Details</h1>
            <div class="">
              <a href="index.html" class="text-secondary-light hover-text-primary hover-underline">Dashboard</a>
              <a href="/members-list" class="text-secondary-light hover-text-primary hover-underline"> / Library</a>
              <span class="text-secondary-light">/ Member Details</span>
            </div>
          </div>
        </div>

        <div class="mt-24">
          <!-- Member Info Card -->
          <div class="card h-100">
            <div class="card-body p-24">
              <div class="d-flex gap-32 flex-md-row flex-column">
                <div class="max-w-300-px w-100 text-center">
                  <figure class="mb-20 w-120-px h-120-px mx-auto rounded-circle overflow-hidden">
                    <img :src="memberImage" alt="Member Image" class="w-100 h-100 object-fit-cover">
                  </figure>
                  <h2 class="h6 text-primary-light mb-4 fw-semibold">{{ member.name }}</h2>
                  <p class="mb-0">Admission No: <span class="text-primary-600 fw-semibold">{{ member.cardNo }}</span></p>
                  <div class="mt-32 d-flex gap-16 w-100">
                    <button type="button"
                      class="btn border fw-medium border-danger-600 bg-hover-danger-200 text-danger-600 text-md d-flex justify-content-center align-items-center gap-8 flex-grow-1 px-12 py-8 radius-8"
                      @click="openSuspendModal">
                      <span class="d-flex text-lg">
                        <i class="ri-delete-bin-2-line"></i>
                      </span>
                      Suspend
                    </button>
                    <button type="button"
                      class="btn btn-primary-600 border fw-medium border-primary-600 text-md d-flex justify-content-center align-items-center gap-8 flex-grow-1 px-12 py-8 radius-8"
                      @click="editMember">
                      <span class="d-flex text-lg">
                        <i class="ri-edit-line"></i>
                      </span>
                      Edit
                    </button>
                  </div>
                </div>
                <div class="">
                  <span class="h-100 w-1-px bg-neutral-200"></span>
                </div>
                <div class="flex-grow-1">
                  <div class="pb-16 border-bottom d-flex align-items-center justify-content-between gap-20">
                    <h3 class="h6 text-primary-light text-lg mb-0 fw-semibold">Personal Info</h3>
                  </div>
                  <div class="mt-16 d-flex flex-column gap-8">
                    <div class="d-flex gap-4">
                      <span class="fw-semibold text-sm text-primary-light w-110-px">Class</span>
                      <span class="fw-normal text-sm text-secondary-light">: {{ member.class }}</span>
                    </div>
                    <div class="d-flex gap-4">
                      <span class="fw-semibold text-sm text-primary-light w-110-px">Section</span>
                      <span class="fw-normal text-sm text-secondary-light">: {{ member.section }}</span>
                    </div>
                    <div class="d-flex gap-4">
                      <span class="fw-semibold text-sm text-primary-light w-110-px">Join Date</span>
                      <span class="fw-normal text-sm text-secondary-light">: {{ member.joinDate }}</span>
                    </div>
                    <div class="d-flex gap-4">
                      <span class="fw-semibold text-sm text-primary-light w-110-px">Gender</span>
                      <span class="fw-normal text-sm text-secondary-light">: {{ member.gender }}</span>
                    </div>
                    <div class="d-flex gap-4">
                      <span class="fw-semibold text-sm text-primary-light w-110-px">Phone Number</span>
                      <span class="fw-normal text-sm text-primary-600">: {{ member.phoneNumber }}</span>
                    </div>
                    <div class="d-flex gap-4">
                      <span class="fw-semibold text-sm text-primary-light w-110-px">Email</span>
                      <span class="fw-normal text-sm text-primary-600">: {{ member.email }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Books Issued Table -->
          <div class="my-16">
            <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
              <div class="card-header bg-base py-10 px-20 d-flex align-items-center justify-content-between">
                <h6 class="text-lg fw-semibold mb-0">Book Issued</h6>
                <button type="button"
                  class="btn btn-primary-600 d-flex align-items-center gap-6 py-8 text-sm"
                  @click="openIssueBookSidebar">
                  <span class="d-flex text-sm">
                    <i class="ri-add-large-line"></i>
                  </span>
                  Add Issue Book
                </button>
              </div>
              <div class="card-body p-0 dataTable-wrapper">
                <div class="d-flex flex-wrap align-items-center gap-24 justify-content-between px-20 py-12">
                  <div class="d-flex flex-wrap align-items-center gap-16">
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

                <table class="table bordered-table mb-0 table-heading-dark-mode w-100 data-table" id="dataTable">
                  <thead>
                    <tr>
                      <th scope="col">
                        <div class="form-check style-check d-flex align-items-center">
                          <input class="form-check-input" type="checkbox" @change="toggleAll">
                          <label class="form-check-label">S.L</label>
                        </div>
                      </th>
                      <th scope="col">Book Name</th>
                      <th scope="col">Number</th>
                      <th scope="col">Issue Date</th>
                      <th scope="col">Return Date</th>
                      <th scope="col">Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(book, index) in issuedBooks" :key="book.id">
                      <td>
                        <div class="form-check style-check d-flex align-items-center">
                          <input class="form-check-input" type="checkbox" v-model="book.selected">
                          <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                        </div>
                      </td>
                      <td>{{ book.bookName }}</td>
                      <td>{{ book.number }}</td>
                      <td>{{ book.issueDate }}</td>
                      <td>{{ book.returnDate }}</td>
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
                                type="button" @click="openReturnModal(book)">
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
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- Issue Book Sidebar -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isIssueBookSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add Book Issue</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleIssueBookSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-6">
            <div class="">
              <label for="selectSubject" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Select Subject</label>
              <select id="selectSubject" class="form-control form-select" v-model="issueBookForm.subject">
                <option value="" selected disabled>Select a Subject</option>
                <option value="Mathematics">Mathematics</option>
                <option value="Science">Science</option>
                <option value="English">English</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="selectBook" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Book</label>
              <select id="selectBook" class="form-control form-select" v-model="issueBookForm.book">
                <option value="" selected disabled>Select a book</option>
                <option value="English">English</option>
                <option value="Mathematics">Mathematics</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="issueDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Issue Date</label>
              <input type="date" class="form-control" id="issueDate" v-model="issueBookForm.issueDate">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="returnDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Return Date</label>
              <input type="date" class="form-control" id="returnDate" v-model="issueBookForm.returnDate">
            </div>
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

    <!-- Suspend Modal -->
    <div class="modal fade" id="suspendModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog modal-sm modal-dialog modal-dialog-centered max-w-340-px">
        <div class="modal-content radius-16 bg-base">
          <div class="modal-body pt-32 px-36 pb-24 text-center">
            <span class="mb-16 fs-1 line-height-1 text-danger">
              <iconify-icon icon="fluent:delete-24-regular" class="menu-icon"></iconify-icon>
            </span>
            <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to Suspend this Student?</h6>
            <div class="d-flex align-items-center justify-content-center gap-3 mt-24">
              <button type="reset"
                class="flex-grow-1 border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-24 py-11 radius-8"
                data-bs-dismiss="modal">
                Cancel
              </button>
              <button type="button"
                class="flex-grow-1 btn btn-primary-600 border border-primary-600 text-md px-16 py-12 radius-8"
                data-bs-dismiss="modal" @click="confirmSuspend">
                Yes, Suspend
              </button>
            </div>
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

    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active': isIssueBookSidebarOpen }" @click="closeSidebar"></div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

export default {
  name: "MemberDetails",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer
  },
  setup() {
    const isIssueBookSidebarOpen = ref(false);
    const returnBookId = ref(null);

    const member = ref({
      name: 'Seth Hallam',
      cardNo: 'AD1256589',
      class: 'Class 6 (2025-26)',
      section: 'A',
      joinDate: '10',
      gender: '10 Nov 2006',
      phoneNumber: '789678456',
      email: 'Set@example.com'
    });

    const memberImage = ref('/assets/images/thumbs/student-details-img.png');

    const issueBookForm = ref({
      subject: '',
      book: '',
      issueDate: '',
      returnDate: ''
    });

    const issuedBooks = ref([
      { id: 1, bookName: 'The Little Prince', number: 101, issueDate: '01 Jun 2015', returnDate: '01 Feb 2015', selected: false },
      { id: 2, bookName: 'To Kill a Mockingbird', number: 102, issueDate: '10 Jul 2016', returnDate: '25 Jul 2016', selected: false },
      { id: 3, bookName: '1984', number: 103, issueDate: '12 Mar 2017', returnDate: '02 Apr 2017', selected: false },
      { id: 4, bookName: 'Pride and Prejudice', number: 104, issueDate: '05 Aug 2018', returnDate: '28 Aug 2018', selected: false },
      { id: 5, bookName: 'The Great Gatsby', number: 105, issueDate: '11 Nov 2018', returnDate: '05 Dec 2018', selected: false },
      { id: 6, bookName: 'The Catcher in the Rye', number: 106, issueDate: '14 Jan 2019', returnDate: '02 Feb 2019', selected: false },
      { id: 7, bookName: 'Jane Eyre', number: 107, issueDate: '03 Apr 2020', returnDate: '20 Apr 2020', selected: false },
      { id: 8, bookName: 'The Hobbit', number: 108, issueDate: '22 May 2021', returnDate: '10 Jun 2021', selected: false },
      { id: 9, bookName: 'The Alchemist', number: 109, issueDate: '09 Oct 2022', returnDate: '28 Oct 2022', selected: false },
      { id: 10, bookName: "Harry Potter and the Sorcerer's Stone", number: 110, issueDate: '15 Jan 2023', returnDate: '10 Feb 2023', selected: false },
    ]);

    const toggleAll = () => {
      const allSelected = issuedBooks.value.every(book => book.selected);
      issuedBooks.value.forEach(book => {
        book.selected = !allSelected;
      });
    };

    const openIssueBookSidebar = () => {
      isIssueBookSidebarOpen.value = true;
    };

    const closeSidebar = () => {
      isIssueBookSidebarOpen.value = false;
    };

    const handleIssueBookSubmit = () => {
      console.log('Issue Book:', issueBookForm.value);
      // Here you would typically make an API call to issue the book
      closeSidebar();
    };

    const openSuspendModal = () => {
      const modal = new bootstrap.Modal(document.getElementById('suspendModal'));
      modal.show();
    };

    const confirmSuspend = () => {
      console.log('Suspend member:', member.value.name);
      // Here you would typically make an API call to suspend the member
    };

    const openReturnModal = (book) => {
      returnBookId.value = book.id;
      const modal = new bootstrap.Modal(document.getElementById('returnModal'));
      modal.show();
    };

    const confirmReturn = () => {
      if (returnBookId.value) {
        issuedBooks.value = issuedBooks.value.filter(book => book.id !== returnBookId.value);
        returnBookId.value = null;
        console.log('Book returned successfully');
      }
    };

    const editMember = () => {
      console.log('Edit member:', member.value.name);
      // Navigate to edit page or open edit modal
    };

    onMounted(async () => {
      await nextTick();
      if (typeof $ !== 'undefined' && $.fn.DataTable) {
        $('.data-table').each(function () {
          const $table = $(this);

          if ($table.hasClass('dataTable-initialized')) return;

          let tableInstance = $table.DataTable({
            pageLength: 10,
            columnDefs: [{ orderable: false, targets: [0, 5] }]
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
      member,
      memberImage,
      issuedBooks,
      isIssueBookSidebarOpen,
      issueBookForm,
      toggleAll,
      openIssueBookSidebar,
      closeSidebar,
      handleIssueBookSubmit,
      openSuspendModal,
      confirmSuspend,
      openReturnModal,
      confirmReturn,
      editMember
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
