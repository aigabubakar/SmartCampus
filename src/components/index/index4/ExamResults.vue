<template>
  <div class="card radius-12 border-0">
    <div
      class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-12 px-20 border-bottom border-neutral-200">
      <h6 class="mb-2 fw-bold text-lg">Exam Results</h6>
      <div class="dropdown">
        <button type="button" data-bs-toggle="dropdown" aria-expanded="false">
          <iconify-icon icon="entypo:dots-three-vertical" class="icon text-secondary-light"></iconify-icon>
        </button>
        <ul class="dropdown-menu p-12 border bg-base shadow">
          <li>
            <button type="button"
              class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10"
              data-bs-toggle="modal" data-bs-target="#exampleModalView">
              <iconify-icon icon="hugeicons:view" class="icon text-lg line-height-1"></iconify-icon>
              View
            </button>
          </li>
          <li>
            <button type="button"
              class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10"
              data-bs-toggle="modal" data-bs-target="#exampleModalEdit">
              <iconify-icon icon="lucide:edit" class="icon text-lg line-height-1"></iconify-icon>
              Edit
            </button>
          </li>
          <li>
            <button type="button"
              class="delete-item dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-danger-100 text-hover-danger-600 d-flex align-items-center gap-10"
              data-bs-toggle="modal" data-bs-target="#exampleModalDelete">
              <iconify-icon icon="fluent:delete-24-regular" class="icon text-lg line-height-1"></iconify-icon>
              Delete
            </button>
          </li>
        </ul>
      </div>
    </div>
    <div class="card-body p-0">
      <div class="table-responsive scroll-sm">
        <table class="table bordered-table mb-0 data-table" id="dataTable" data-page-length='10'>
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Exam Name</th>
              <th scope="col">Subject</th>
              <th scope="col">Grade</th>
              <th scope="col">Marks%</th>
              <th scope="col">CGPA</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD52365</span></td>
              <td class="py-10-px">Class Test</td>
              <td class="py-10-px">English</td>
              <td class="py-10-px">A</td>
              <td class="py-10-px">95%</td>
              <td class="py-10-px">4.2</td>
              <td class="py-10-px">
                <span class="bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm">Pass</span>
              </td>
            </tr>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD52365</span></td>
              <td class="py-10-px">First Semester</td>
              <td class="py-10-px">Chemistry </td>
              <td class="py-10-px">A</td>
              <td class="py-10-px">80%</td>
              <td class="py-10-px">3.2</td>
              <td class="py-10-px">
                <span class="bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm">Pass</span>
              </td>
            </tr>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD52365</span></td>
              <td class="py-10-px">Class Test</td>
              <td class="py-10-px">Accounting</td>
              <td class="py-10-px">C</td>
              <td class="py-10-px">60%</td>
              <td class="py-10-px">3.9</td>
              <td class="py-10-px">
                <span class="bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm">Pass</span>
              </td>
            </tr>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD52365</span></td>
              <td class="py-10-px">First Semester</td>
              <td class="py-10-px">Chemistry </td>
              <td class="py-10-px">A</td>
              <td class="py-10-px">80%</td>
              <td class="py-10-px">3.2</td>
              <td class="py-10-px">
                <span class="bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm">Pass</span>
              </td>
            </tr>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD52365</span></td>
              <td class="py-10-px">Class Test</td>
              <td class="py-10-px">English </td>
              <td class="py-10-px">F</td>
              <td class="py-10-px">30%</td>
              <td class="py-10-px">2.5</td>
              <td class="py-10-px">
                <span class="bg-danger-100 text-danger-600 px-24 py-4 radius-4 fw-medium text-sm">Fail</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';

export default {
  name: "ExamResults4",
  setup() {
    onMounted(() => {
        // Initialize DataTable if jQuery is available
        if (typeof $ !== 'undefined' && $.fn.DataTable) {
             $('#dataTable').DataTable({
                 pageLength: 10,
             });
        }
    });
  }
}
</script>
