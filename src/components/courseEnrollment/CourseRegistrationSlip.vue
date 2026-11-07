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

          <!-- Academic Standing & Adviser Approval Badges -->
          <div class="text-md-end flex-shrink-0">
            <span class="d-block text-xxs text-secondary-light text-uppercase fw-semibold">Cumulative GPA</span>
            <span class="text-base fw-bold text-success-700 font-monospace mb-4 d-block">{{ slip?.student?.cgpa?.toFixed(2) }} CGPA</span>
            
            <span 
              v-if="slip?.adviserApproval?.isApproved"
              class="badge bg-success-600 text-white text-xxs px-8 py-3 radius-4 d-inline-flex align-items-center gap-4 fw-bold"
            >
              <i class="ri-checkbox-circle-fill"></i> Adviser Approved & Signed
            </span>
            <span 
              v-else-if="slip?.adviserApproval?.isDisapproved"
              class="badge bg-danger-600 text-white text-xxs px-8 py-3 radius-4 d-inline-flex align-items-center gap-4 fw-bold"
            >
              <i class="ri-close-circle-fill"></i> Disapproved • Revision Required
            </span>
            <span 
              v-else
              class="badge bg-warning-500 text-white text-xxs px-8 py-3 radius-4 d-inline-flex align-items-center gap-4 fw-bold"
            >
              <i class="ri-time-fill"></i> Awaiting Adviser Approval
            </span>
          </div>
        </div>

        <!-- Level Adviser Endorsement Remarks (if provided) -->
        <div v-if="slip?.adviserApproval?.adviserRemarks" class="mt-16 p-12 radius-10 bg-neutral-50 border border-neutral-300">
          <div class="d-flex align-items-start gap-8">
            <i class="ri-chat-check-fill text-primary-600 text-base flex-shrink-0 mt-2"></i>
            <div>
              <span class="text-xxs fw-bold text-neutral-800 text-uppercase d-block mb-2">
                Level Adviser Official Remarks:
              </span>
              <p class="text-xs text-neutral-900 mb-0 fst-italic">
                "{{ slip?.adviserApproval?.adviserRemarks }}" — <strong>{{ slip?.adviserApproval?.adviserName || 'Prof. Alistair Finch' }}</strong>
                <span v-if="slip?.adviserApproval?.approvedAt" class="text-secondary-light"> ({{ slip?.adviserApproval?.approvedAt }})</span>
              </p>
            </div>
          </div>
        </div>

        <!-- Senate Underload Concession Seal (Appears when student registered underload) -->
        <div 
          v-if="slip?.underloadConcession?.isUnderload || slip?.summary?.isUnderload" 
          class="mt-16 p-14 radius-10 bg-warning-50 border border-warning-400 d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-12"
        >
          <div class="d-flex align-items-center gap-12">
            <span class="badge bg-warning-600 text-white rounded-circle p-8 flex-shrink-0">
              <i class="ri-shield-user-fill text-base"></i>
            </span>
            <div>
              <div class="d-flex align-items-center gap-8 mb-2">
                <span class="text-xs fw-bold text-warning-900 text-uppercase letter-spacing-1">
                  Senate Underload Concession Approved
                </span>
                <span class="badge bg-neutral-900 text-white font-monospace text-xxs px-6 py-2 radius-4">
                  Ref: {{ slip?.underloadConcession?.concessionReference || 'AMU/SEN/UND-2026/ACAD' }}
                </span>
              </div>
              <p class="text-xxs text-warning-900 mb-0">
                <strong>Justification:</strong> {{ slip?.underloadConcession?.reason || 'Final Year Clearance / Senate Approved Workload Pacing' }}
              </p>
            </div>
          </div>

          <div class="text-md-end flex-shrink-0">
            <span class="badge bg-warning-200 text-warning-900 border border-warning-300 text-xxs px-8 py-4 radius-6 fw-bold">
              Regulation 4.6 Concession Validated
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
                    <span v-if="slip?.summary?.isUnderload || slip?.underloadConcession?.isUnderload" class="text-warning-800 fw-bold ms-4 badge bg-warning-100 border border-warning-300 text-xxs px-6 py-2 radius-4">
                      <i class="ri-shield-user-fill"></i> Senate Approved Underload Concession
                    </span>
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

                <!-- Level Adviser Signature Column -->
                <div class="col-4">
                  <div class="border-bottom border-neutral-400 pb-8 mb-4 min-h-48-px d-flex flex-column align-items-center justify-content-end">
                    <template v-if="slip?.adviserApproval?.isApproved">
                      <span class="font-cursive text-sm text-primary-600 fw-bold">{{ slip?.adviserApproval?.adviserName || 'Prof. Alistair Finch' }}</span>
                      <span class="badge bg-success-100 text-success-700 border border-success-300 text-xxs px-4 py-1 radius-4 mt-2">
                        <i class="ri-checkbox-circle-fill"></i> Endorsed & Signed
                      </span>
                    </template>
                    <template v-else-if="slip?.adviserApproval?.isDisapproved">
                      <span class="badge bg-danger-100 text-danger-700 border border-danger-300 text-xxs px-4 py-2 radius-4">
                        <i class="ri-close-circle-fill"></i> Revision Required
                      </span>
                    </template>
                    <template v-else>
                      <span class="badge bg-warning-50 text-warning-700 border border-warning-200 text-xxs px-4 py-1 radius-4">
                        <i class="ri-time-line"></i> Awaiting Review
                      </span>
                    </template>
                  </div>
                  <span class="text-xxs text-secondary-light text-uppercase fw-semibold d-block">
                    {{ slip?.adviserApproval?.adviserTitle || 'Course Adviser' }}
                  </span>
                  <span v-if="slip?.adviserApproval?.approvedAt && slip?.adviserApproval?.isApproved" class="text-xxs text-neutral-400 font-monospace d-block">
                    {{ slip?.adviserApproval?.approvedAt.split(' - ')[0] }}
                  </span>
                </div>

                <!-- Dean of Faculty Column -->
                <div class="col-4">
                  <div class="border-bottom border-neutral-400 pb-8 mb-4 min-h-48-px d-flex flex-column align-items-center justify-content-end">
                    <template v-if="slip?.adviserApproval?.isApproved">
                      <span class="font-cursive text-sm text-primary-600 fw-bold">Prof. E. Vance</span>
                      <span class="badge bg-primary-50 text-primary-700 border border-primary-200 text-xxs px-4 py-1 radius-4 mt-2">
                        <i class="ri-award-fill"></i> Faculty Dean Seal
                      </span>
                    </template>
                    <template v-else>
                      <span class="text-xxs text-neutral-400 fst-italic">Pending Adviser Sign-off</span>
                    </template>
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
