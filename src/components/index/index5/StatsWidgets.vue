<template>
  <div class="row g-3">
    <div class="col-sm-6">
      <div class="border rounded-3">
        <div class="px-16 py-12 d-flex gap-8 align-items-center">
          <span
            class="d-flex align-items-center justify-content-center w-32-px h-32-px rounded-circle bg-primary-100">
            <img src="/assets/images/icons/lms-icon-1.png" alt="Icon">
          </span>
          <span class="text-primary-light fw-medium">Enrolled Courses</span>
        </div>
        <div class="position-relative z-1">
          <img src="/assets/images/icons/lms-card-gradient-bg1.png"
            class="position-absolute w-100 h-100 z-n1 object-fit-cover lms-card-gradient-bg" alt="Gradient BG">
          <div class="px-16 py-12 d-flex align-items-center justify-content-between gap-12 flex-wrap">
            <div class="">
              <h6 class="mb-6">500</h6>
              <span class="fw-medium text-success-600 text-md d-flex gap-6 align-items-center">
                <i class="text-lg line-height-1 fw-medium ri-arrow-left-up-line"></i>
                43,9%
              </span>
              <span class="text-secondary-light fw-medium mt-6 d-block">From last month</span>
            </div>
            <div class="">
              <div id="enrolledCourses" class="remove-tooltip-title rounded-tooltip-value"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-sm-6">
      <div class="border rounded-3">
        <div class="px-16 py-12 d-flex gap-8 align-items-center">
          <span
            class="d-flex align-items-center justify-content-center w-32-px h-32-px rounded-circle bg-purple-100">
            <img src="/assets/images/icons/lms-icon-2.png" alt="Icon">
          </span>
          <span class="text-primary-light fw-medium">Total Students</span>
        </div>
        <div class="position-relative z-1">
          <img src="/assets/images/icons/lms-card-gradient-bg2.png"
            class="position-absolute w-100 h-100 z-n1 object-fit-cover lms-card-gradient-bg" alt="Gradient BG">
          <div class="px-16 py-12 d-flex align-items-center justify-content-between gap-12 flex-wrap">
            <div class="">
              <h6 class="mb-6">3,570</h6>
              <span class="fw-medium text-success-600 text-md d-flex gap-6 align-items-center">
                <i class="text-lg line-height-1 fw-medium ri-arrow-left-up-line"></i>
                43,9%
              </span>
              <span class="text-secondary-light fw-medium mt-6 d-block">From last month</span>
            </div>
            <div class="">
              <div id="barChart" class="barChart remove-tooltip-title rounded-tooltip-value"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-sm-6">
      <div class="border rounded-3">
        <div class="px-16 py-12 d-flex gap-8 align-items-center">
          <span
            class="d-flex align-items-center justify-content-center w-32-px h-32-px rounded-circle bg-warning-100">
            <img src="/assets/images/icons/lms-icon-3.png" alt="Icon">
          </span>
          <span class="text-primary-light fw-medium">Total Courses</span>
        </div>
        <div class="position-relative z-1">
          <img src="/assets/images/icons/lms-card-gradient-bg3.png"
            class="position-absolute w-100 h-100 z-n1 object-fit-cover lms-card-gradient-bg" alt="Gradient BG">
          <div class="px-16 py-12 d-flex align-items-center justify-content-between gap-12 flex-wrap">
            <div class="">
              <h6 class="mb-6">30</h6>
              <span class="fw-medium text-success-600 text-md d-flex gap-6 align-items-center">
                <i class="text-lg line-height-1 fw-medium ri-arrow-left-up-line"></i>
                43,9%
              </span>
              <span class="text-secondary-light fw-medium mt-6 d-block">From last month</span>
            </div>
            <div class="">
              <div id="barChartTwo" class="barChart remove-tooltip-title rounded-tooltip-value"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-sm-6">
      <div class="border rounded-3">
        <div class="px-16 py-12 d-flex gap-8 align-items-center">
          <span
            class="d-flex align-items-center justify-content-center w-32-px h-32-px rounded-circle bg-success-100">
            <img src="/assets/images/icons/lms-icon-4.png" alt="Icon">
          </span>
          <span class="text-primary-light fw-medium">Total Earnings</span>
        </div>
        <div class="position-relative z-1">
          <img src="/assets/images/icons/lms-card-gradient-bg4.png"
            class="position-absolute w-100 h-100 z-n1 object-fit-cover lms-card-gradient-bg" alt="Gradient BG">
          <div class="px-16 py-12 d-flex align-items-center justify-content-between gap-12 flex-wrap">
            <div class="">
              <h6 class="mb-6">$50,000</h6>
              <span class="fw-medium text-danger-600 text-md d-flex gap-6 align-items-center">
                <i class="text-lg line-height-1 fw-medium ri-arrow-left-down-line"></i>
                20,3%
              </span>
              <span class="text-secondary-light fw-medium mt-6 d-block">From last month</span>
            </div>
            <div class="">
              <div id="totalEarnings" class="remove-tooltip-title rounded-tooltip-value"></div>
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
  name: "StatsWidgets5",
  setup() {
    onMounted(() => {
        // Area Chart
        function createChart(chartId, chartColor, curveClass) {
            let currentYear = new Date().getFullYear();
            var options = {
                series: [
                    {
                        name: 'series1',
                        data: [31, 24, 30, 25, 32, 28, 40, 32, 42, 38, 40, 32, 38, 35, 45],
                    },
                ],
                chart: {
                    type: 'area',
                    width: 150,
                    height: 60,
                    sparkline: {
                        enabled: true // Remove whitespace
                    },
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
                    curve: `${curveClass}`,
                    width: 2,
                    colors: [chartColor],
                    lineCap: 'round'
                },
                grid: {
                    show: true,
                    borderColor: 'transparent',
                    strokeDashArray: 0,
                    position: 'back',
                    xaxis: {
                        lines: {
                            show: false
                        }
                    },
                    yaxis: {
                        lines: {
                            show: false
                        }
                    },
                    padding: {
                        top: -3,
                        right: 0,
                        bottom: 0,
                        left: 0
                    },
                },
                fill: {
                    type: 'gradient',
                    colors: [chartColor],
                    gradient: {
                        shade: 'light',
                        type: 'vertical',
                        shadeIntensity: 0.5,
                        gradientToColors: [`${chartColor}00`],
                        inverseColors: false,
                        opacityFrom: .5,
                        opacityTo: 0.3,
                        stops: [0, 100],
                    },
                },
                markers: {
                    colors: [chartColor],
                    strokeWidth: 2,
                    size: 0,
                    hover: {
                        size: 8
                    }
                },
                xaxis: {
                    labels: {
                        show: false
                    },
                    categories: [`Jan ${currentYear}`, `Feb ${currentYear}`, `Mar ${currentYear}`, `Apr ${currentYear}`, `May ${currentYear}`, `Jun ${currentYear}`, `Jul ${currentYear}`, `Aug ${currentYear}`, `Sep ${currentYear}`, `Oct ${currentYear}`, `Nov ${currentYear}`, `Dec ${currentYear}`],
                    tooltip: {
                        enabled: false,
                    },
                },
                yaxis: {
                    labels: {
                        show: false
                    }
                },
                tooltip: {
                    x: {
                        format: 'dd/MM/yy HH:mm'
                    },
                },
            };
            var chart = new ApexCharts(document.querySelector(`#${chartId}`), options);
            chart.render();
        }

        // Bar Chart
        function createBarChart(barChartId, barChartColor) {
            var options = {
                series: [{
                    name: "Sales",
                    data: [{
                        x: 'Sun',
                        y: 15,
                    }, {
                        x: 'Mon',
                        y: 12,
                    }, {
                        x: 'Tue',
                        y: 18,
                    }, {
                        x: 'Wed',
                        y: 20,
                    }, {
                        x: 'Thu',
                        y: 13,
                    }]
                }],
                chart: {
                    type: 'bar',
                    height: 80,
                    width: 140,
                    sparkline: {
                        enabled: true 
                    },
                    toolbar: {
                        show: false
                    },
                },
                plotOptions: {
                    bar: {
                        borderRadius: 4,
                        horizontal: false,
                        columnWidth: '60%',
                        endingShape: 'rounded',
                    }
                },
                dataLabels: {
                    enabled: false
                },
                fill: {
                    type: 'gradient',
                    colors: [barChartColor],
                    gradient: {
                        shade: 'light',
                        type: 'vertical',
                        shadeIntensity: 0.5,
                        gradientToColors: [barChartColor],
                        inverseColors: false,
                        opacityFrom: 1,
                        opacityTo: 1,
                        stops: [0, 100],
                    },
                },
                grid: {
                    show: false,
                    borderColor: '#D1D5DB',
                    strokeDashArray: 4,
                    position: 'back',
                },
                xaxis: {
                    type: 'category',
                    categories: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu'],
                    labels: { show: false },
                    axisBorder: { show: false },
                    axisTicks: { show: false },
                },
                yaxis: {
                    show: false,
                },
                tooltip: {
                    enabled: true,
                }
            };
            var chart = new ApexCharts(document.querySelector(`#${barChartId}`), options);
            chart.render();
        }

        createChart('enrolledCourses', '#0A51CE', 'smooth');
        createChart('totalEarnings', '#00B252', 'straight');
        createBarChart('barChart', '#8247FF');
        createBarChart('barChartTwo', '#FEAC3B');
    });
  }
}
</script>
