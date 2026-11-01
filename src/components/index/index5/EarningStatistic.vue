  <template>
  <div class="card h-100">
    <div class="card-body">
      <div class="d-flex flex-wrap align-items-center justify-content-between">
        <h6 class="text-lg mb-0">Earning Statistic</h6>
        <select class="form-select bg-base form-select-sm w-auto radius-8">
          <option>Yearly</option>
          <option>Monthly</option>
          <option>Weekly</option>
          <option>Today</option>
        </select>
      </div>
      <div class="d-flex flex-wrap align-items-center gap-2 mt-8">
        <h6 class="mb-0">$27,200</h6>
        <span
          class="text-sm fw-semibold rounded-pill bg-success-focus text-success-main border br-success px-8 py-4 line-height-1 d-flex align-items-center gap-1">
          10% <iconify-icon icon="bxs:up-arrow" class="text-xs"></iconify-icon>
        </span>
        <span class="text-xs fw-medium">+ $1500 Per Day</span>
      </div>
      <div id="earningStatistic" class=" pt-28 apexcharts-tooltip-style-1"></div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';

export default {
  name: "EarningStatistic",
  setup() {
    onMounted(() => {
      var options = {
        series: [
          {
            name: 'Actual',
            data: [
              {
                x: 'Jan',
                y: 100,
                goals: [
                  {
                    name: 'Expected',
                    value: 103,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Feb',
                y: 452,
                goals: [
                  {
                    name: 'Expected',
                    value: 455,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Mar',
                y: 303,
                goals: [
                  {
                    name: 'Expected',
                    value: 306,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Apr',
                y: 503,
                goals: [
                  {
                    name: 'Expected',
                    value: 506,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'May',
                y: 93,
                goals: [
                  {
                    name: 'Expected',
                    value: 96,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Jun',
                y: 302,
                goals: [
                  {
                    name: 'Expected',
                    value: 305,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Jul',
                y: 452,
                goals: [
                  {
                    name: 'Expected',
                    value: 455,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Aug',
                y: 153,
                goals: [
                  {
                    name: 'Expected',
                    value: 156,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Sep',
                y: 453,
                goals: [
                  {
                    name: 'Expected',
                    value: 456,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Oct',
                y: 103,
                goals: [
                  {
                    name: 'Expected',
                    value: 106,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Nov',
                y: 253,
                goals: [
                  {
                    name: 'Expected',
                    value: 256,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
              {
                x: 'Dec',
                y: 153,
                goals: [
                  {
                    name: 'Expected',
                    value: 156,
                    strokeHeight: 3,
                    strokeColor: '#25A194'
                  }
                ]
              },
            ]
          }
        ],
        chart: {
          height: 280,
          type: 'bar',
          toolbar: {
            show: false
          },
        },
        plotOptions: {
          bar: {
            columnWidth: '100%'
          }
        },
        colors: ['#25A1941F', "#000"],
        dataLabels: {
          enabled: false
        },
        legend: {
          show: false,
          showForSingleSeries: true,
          customLegendItems: ['Actual', 'Expected'],
        }
      };

      var chart = new ApexCharts(document.querySelector("#earningStatistic"), options);
      chart.render();
    });
  }
}
</script>