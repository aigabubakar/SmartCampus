<template>
  <div class="card h-100">
    <div class="card-body p-0">
      <div
        class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <h6 class="text-lg mb-0">New Admissions</h6>
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
      <div class="p-20">
        <div class="position-relative text-center">
          <div id="newAdmissions" ref="chart" class="y-value-left apexcharts-tooltip-z-none"></div>
          <div class="text-center position-absolute top-50 start-50 translate-middle">
            <h5 class="mb-4">50</h5>
            <span class="text-secondary-light">Total Admissions</span>
          </div>
        </div>
        <ul class="d-flex flex-wrap align-items-center justify-content-center mt-48 gap-24">
          <li class="d-flex align-items-center gap-2">
            <span class="w-12-px h-12-px radius-2 bg-success-600 rotate-45-deg"></span>
            <div class="">
              <span class="text-secondary-light fw-medium">
                English:
                <span class="fw-bold text-primary-light">15</span>
              </span>
            </div>
          </li>
          <li class="d-flex align-items-center gap-2">
            <span class="w-12-px h-12-px radius-2 bg-blue-600 rotate-45-deg"></span>
            <div class="">
              <span class="text-secondary-light fw-medium">
                Math:
                <span class="fw-bold text-primary-light">15</span>
              </span>
            </div>
          </li>
          <li class="d-flex align-items-center gap-2">
            <span class="w-12-px h-12-px radius-2 bg-warning-600 rotate-45-deg"></span>
            <div class="">
              <span class="text-secondary-light fw-medium">
                Biology:
                <span class="fw-bold text-primary-light">5</span>
              </span>
            </div>
          </li>
          <li class="d-flex align-items-center gap-2">
            <span class="w-12-px h-12-px radius-2 bg-primary-600 rotate-45-deg"></span>
            <div class="">
              <span class="text-secondary-light fw-medium">
                Physics:
                <span class="fw-bold text-primary-light">10</span>
              </span>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NewAdmissions",
  mounted() {
    var options = {
      series: [40, 87, 87, 30],
      colors: ['#0A51CE', '#25A194', '#FF7A2C', '#009F5E'],
      labels: ['Health', 'Business', 'Lifestyle', 'Entertainment'],
      legend: {
        show: false
      },
      chart: {
        type: 'donut',
        height: 270,
        sparkline: {
          enabled: true // Remove whitespace
        },
        margin: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        },
        padding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        }
      },
      stroke: {
        width: 2,
      },
      dataLabels: {
        enabled: false
      },
      responsive: [{
        breakpoint: 480,
        options: {
          chart: {
            width: 200
          },
          legend: {
            position: 'bottom'
          }
        }
      }],
    };

    if (window.ApexCharts) {
      var chart = new window.ApexCharts(this.$refs.chart, options);
      chart.render();
    }
  }
}
</script>
