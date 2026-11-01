<template>
  <div class="card radius-12 border-0">
    <div
      class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-12 px-20 border-bottom border-neutral-200">
      <h6 class="mb-2 fw-bold text-lg">Student Marks</h6>
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
              <iconify-icon icon="fluent:delete-24-regular"
                class="icon text-lg line-height-1"></iconify-icon>
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
              <th scope="col">Admission No</th>
              <th scope="col">Name</th>
              <th scope="col">Class</th>
              <th scope="col">Marks%</th>
              <th scope="col">CGPA</th>
              <th scope="col">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD45231</span></td>
              <td class="py-10-px">
                <div class="d-flex align-items-center">
                  <img src="/assets/images/thumbs/avatar-img2.png" alt="Image"
                    class="flex-shrink-0 me-12 radius-8">
                  <div>
                    <h6 class="text-md mb-0 fw-medium">Wade Warren</h6>
                    <span>Roll No: <span class="fw-semibold">08</span></span>
                  </div>
                </div>
              </td>
              <td class="py-10-px">Class 2 (B)</td>
              <td class="py-10-px">88%</td>
              <td class="py-10-px">3.9</td>
              <td class="py-10-px">
                <span class="bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm">Pass</span>
              </td>
            </tr>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD67452</span></td>
              <td class="py-10-px">
                <div class="d-flex align-items-center">
                  <img src="/assets/images/thumbs/avatar-img3.png" alt="Image"
                    class="flex-shrink-0 me-12 radius-8">
                  <div>
                    <h6 class="text-md mb-0 fw-medium">Brooklyn Simmons</h6>
                    <span>Roll No: <span class="fw-semibold">15</span></span>
                  </div>
                </div>
              </td>
              <td class="py-10-px">Class 3 (A)</td>
              <td class="py-10-px">72%</td>
              <td class="py-10-px">3.1</td>
              <td class="py-10-px">
                <span class="bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm">Pass</span>
              </td>
            </tr>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD98214</span></td>
              <td class="py-10-px">
                <div class="d-flex align-items-center">
                  <img src="/assets/images/thumbs/avatar-img4.png" alt="Image"
                    class="flex-shrink-0 me-12 radius-8">
                  <div>
                    <h6 class="text-md mb-0 fw-medium">Darlene Robertson</h6>
                    <span>Roll No: <span class="fw-semibold">20</span></span>
                  </div>
                </div>
              </td>
              <td class="py-10-px">Class 4 (C)</td>
              <td class="py-10-px">54%</td>
              <td class="py-10-px">2.4</td>
              <td class="py-10-px">
                <span class="bg-danger-100 text-danger-600 px-24 py-4 radius-4 fw-medium text-sm">Fail</span>
              </td>
            </tr>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD76133</span></td>
              <td class="py-10-px">
                <div class="d-flex align-items-center">
                  <img src="/assets/images/thumbs/avatar-img5.png" alt="Image"
                    class="flex-shrink-0 me-12 radius-8">
                  <div>
                    <h6 class="text-md mb-0 fw-medium">Theresa Webb</h6>
                    <span>Roll No: <span class="fw-semibold">11</span></span>
                  </div>
                </div>
              </td>
              <td class="py-10-px">Class 5 (A)</td>
              <td class="py-10-px">41%</td>
              <td class="py-10-px">1.9</td>
              <td class="py-10-px">
                <span class="bg-danger-100 text-danger-600 px-24 py-4 radius-4 fw-medium text-sm">Fail</span>
              </td>
            </tr>
            <tr>
              <td class="py-10-px"><span class="text-primary-600">AD33578</span></td>
              <td class="py-10-px">
                <div class="d-flex align-items-center">
                  <img src="/assets/images/thumbs/avatar-img6.png" alt="Image"
                    class="flex-shrink-0 me-12 radius-8">
                  <div>
                    <h6 class="text-md mb-0 fw-medium">Arlene McCoy</h6>
                    <span>Roll No: <span class="fw-semibold">06</span></span>
                  </div>
                </div>
              </td>
              <td class="py-10-px">Class 1 (C)</td>
              <td class="py-10-px">91%</td>
              <td class="py-10-px">4.0</td>
              <td class="py-10-px">
                <span class="bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm">Pass</span>
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
  name: "StudentMarks",
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
