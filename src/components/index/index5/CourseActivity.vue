<template>
  <div class="card h-100">
    <div class="card-body">
      <div class="d-flex flex-wrap align-items-center justify-content-between">
        <h6 class="text-lg mb-0">Course Activity</h6>
        <select class="form-select bg-base form-select-sm w-auto radius-8">
          <option>Yearly</option>
          <option>Monthly</option>
          <option>Weekly</option>
          <option>Today</option>
        </select>
      </div>

      <ul class="d-flex flex-wrap align-items-center justify-content-center my-32 gap-3">
        <li class="d-flex align-items-center gap-2">
          <span class="w-12-px h-12-px rounded-circle bg-primary-600"></span>
          <span class="text-secondary-light text-sm">Paid Course:
            <span class="text-primary-light text-md fw-bold line-height-1 ms-4">500</span>
          </span>
        </li>
        <li class="d-flex align-items-center gap-2">
          <span class="w-12-px h-12-px rounded-circle bg-warning-600"></span>
          <span class="text-secondary-light text-sm">Free Course:
            <span class="text-primary-light text-xl fw-bold line-height-1 ms-4">200</span>
          </span>
        </li>
      </ul>
      <div class="margin-16-minus">
        <div id="courseActivityChart" class="apexcharts-tooltip-style-1"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';

export default {
  name: "CourseActivity",
  setup() {
    onMounted(() => {
        var options = {
            series: [{
                name: 'Free Course',
                data: [48, 35, 55, 32, 48, 30, 55, 50, 57]
            }, {
                name: 'Paid Course',
                data: [12, 20, 15, 26, 22, 60, 40, 48, 25]
            }],
            legend: {
                show: false
            },
            chart: {
                type: 'area',
                width: '100%',
                height: 260,
                toolbar: {
                    show: false
                },
                padding: {
                    left: 0,
                    right: 0,
                    top: 0,
                    bottom: 0
                }
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'smooth',
                width: 3,
                colors: ['#487FFF', '#FF9F29'], 
                lineCap: 'round'
            },
            grid: {
                show: true,
                borderColor: '#D1D5DB',
                strokeDashArray: 1,
                position: 'back',
                xaxis: {
                    lines: {
                        show: false
                    }
                },
                yaxis: {
                    lines: {
                        show: true
                    }
                },
                padding: {
                    top: -20,
                    right: 0,
                    bottom: -10,
                    left: 0
                },
            },
            colors: ['#487FFF', '#FF9F29'], // Added explicit colors
            xaxis: {
                labels: {
                    show: false
                },
                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], // Dummy categories
                tooltip: {
                    enabled: false
                }
            },
            yaxis: {
                labels: {
                    show: true // Show Y axis labels as per screenshot/usual area charts
                }
            },
            tooltip: {
                x: {
                    format: 'dd/MM/yy HH:mm'
                },
            }
        };

        var chart = new ApexCharts(document.querySelector("#courseActivityChart"), options);
        chart.render();
    });
  }
}
</script>
