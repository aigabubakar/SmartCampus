<template>
  <div class="card h-100 shadow-1 radius-12 border-0">
    <div class="card-body p-0">
      <div class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <div>
          <h6 class="text-lg mb-0 fw-bold text-neutral-900">Campus Community Demographics</h6>
          <span class="text-secondary-light text-xs">Total Active University Population: 16,282</span>
        </div>
      </div>
      <div class="p-20">
        <div>
          <div class="mt-40 mb-24 pe-110 position-relative max-w-288-px mx-auto">
            <div
              class="w-170-px h-170-px rounded-circle z-1 position-relative d-inline-flex justify-content-center align-items-center">
              <img src="/assets/images/icons/radial-bg1.png" alt="Image"
                class="position-absolute top-0 start-0 z-n1 w-100 h-100 object-fit-cover">
              <div class="text-center">
                <h5 class="text-white mb-0"> 91% </h5>
                <span class="text-white text-xs opacity-75">Students</span>
              </div>
            </div>
            <div
              class="w-144-px h-144-px rounded-circle z-1 position-relative d-inline-flex justify-content-center align-items-center position-absolute top-0 end-0 mt--36">
              <img src="/assets/images/icons/radial-bg2.png" alt="Image"
                class="position-absolute top-0 start-0 z-n1 w-100 h-100 object-fit-cover">
              <div class="text-center">
                <h5 class="text-white mb-0"> 5% </h5>
                <span class="text-white text-xs opacity-75">Faculty</span>
              </div>
            </div>
            <div
              class="w-110-px h-110-px rounded-circle z-1 position-relative d-inline-flex justify-content-center align-items-center position-absolute bottom-0 start-50 translate-middle-x ms-48">
              <img src="/assets/images/icons/radial-bg3.png" alt="Image"
                class="position-absolute top-0 start-0 z-n1 w-100 h-100 object-fit-cover">
              <div class="text-center">
                <h5 class="text-white mb-0"> 4% </h5>
                <span class="text-white text-xs opacity-75">Staff</span>
              </div>
            </div>
          </div>

          <div class="d-flex align-items-center flex-wrap gap-24 justify-content-evenly pt-16 border-top border-neutral-100">
            <div class="d-flex flex-column align-items-start">
              <div class="d-flex align-items-center gap-2">
                <span class="w-12-px h-12-px rounded-pill bg-success-600"></span>
                <span class="text-secondary-light text-sm fw-normal">Undergrad & Postgrad</span>
              </div>
              <h6 class="text-primary-light fw-bold mb-0 mt-4 text-lg">14,820</h6>
            </div>
            <div class="d-flex flex-column align-items-start">
              <div class="d-flex align-items-center gap-2">
                <span class="w-12-px h-12-px rounded-pill bg-warning-600"></span>
                <span class="text-secondary-light text-sm fw-normal">Academic Faculty</span>
              </div>
              <h6 class="text-primary-light fw-bold mb-0 mt-4 text-lg">842</h6>
            </div>
            <div class="d-flex flex-column align-items-start">
              <div class="d-flex align-items-center gap-2">
                <span class="w-12-px h-12-px rounded-pill bg-blue-600"></span>
                <span class="text-secondary-light text-sm fw-normal">Staff & Registry</span>
              </div>
              <h6 class="text-primary-light fw-bold mb-0 mt-4 text-lg">620</h6>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserOverview"
}
</script>
