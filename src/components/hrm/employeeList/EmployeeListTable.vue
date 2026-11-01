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

          <!-- Filter Dropdown -->
          <div class="dropdown">
            <button type="button"
              class="px-12 py-5-px border border-neutral-300 radius-8 d-flex align-items-center gap-20"
              data-bs-toggle="dropdown" aria-expanded="false">
              <span class="d-flex align-items-center gap-1 text-secondary-light text-sm">
                Filter
              </span>
              <span class="">
                <i class="ri-arrow-down-s-line"></i>
              </span>
            </button>
            <div class="dropdown-menu border bg-base shadow dropdown-menu-lg p-0">
              <div class="d-flex align-items-center justify-content-between border-bottom py-8 px-16">
                <span class="fw-semibold text-lg text-primary-light">Filter</span>
                <button type="button">
                  <i class="ri-close-large-line"></i>
                </button>
              </div>

              <form action="#" class="p-16">
                <div class="row g-3">
                  <div class="col-12">
                    <label for="subject" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Subject</label>
                    <select id="subject" class="form-control form-select">
                      <option value="Select">Select Subject</option>
                      <option value="Mathematics">Mathematics</option>
                      <option value="English">English</option>
                      <option value="Physics">Physics</option>
                      <option value="Chemistry">Chemistry</option>
                      <option value="Biology">Biology</option>
                    </select>
                  </div>
                  <div class="col-12">
                    <label for="status" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                    <select id="status" class="form-control form-select">
                      <option value="Select">Select Status</option>
                      <option value="Active">Active</option>
                      <option value="Inactive">Inactive</option>
                    </select>
                  </div>
                  <div class="col-6">
                    <button type="reset" class="btn btn-danger-200 text-danger-600 w-100">Reset</button>
                  </div>
                  <div class="col-6">
                    <button type="submit" class="btn btn-primary-600 w-100">Apply</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
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
                <th scope="col">ID</th>
                <th scope="col">Name</th>
                <th scope="col">Subject</th>
                <th scope="col">Class</th>
                <th scope="col">Email</th>
                <th scope="col">Phone Number</th>
                <th scope="col">Join Date</th>
                <th scope="col">Status</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(employee, index) in employees" :key="employee.id">
                <td>
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="employee.selected">
                    <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                  </div>
                </td>
                <td><span class="text-primary-600">{{ employee.employeeId }}</span></td>
                <td>
                  <div class="d-flex align-items-center">
                    <img :src="employee.avatar" :alt="employee.name + ' Image'" class="flex-shrink-0 me-12 radius-8">
                    <div class="">
                      <h6 class="text-md mb-0 fw-medium flex-grow-1">{{ employee.name }}</h6>
                    </div>
                  </div>
                </td>
                <td>{{ employee.subject }}</td>
                <td>{{ employee.class }}</td>
                <td>{{ employee.email }}</td>
                <td>{{ employee.phone }}</td>
                <td>{{ employee.joinDate }}</td>
                <td>
                  <span class="px-24 py-4 radius-4 fw-medium text-sm"
                    :class="employee.status === 'Active' ? 'bg-success-100 text-success-600' : 'bg-danger-100 text-danger-600'">
                    {{ employee.status }}
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
                          @click="viewDetails">
                          <i class="ri-user-3-line"></i>
                          View Details
                        </button>
                      </li>
                      <li>
                        <button type="button"
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          @click="$emit('edit-item', employee)">
                          <i class="ri-edit-2-line"></i>
                          Edit
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button">
                          <i class="ri-error-warning-line"></i>
                          {{ employee.status === 'Active' ? 'Deactivate' : 'Activate' }}
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button" @click="openDeleteModal(employee.id)">
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
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this employee?</h6>
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
import { useRouter } from 'vue-router';

export default {
  name: "EmployeeListTable",
  emits: ['edit-item'],
  setup() {
    const router = useRouter();
    const deleteId = ref(null);

    const employees = ref([
      { id: 1, employeeId: 'AD52365', name: 'Marvin McKinney', avatar: 'assets/images/thumbs/teacher-avatar-img1.png', subject: 'Mathematics', class: '1 (A), 2(A), 3(A)', email: 'chinthaka@hotmail.com', phone: '209.555.0104', joinDate: '05 May 2012', status: 'Active', selected: false },
      { id: 2, employeeId: 'AD52366', name: 'Ralph Edwards', avatar: 'assets/images/thumbs/teacher-avatar-img2.png', subject: 'Physics', class: '9 (A), 10 (B)', email: 'mobileip@mac.com', phone: '209.555.0104', joinDate: '05 May 2012', status: 'Inactive', selected: false },
      { id: 3, employeeId: 'AD52367', name: 'Courtney Henry', avatar: 'assets/images/thumbs/teacher-avatar-img3.png', subject: 'Biology', class: '6 (A), 7 (B)', email: 'courtney@edu.com', phone: '209.555.0134', joinDate: '18 Jan 2014', status: 'Active', selected: false },
      { id: 4, employeeId: 'AD52368', name: 'Eleanor Pena', avatar: 'assets/images/thumbs/teacher-avatar-img4.png', subject: 'Chemistry', class: '8 (B), 9 (A)', email: 'eleanor.pena@school.org', phone: '209.555.0189', joinDate: '22 Aug 2016', status: 'Inactive', selected: false },
      { id: 5, employeeId: 'AD52369', name: 'Cody Fisher', avatar: 'assets/images/thumbs/teacher-avatar-img5.png', subject: 'English', class: '5 (A), 6 (A)', email: 'cody.fisher@school.com', phone: '209.555.0192', joinDate: '14 Mar 2015', status: 'Active', selected: false },
      { id: 6, employeeId: 'AD52370', name: 'Devon Lane', avatar: 'assets/images/thumbs/teacher-avatar-img6.png', subject: 'Geography', class: '7 (C), 8 (A)', email: 'devon@edu.org', phone: '209.555.0119', joinDate: '09 Jul 2018', status: 'Active', selected: false },
      { id: 7, employeeId: 'AD52371', name: 'Bessie Cooper', avatar: 'assets/images/thumbs/teacher-avatar-img7.png', subject: 'History', class: '9 (B), 10 (A)', email: 'bessie.cooper@school.org', phone: '209.555.0156', joinDate: '23 Feb 2013', status: 'Inactive', selected: false },
      { id: 8, employeeId: 'AD52372', name: 'Arlene McCoy', avatar: 'assets/images/thumbs/teacher-avatar-img8.png', subject: 'Economics', class: '11 (B), 12 (A)', email: 'arlene.mccoy@edu.org', phone: '209.555.0172', joinDate: '16 Oct 2019', status: 'Active', selected: false },
      { id: 9, employeeId: 'AD52373', name: 'Annette Black', avatar: 'assets/images/thumbs/teacher-avatar-img9.png', subject: 'ICT', class: '8 (A), 9 (B)', email: 'annette@school.edu', phone: '209.555.0195', joinDate: '05 May 2020', status: 'Active', selected: false },
      { id: 10, employeeId: 'AD52374', name: 'Guy Hawkins', avatar: 'assets/images/thumbs/teacher-avatar-img2.png', subject: 'Accounting', class: '10 (A), 11 (A)', email: 'guy.hawkins@edu.com', phone: '209.555.0184', joinDate: '11 Dec 2017', status: 'Inactive', selected: false },
      { id: 11, employeeId: 'AD52375', name: 'Theresa Webb', avatar: 'assets/images/thumbs/teacher-avatar-img9.png', subject: 'Computer Science', class: '11 (B), 12 (A)', email: 'theresa.webb@school.edu', phone: '209.555.0217', joinDate: '29 Mar 2019', status: 'Active', selected: false },
      { id: 12, employeeId: 'AD52376', name: 'Kathryn Murphy', avatar: 'assets/images/thumbs/teacher-avatar-img6.png', subject: 'Environmental Science', class: '9 (A), 10 (B)', email: 'kathryn.murphy@college.edu', phone: '209.555.0259', joinDate: '03 Feb 2020', status: 'Inactive', selected: false },
    ]);

    const toggleAll = () => {
      const allSelected = employees.value.every(employee => employee.selected);
      employees.value.forEach(employee => {
        employee.selected = !allSelected;
      });
    };

    const openDeleteModal = (id) => {
      deleteId.value = id;
      const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
      modal.show();
    };

    const confirmDelete = () => {
      if (deleteId.value) {
        employees.value = employees.value.filter(employee => employee.id !== deleteId.value);
        deleteId.value = null;
        console.log('Employee deleted successfully');
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

    const viewDetails = () => {
      router.push('/employee-details');
    };

    return {
      employees,
      toggleAll,
      viewDetails,
      openDeleteModal,
      confirmDelete
    };
  }
}
</script>
