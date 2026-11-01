<template>
  <div class="card h-100">
    <div class="card-body p-0 dataTable-wrapper">
      <div class="d-flex align-items-center justify-content-between flex-wrap gap-16 px-20 py-12 border-bottom border-neutral-200">
        <div class="d-flex flex-wrap align-items-center gap-16">
          <!-- Export Dropdown -->
          <div class="dropdown">
            <button type="button" class="px-12 py-5-px border border-neutral-300 radius-8 d-flex align-items-center gap-20" data-bs-toggle="dropdown" aria-expanded="false">
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
                <button type="button" class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10">
                  <i class="ri-file-3-line"></i>
                  PDF
                </button>
              </li>
              <li>
                <button type="button" class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10">
                  <i class="ri-file-excel-line"></i>
                  Excel
                </button>
              </li>
            </ul>
          </div>

          <!-- Search -->
          <form class="navbar-search dt-search m-0">
            <input type="text" class="dt-input bg-transparent radius-4" placeholder="Search...">
            <i class="ri-search-line icon"></i>
          </form>

          <!-- Filter Dropdown -->
          <div class="dropdown">
            <button type="button" class="px-12 py-5-px border border-neutral-300 radius-8 d-flex align-items-center gap-20" data-bs-toggle="dropdown" aria-expanded="false">
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
              <form class="p-16">
                <div class="row g-3">
                  <div class="col-12">
                    <label for="departmentFilter" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Department</label>
                    <select id="departmentFilter" class="form-control form-select">
                      <option value="">Select Department</option>
                      <option value="English">English</option>
                      <option value="Mathematics">Mathematics</option>
                      <option value="Science">Science</option>
                      <option value="IT">IT</option>
                    </select>
                  </div>
                  <div class="col-12">
                    <label for="statusFilter" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                    <select id="statusFilter" class="form-control form-select">
                      <option value="">Select Status</option>
                      <option value="Paid">Paid</option>
                      <option value="Pending">Pending</option>
                      <option value="Unpaid">Unpaid</option>
                    </select>
                  </div>
                  <div class="col-6">
                    <button type="reset" class="btn btn-danger-200 text-danger-600 w-100">Reset</button>
                  </div>
                  <div class="col-6">
                    <button type="button" class="btn btn-primary-600 w-100">Apply</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>

        <!-- Rows per page -->
        <div class="d-flex align-items-center gap-8 text-secondary-light">
          <span class="">Rows per page:</span>
          <div class="dt-length">
            <select class="dt-input form-control form-select">
              <option value="5">5</option>
              <option value="10" selected>10</option>
              <option value="25">25</option>
              <option value="50">50</option>
              <option value="100">100</option>
            </select>
          </div>
        </div>
      </div>

      <!-- Table -->
      <div class="p-0">
        <table class="table bordered-table mb-0 data-table" id="payrollTable">
          <thead>
            <tr>
              <th scope="col">
                <div class="form-check style-check d-flex align-items-center">
                  <input class="form-check-input" type="checkbox" @change="toggleAll" v-model="selectAll">
                  <label class="form-check-label">S.L</label>
                </div>
              </th>
              <th scope="col">ID</th>
              <th scope="col">Name</th>
              <th scope="col">Department</th>
              <th scope="col">Designation</th>
              <th scope="col">Payment Method</th>
              <th scope="col">Net Salary</th>
              <th scope="col">Status</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(employee, index) in employees" :key="employee.id">
              <td>
                <div class="form-check style-check d-flex align-items-center">
                  <input class="form-check-input" type="checkbox" v-model="employee.selected">
                  <label class="form-check-label">{{ String(index + 1).padStart(2, '0') }}</label>
                </div>
              </td>
              <td><span class="text-primary-600">{{ employee.employeeId }}</span></td>
              <td>
                <div class="d-flex align-items-center">
                  <img :src="employee.avatar" :alt="employee.name + ' Image'" class="flex-shrink-0 me-12 radius-8 w-40-px h-40-px object-fit-cover">
                  <div>
                    <h6 class="text-md mb-0 fw-medium flex-grow-1">{{ employee.name }}</h6>
                  </div>
                </div>
              </td>
              <td>{{ employee.department }}</td>
              <td>{{ employee.designation }}</td>
              <td>{{ employee.paymentMethod }}</td>
              <td>${{ employee.netSalary.toLocaleString() }}</td>
              <td>
                <span :class="getStatusClass(employee.status)">
                  {{ employee.status }}
                </span>
              </td>
              <td>
                <button type="button" class="bg-neutral-200 bg-hover-neutral-300 text-neutral-600 px-20 py-4 radius-4 fw-medium text-sm" @click="viewPayslip(employee)">
                  View Payslip
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from 'vue';

export default {
  name: "PayrollTable",
  emits: ['view-payslip'],
  setup(props, { emit }) {
    const selectAll = ref(false);
    
    const employees = ref([
      { id: 1, employeeId: 'AD52365', name: 'Marvin McKinney', avatar: 'assets/images/thumbs/teacher-avatar-img1.png', department: 'English Department', designation: 'Principal', paymentMethod: 'Bank', netSalary: 5000, status: 'Paid', selected: false },
      { id: 2, employeeId: 'AD52366', name: 'Courtney Henry', avatar: 'assets/images/thumbs/teacher-avatar-img2.png', department: 'Mathematics Department', designation: 'Vice Principal', paymentMethod: 'Cash', netSalary: 4200, status: 'Pending', selected: false },
      { id: 3, employeeId: 'AD52367', name: 'Ralph Edwards', avatar: 'assets/images/thumbs/teacher-avatar-img3.png', department: 'Science Department', designation: 'Lecturer', paymentMethod: 'Bank', netSalary: 3500, status: 'Paid', selected: false },
      { id: 4, employeeId: 'AD52368', name: 'Annette Black', avatar: 'assets/images/thumbs/teacher-avatar-img4.png', department: 'IT Department', designation: 'Software Engineer', paymentMethod: 'Bank', netSalary: 4800, status: 'Paid', selected: false },
      { id: 5, employeeId: 'AD52369', name: 'Theresa Webb', avatar: 'assets/images/thumbs/teacher-avatar-img5.png', department: 'Administration', designation: 'Office Manager', paymentMethod: 'Cheque', netSalary: 3200, status: 'Unpaid', selected: false },
      { id: 6, employeeId: 'AD52370', name: 'Jacob Jones', avatar: 'assets/images/thumbs/teacher-avatar-img6.png', department: 'Finance Department', designation: 'Accountant', paymentMethod: 'Bank', netSalary: 4000, status: 'Paid', selected: false },
      { id: 7, employeeId: 'AD52371', name: 'Kathryn Murphy', avatar: 'assets/images/thumbs/teacher-avatar-img7.png', department: 'Human Resources', designation: 'HR Manager', paymentMethod: 'Bank', netSalary: 4600, status: 'Paid', selected: false },
      { id: 8, employeeId: 'AD52372', name: 'Esther Howard', avatar: 'assets/images/thumbs/teacher-avatar-img8.png', department: 'Marketing Department', designation: 'Marketing Executive', paymentMethod: 'Cash', netSalary: 3700, status: 'Pending', selected: false },
      { id: 9, employeeId: 'AD52373', name: 'Floyd Miles', avatar: 'assets/images/thumbs/teacher-avatar-img9.png', department: 'Library Department', designation: 'Librarian', paymentMethod: 'Cheque', netSalary: 3000, status: 'Unpaid', selected: false },
      { id: 10, employeeId: 'AD52374', name: 'Jane Cooper', avatar: 'assets/images/thumbs/teacher-avatar-img4.png', department: 'Support Department', designation: 'Office Assistant', paymentMethod: 'Cash', netSalary: 2500, status: 'Pending', selected: false },
      { id: 11, employeeId: 'AD52375', name: 'Robert Fox', avatar: 'assets/images/thumbs/teacher-avatar-img1.png', department: 'English Department', designation: 'Teacher', paymentMethod: 'Bank', netSalary: 3800, status: 'Paid', selected: false },
      { id: 12, employeeId: 'AD52376', name: 'Jenny Wilson', avatar: 'assets/images/thumbs/teacher-avatar-img2.png', department: 'Science Department', designation: 'Lab Assistant', paymentMethod: 'Cash', netSalary: 2800, status: 'Paid', selected: false },
      { id: 13, employeeId: 'AD52377', name: 'Devon Lane', avatar: 'assets/images/thumbs/teacher-avatar-img3.png', department: 'Mathematics Department', designation: 'Teacher', paymentMethod: 'Bank', netSalary: 3900, status: 'Pending', selected: false },
      { id: 14, employeeId: 'AD52378', name: 'Cameron Williamson', avatar: 'assets/images/thumbs/teacher-avatar-img4.png', department: 'IT Department', designation: 'IT Support', paymentMethod: 'Bank', netSalary: 3300, status: 'Unpaid', selected: false },
      { id: 15, employeeId: 'AD52379', name: 'Leslie Alexander', avatar: 'assets/images/thumbs/teacher-avatar-img5.png', department: 'Administration', designation: 'Receptionist', paymentMethod: 'Cash', netSalary: 2200, status: 'Paid', selected: false }
    ]);

    const toggleAll = () => {
      const allSelected = employees.value.every(emp => emp.selected);
      employees.value.forEach(emp => {
        emp.selected = !allSelected;
      });
    };

    const getStatusClass = (status) => {
      const classes = {
        'Paid': 'bg-success-100 text-success-600 px-20 py-4 radius-4 fw-medium text-sm',
        'Pending': 'bg-warning-100 text-warning-600 px-20 py-4 radius-4 fw-medium text-sm',
        'Unpaid': 'bg-danger-100 text-danger-600 px-20 py-4 radius-4 fw-medium text-sm'
      };
      return classes[status] || '';
    };

    const viewPayslip = (employee) => {
      emit('view-payslip', employee);
    };

    onMounted(async () => {
      await nextTick();
      if (typeof $ !== 'undefined' && $.fn.DataTable) {
        $('.data-table').each(function () {
          const $table = $(this);

          if ($table.hasClass('dataTable-initialized')) return;

          let tableInstance = $table.DataTable({
            pageLength: 10,
            columnDefs: [{ orderable: false, targets: [0, 8] }] // Disable sorting on first (Checkbox) and last (Action) columns
          });

          $table.addClass('dataTable-initialized');

          // Bind custom search input
          $table.closest('.dataTable-wrapper').find('.dt-search .dt-input').on('keyup', function () {
            tableInstance.search(this.value).draw();
          });

          // Bind custom page length select
          $table.closest('.dataTable-wrapper').find('.dt-length .dt-input').on('change', function () {
            const value = $(this).val();
            tableInstance.page.len(value).draw();
          });
        });
      }
    });

    return {
      selectAll,
      employees,
      toggleAll,
      getStatusClass,
      viewPayslip
    };
  }
}
</script>
