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
              <th scope="col">Matriculation No</th>
              <th scope="col">Student Name</th>
              <th scope="col">Level & Program</th>
              <th scope="col">Admission Cohort</th>
              <th scope="col">Gender</th>
              <th scope="col">Guardian Contact</th>
              <th scope="col">Academic CGPA</th>
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
                  <img :src="student.image || '/assets/images/thumbs/user-img1.png'" alt="Image" class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0 me-12 radius-8" @error="(e) => e.target.src = '/assets/images/thumbs/user-img1.png'">
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
              <td> <span :class="student.statusClass" class="px-24 py-4 radius-4 fw-medium text-sm">{{ student.status }}</span>
              </td>
              <td>
                <div class="btn-group">
                  <button type="button" class="text-primary-light text-xl" data-bs-toggle="dropdown"
                    data-bs-display="static" aria-expanded="false">
                    <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                    <li>
                      <router-link to="/student-details"
                        class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6">
                        <i class="ri-user-3-line"></i>
                        View Academic Dossier
                      </router-link>
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
                        class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6">
                        <i class="ri-money-dollar-box-line"></i>
                        Collect Fees
                      </button>
                    </li>
                    <li>
                      <button
                        class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6">
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
import { ref, onMounted, nextTick } from 'vue';
import { studentsApi } from '@/services/api.js';
import avatar1 from '@/assets/images/thumbs/avatar-img1.png';
import avatar2 from '@/assets/images/thumbs/avatar-img2.png';
import avatar3 from '@/assets/images/thumbs/avatar-img3.png';
import avatar4 from '@/assets/images/thumbs/avatar-img4.png';
import avatar5 from '@/assets/images/thumbs/avatar-img5.png';
import avatar6 from '@/assets/images/thumbs/avatar-img6.png';
import avatar7 from '@/assets/images/thumbs/avatar-img7.png';

export default {
  name: "StudentTable",
  setup() {
    const avatarList = [avatar1, avatar2, avatar3, avatar4, avatar5, avatar6, avatar7];
    const defaultStudents = [
      {
        id: 1,
        admissionNo: "SCI/2026/0491",
        name: "Ibrahim Abubakar",
        rollNo: "STU-2026-089",
        classInfo: "300 Level • B.Sc Computer Science",
        dob: "2023 Cohort",
        gender: "Male",
        phone: "+234 803 555 0192",
        category: "CGPA: 4.62",
        status: "Active",
        statusClass: "bg-success-100 text-success-600",
        image: avatar1
      },
      {
        id: 2,
        admissionNo: "SCI/2026/0512",
        name: "Chisom Eze",
        rollNo: "STU-2026-090",
        classInfo: "300 Level • B.Sc Computer Science",
        dob: "2023 Cohort",
        gender: "Female",
        phone: "+234 802 334 1120",
        category: "CGPA: 4.15",
        status: "Active",
        statusClass: "bg-success-100 text-success-600",
        image: avatar2
      },
      {
        id: 3,
        admissionNo: "ENG/2026/0104",
        name: "Oluwaseun Adeleke",
        rollNo: "STU-2026-091",
        classInfo: "200 Level • B.Eng Software Engineering",
        dob: "2024 Cohort",
        gender: "Male",
        phone: "+234 814 990 4421",
        category: "CGPA: 3.48",
        status: "Active",
        statusClass: "bg-success-100 text-success-600",
        image: avatar3
      },
      {
        id: 4,
        admissionNo: "SCI/2026/0338",
        name: "Amina Bello",
        rollNo: "STU-2026-092",
        classInfo: "400 Level • B.Sc Information Technology",
        dob: "2022 Cohort",
        gender: "Female",
        phone: "+234 809 111 8872",
        category: "CGPA: 4.88",
        status: "Active",
        statusClass: "bg-success-100 text-success-600",
        image: avatar4
      }
    ];

    const students = ref(defaultStudents);
    const isLoading = ref(false);

    const mapApiStudent = (s, idx) => ({
      id: s.id,
      admissionNo: s.matricNumber || `SCI/2026/049${idx + 1}`,
      name: s.name,
      rollNo: s.userId || `STU-${s.id}`,
      classInfo: s.level && s.program ? `${s.level} • ${s.program}` : "300 Level • B.Sc Computer Science",
      dob: s.admissionYear ? `${s.admissionYear} Cohort` : "2023 Cohort",
      gender: s.gender || "Active Student",
      phone: s.guardianPhone || "+234 803 555 0192",
      category: typeof s.cgpa === "number" ? `CGPA: ${s.cgpa.toFixed(2)}` : "CGPA: 3.80",
      status: s.status || "Active",
      statusClass: s.status === "Suspended" ? "bg-danger-100 text-danger-600" : "bg-success-100 text-success-600",
      image: s.avatar || avatarList[idx % avatarList.length]
    });

    const initDataTable = () => {
      if (typeof $ !== 'undefined') {
        $('.data-table').each(function () {
          const $table = $(this);
          if ($table.hasClass('dataTable-initialized')) return;

          let tableInstance;
          if ($.fn.DataTable) {
            tableInstance = $table.DataTable({
              pageLength: 10,
              columnDefs: [{ orderable: false, targets: [0, 8] }]
            });
            $table.addClass('dataTable-initialized');
          }

          if (tableInstance) {
            $table.closest('.dataTable-wrapper').find('.dt-search .dt-input').on('keyup', function () {
              tableInstance.search(this.value).draw();
            });
            $table.closest('.dataTable-wrapper').find('.dt-length .dt-input').on('change', function () {
              const value = $(this).val();
              tableInstance.page.len(value).draw();
            });
          }
        });
      }
    };

    onMounted(async () => {
      isLoading.value = true;
      try {
        const records = await studentsApi.listStudents();
        if (Array.isArray(records) && records.length > 0) {
          students.value = records.map(mapApiStudent);
        }
      } catch (err) {
        console.warn("Using fallback tertiary student roster:", err);
      } finally {
        isLoading.value = false;
        await nextTick();
        initDataTable();
      }
    });

    return {
      students,
      isLoading
    };
  }
}
</script>
