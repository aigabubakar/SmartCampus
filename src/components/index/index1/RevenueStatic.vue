<template>
  <div class="card h-100 shadow-1 radius-12 border-0">
    <div class="card-body p-0">
      <div class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <div>
          <h6 class="text-lg mb-0 fw-bold text-neutral-900">Bursary Revenue & Tuition Inflow</h6>
          <span class="text-secondary-light text-xs">2026/2027 Academic Year • All Faculties</span>
        </div>
        <div class="d-flex align-items-center gap-8">
          <span class="badge bg-success-subtle text-success-700 radius-6 text-xs px-8 py-4 fw-semibold">
            91.4% Collection Rate
          </span>
        </div>
      </div>
      <div class="p-20">
        <ul class="d-flex flex-wrap align-items-center justify-content-center mb-16 gap-4">
          <li class="d-flex align-items-center gap-8">
            <span class="w-12-px h-12-px radius-2 bg-primary-600"></span>
            <span class="text-secondary-light text-sm fw-medium">
              Total Projected:
              <strong class="text-primary-light fw-bold">$4,600,000</strong>
            </span>
          </li>
          <li class="d-flex align-items-center gap-8">
            <span class="w-12-px h-12-px radius-2 bg-warning-600"></span>
            <span class="text-secondary-light text-sm fw-medium">
              Realized Collections:
              <strong class="text-primary-light fw-bold">$4,204,400</strong>
            </span>
          </li>
          <li class="d-flex align-items-center gap-8">
            <span class="w-12-px h-12-px radius-2 bg-danger-600"></span>
            <span class="text-secondary-light text-sm fw-medium">
              Outstanding:
              <strong class="text-danger-600 fw-bold">$395,600</strong>
            </span>
          </li>
        </ul>
        <div id="revenueStatistic" ref="chart"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RevenueStatic",
  mounted() {
    var options = {
      series: [{
        name: 'Projected Billings',
        data: [420, 580, 750, 890, 620, 480, 410, 450]
      }, {
        name: 'Collected Inflow',
        data: [390, 550, 690, 820, 580, 440, 390, 344]
      }],
      chart: {
        type: 'bar',
        height: 250,
        stacked: false,
        toolbar: {
          show: false
        }
      },
      colors: ["#25A194", "#FF9F29"],
      plotOptions: {
        bar: {
          horizontal: false,
          columnWidth: "45%",
          borderRadius: 4
        },
      },
      xaxis: {
        categories: ['Oct (Reg)', 'Nov (Harmattan)', 'Dec (Mid-term)', 'Jan (Exam)', 'Feb (Rain Reg)', 'Mar (Lectures)', 'Apr (Rain CAT)', 'May (Finals)'],
        labels: {
          style: {
            fontSize: '11px'
          }
        }
      },
      yaxis: {
        labels: {
          formatter: function (value) {
            return "$" + value + "k";
          },
          style: {
            fontSize: "12px"
          }
        },
      },
      legend: {
        position: 'top',
        horizontalAlign: 'right',
        fontSize: '12px'
      },
      fill: {
        opacity: 1
      }
    };

    if (window.ApexCharts) {
      var chart = new window.ApexCharts(this.$refs.chart, options);
      chart.render();
    }
  }
}
</script>
