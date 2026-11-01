<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navabar />
    
    <div class="dashboard-main-body">
      <Breadcrumb />

      <div class="mt-24">
        <!-- Stats Widgets -->
        <StatsWidgets />

        <div class="mt-16">
          <div class="row gy-4">
            <div class="col-xxl-8">
              <div class="row gy-4">
                <!-- Statistics Chart -->
                <div class="col-12">
                  <StatisticsChart />
                </div>

                <!-- Today's Class / Leave Status -->
                <div class="col-md-6">
                  <ParentLeaveStatus />
                </div>

                <!-- Notice Board -->
                <div class="col-md-6">
                  <NoticeBoard />
                </div>

                <!-- Exam Results -->
                <div class="col-12">
                  <ExamResults />
                </div>
              </div>
            </div>

            <div class="col-xxl-4">
              <div class="d-flex flex-column gap-24">
                <!-- My Kids -->
                <MyKids />

                <!-- Upcoming Events -->
                <UpcomingEvents />
              </div>
            </div>
            
          </div>
        </div>
      </div>
    </div>
    
    <Footer />
  </main>
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navabar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';

// Index 4 Components
import Breadcrumb from '@/components/index/index4/Breadcrumb.vue';
import StatsWidgets from '@/components/index/index4/StatsWidgets.vue';
import StatisticsChart from '@/components/index/index4/StatisticsChart.vue';
import ParentLeaveStatus from '@/components/index/index4/ParentLeaveStatus.vue';
import NoticeBoard from '@/components/index/index4/NoticeBoard.vue';
import ExamResults from '@/components/index/index4/ExamResults.vue';
import MyKids from '@/components/index/index4/MyKids.vue';
import UpcomingEvents from '@/components/index/index4/UpcomingEvents.vue';

export default {
  name: "Index4",
  components: {
    Sidebar,
    Navabar,
    Footer,
    Breadcrumb,
    StatsWidgets,
    StatisticsChart,
    ParentLeaveStatus,
    NoticeBoard,
    ExamResults,
    MyKids,
    UpcomingEvents
  }
}
</script>
