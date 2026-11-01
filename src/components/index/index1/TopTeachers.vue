<template>
  <div class="card h-100 shadow-1 radius-12 border-0">
    <div class="card-body p-0">
      <div class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <div>
          <h6 class="text-lg mb-0 fw-bold text-neutral-900">Distinguished Faculty & Chairs</h6>
          <span class="text-secondary-light text-xs">Deans, Research Directors & Department Heads</span>
        </div>
        <router-link to="/teacher-list" class="text-primary-600 text-xs fw-semibold d-flex align-items-center gap-4">
          All Faculty
          <iconify-icon icon="solar:arrow-right-linear"></iconify-icon>
        </router-link>
      </div>

      <div class="ps-20 pt-20 pb-20">
        <div class="pe-20 d-flex flex-column gap-20 max-h-462-px overflow-y-auto scroll-sm">
          
          <div class="d-flex align-items-center justify-content-between gap-16 pb-12 border-bottom border-neutral-100">
            <div class="d-flex align-items-center gap-16">
              <img src="/assets/images/thumbs/top-teacher-img1.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div>
                <h6 class="mb-0 text-sm fw-bold text-neutral-900">Prof. Theresa Webb, PhD</h6>
                <span class="text-secondary-light text-xs mb-0">Dean, Faculty of Computing & AI</span>
              </div>
            </div>
            <div class="text-end">
              <span class="badge bg-primary-50 text-primary-600 text-xs px-8 py-4 radius-6 fw-semibold">
                AI Research Chair
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center justify-content-between gap-16 pb-12 border-bottom border-neutral-100">
            <div class="d-flex align-items-center gap-16">
              <img src="/assets/images/thumbs/top-teacher-img2.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div>
                <h6 class="mb-0 text-sm fw-bold text-neutral-900">Dr. Darrell Steward, DSc</h6>
                <span class="text-secondary-light text-xs mb-0">HOD, Mechatronics Engineering</span>
              </div>
            </div>
            <div class="text-end">
              <span class="badge bg-warning-50 text-warning-700 text-xs px-8 py-4 radius-6 fw-semibold">
                Robotics Lab Lead
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center justify-content-between gap-16 pb-12 border-bottom border-neutral-100">
            <div class="d-flex align-items-center gap-16">
              <img src="/assets/images/thumbs/top-teacher-img3.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div>
                <h6 class="mb-0 text-sm fw-bold text-neutral-900">Prof. Jane Cooper, SAN</h6>
                <span class="text-secondary-light text-xs mb-0">Dean, Faculty of Law</span>
              </div>
            </div>
            <div class="text-end">
              <span class="badge bg-purple-50 text-purple-600 text-xs px-8 py-4 radius-6 fw-semibold">
                Constitutional Law
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center justify-content-between gap-16 pb-12 border-bottom border-neutral-100">
            <div class="d-flex align-items-center gap-16">
              <img src="/assets/images/thumbs/top-teacher-img4.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div>
                <h6 class="mb-0 text-sm fw-bold text-neutral-900">Dr. Savannah Nguyen, MD</h6>
                <span class="text-secondary-light text-xs mb-0">Chair, Clinical Pathology</span>
              </div>
            </div>
            <div class="text-end">
              <span class="badge bg-success-50 text-success-700 text-xs px-8 py-4 radius-6 fw-semibold">
                Medical Sciences
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="d-flex align-items-center gap-16">
              <img src="/assets/images/thumbs/top-teacher-img5.png" alt="Thumbnail"
                class="w-40-px h-40-px rounded-circle object-fit-cover flex-shrink-0">
              <div>
                <h6 class="mb-0 text-sm fw-bold text-neutral-900">Prof. Eleanor Pena, PhD</h6>
                <span class="text-secondary-light text-xs mb-0">Director, Central Innovation Hub</span>
              </div>
            </div>
            <div class="text-end">
              <span class="badge bg-cyan-50 text-cyan-700 text-xs px-8 py-4 radius-6 fw-semibold">
                Tech Transfer
              </span>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopTeachers"
}
</script>
