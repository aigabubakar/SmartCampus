<template>
  <div class="card radius-16 border-0 shadow-1 h-100">
    <div class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-16 px-20 border-bottom border-neutral-200">
      <div>
        <h6 class="mb-0 fw-bold text-lg text-neutral-900">Today's Lectures & Labs</h6>
        <span class="text-secondary-light text-xs">Harmattan Semester • Wednesday Lecture Roster</span>
      </div>
      <span class="badge bg-primary-50 text-primary-600 text-xs px-8 py-4 radius-6 fw-semibold">
        4 Sessions Scheduled
      </span>
    </div>

    <div class="card-body p-20">
      <div class="d-flex flex-column max-h-390-px overflow-y-auto scroll-sm pe-8 gap-16">
        
        <!-- Lecture 1 -->
        <div class="p-12 radius-8 border border-neutral-200 d-flex align-items-center justify-content-between gap-12 bg-neutral-50">
          <div class="flex-grow-1">
            <div class="d-flex align-items-center gap-8 mb-4">
              <span class="badge bg-primary-subtle text-primary-700 text-xs px-6 py-2 radius-4 fw-bold">CSC 301</span>
              <h6 class="text-sm mb-0 fw-bold text-neutral-900">Advanced Algorithms & Data Structures</h6>
            </div>
            <div class="d-flex align-items-center gap-12 text-xs text-secondary-light">
              <span class="d-flex align-items-center gap-4">
                <iconify-icon icon="solar:clock-circle-bold" class="text-primary-600"></iconify-icon>
                08:30 AM – 10:00 AM
              </span>
              <span>•</span>
              <span class="d-flex align-items-center gap-4">
                <iconify-icon icon="solar:map-point-bold" class="text-danger-600"></iconify-icon>
                Lecture Theatre 2 (LT-2)
              </span>
              <span>•</span>
              <span>Prof. Finch</span>
            </div>
          </div>
          <span class="badge bg-success-subtle text-success-800 px-10 py-4 radius-6 fw-bold text-xs">Completed</span>
        </div>

        <!-- Lecture 2 -->
        <div class="p-12 radius-8 border border-warning-subtle d-flex align-items-center justify-content-between gap-12 bg-warning-50 bg-opacity-25">
          <div class="flex-grow-1">
            <div class="d-flex align-items-center gap-8 mb-4">
              <span class="badge bg-purple-subtle text-purple-700 text-xs px-6 py-2 radius-4 fw-bold">AI 303</span>
              <h6 class="text-sm mb-0 fw-bold text-neutral-900">Deep Learning & Neural Architectures</h6>
            </div>
            <div class="d-flex align-items-center gap-12 text-xs text-secondary-light">
              <span class="d-flex align-items-center gap-4">
                <iconify-icon icon="solar:clock-circle-bold" class="text-warning-600"></iconify-icon>
                10:15 AM – 12:15 PM
              </span>
              <span>•</span>
              <span class="d-flex align-items-center gap-4">
                <iconify-icon icon="solar:map-point-bold" class="text-danger-600"></iconify-icon>
                AI Systems Lab 3
              </span>
              <span>•</span>
              <span>Dr. Vance</span>
            </div>
          </div>
          <span class="badge bg-warning text-white px-10 py-4 radius-6 fw-bold text-xs">In Progress</span>
        </div>

        <!-- Lecture 3 -->
        <div class="p-12 radius-8 border border-neutral-200 d-flex align-items-center justify-content-between gap-12">
          <div class="flex-grow-1">
            <div class="d-flex align-items-center gap-8 mb-4">
              <span class="badge bg-neutral-200 text-neutral-800 text-xs px-6 py-2 radius-4 fw-bold">ENG 201</span>
              <h6 class="text-sm mb-0 fw-bold text-neutral-900">Engineering Mathematics III</h6>
            </div>
            <div class="d-flex align-items-center gap-12 text-xs text-secondary-light">
              <span class="d-flex align-items-center gap-4">
                <iconify-icon icon="solar:clock-circle-bold" class="text-secondary-light"></iconify-icon>
                01:30 PM – 03:00 PM
              </span>
              <span>•</span>
              <span class="d-flex align-items-center gap-4">
                <iconify-icon icon="solar:map-point-bold" class="text-secondary-light"></iconify-icon>
                Auditorium B
              </span>
              <span>•</span>
              <span>Dr. Steward</span>
            </div>
          </div>
          <span class="badge bg-neutral-100 text-secondary-light px-10 py-4 radius-6 fw-medium text-xs">Upcoming</span>
        </div>

        <!-- Lecture 4 -->
        <div class="p-12 radius-8 border border-neutral-200 d-flex align-items-center justify-content-between gap-12">
          <div class="flex-grow-1">
            <div class="d-flex align-items-center gap-8 mb-4">
              <span class="badge bg-neutral-200 text-neutral-800 text-xs px-6 py-2 radius-4 fw-bold">CSC 305</span>
              <h6 class="text-sm mb-0 fw-bold text-neutral-900">Operating System Internals</h6>
            </div>
            <div class="d-flex align-items-center gap-12 text-xs text-secondary-light">
              <span class="d-flex align-items-center gap-4">
                <iconify-icon icon="solar:clock-circle-bold" class="text-secondary-light"></iconify-icon>
                03:15 PM – 04:45 PM
              </span>
              <span>•</span>
              <span class="d-flex align-items-center gap-4">
                <iconify-icon icon="solar:map-point-bold" class="text-secondary-light"></iconify-icon>
                Computing Hall A
              </span>
              <span>•</span>
              <span>Prof. Webb</span>
            </div>
          </div>
          <span class="badge bg-neutral-100 text-secondary-light px-10 py-4 radius-6 fw-medium text-xs">Upcoming</span>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TodaysClass"
}
</script>
