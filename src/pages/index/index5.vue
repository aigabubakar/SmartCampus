<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navabar />
    
    <div class="dashboard-main-body">
      <Breadcrumb />

      <div class="mt-24">
        <div class="row gy-4">
          
          <!-- Widgets (Stats) -->
          <div class="col-xxl-6">
            <div class="bg-base rounded-3 p-20">
               <StatsWidgets />
            </div>
          </div>

          <!-- Earning Statistic -->
          <div class="col-xxl-6">
            <EarningStatistic />
          </div>

          <!-- Calendar -->
          <div class="col-xxl-5">
            <Calendar />
          </div>

          <!-- Upcoming Sessions -->
          <div class="col-xxl-7">
            <UpcomingSessions />
          </div>

          <!-- User Activity -->
          <div class="col-xl-6 col-xxl-4 col-lg-6">
            <UserActivity />
          </div>

          <!-- Top Student -->
          <div class="col-xxl-4 col-lg-6">
            <TopStudent />
          </div>

          <!-- Top Instructor -->
          <div class="col-xxl-4">
            <TopInstructor />
          </div>

          <!-- Recent Enrolled Courses -->
          <div class="col-xxl-8">
            <RecentEnrolledCourses />
          </div>

          <!-- Course Activity -->
          <div class="col-xxl-4">
            <CourseActivity />
          </div>

        </div>
      </div>
    </div>
    
    <Footer />
  </main>
  
  <ThemeCustomizer />
</template>

<script>
import Sidebar from '@/components/layout/Sidebar.vue';
import Navabar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

// Index 5 Components
import Breadcrumb from '@/components/index/index5/Breadcrumb.vue';
import StatsWidgets from '@/components/index/index5/StatsWidgets.vue';
import EarningStatistic from '@/components/index/index5/EarningStatistic.vue';
import Calendar from '@/components/index/index5/Calendar.vue';
import UpcomingSessions from '@/components/index/index5/UpcomingSessions.vue';
import UserActivity from '@/components/index/index5/UserActivity.vue';
import TopStudent from '@/components/index/index5/TopStudent.vue';
import TopInstructor from '@/components/index/index5/TopInstructor.vue';
import RecentEnrolledCourses from '@/components/index/index5/RecentEnrolledCourses.vue';
import CourseActivity from '@/components/index/index5/CourseActivity.vue';

export default {
  name: "Index5",
  components: {
    Sidebar,
    Navabar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    StatsWidgets,
    EarningStatistic,
    Calendar,
    UpcomingSessions,
    UserActivity,
    TopStudent,
    TopInstructor,
    RecentEnrolledCourses,
    CourseActivity
  }
}
</script>
