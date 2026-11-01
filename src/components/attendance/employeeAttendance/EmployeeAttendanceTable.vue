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
                <button type="button" class="d-flex" @click="closeDropdown($event)">
                  <i class="ri-close-large-line"></i>
                </button>
              </div>

              <form class="p-16">
                <div class="row g-3">
                  <div class="col-6">
                    <label for="departments" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Departments</label>
                    <select id="departments" class="form-control form-select">
                        <option value="Principal">Principal</option>
                        <option value="Senior Teacher">Senior Teacher</option>
                        <option value="Subject Teacher">Subject Teacher</option>
                        <option value="Assistant Teacher">Assistant Teacher</option>
                        <option value="Librarian">Librarian</option>
                    </select>
                  </div>
                  <div class="col-6">
                    <label for="designation" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Designation</label>
                    <select id="designation" class="form-control form-select">
                        <option value="English">English</option>
                        <option value="Bangla">Bangla</option>
                        <option value="Math">Mathematics</option>
                        <option value="Physics">Physics</option>
                        <option value="Chemistry">Chemistry</option>
                    </select>
                  </div>
                  <div class="col-12">
                    <label for="date" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Date</label>
                    <input type="date" class="form-control" id="date">
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
                    <input class="form-check-input" type="checkbox" v-model="selectAll" @change="toggleAll">
                    <label class="form-check-label">S.L</label>
                  </div>
                </th>
                <th scope="col">Admission No</th>
                <th scope="col">Name</th>
                <th scope="col">Departments</th>
                <th scope="col">Designation</th>
                <th scope="col">Attendance</th>
                <th scope="col">Note</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(employee, index) in employees" :key="index">
                <td>
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="selectedItems" :value="employee.id">
                    <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                  </div>
                </td>
                <td><span class="text-primary-600">{{ employee.admissionNo }}</span></td>
                <td>
                  <div class="d-flex align-items-center flex-grow-1">
                    <img :src="employee.image" alt="Employee Image" class="flex-shrink-0 me-12 radius-8" width="40" height="40">
                    <div class="">
                      <h6 class="text-md mb-0 fw-medium flex-grow-1">{{ employee.name }}</h6>
                    </div>
                  </div>
                </td>
                <td>{{ employee.department }}</td>
                 <td>{{ employee.designation }}</td>
                <td>
                  <div class="d-flex align-items-center flex-wrap gap-28">
                    <div class="form-check checked-primary d-flex align-items-center gap-2" v-for="type in attendanceTypes" :key="type.value">
                      <input 
                        class="form-check-input" 
                        type="radio" 
                        :name="'attendance_' + employee.id" 
                        :id="'attendance_' + type.value + '_' + employee.id"
                        :value="type.value"
                        v-model="employee.attendance"
                      >
                      <label class="form-check-label" :for="'attendance_' + type.value + '_' + employee.id">{{ type.label }}</label>
                    </div>
                  </div>
                </td>
                <td>
                  <input type="text" class="form-control" placeholder="Write note..." v-model="employee.note">
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from 'vue';

// Import images for mock data (Using teacher avatars if available or student ones as placeholders based on provided HTML snippet reference)
import img1 from '@/assets/images/thumbs/teacher-avatar-img1.png';
import img2 from '@/assets/images/thumbs/teacher-avatar-img2.png';
import img3 from '@/assets/images/thumbs/teacher-avatar-img3.png';
import img4 from '@/assets/images/thumbs/teacher-avatar-img4.png';
import img5 from '@/assets/images/thumbs/teacher-avatar-img5.png';
import img6 from '@/assets/images/thumbs/teacher-avatar-img6.png';
import img7 from '@/assets/images/thumbs/teacher-avatar-img7.png'; // Assuming exists
import img8 from '@/assets/images/thumbs/teacher-avatar-img8.png'; // Assuming exists
import img9 from '@/assets/images/thumbs/teacher-avatar-img9.png'; // Assuming exists


export default {
  name: "EmployeeAttendanceTable",
  setup() {
    const selectAll = ref(false);
    const selectedItems = ref([]);

    const attendanceTypes = [
      { label: 'Present', value: 'present' },
      { label: 'Late', value: 'late' },
      { label: 'Absent', value: 'absent' },
      { label: 'Halfday', value: 'halfday' },
      { label: 'Holiday', value: 'holiday' },
    ];

    const employees = ref([
      { id: 1, admissionNo: 'AD52365', name: 'Marvin McKinney', department: 'Mathematics', designation: 'Principal', image: img1, attendance: '', note: '' },
      { id: 2, admissionNo: 'AD52366', name: 'Cody Fisher', department: 'Physics', designation: 'Senior Teacher', image: img2, attendance: '', note: '' },
      { id: 3, admissionNo: 'AD52367', name: 'Jenny Wilson', department: 'Biology', designation: 'Subject Teacher', image: img3, attendance: '', note: '' },
      { id: 4, admissionNo: 'AD52368', name: 'Guy Hawkins', department: 'English', designation: 'Assistant Teacher', image: img4, attendance: '', note: '' },
      { id: 5, admissionNo: 'AD52369', name: 'Esther Howard', department: 'Math', designation: 'Pre-Primary Teacher', image: img5, attendance: '', note: '' },
      { id: 6, admissionNo: 'AD52370', name: 'Jane Cooper', department: 'Chemistry', designation: 'Librarian', image: img6, attendance: '', note: '' },
      { id: 7, admissionNo: 'AD52371', name: 'Robert Fox', department: 'Biology', designation: 'Lab Assistant', image: img7 || img1, attendance: '', note: '' },
      { id: 8, admissionNo: 'AD52372', name: 'Theresa Webb', department: 'Mathematics', designation: 'Senior Teacher', image: img8 || img2, attendance: '', note: '' },
      { id: 9, admissionNo: 'AD52373', name: 'Courtney Henry', department: 'Physics', designation: 'Senior Teacher', image: img9 || img3, attendance: '', note: '' }, 
      { id: 10, admissionNo: 'AD52374', name: 'Wade Warren', department: 'Biology', designation: 'Subject Teacher', image: img6, attendance: '', note: '' },  // Reusing img6
    ]);

    const toggleAll = () => {
      if (selectAll.value) {
        selectedItems.value = employees.value.map(s => s.id);
      } else {
        selectedItems.value = [];
      }
    };

    const closeDropdown = (event) => {
        const btn = event.target.closest('.dropdown-menu').previousElementSibling;
        if(btn) btn.click();
    };

    onMounted(async () => {
      await nextTick();
      if (typeof $ !== 'undefined' && $.fn.DataTable) {
        $('.data-table').each(function () {
          const $table = $(this);

          if ($table.hasClass('dataTable-initialized')) return;

          let tableInstance = $table.DataTable({
            pageLength: 10,
            columnDefs: [{ orderable: false, targets: [0, 5, 6] }] 
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
      employees,
      selectAll,
      selectedItems,
      attendanceTypes,
      toggleAll,
      closeDropdown
    };
  }
}
</script>
