<template>
  <div class="card h-100 shadow-1 radius-12 border-0">
    <div class="card-body p-0">
      <div class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <div>
          <h6 class="text-lg mb-0 fw-bold text-neutral-900">Lecture & Lab Attendance</h6>
          <span class="text-secondary-light text-xs">75% Minimum Exam Clearance Requirement</span>
        </div>
        <span class="badge bg-success-subtle text-success-700 radius-6 text-xs px-8 py-4 fw-semibold">
          Harmattan Semester
        </span>
      </div>
      <div class="p-20">
        <!-- Progress Bar Segmentation -->
        <div class="progress rounded-pill bg-neutral-200 overflow-hidden" style="height: 14px;">
          <div class="progress-bar bg-primary-600" style="width: 86%;" title="Lecture Attendance: 86%"></div>
          <div class="progress-bar bg-cyan-600" style="width: 8%;" title="Official Academic Leave: 8%"></div>
          <div class="progress-bar bg-danger-600" style="width: 6%;" title="At Risk (<75%): 6%"></div>
        </div>

        <div class="mt-24 d-flex flex-column gap-16">
          <div class="d-flex align-items-center justify-content-between py-4 border-bottom border-neutral-100">
            <div class="d-flex align-items-center gap-8">
              <span class="w-12-px h-12-px rounded-circle bg-primary-600"></span>
              <span class="text-neutral-700 text-sm fw-medium">Regular Lecture Attendance</span>
            </div>
            <span class="fw-bold text-primary-light text-sm">86.2%</span>
          </div>

          <div class="d-flex align-items-center justify-content-between py-4 border-bottom border-neutral-100">
            <div class="d-flex align-items-center gap-8">
              <span class="w-12-px h-12-px rounded-circle bg-cyan-600"></span>
              <span class="text-neutral-700 text-sm fw-medium">Official Approved Leave (Medical / Athletic)</span>
            </div>
            <span class="fw-bold text-primary-light text-sm">8.1%</span>
          </div>

          <div class="d-flex align-items-center justify-content-between py-4 border-bottom border-neutral-100">
            <div class="d-flex align-items-center gap-8">
              <span class="w-12-px h-12-px rounded-circle bg-warning-600"></span>
              <span class="text-neutral-700 text-sm fw-medium">Borderline Compliance (75% - 79%)</span>
            </div>
            <span class="fw-bold text-warning-700 text-sm">3.7%</span>
          </div>

          <div class="d-flex align-items-center justify-content-between py-4">
            <div class="d-flex align-items-center gap-8">
              <span class="w-12-px h-12-px rounded-circle bg-danger-600"></span>
              <span class="text-danger-600 text-sm fw-bold">Critical: Below 75% Disqualification Line</span>
            </div>
            <span class="fw-bold text-danger-600 text-sm">2.0%</span>
          </div>
        </div>

        <!-- Clearance Warning Note -->
        <div class="p-12 radius-8 bg-danger-50 border border-danger-subtle mt-20 d-flex align-items-center gap-10">
          <iconify-icon icon="solar:danger-triangle-bold" class="text-danger-600 text-xl flex-shrink-0"></iconify-icon>
          <p class="text-danger-700 text-xs mb-0">
            <strong>Senate Rule 14.2:</strong> Students below 75% biometric attendance are locked out of digital examination hall pass generation.
          </p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StuAttendees"
}
</script>
