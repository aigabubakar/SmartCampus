<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-login-details="openLoginDetails" />

        <div class="mt-24">
          <ProfileCard :employee="employee" @suspend-employee="suspendEmployee" @edit-employee="editEmployee" />

          <!-- Tabs -->
          <div class="my-16">
            <ul class="nav nav-pills bordered-tab mb-3" id="pills-tab" role="tablist">
              <li class="nav-item" role="presentation">
                <button
                  class="nav-link d-flex align-items-center gap-8 text-secondary-light fw-medium text-sm text-hover-primary-600 text-capitalize bg-transparent px-20 py-12 active"
                  id="pills-employeeDetails-tab" data-bs-toggle="pill" data-bs-target="#pills-employeeDetails"
                  type="button" role="tab" aria-controls="pills-employeeDetails" aria-selected="true">
                  <span class="d-flex tab-icon line-height-1 text-md">
                    <i class="ri-group-line"></i>
                  </span>
                  Employee Details
                </button>
              </li>
              <li class="nav-item" role="presentation">
                <button
                  class="nav-link d-flex align-items-center gap-8 text-secondary-light fw-medium text-sm text-hover-primary-600 text-capitalize bg-transparent px-20 py-12"
                  id="pills-attendance-tab" data-bs-toggle="pill" data-bs-target="#pills-attendance"
                  type="button" role="tab" aria-controls="pills-attendance" aria-selected="false">
                  <span class="d-flex tab-icon line-height-1 text-md">
                    <i class="ri-calendar-check-line"></i>
                  </span>
                  Attendance
                </button>
              </li>
              <li class="nav-item" role="presentation">
                <button
                  class="nav-link d-flex align-items-center gap-8 text-secondary-light fw-medium text-sm text-hover-primary-600 text-capitalize bg-transparent px-20 py-12"
                  id="pills-leave-tab" data-bs-toggle="pill" data-bs-target="#pills-leave" type="button"
                  role="tab" aria-controls="pills-leave" aria-selected="false">
                  <span class="d-flex tab-icon line-height-1 text-md">
                    <i class="ri-login-box-line"></i>
                  </span>
                  Leave
                </button>
              </li>
              <li class="nav-item" role="presentation">
                <button
                  class="nav-link d-flex align-items-center gap-8 text-secondary-light fw-medium text-sm text-hover-primary-600 text-capitalize bg-transparent px-20 py-12"
                  id="pills-payroll-tab" data-bs-toggle="pill" data-bs-target="#pills-payroll" type="button"
                  role="tab" aria-controls="pills-payroll" aria-selected="false">
                  <span class="d-flex tab-icon line-height-1 text-md">
                    <i class="ri-money-dollar-box-line"></i>
                  </span>
                  Payroll
                </button>
              </li>
            </ul>

            <div class="tab-content" id="pills-tabContent">
              <!-- Employee Details Tab -->
              <div class="tab-pane fade show active" id="pills-employeeDetails" role="tabpanel"
                aria-labelledby="pills-employeeDetails-tab" tabindex="0">
                <EmployeeDetailsTab :details="employeeDetails" />
              </div>

              <!-- Attendance Tab -->
              <div class="tab-pane fade" id="pills-attendance" role="tabpanel"
                aria-labelledby="pills-attendance-tab" tabindex="0">
                <AttendanceTab :stats="attendanceStats" :attendanceData="attendanceData" />
              </div>

              <!-- Leave Tab -->
              <div class="tab-pane fade" id="pills-leave" role="tabpanel"
                aria-labelledby="pills-leave-tab" tabindex="0">
                <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                  <div class="card-header border-bottom bg-base py-16 px-24">
                    <h6 class="text-lg fw-semibold mb-0">Leave History</h6>
                  </div>
                  <div class="card-body p-20">
                    <p class="text-secondary-light">Leave history will be displayed here.</p>
                  </div>
                </div>
              </div>

              <!-- Payroll Tab -->
              <div class="tab-pane fade" id="pills-payroll" role="tabpanel"
                aria-labelledby="pills-payroll-tab" tabindex="0">
                <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                  <div class="card-header border-bottom bg-base py-16 px-24">
                    <h6 class="text-lg fw-semibold mb-0">Payroll Information</h6>
                  </div>
                  <div class="card-body p-20">
                    <p class="text-secondary-light">Payroll information will be displayed here.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />
  </div>
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/hrm/employeeDetails/Breadcrumb.vue';
import ProfileCard from '@/components/hrm/employeeDetails/ProfileCard.vue';
import EmployeeDetailsTab from '@/components/hrm/employeeDetails/EmployeeDetailsTab.vue';
import AttendanceTab from '@/components/hrm/employeeDetails/AttendanceTab.vue';
import teacherImg from '@/assets/images/thumbs/teacher-details-img.png';

export default {
  name: "EmployeeDetails",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    ProfileCard,
    EmployeeDetailsTab,
    AttendanceTab
  },
  setup() {
    const employee = ref({
      name: 'Marvin McKinney',
      employeeId: 'AD1256589',
      avatar: teacherImg,
      subject: 'Mathematics',
      class: 'Class 6 (2025-26)',
      contractType: 'Permanent',
      shift: 'Morning',
      workLocation: '2nd Floor',
      dateOfBirth: '10 Nov 2006',
      gender: 'Male',
      joinDate: '05 May 2012',
      phone: '789678456',
      email: 'set@example.com',
      status: 'Active'
    });

    const employeeDetails = ref({
      dateOfBirth: '10 Nov 1995',
      maritalStatus: 'Married',
      qualification: 'MBA',
      experience: '7 Years',
      fatherName: 'Ralph Edwards',
      motherName: 'Floyd Miles',
      previousSchool: 'Stuyvesant High School',
      currentSchool: 'Bronx High School of Science',
      currentAddress: '8502 Preston Rd. Inglewood, Maine 98380',
      permanentAddress: '2118 Thornridge Cir. Syracuse, Connecticut 35624',
      bankName: 'Bank of America',
      branch: 'New York',
      ifscCode: '5283209832',
      bloodGroup: 'O+',
      height: '5.2',
      weight: '60kg',
      documents: [
        { name: 'BirthCertificate.pdf' }
      ],
      facebook: 'www.facebook.com',
      linkedin: 'www.linkedin.com',
      instagram: 'www.instagram.com'
    });

    const attendanceStats = ref({
      totalPresent: 227,
      totalAbsent: 70,
      halfDay: 27,
      totalLate: 28,
      totalHoliday: 12
    });

    const attendanceData = ref([
      {
        name: 'Jan',
        days: ['P', 'H', 'A', 'P', 'P', 'P', 'F', 'L', 'H', 'P', 'A', 'P', 'P', 'L', 'H', 'P', 'P', 'P', 'P', 'P', 'F', 'H', 'P', 'P', 'P', 'P', 'P', 'A', 'H', 'P']
      },
      {
        name: 'Feb',
        days: ['P', 'A', 'P', 'H', 'P', 'F', 'P', 'L', 'A', 'H', 'P', 'F', 'P', 'L', 'H', 'A', 'P', 'P', 'H', 'P', 'F', 'P', 'L', 'A', 'H', 'P', 'F', 'P', 'L', 'A']
      },
      {
        name: 'Mar',
        days: ['P', 'A', 'P', 'P', 'F', 'H', 'P', 'L', 'P', 'A', 'P', 'H', 'P', 'L', 'F', 'A', 'P', 'H', 'P', 'P', 'A', 'P', 'L', 'P', 'H', 'P', 'A', 'F', 'H', 'P']
      },
      {
        name: 'Apr',
        days: ['P', 'A', 'P', 'H', 'P', 'F', 'L', 'P', 'H', 'A', 'P', 'P', 'L', 'P', 'F', 'H', 'P', 'A', 'P', 'P', 'H', 'P', 'F', 'L', 'P', 'A', 'P', 'H', 'P', 'H']
      },
      {
        name: 'May',
        days: ['P', 'A', 'P', 'H', 'P', 'F', 'L', 'P', 'H', 'A', 'P', 'P', 'L', 'P', 'F', 'H', 'P', 'A', 'P', 'P', 'H', 'P', 'F', 'L', 'P', 'A', 'P', 'H', 'P', 'P']
      }
    ]);

    const openLoginDetails = () => {
      console.log('Open login details sidebar');
    };

    const suspendEmployee = () => {
      console.log('Suspend employee');
    };

    const editEmployee = () => {
      console.log('Edit employee');
    };

    return {
      employee,
      employeeDetails,
      attendanceStats,
      attendanceData,
      openLoginDetails,
      suspendEmployee,
      editEmployee
    };
  }
}
</script>
