<template>
  <div class="card h-100">
    <div class="card-body p-0">
      <div
        class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <h6 class="text-lg mb-0">Leave Requests</h6>
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
      <div class="ps-20 pt-20 pb-20">
        <div class="pe-20 d-flex flex-column gap-28 max-h-462-px overflow-y-auto scroll-sm">
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="d-flex align-items-start gap-16">
              <img src="/assets/images/thumbs/leave-request-img1.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div class="">
                <h6 class="mb-0 text-lg">Darlene Robertson</h6>
                <span class="text-secondary-light text-sm mb-0">English Teacher</span>
              </div>
            </div>
            <div class="text-end">
              <span class="d-block fw-bold text-primary-light">3 Days</span>
              <p class="text-secondary-light text-sm mb-0">Apply on: 10 April</p>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="d-flex align-items-start gap-16">
              <img src="/assets/images/thumbs/leave-request-img2.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div class="">
                <h6 class="mb-0 text-lg">Esther Howard</h6>
                <span class="text-secondary-light text-sm mb-0">English Teacher</span>
              </div>
            </div>
            <div class="text-end">
              <span class="d-block fw-bold text-primary-light">3 Days</span>
              <p class="text-secondary-light text-sm mb-0">Apply on: 10 April</p>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="d-flex align-items-start gap-16">
              <img src="/assets/images/thumbs/leave-request-img3.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div class="">
                <h6 class="mb-0 text-lg">Kristin Watson</h6>
                <span class="text-secondary-light text-sm mb-0">English Teacher</span>
              </div>
            </div>
            <div class="text-end">
              <span class="d-block fw-bold text-primary-light">3 Days</span>
              <p class="text-secondary-light text-sm mb-0">Apply on: 10 April</p>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="d-flex align-items-start gap-16">
              <img src="/assets/images/thumbs/leave-request-img4.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div class="">
                <h6 class="mb-0 text-lg">Leslie Alexander</h6>
                <span class="text-secondary-light text-sm mb-0">English Teacher</span>
              </div>
            </div>
            <div class="text-end">
              <span class="d-block fw-bold text-primary-light">3 Days</span>
              <p class="text-secondary-light text-sm mb-0">Apply on: 10 April</p>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="d-flex align-items-start gap-16">
              <img src="/assets/images/thumbs/leave-request-img5.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div class="">
                <h6 class="mb-0 text-lg">Dianne Russell</h6>
                <span class="text-secondary-light text-sm mb-0">English Teacher</span>
              </div>
            </div>
            <div class="text-end">
              <span class="d-block fw-bold text-primary-light">3 Days</span>
              <p class="text-secondary-light text-sm mb-0">Apply on: 10 April</p>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="d-flex align-items-start gap-16">
              <img src="/assets/images/thumbs/leave-request-img3.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div class="">
                <h6 class="mb-0 text-lg">Kristin Watson</h6>
                <span class="text-secondary-light text-sm mb-0">English Teacher</span>
              </div>
            </div>
            <div class="text-end">
              <span class="d-block fw-bold text-primary-light">3 Days</span>
              <p class="text-secondary-light text-sm mb-0">Apply on: 10 April</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LeaveRequests"
}
</script>
