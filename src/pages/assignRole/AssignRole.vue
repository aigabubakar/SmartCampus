<template>
  <div v-if="isAuthorized">
    
    <!-- Overlay for sidebars -->
    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300"></div>

    <Sidebar />

    <main class="dashboard-main">
      <Navbar />

      <div class="dashboard-main-body">
        <Breadcrumb />

        <div class="mt-24">
          <!-- Pass roles data to the list component -->
          <AssignRoleList :roles="roles" />
        </div>
      </div>

      <Footer />
    </main>

    <AssignRoleAddSidebar />
    <AssignRoleEditSidebar />

  </div>
</template>

<script>
import { onMounted, nextTick, computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';

// Page Components
import Breadcrumb from '@/components/assignRole/Breadcrumb.vue';
import AssignRoleList from '@/components/assignRole/AssignRoleList.vue';
import AssignRoleAddSidebar from '@/components/assignRole/AssignRoleAddSidebar.vue';
import AssignRoleEditSidebar from '@/components/assignRole/AssignRoleEditSidebar.vue';

export default {
  name: "AssignRole",
  components: {
    Sidebar,
    Navbar,
    Footer,
    Breadcrumb,
    AssignRoleList,
    AssignRoleAddSidebar,
    AssignRoleEditSidebar
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isAuthorized = computed(() => authStore.isSuperAdmin);

    onMounted(() => {
      if (!isAuthorized.value) {
        toastStore.error(
          'Security Interception: Role Assignment is restricted to the Super Administrator.',
          '403 Forbidden'
        );
        router.replace('/403');
      }
    });
    const roles = [
      { date: '05 Jan 2018', roleName: 'Administrator', features: 'User Management, System Settings, Notifications' },
      { date: '12 Mar 2019', roleName: 'Accountant', features: 'Payroll, Ledger Management, Expense Tracking' },
      { date: '22 Jul 2020', roleName: 'Teacher', features: 'Class Management, Attendance, Student Reports' },
      { date: '09 Sep 2017', roleName: 'Librarian', features: 'Book Records, Issue/Return, Fine Collection' },
      { date: '15 Nov 2021', roleName: 'Receptionist', features: 'Visitor Entry, Call Handling, Appointment Scheduling' },
      { date: '10 Dec 2016', roleName: 'HR Manager', features: 'Staff Management, Recruitment, Attendance Control' },
      { date: '03 Apr 2022', roleName: 'IT Support', features: 'Technical Support, Software Maintenance, Network Issues' },
      { date: '18 Jun 2020', roleName: 'Parent', features: 'Student Monitoring, Fee Checking, Communication' },
      { date: '25 Aug 2019', roleName: 'Student', features: 'Online Classes, Exam Portal, Assignments' },
      { date: '14 Oct 2018', roleName: 'Exam Coordinator', features: 'Exam Schedule, Question Papers, Result Publishing' },
    ];

    onMounted(async () => {
      await nextTick();
      if (typeof $ !== 'undefined') {
        // Sidebar JS - Handles opening/closing of Add/Edit sidebars
        // Note: The buttons are in child components (Breadcrumb, AssignRoleList)
        // The sidebars are siblings here.
        
        // Add Sidebar Logic
        $(document).on('click', '.my-sidebar-btn', function () {
            $('.my-sidebar').addClass('active');
            $('.overlay').addClass('active');
        });
        
        $('.close-my-sidebar, .overlay').on('click', function () {
            $('.my-sidebar').removeClass('active');
            $('.overlay').removeClass('active');
            // Ensure theme customizer logic doesn't conflict if it uses overlay
            // $(".theme-customization-sidebar").removeClass("active"); 
        });

        // Edit Sidebar Logic
        // Since buttons might be inside a DataTable which re-renders, use delegated events or re-bind.
        // AssignRoleList initializes DataTable, but we can catch the click at document level
        $(document).on('click', '.edit-sidebar-btn', function () {
            $('.edit-sidebar').addClass('active');
            $('.overlay').addClass('active');
        });
        
        $('.close-edit-sidebar, .overlay').on('click', function () {
            $('.edit-sidebar').removeClass('active');
            $('.overlay').removeClass('active');
        });
      }
    });

    return {
        isAuthorized,
        roles
    };
  }
}
</script>
