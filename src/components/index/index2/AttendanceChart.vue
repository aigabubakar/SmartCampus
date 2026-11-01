<template>
  <div class="card radius-12 border-0 h-100">
    <div
      class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-12 px-20 border-bottom border-neutral-200">
      <h6 class="mb-2 fw-bold text-lg">Attendance</h6>
      <select class="form-select bg-base form-select-sm w-auto radius-8">
        <option>Yearly</option>
        <option>Monthly</option>
        <option>Weekly</option>
        <option>Today</option>
      </select>
    </div>
    <div class="card-body py-24">
      <div class=" gap-20">
        <div class="text-center">
          <div id="userOverviewDonutChart" class="apexcharts-tooltip-z-none"></div>
        </div>
        <div class="d-flex gap-12 justify-content-around mt-24">
          <div class="d-flex align-items-start gap-8">
            <span class="w-6-px h-16-px bg-success-500 rounded-pill position-relative mt-8">
            </span>
            <div class="">
              <h6 class="mb-0">200</h6>
              <p class="text-secondary-light text-sm mb-0">Present</p>
            </div>
          </div>
          <div class="d-flex align-items-start gap-8">
            <span class="w-6-px h-16-px bg-info rounded-pill position-relative mt-8">
            </span>
            <div class="">
              <h6 class="mb-0">300</h6>
              <p class="text-secondary-light text-sm mb-0">Half Day </p>
            </div>
          </div>
          <div class="d-flex align-items-start gap-8">
            <span class="w-6-px h-16-px bg-purple rounded-pill position-relative mt-8"></span>
            <div class="">
              <h6 class="mb-0">172</h6>
              <p class="text-secondary-light text-sm mb-0">Late</p>
            </div>
          </div>
          <div class="d-flex align-items-start gap-8">
            <span class="w-6-px h-16-px bg-warning rounded-pill position-relative mt-8"></span>
            <div class="">
              <h6 class="mb-0">500</h6>
              <p class="text-secondary-light text-sm mb-0">Absent</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';

export default {
  name: "AttendanceChart",
  setup() {
    onMounted(() => {
        var options = {
            series: [200, 200, 200, 200],
            colors: ['#487FFF', '#9935FE', '#FF9F29', "#45B369"],
            labels: ['Total Visitors', 'Registrations', 'Total Page Views', 'Registrations'],
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
                width: 0,
            },
            dataLabels: {
                enabled: false
            },
            responsive: [{
                breakpoint: 480,
                options: {
                    chart: {
                        width: 300
                    },
                    legend: {
                        position: 'bottom'
                    }
                }
            }],
        };

        var chart = new ApexCharts(document.querySelector("#userOverviewDonutChart"), options);
        chart.render();
    });
  }
}
</script>
