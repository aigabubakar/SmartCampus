<template>
  <div class="card h-100">
    <div class="card-body p-0 dataTable-wrapper">
      <div
        class="d-flex align-items-center justify-content-between flex-wrap gap-16 px-20 py-12 border-bottom border-neutral-200">
        <div class="d-flex flex-wrap align-items-center gap-16">
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
          <form class="navbar-search dt-search m-0">
            <input type="text" class="dt-input bg-transparent radius-4" aria-controls="dataTable" name="search"
              placeholder="Search...">
            <iconify-icon icon="ion:search-outline" class="icon"></iconify-icon>
          </form>
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

              <form action="#" class="p-16 d-grid grid-cols-2 gap-16">
                <div class="">
                  <label for="class" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
                  <select id="class" class="form-control form-select">
                    <option value="Select" disabled>Select Class</option>
                    <option value="Primary">Primary</option>
                    <option value="SSC">SSC</option>
                    <option value="HSC">HSC</option>
                    <option value="Hons">Hons</option>
                    <option value="Masters">Masters</option>
                  </select>
                </div>
                <div class="">
                  <label for="section" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section</label>
                  <select id="section" class="form-control form-select">
                    <option value="Select">Select Section</option>
                    <option value="Arts">Arts</option>
                    <option value="Science">Science</option>
                    <option value="Commerce">Commerce</option>
                  </select>
                </div>
                <div class="">
                  <label for="gender" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Gender</label>
                  <select id="gender" class="form-control form-select">
                    <option value="Select">Select Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                  </select>
                </div>
                <div class="">
                  <label for="status" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                  <select id="status" class="form-control form-select">
                    <option value="Select">Select Status</option>
                    <option value="Active">Active</option>
                    <option value="Inactive">Inactive</option>
                  </select>
                </div>
                <div class="">
                  <button type="reset" class="btn btn-danger-200 text-danger-600 w-100">Reset</button>
                </div>
                <div class="">
                  <button type="submit" class="btn btn-primary-600 w-100">Apply</button>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div class="d-flex align-items-center gap-8 text-secondary-light">
          <span class="">
            Rows per page:
          </span>
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
        <table class="table bordered-table mb-0 data-table" id="dataTable" data-page-length='10'>
          <thead>
            <tr>
              <th scope="col">
                <div class="form-check style-check d-flex align-items-center">
                  <input class="form-check-input" type="checkbox">
                  <label class="form-check-label">
                    S.L
                  </label>
                </div>
              </th>
              <th scope="col">Admission No</th>
              <th scope="col">Name</th>
              <th scope="col">Class</th>
              <th scope="col">Date of Birth</th>
              <th scope="col">Gender</th>
              <th scope="col">Mobile Number</th>
              <th scope="col">Category</th>
              <th scope="col">Status</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(student, index) in students" :key="index">
              <td>
                <div class="form-check style-check d-flex align-items-center">
                  <input class="form-check-input" type="checkbox">
                  <label class="form-check-label">
                    {{ index < 9 ? `0${index + 1}` : index + 1 }}
                  </label>
                </div>
              </td>
              <td><span class="text-primary-600">{{ student.admissionNo }}</span></td>
              <td>
                <div class="d-flex align-items-center">
                  <img :src="student.image" alt="Image" class="flex-shrink-0 me-12 radius-8">
                  <div class="">
                    <h6 class="text-md mb-0 fw-medium flex-grow-1">{{ student.name }}</h6>
                    <span class="">Roll No: <span class="fw-semibold">{{ student.rollNo }}</span> </span>
                  </div>
                </div>
              </td>
              <td>{{ student.classInfo }}</td>
              <td>{{ student.dob }}</td>
              <td>{{ student.gender }}</td>
              <td>{{ student.phone }}</td>
              <td>{{ student.category }}</td>
              <td> <span class="bg-danger-100 text-danger-600 px-24 py-4 radius-4 fw-medium text-sm">{{ student.status }}</span>
              </td>
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
                        type="button">
                        <i class="ri-user-3-line"></i>
                        View Teacher
                      </button>
                    </li>
                    <li>
                      <router-link to="/edit-student"
                        class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6">
                        <i class="ri-edit-2-line"></i>
                        Edit
                      </router-link>
                    </li>
                    <li>
                      <button
                        class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                        type="button">
                        <i class="ri-money-dollar-box-line"></i>
                        Collect Fees
                      </button>
                    </li>
                    <li>
                      <button
                        class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                        type="button">
                        <i class="ri-error-warning-line"></i>
                        Inactive
                      </button>
                    </li>
                    <li>
                      <button
                        class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                        data-bs-toggle="modal" data-bs-target="#exampleModalDelete"><i
                          class="ri-delete-bin-6-line"></i>Delete</button>
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
</template>

<script>
import { ref, onMounted } from 'vue';
import avatar1 from '@/assets/images/thumbs/avatar-img1.png';
import avatar2 from '@/assets/images/thumbs/avatar-img2.png';
import avatar3 from '@/assets/images/thumbs/avatar-img3.png';
import avatar4 from '@/assets/images/thumbs/avatar-img4.png';
import avatar5 from '@/assets/images/thumbs/avatar-img5.png';
import avatar6 from '@/assets/images/thumbs/avatar-img6.png';
import avatar7 from '@/assets/images/thumbs/avatar-img7.png';

export default {
  name: "SuspendedStudentTable",
  setup() {
    const students = ref([
      {
        id: 1,
        admissionNo: "AD52365",
        name: "Kathryn Murphy",
        rollNo: 12,
        classInfo: "Class 1 (A)",
        dob: "05 May 2012",
        gender: "Male",
        phone: "209.555.0104",
        category: "General",
        status: "Suspend",
        image: avatar1
      },
      {
        id: 2,
        admissionNo: "AD52365",
        name: "Floyd Miles",
        rollNo: 1,
        classInfo: "Class 2 (B)",
        dob: "05 May 2012",
        gender: "Female",
        phone: "209.555.0104",
        category: "Special",
        status: "Suspend",
        image: avatar2
      },
      {
        id: 3,
        admissionNo: "AD52367",
        name: "Cody Fisher",
        rollNo: 7,
        classInfo: "Class 3 (A)",
        dob: "12 Feb 2013",
        gender: "Male",
        phone: "207.445.9821",
        category: "OBC",
        status: "Suspend",
        image: avatar3
      },
      {
        id: 4,
        admissionNo: "AD52368",
        name: "Jane Cooper",
        rollNo: 8,
        classInfo: "Class 4 (C)",
        dob: "17 Mar 2014",
        gender: "Female",
        phone: "204.658.4421",
        category: "Special",
        status: "Suspend",
        image: avatar4
      },
      {
        id: 5,
        admissionNo: "AD52369",
        name: "Esther Howard",
        rollNo: 15,
        classInfo: "Class 5 (B)",
        dob: "25 Jul 2013",
        gender: "Female",
        phone: "209.875.9987",
        category: "General",
        status: "Suspend",
        image: avatar5
      },
      {
        id: 6,
        admissionNo: "AD52370",
        name: "Albert Flores",
        rollNo: 3,
        classInfo: "Class 6 (A)",
        dob: "08 Dec 2011",
        gender: "Male",
        phone: "208.324.1110",
        category: "OBC",
        status: "Suspend",
        image: avatar6
      },
      {
        id: 7,
        admissionNo: "AD52371",
        name: "Jenny Wilson",
        rollNo: 9,
        classInfo: "Class 7 (C)",
        dob: "19 Sep 2010",
        gender: "Female",
        phone: "206.211.4567",
        category: "General",
        status: "Suspend",
        image: avatar7
      },
      {
        id: 8,
        admissionNo: "AD52367",
        name: "Jane Cooper",
        rollNo: 5,
        classInfo: "Class 3 (A)",
        dob: "12 Jan 2013",
        gender: "Female",
        phone: "202.444.0089",
        category: "OBC",
        status: "Suspend",
        image: avatar3
      },
      {
        id: 9,
        admissionNo: "AD52368",
        name: "Cameron Williamson",
        rollNo: 23,
        classInfo: "Class 4 (C)",
        dob: "08 Jul 2011",
        gender: "Male",
        phone: "203.111.0456",
        category: "SC",
        status: "Suspend",
        image: avatar4
      },
      {
        id: 10,
        admissionNo: "AD52369",
        name: "Theresa Webb",
        rollNo: 10,
        classInfo: "Class 5 (A)",
        dob: "18 Nov 2010",
        gender: "Female",
        phone: "205.777.0190",
        category: "General",
        status: "Suspend",
        image: avatar5
      },
      {
        id: 11,
        admissionNo: "AD52370",
        name: "Marvin McKinney",
        rollNo: 7,
        classInfo: "Class 6 (B)",
        dob: "21 Mar 2011",
        gender: "Male",
        phone: "209.660.0912",
        category: "General",
        status: "Suspend",
        image: avatar6
      },
      {
        id: 12,
        admissionNo: "AD52371",
        name: "Courtney Henry",
        rollNo: 15,
        classInfo: "Class 7 (A)",
        dob: "10 Feb 2009",
        gender: "Female",
        phone: "204.120.0023",
        category: "OBC",
        status: "Suspend",
        image: avatar7
      }
    ]);

    onMounted(() => {
      // Data Table
      if (typeof $ !== 'undefined') {
        $('.data-table').each(function () {
          const $table = $(this);
          
          if ($table.hasClass('dataTable-initialized')) return; // Prevent re-init

          let tableInstance;
          if ($.fn.DataTable) {
               tableInstance = $table.DataTable({
                   pageLength: 10,
                   columnDefs: [{ orderable: false, targets: [0, 9] }] // Disable sorting on checkbox and action columns
               });
               $table.addClass('dataTable-initialized');
          }

          if (tableInstance) {
            // Handle search input (inside same wrapper)
            $table.closest('.dataTable-wrapper').find('.dt-search .dt-input').on('keyup', function () {
              tableInstance.search(this.value).draw();
            });

            // Handle page length change (inside same wrapper)
            $table.closest('.dataTable-wrapper').find('.dt-length .dt-input').on('change', function () {
              const value = $(this).val();
              tableInstance.page.len(value).draw();
            });
          }
        });
      }
    });

    return {
      students
    };
  }
}
</script>
