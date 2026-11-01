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
                <th scope="col">Name</th>
                <th scope="col">Class</th>
                <th scope="col">Certificate Name</th>
                <th scope="col">Background Image</th>
                <th scope="col">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(certificate, index) in certificates" :key="certificate.id">
                <td>
                  <div class="form-check style-check d-flex align-items-center">
                    <input class="form-check-input" type="checkbox" v-model="certificate.selected">
                    <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                  </div>
                </td>
                <td>
                  <div class="d-flex align-items-center flex-grow-1">
                    <img :src="certificate.studentImage" :alt="certificate.studentName"
                      class="flex-shrink-0 me-12 radius-8 w-40-px h-40-px object-fit-cover">
                    <div>
                      <h6 class="text-md mb-0 fw-medium flex-grow-1">{{ certificate.studentName }}</h6>
                      <span>Roll No: <span class="fw-semibold">{{ certificate.rollNo }}</span></span>
                    </div>
                  </div>
                </td>
                <td>{{ certificate.class }}</td>
                <td>{{ certificate.certificateName }}</td>
                <td><img :src="certificate.backgroundImage" alt="Background" class="w-60-px h-40-px object-fit-cover"></td>
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
                          @click="$emit('view-certificate', certificate)">
                          <i class="ri-eye-line"></i>
                          View
                        </button>
                      </li>
                      <li>
                        <button type="button"
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          @click="printCertificate(certificate)">
                          <i class="ri-printer-line"></i>
                          Print
                        </button>
                      </li>
                      <li>
                        <button type="button"
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          @click="$emit('edit-certificate', certificate)">
                          <i class="ri-edit-2-line"></i>
                          Edit
                        </button>
                      </li>
                      <li>
                        <button
                          class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                          type="button" @click="openDeleteModal(certificate)">
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
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this certificate?</h6>
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

import avatar1 from '@/assets/images/thumbs/avatar-img1.png';
import avatar2 from '@/assets/images/thumbs/avatar-img2.png';
import avatar3 from '@/assets/images/thumbs/avatar-img3.png';
import avatar4 from '@/assets/images/thumbs/avatar-img4.png';
import avatar5 from '@/assets/images/thumbs/avatar-img5.png';
import avatar6 from '@/assets/images/thumbs/avatar-img6.png';
import avatar7 from '@/assets/images/thumbs/avatar-img7.png';
import avatar8 from '@/assets/images/thumbs/avatar-img8.png';
import avatar9 from '@/assets/images/thumbs/avatar-img9.png';
import avatar10 from '@/assets/images/thumbs/avatar-img10.png';
import backgroundImage from '@/assets/images/thumbs/background-img.png';

export default {
  name: "CertificateTable",
  emits: ['view-certificate', 'edit-certificate'],
  setup() {
    const deleteId = ref(null);

    const certificates = ref([
      { id: 1, studentName: 'Marvin McKinney', rollNo: 12, class: 'Class 1 (A)', certificateName: 'Transfer Certificate', studentImage: avatar1, backgroundImage: backgroundImage, selected: false },
      { id: 2, studentName: 'Kathryn Murphy', rollNo: 18, class: 'Class 2 (B)', certificateName: 'Character Certificate', studentImage: avatar2, backgroundImage: backgroundImage, selected: false },
      { id: 3, studentName: 'Devon Lane', rollNo: 21, class: 'Class 3 (A)', certificateName: 'Sports Achievement Certificate', studentImage: avatar3, backgroundImage: backgroundImage, selected: false },
      { id: 4, studentName: 'Cody Fisher', rollNo: 9, class: 'Class 4 (C)', certificateName: 'Merit Certificate', studentImage: avatar4, backgroundImage: backgroundImage, selected: false },
      { id: 5, studentName: 'Theresa Webb', rollNo: 15, class: 'Class 5 (B)', certificateName: 'Attendance Certificate', studentImage: avatar5, backgroundImage: backgroundImage, selected: false },
      { id: 6, studentName: 'Darrell Steward', rollNo: 5, class: 'Class 6 (A)', certificateName: 'Scholarship Certificate', studentImage: avatar6, backgroundImage: backgroundImage, selected: false },
      { id: 7, studentName: 'Leslie Alexander', rollNo: 11, class: 'Class 7 (B)', certificateName: 'Excellence Certificate', studentImage: avatar7, backgroundImage: backgroundImage, selected: false },
      { id: 8, studentName: 'Guy Hawkins', rollNo: 17, class: 'Class 8 (A)', certificateName: 'Science Fair Certificate', studentImage: avatar8, backgroundImage: backgroundImage, selected: false },
      { id: 9, studentName: 'Brooklyn Simmons', rollNo: 22, class: 'Class 9 (C)', certificateName: 'Best Student Award', studentImage: avatar9, backgroundImage: backgroundImage, selected: false },
      { id: 10, studentName: 'Kristin Watson', rollNo: 19, class: 'Class 10 (A)', certificateName: 'Completion Certificate', studentImage: avatar10, backgroundImage: backgroundImage, selected: false },
    ]);

    const toggleAll = () => {
      const allSelected = certificates.value.every(cert => cert.selected);
      certificates.value.forEach(cert => {
        cert.selected = !allSelected;
      });
    };

    const openDeleteModal = (certificate) => {
      deleteId.value = certificate.id;
      const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
      modal.show();
    };

    const confirmDelete = () => {
      if (deleteId.value) {
        certificates.value = certificates.value.filter(cert => cert.id !== deleteId.value);
        deleteId.value = null;
      }
    };

    const printCertificate = (certificate) => {
      console.log('Printing certificate for:', certificate.studentName);
      // Implement print functionality
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
      certificates,
      toggleAll,
      openDeleteModal,
      confirmDelete,
      printCertificate
    };
  }
}
</script>
