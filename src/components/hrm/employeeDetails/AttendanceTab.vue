<template>
  <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Attendance</h6>
    </div>
    <div class="card-body p-0">
      <!-- Stats Cards -->
      <div class="px-20 pt-20">
        <div class="row row-cols-xxl-5 row-cols-lg-3 row-cols-sm-2 row-cols-1 g-3">
          <div class="col">
            <div class="card px-20 py-28 shadow-2 radius-8 h-100 border border-neutral-200 shadow-none gradient-bg-end-7">
              <div class="card-body p-0">
                <div class="d-flex flex-wrap align-items-center justify-content-between gap-1">
                  <div>
                    <h6 class="fw-semibold mb-2">{{ stats.totalPresent }}</h6>
                    <span class="fw-medium text-secondary-light text-sm">Total Present</span>
                  </div>
                  <span class="mb-0 w-48-px h-48-px bg-success-600 text-white flex-shrink-0 d-flex justify-content-center align-items-center rounded-circle h6 mb-0">
                    <img src="@/assets/images/icons/attendence-icon1.png" alt="Present Icon">
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card px-20 py-28 shadow-2 radius-8 h-100 border border-neutral-200 shadow-none gradient-bg-end-8">
              <div class="card-body p-0">
                <div class="d-flex flex-wrap align-items-center justify-content-between gap-1">
                  <div>
                    <h6 class="fw-semibold mb-2">{{ stats.totalAbsent }}</h6>
                    <span class="fw-medium text-secondary-light text-sm">Total Absent</span>
                  </div>
                  <span class="mb-0 w-48-px h-48-px bg-danger-600 text-white flex-shrink-0 d-flex justify-content-center align-items-center rounded-circle h6 mb-0">
                    <img src="@/assets/images/icons/attendence-icon2.png" alt="Absent Icon">
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card px-20 py-28 shadow-2 radius-8 h-100 border border-neutral-200 shadow-none gradient-bg-end-9">
              <div class="card-body p-0">
                <div class="d-flex flex-wrap align-items-center justify-content-between gap-1">
                  <div>
                    <h6 class="fw-semibold mb-2">{{ stats.halfDay }}</h6>
                    <span class="fw-medium text-secondary-light text-sm">Half Day</span>
                  </div>
                  <span class="mb-0 w-48-px h-48-px bg-purple-600 text-white flex-shrink-0 d-flex justify-content-center align-items-center rounded-circle h6 mb-0">
                    <img src="@/assets/images/icons/attendence-icon3.png" alt="Calendar Icon">
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card px-20 py-28 shadow-2 radius-12 h-100 border border-neutral-200 shadow-none gradient-bg-end-10">
              <div class="card-body p-0">
                <div class="d-flex flex-wrap align-items-center justify-content-between gap-1">
                  <div>
                    <h6 class="fw-semibold mb-2">{{ stats.totalLate }}</h6>
                    <span class="fw-medium text-secondary-light text-sm">Total Late</span>
                  </div>
                  <span class="mb-0 w-48-px h-48-px bg-info-600 text-white flex-shrink-0 d-flex justify-content-center align-items-center rounded-circle h6 mb-0">
                    <img src="@/assets/images/icons/attendence-icon4.png" alt="Clock Icon">
                  </span>
                </div>
              </div>
            </div>
          </div>
          <div class="col">
            <div class="card px-20 py-28 shadow-2 radius-8 h-100 border border-neutral-200 shadow-none gradient-bg-end-11">
              <div class="card-body p-0">
                <div class="d-flex flex-wrap align-items-center justify-content-between gap-1">
                  <div>
                    <h6 class="fw-semibold mb-2">{{ stats.totalHoliday }}</h6>
                    <span class="fw-medium text-secondary-light text-sm">Total Holiday</span>
                  </div>
                  <span class="mb-0 w-48-px h-48-px bg-orange text-white flex-shrink-0 d-flex justify-content-center align-items-center rounded-circle h6 mb-0">
                    <img src="@/assets/images/icons/attendence-icon5.png" alt="Holiday Icon">
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Filters and Legend -->
      <div class="mt-24 mb-16 mx-20">
        <div class="d-flex flex-wrap align-items-center gap-24 justify-content-between flex-wrap">
          <div class="d-flex flex-wrap align-items-center gap-16">
            <div class="">
              <select class="form-control form-select">
                <option value="Jun 2025/2026">Jun 2025/2026</option>
                <option value="Jun 2026/2027">Jun 2026/2027</option>
                <option value="Jun 2027/2028">Jun 2027/2028</option>
                <option value="Jun 2028/2029">Jun 2028/2029</option>
              </select>
            </div>
            <div class="dropdown">
              <button type="button"
                class="px-12 py-8 border border-neutral-300 radius-8 d-flex align-items-center gap-20"
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
          </div>
          <div class="d-flex align-items-center flex-wrap gap-8">
            <p class="text-primary-light text-sm fw-medium mb-0">
              Present: <span class="fw-semibold text-success-600">P</span>
            </p>
            <p class="text-primary-light text-sm fw-medium mb-0">
              Absent: <span class="fw-semibold text-danger-600">A</span>
            </p>
            <p class="text-primary-light text-sm fw-medium mb-0">
              Holiday: <span class="fw-semibold text-warning-600">H</span>
            </p>
            <p class="text-primary-light text-sm fw-medium mb-0">
              Late: <span class="fw-semibold text-info-600">L</span>
            </p>
            <p class="text-primary-light text-sm fw-medium mb-0">
              Half Day: <span class="fw-semibold text-purple-600">F</span>
            </p>
          </div>
        </div>
      </div>

      <!-- Attendance Table -->
      <div class="table-responsive overflow-x-auto">
        <table class="table mb-0 table-heading-dark-mode">
          <thead>
            <tr>
              <th class="bg-neutral-100 text-sm text-primary-light px-10 py-16">Month</th>
              <th v-for="day in 30" :key="day" class="bg-neutral-100 text-sm text-primary-light px-10 py-16">{{ day }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="month in attendanceData" :key="month.name">
              <td class="px-10 py-16 text-sm">{{ month.name }}</td>
              <td v-for="(status, index) in month.days" :key="index" class="px-10 py-14 text-sm text-uppercase">
                <span class="attendance">{{ status }}</span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AttendanceTab",
  props: {
    stats: {
      type: Object,
      default: () => ({
        totalPresent: 227,
        totalAbsent: 70,
        halfDay: 27,
        totalLate: 28,
        totalHoliday: 12
      })
    },
    attendanceData: {
      type: Array,
      default: () => []
    }
  }
}
</script>
