<template>
  <div class="card border-0 shadow-1 radius-16 course-slip-container">
    <div class="card-body p-24 p-md-36">
      <!-- Action Toolbar (Hidden during print) -->
      <div class="d-flex align-items-center justify-content-between pb-20 mb-24 border-bottom border-neutral-200 no-print">
        <button 
          type="button" 
          class="btn btn-outline-secondary btn-sm radius-8 d-inline-flex align-items-center gap-6"
          @click="enrollmentStore.activeTab = 'registration'"
        >
          <i class="ri-arrow-left-line"></i> Back to Course Selection
        </button>

        <div class="d-flex align-items-center gap-12">
          <button 
            type="button" 
            class="btn btn-primary btn-sm radius-8 d-inline-flex align-items-center gap-6 px-16 py-8"
            @click="handlePrint"
          >
            <i class="ri-printer-line text-base"></i> Print Official Slip
          </button>
        </div>
      </div>

      <!-- Printable Slip Area -->
      <div id="printableSlip" class="printable-slip">
        <!-- University Header -->
        <div class="text-center pb-20 border-bottom border-neutral-300">
          <img 
            :src="slip?.institution?.crestUrl || '/assets/images/logo-icon.png'" 
            alt="University Crest" 
            class="w-64-px h-64-px object-fit-contain mb-10"
            @error="(e) => e.target.src = '/assets/images/logo-icon.png'"
          />
          <h4 class="text-xl fw-bold text-neutral-900 mb-2 letter-spacing-1 text-uppercase">
            {{ slip?.institution?.name || 'Apex Metropolitan University' }}
          </h4>
          <p class="text-xs text-secondary-light mb-4 text-uppercase fw-semibold">
            Office of the Academic Registrar • Senate Secretariat
          </p>
          <span class="badge bg-neutral-100 text-neutral-800 text-xs px-12 py-4 radius-pill fw-bold">
            OFFICIAL COURSE REGISTRATION SLIP ({{ slip?.institution?.academicSession || '2026/2027' }} - {{ slip?.institution?.semester || 'First Semester' }})
          </span>
        </div>

        <!-- Student Dossier Banner -->
        <div class="mt-20 p-16 radius-12 bg-neutral-50 border border-neutral-200 d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-20">
          <div class="d-flex align-items-center gap-16">
            <img 
              :src="slip?.student?.avatar || '/assets/images/thumbs/user-img1.png'" 
              alt="Student Passport" 
              class="w-64-px h-64-px rounded-circle object-fit-cover border border-neutral-300 shadow-xs flex-shrink-0"
              @error="(e) => e.target.src = '/assets/images/thumbs/user-img1.png'"
            />
            <div>
              <h5 class="text-md fw-bold text-neutral-900 mb-4">{{ slip?.student?.name }}</h5>
              <div class="d-flex flex-wrap align-items-center gap-12 text-xs text-secondary-light">
                <span><strong>Matric No:</strong> <span class="font-monospace text-neutral-900">{{ slip?.student?.matricNumber }}</span></span>
                <span>•</span>
                <span><strong>Program:</strong> {{ slip?.student?.program }}</span>
                <span>•</span>
                <span><strong>Level:</strong> {{ slip?.student?.level }}</span>
              </div>
              <div class="d-flex flex-wrap align-items-center gap-12 text-xs text-secondary-light mt-4">
                <span><strong>Faculty:</strong> {{ slip?.student?.faculty }}</span>
                <span>•</span>
                <span><strong>Department:</strong> {{ slip?.student?.department }}</span>
              </div>
            </div>
          </div>

          <!-- Academic Standing Badge -->
          <div class="text-md-end flex-shrink-0">
            <span class="d-block text-xxs text-secondary-light text-uppercase fw-semibold">Cumulative GPA</span>
            <span class="text-base fw-bold text-success-700 font-monospace">{{ slip?.student?.cgpa?.toFixed(2) }} CGPA</span>
            <span class="badge bg-success-50 text-success-700 border border-success-200 text-xxs px-8 py-2 radius-4 d-block mt-4">
              Senate Enrolled & Cleared
            </span>
          </div>
        </div>

        <!-- Registered Courses Table -->
        <div class="mt-24">
          <div class="table-responsive">
            <table class="table bordered-table mb-0 align-middle">
              <thead class="bg-neutral-100">
                <tr>
                  <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-10">S/N</th>
                  <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-10">Course Code</th>
                  <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-10">Course Title</th>
                  <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-10">Units</th>
                  <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-10">Category</th>
                  <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-10">Level</th>
                  <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-10">Assigned Lecturer</th>
                  <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-10 text-end">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr 
                  v-for="(course, idx) in slip?.courses" 
                  :key="course.code"
                  :class="{ 'bg-danger-50 bg-opacity-25': course.isCarryover }"
                >
                  <td class="text-xs text-secondary-light">{{ idx + 1 < 10 ? '0' + (idx + 1) : idx + 1 }}</td>
                  <td>
                    <span class="fw-bold font-monospace" :class="course.isCarryover ? 'text-danger-700' : 'text-primary-600'">
                      {{ course.code }}
                    </span>
                  </td>
                  <td>
                    <span class="text-xs fw-semibold text-neutral-800">{{ course.title }}</span>
                  </td>
                  <td>
                    <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-8 py-2 radius-4 fw-bold">
                      {{ course.creditUnits }} Units
                    </span>
                  </td>
                  <td>
                    <span 
                      class="badge text-xxs px-8 py-2 radius-4 fw-bold"
                      :class="course.isCarryover ? 'bg-danger-600 text-white' : 'bg-primary-50 text-primary-700'"
                    >
                      {{ course.category }}
                    </span>
                  </td>
                  <td class="text-xs text-secondary-light">{{ course.level }}</td>
                  <td class="text-xs text-secondary-light">{{ course.lecturer || 'Faculty Board' }}</td>
                  <td class="text-end">
                    <span class="badge bg-success-100 text-success-700 text-xxs px-8 py-2 radius-4 fw-bold">
                      <i class="ri-check-line"></i> Registered
                    </span>
                  </td>
                </tr>
              </tbody>
              <tfoot class="bg-neutral-50 fw-bold border-top border-neutral-300">
                <tr>
                  <td colspan="3" class="text-end text-xs text-neutral-800">Summary Totals:</td>
                  <td class="text-xs text-primary-600 font-monospace fs-6">
                    {{ slip?.summary?.totalCreditUnits }} Units
                  </td>
                  <td colspan="4" class="text-xs text-secondary-light">
                    {{ slip?.summary?.carryoverUnits }} Carryover Units • {{ slip?.summary?.coreUnits }} Core Units • {{ slip?.summary?.electiveUnits }} Elective Units ({{ slip?.summary?.totalCourses }} Courses Total)
                  </td>
                </tr>
              </tfoot>
            </table>
          </div>
        </div>

        <!-- Verification Seal & Signatures -->
        <div class="mt-32 pt-20 border-top border-neutral-300">
          <div class="row g-24 align-items-end">
            <!-- Digital Security Token -->
            <div class="col-md-5">
              <div class="p-14 radius-10 bg-neutral-50 border border-neutral-200">
                <div class="d-flex align-items-center gap-10 mb-8">
                  <i class="ri-shield-keyhole-fill text-2xl text-primary-600"></i>
                  <div>
                    <span class="d-block text-xxs text-secondary-light text-uppercase fw-bold">Verification SHA-256 Token</span>
                    <span class="font-monospace text-xs fw-bold text-neutral-900 letter-spacing-1">
                      {{ slip?.verificationToken || 'VERIFIED-AMU-ACADEMIC-SEAL' }}
                    </span>
                  </div>
                </div>
                <p class="text-xxs text-secondary-light mb-0">
                  Digitally sealed by SmartCampus Senate Operations on {{ slip?.generatedAt }}. Valid for examination clearance and transcript accreditation.
                </p>
              </div>
            </div>

            <!-- Signature Lines -->
            <div class="col-md-7">
              <div class="row g-16 text-center">
                <div class="col-4">
                  <div class="border-bottom border-neutral-400 pb-8 mb-4 min-h-40-px d-flex align-items-end justify-content-center">
                    <span class="font-cursive text-xs text-secondary-light">{{ slip?.student?.name }}</span>
                  </div>
                  <span class="text-xxs text-secondary-light text-uppercase fw-semibold d-block">Student Signature</span>
                </div>

                <div class="col-4">
                  <div class="border-bottom border-neutral-400 pb-8 mb-4 min-h-40-px d-flex align-items-end justify-content-center">
                    <span class="font-cursive text-xs text-primary-600">Prof. A. Finch</span>
                  </div>
                  <span class="text-xxs text-secondary-light text-uppercase fw-semibold d-block">Course Adviser</span>
                </div>

                <div class="col-4">
                  <div class="border-bottom border-neutral-400 pb-8 mb-4 min-h-40-px d-flex align-items-end justify-content-center">
                    <span class="font-cursive text-xs text-primary-600">Senate Dean</span>
                  </div>
                  <span class="text-xxs text-secondary-light text-uppercase fw-semibold d-block">Dean of Faculty</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: 'CourseRegistrationSlip',
  setup() {
    const enrollmentStore = useEnrollmentStore();
    const slip = computed(() => enrollmentStore.registrationSlip);

    onMounted(async () => {
      if (!slip.value) {
        await enrollmentStore.fetchSlip();
      }
    });

    const handlePrint = () => {
      window.print();
    };

    return {
      enrollmentStore,
      slip,
      handlePrint
    };
  }
};
</script>

<style scoped>
.font-cursive {
  font-family: 'Brush Script MT', cursive, sans-serif;
}

.min-h-40-px {
  min-height: 40px;
}

@media print {
  .no-print {
    display: none !important;
  }
  .printable-slip {
    padding: 0 !important;
    background: transparent !important;
  }
  body {
    background: white !important;
  }
}
</style>
