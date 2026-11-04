<template>
  <div class="card h-100 shadow-1 radius-16 border-0">
    <div class="card-body p-0 d-flex flex-column">
      <div
        class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <div>
          <h6 class="text-lg mb-0 fw-bold text-neutral-900">Upcoming Campus Events</h6>
          <span class="text-secondary-light text-xs">Seminars, Hackathons & Key Deadlines</span>
        </div>
      </div>
      <div class="ps-20 pt-16 pb-16 flex-grow-1">
        <div class="pe-20 d-flex flex-column gap-18 overflow-y-auto max-h-310-px scroll-sm" style="max-height: 310px;">
          
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-purple-600 min-w-0">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-base fw-bold mb-0 text-primary-light">09:00 - 11:30</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">AM</span>
              </div>
              <p class="text-primary-light fw-medium mt-4 mb-2 text-sm text-truncate">
                Annual Hackathon & AI Symposium
              </p>
              <p class="text-xs text-secondary-light mb-0 text-truncate">
                Venue: Faculty of Technology Hub
              </p>
            </div>
            <div class="flex-shrink-0">
              <span class="badge bg-purple-subtle text-purple-800 text-xs px-12 py-6 radius-6 fw-semibold">
                Registered
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-warning-600 min-w-0">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-base fw-bold mb-0 text-primary-light">12:00 - 01:30</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">PM</span>
              </div>
              <p class="text-primary-light fw-medium mt-4 mb-2 text-sm text-truncate">
                Mid-Semester Assessment (CAT-2)
              </p>
              <p class="text-xs text-secondary-light mb-0 text-truncate">
                Venue: Main Examination Hall A
              </p>
            </div>
            <div class="flex-shrink-0">
              <span class="badge bg-warning-subtle text-warning-800 text-xs px-12 py-6 radius-6 fw-semibold">
                Mandatory
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-blue-600 min-w-0">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-base fw-bold mb-0 text-primary-light">02:00 - 03:30</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">PM</span>
              </div>
              <p class="text-primary-light fw-medium mt-4 mb-2 text-sm text-truncate">
                Final Year Project Defense Briefing
              </p>
              <p class="text-xs text-secondary-light mb-0 text-truncate">
                Lead: Dr. Vance, Dept of CS
              </p>
            </div>
            <div class="flex-shrink-0">
              <span class="badge bg-info-subtle text-info-800 text-xs px-12 py-6 radius-6 fw-semibold">
                Academic
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-success-600 min-w-0">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-base fw-bold mb-0 text-primary-light">04:15 - 05:45</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">PM</span>
              </div>
              <p class="text-primary-light fw-medium mt-4 mb-2 text-sm text-truncate">
                Student Union Senate Assembly
              </p>
              <p class="text-xs text-secondary-light mb-0 text-truncate">
                Venue: University Assembly Hall
              </p>
            </div>
            <div class="flex-shrink-0">
              <span class="badge bg-success-subtle text-success-800 text-xs px-12 py-6 radius-6 fw-semibold">
                Open
              </span>
            </div>
          </div>

          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-primary-600 min-w-0">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-base fw-bold mb-0 text-primary-light">10:00 - 02:00</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">PM</span>
              </div>
              <p class="text-primary-light fw-medium mt-4 mb-2 text-sm text-truncate">
                Campus Tech Career & Internship Expo
              </p>
              <p class="text-xs text-secondary-light mb-0 text-truncate">
                Venue: Multipurpose Sports Complex
              </p>
            </div>
            <div class="flex-shrink-0">
              <span class="badge bg-primary-subtle text-primary-800 text-xs px-12 py-6 radius-6 fw-semibold">
                Career
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
  name: "UpcomingEvents"
}
</script>

