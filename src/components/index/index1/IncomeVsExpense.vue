<template>
  <div class="card h-100">
    <div class="card-body p-0">
      <div
        class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <h6 class="text-lg mb-0">Income Vs Expense </h6>
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
        <ul class="d-flex flex-wrap align-items-center justify-content-center mb-16 gap-3">
          <li class="d-flex align-items-center gap-8">
            <span class="w-12-px h-12-px rounded-circle bg-primary-600"></span>
            <span class="text-secondary-light text-sm fw-semibold">
              Income:
              <span class="text-primary-light fw-bold">$500</span>
            </span>
          </li>
          <li class="d-flex align-items-center gap-8">
            <span class="w-12-px h-12-px rounded-circle bg-warning-600"></span>
            <span class="text-secondary-light text-sm font-semibold">
              Expense:
              <span class="text-primary-light fw-bold"> $300</span>
            </span>
          </li>
        </ul>
        <div id="incomeExpense" ref="chart" class="apexcharts-tooltip-style-1"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "IncomeVsExpense",
  mounted() {
    const color1 = '#16a34a';
    const color2 = '#FF9F29';
    var options = {
      series: [{
        name: 'Income',
        data: [48, 35, 55, 32, 48, 30, 15, 50, 57]
      }, {
        name: 'Expense',
        data: [12, 20, 15, 26, 22, 60, 40, 32, 25]
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
        curve: 'stepline',
        width: 2,
        colors: [color1, color2],
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
          colors: undefined, // takes an array which will be repeated on columns
          opacity: 0.2
        },
        column: {
          colors: undefined,
          opacity: 0.2
        },
        padding: {
          top: -20,
          right: 0,
          bottom: -10,
          left: 0
        },
      },
      colors: [color1, color2],
      markers: {
        colors: [color1, color2],
        strokeWidth: 1,
        size: 0,
        hover: {
          size: 10
        }
      },
      xaxis: {
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
          formatter: function (value) {
            return "$" + value + "k";
          },
          style: {
            fontSize: "14px"
          }
        },
      },
      tooltip: {
        x: {
          format: 'dd/MM/yy HH:mm'
        }
      },
      fill: {
        type: "gradient",
        gradient: {
          shade: "light",
          type: "vertical",
          opacityFrom: 0.4,
          opacityTo: 0.05,
          stops: [0, 100]
        }
      }
    };

    if (window.ApexCharts) {
      var chart = new window.ApexCharts(this.$refs.chart, options);
      chart.render();
    }
  }
}
</script>
