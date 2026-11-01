 <template>
  <div class="card radius-12 border-0 h-100">
    <div
      class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-12 px-20 border-bottom border-neutral-200">
      <h6 class="mb-2 fw-bold text-lg">User activity</h6>
      <select class="form-select bg-base form-select-sm w-auto radius-8">
        <option>Yearly</option>
        <option>Monthly</option>
        <option>Weekly</option>
        <option>Today</option>
      </select>
    </div>
    <div class="card-body py-24 d-flex flex-column justify-content-center">
      <div class="d-flex align-items-center gap-20 flex-sm-nowrap flex-wrap">
        <div class="d-flex flex-column gap-12">
          <div class="d-flex align-items-start gap-12">
            <div class="">
              <span class="w-16-px h-16-px bg-primary-600 radius-4 position-relative mt-6"></span>
            </div>
            <div class="">
              <p class="text-secondary-light text-md mb-0">Organic Search</p>
              <h6 class="mb-0 text-lg">875</h6>
            </div>
          </div>
          <div class="d-flex align-items-start gap-12">
            <div class="">
              <span class="w-16-px h-16-px bg-warning-600 radius-4 position-relative mt-6"></span>
            </div>
            <div class="">
              <p class="text-secondary-light text-md mb-0">Referrals</p>
              <h6 class="mb-0 text-lg">350</h6>
            </div>
          </div>
          <div class="d-flex align-items-start gap-12">
            <div class="">
              <span class="w-16-px h-16-px bg-success-main radius-4 position-relative mt-6"></span>
            </div>
            <div class="">
              <p class="text-secondary-light text-md mb-0">Social Media</p>
              <h6 class="mb-0 text-lg">320</h6>
            </div>
          </div>
          <div class="d-flex align-items-start gap-12">
            <div class="">
              <span class="w-16-px h-16-px bg-purple radius-4 position-relative mt-6"></span>
            </div>
            <div class="">
              <p class="text-secondary-light text-md mb-0">Google Search</p>
              <h6 class="mb-0 text-lg">340</h6>
            </div>
          </div>
        </div>
        <div class="">
          <div id="userOverviewDonutChart" class="apexcharts-tooltip-z-none"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';

export default {
  name: "UserActivity",
  setup() {
    onMounted(() => {
      var options = {
        series: [300, 200, 500, 172],
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
              width: 200
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