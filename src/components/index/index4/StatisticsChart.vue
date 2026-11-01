<template>
  <div class="card radius-12 border-0 h-100">
    <div
      class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-12 px-20 border-bottom border-neutral-200">
      <h6 class="mb-2 fw-bold text-lg">Statistic</h6>
      <select class="form-select bg-base form-select-sm w-auto radius-8">
        <option>Yearly</option>
        <option>Monthly</option>
        <option>Weekly</option>
        <option>Today</option>
      </select>
    </div>
    <div class="card-body py-20 d-flex flex-column justify-content-center">
      <ul class="d-flex flex-wrap align-items-center justify-content-center mb-20 gap-3">
        <li class="d-flex align-items-center gap-2">
          <span class="w-12-px h-12-px rounded-circle bg-warning-600"></span>
          <span class="text-secondary-light text-sm">Avg. Attendance:
            <span class="text-primary-light text-xl fw-bold line-height-1 ms-4">200</span>
          </span>
        </li>
        <li class="d-flex align-items-center gap-2">
          <span class="w-12-px h-12-px rounded-circle bg-primary-600"></span>
          <span class="text-secondary-light text-sm">Avg. Exam Score:
            <span class="text-primary-light text-md fw-bold line-height-1 ms-4">500</span>
          </span>
        </li>
      </ul>
      <div id="courseActivityChart" class="apexcharts-tooltip-style-1"></div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';

export default {
  name: "StatisticsChart",
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
                height: 210,
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
                colors: ['#487FFF', '#FF9F29'], // Use two colors for the lines
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
                row: {
                    colors: undefined,
                    opacity: 0.5
                },
                column: {
                    colors: undefined,
                    opacity: 0.5
                },
                padding: {
                    top: -20,
                    right: 0,
                    bottom: -10,
                    left: 0
                },
            },
            colors: ['#487FFF', '#FF9F29'],
            markers: {
                colors: ['#487FFF', '#FF9F29'], // Use two colors for the markers
                strokeWidth: 3,
                size: 0,
                hover: {
                    size: 10
                }
            },
            xaxis: {
                labels: {
                    show: false
                },
                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                tooltip: {
                    enabled: false
                },
                labels: {
                    formatter: function (value) {
                        return value;
                    },
                    style: {
                        fontSize: "14px"
                    }
                }
            },
            yaxis: {
                labels: {
                    style: {
                        fontSize: "14px"
                    }
                },
            },
            tooltip: {
                x: {
                    format: 'dd/MM/yy HH:mm'
                }
            }
        };

        var chart = new ApexCharts(document.querySelector("#courseActivityChart"), options);
        chart.render();
    });
  }
}
</script>
