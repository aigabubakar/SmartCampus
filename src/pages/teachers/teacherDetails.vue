<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />

      <div class="mt-24">
        <TeacherHeader />

        <div class="my-16">
          <ul class="nav nav-pills bordered-tab mb-3" role="tablist">
            <li class="nav-item" role="presentation" v-for="tab in tabs" :key="tab.id">
              <button class="nav-link d-flex align-items-center gap-8 text-secondary-light fw-medium text-sm text-hover-primary-600 text-capitalize bg-transparent px-20 py-12"
                :class="{ active: activeTab === tab.id }" @click="activeTab = tab.id" type="button" role="tab">
                <span class="d-flex tab-icon line-height-1 text-md">
                  <i :class="tab.icon"></i>
                </span>
                {{ tab.label }}
              </button>
            </li>
          </ul>

          <div class="tab-content" id="pills-tabContent">
            <div class="tab-pane fade show active" role="tabpanel">
               <component :is="activeTabComponent" />
            </div>
          </div>
        </div>
      </div>

    </div>
    <Footer />
  </main>
  <ThemeCustomizer />
</template>

<script>
import { ref, computed } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/teachers/teacherDetails/Breadcrumb.vue';
import TeacherHeader from '@/components/teachers/teacherDetails/TeacherHeader.vue';
import TeacherDetailsTab from '@/components/teachers/teacherDetails/TeacherDetailsTab.vue';
import ClassRoutineTab from '@/components/teachers/teacherDetails/ClassRoutineTab.vue';

// Placeholders for other tabs
const AttendanceTab = { template: '<div class="card h-100 p-20"><h6>Attendance Content Coming Soon</h6></div>' };
const LeaveTab = { template: '<div class="card h-100 p-20"><h6>Leave Content Coming Soon</h6></div>' };
const PayrollTab = { template: '<div class="card h-100 p-20"><h6>Payroll Content Coming Soon</h6></div>' };
const LibraryTab = { template: '<div class="card h-100 p-20"><h6>Library Content Coming Soon</h6></div>' };

export default {
  name: "TeacherDetails",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    TeacherHeader,
    TeacherDetailsTab,
    ClassRoutineTab,
    AttendanceTab,
    LeaveTab,
    PayrollTab,
    LibraryTab
  },
  setup() {
    const activeTab = ref('teacherDetails');

    const tabs = [
      { id: 'teacherDetails', label: 'Teacher Details', icon: 'ri-group-line' },
      { id: 'classRoutine', label: 'Class Routine', icon: 'ri-file-edit-line' },
      { id: 'attendance', label: 'Attendance', icon: 'ri-calendar-check-line' },
      { id: 'leave', label: 'Leave', icon: 'ri-login-box-line' },
      { id: 'payroll', label: 'Payroll', icon: 'ri-money-dollar-box-line' },
      { id: 'library', label: 'Library', icon: 'ri-book-line' },
    ];

    const activeTabComponent = computed(() => {
      switch (activeTab.value) {
        case 'teacherDetails': return TeacherDetailsTab;
        case 'classRoutine': return ClassRoutineTab;
        case 'attendance': return AttendanceTab;
        case 'leave': return LeaveTab;
        case 'payroll': return PayrollTab;
        case 'library': return LibraryTab;
        default: return TeacherDetailsTab;
      }
    });

    return {
      activeTab,
      tabs,
      activeTabComponent
    };
  }
}
</script>
