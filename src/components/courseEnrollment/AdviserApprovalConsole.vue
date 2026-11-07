<template>
  <div class="adviser-approval-console">
    <!-- 1. Metrics & Overview Cards -->
    <div class="row g-16 mb-24">
      <div class="col-sm-6 col-xl-3">
        <div class="card border-0 shadow-1 radius-12 p-16 bg-base">
          <div class="d-flex align-items-center justify-content-between mb-8">
            <span class="text-xs text-secondary-light text-uppercase fw-semibold">Total Submissions</span>
            <span class="badge bg-primary-50 text-primary-600 rounded-circle p-8">
              <i class="ri-survey-line text-lg"></i>
            </span>
          </div>
          <h4 class="fw-bold text-neutral-900 mb-2">{{ enrollmentStore.adviserSummary?.totalSubmissions || 0 }}</h4>
          <span class="text-xxs text-secondary-light">Harmattan Semester 2026/2027</span>
        </div>
      </div>

      <div class="col-sm-6 col-xl-3">
        <div class="card border-0 shadow-1 radius-12 p-16 bg-base">
          <div class="d-flex align-items-center justify-content-between mb-8">
            <span class="text-xs text-warning-800 text-uppercase fw-semibold">Pending Review</span>
            <span class="badge bg-warning-50 text-warning-600 rounded-circle p-8">
              <i class="ri-time-line text-lg"></i>
            </span>
          </div>
          <h4 class="fw-bold text-warning-700 mb-2">{{ enrollmentStore.adviserSummary?.pendingCount || 0 }}</h4>
          <span class="text-xxs text-warning-700 fw-medium">Requires Adviser Action</span>
        </div>
      </div>

      <div class="col-sm-6 col-xl-3">
        <div class="card border-0 shadow-1 radius-12 p-16 bg-base">
          <div class="d-flex align-items-center justify-content-between mb-8">
            <span class="text-xs text-success-800 text-uppercase fw-semibold">Approved Dockets</span>
            <span class="badge bg-success-50 text-success-600 rounded-circle p-8">
              <i class="ri-checkbox-circle-fill text-lg"></i>
            </span>
          </div>
          <h4 class="fw-bold text-success-700 mb-2">{{ enrollmentStore.adviserSummary?.approvedCount || 0 }}</h4>
          <span class="text-xxs text-success-700 fw-medium">Digitally Signed & Endorsed</span>
        </div>
      </div>

      <div class="col-sm-6 col-xl-3">
        <div class="card border-0 shadow-1 radius-12 p-16 bg-base">
          <div class="d-flex align-items-center justify-content-between mb-8">
            <span class="text-xs text-danger-800 text-uppercase fw-semibold">Revision Required</span>
            <span class="badge bg-danger-50 text-danger-600 rounded-circle p-8">
              <i class="ri-close-circle-line text-lg"></i>
            </span>
          </div>
          <h4 class="fw-bold text-danger-700 mb-2">{{ enrollmentStore.adviserSummary?.disapprovedCount || 0 }}</h4>
          <span class="text-xxs text-danger-700 fw-medium">Sent Back for Corrections</span>
        </div>
      </div>
    </div>

    <!-- 2. Filters & Search Toolbar -->
    <div class="card border-0 shadow-1 radius-16 mb-24">
      <div class="card-body p-16 p-md-20">
        <div class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-16">
          <div class="d-flex flex-wrap align-items-center gap-12 flex-grow-1">
            <!-- Search -->
            <div class="position-relative flex-grow-1" style="max-width: 320px;">
              <input 
                type="text" 
                v-model="enrollmentStore.adviserSearchQuery"
                @input="handleSearch"
                placeholder="Search student or matric number..." 
                class="form-control form-control-sm ps-36 radius-8 text-xs border-neutral-300"
              />
              <i class="ri-search-line position-absolute top-50 start-0 translate-middle-y ms-12 text-secondary-light"></i>
            </div>

            <!-- Level Filter -->
            <select 
              v-model="enrollmentStore.adviserLevelFilter"
              @change="handleFilterChange"
              class="form-select form-select-sm radius-8 text-xs border-neutral-300" 
              style="width: 140px;"
            >
              <option value="All Levels">All Levels</option>
              <option value="100 Level">100 Level</option>
              <option value="200 Level">200 Level</option>
              <option value="300 Level">300 Level</option>
              <option value="400 Level">400 Level</option>
            </select>

            <!-- Status Filter -->
            <select 
              v-model="enrollmentStore.adviserStatusFilter"
              @change="handleFilterChange"
              class="form-select form-select-sm radius-8 text-xs border-neutral-300" 
              style="width: 160px;"
            >
              <option value="All">All Statuses</option>
              <option value="Pending">Pending Review</option>
              <option value="Approved">Approved</option>
              <option value="Disapproved">Disapproved</option>
            </select>
          </div>

          <div class="d-flex align-items-center gap-8 flex-shrink-0">
            <button 
              type="button" 
              class="btn btn-outline-secondary btn-sm radius-8 d-inline-flex align-items-center gap-6 text-xs"
              @click="loadSubmissions"
            >
              <i class="ri-refresh-line"></i> Refresh
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- 3. Submissions Table -->
    <div class="card border-0 shadow-1 radius-16">
      <div class="card-body p-0">
        <div v-if="enrollmentStore.isAdviserLoading" class="text-center py-48">
          <div class="spinner-border text-primary-600 mb-12" role="status"></div>
          <span class="d-block text-xs text-secondary-light">Retrieving student registration dockets...</span>
        </div>

        <div v-else-if="enrollmentStore.adviserSubmissions.length === 0" class="text-center py-48 p-24">
          <i class="ri-inbox-line text-4xl text-neutral-400 d-block mb-8"></i>
          <h6 class="text-sm fw-bold text-neutral-800 mb-4">No course registration submissions found</h6>
          <p class="text-xxs text-secondary-light mb-0">Adjust your filters or search query to find student dockets.</p>
        </div>

        <div v-else class="table-responsive">
          <table class="table bordered-table mb-0 align-middle">
            <thead class="bg-neutral-100">
              <tr>
                <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-12 ps-20">Student Dossier</th>
                <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-12">Academic Level & CGPA</th>
                <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-12">Load Accounting</th>
                <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-12">AI Carryover Audit</th>
                <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-12">Review Status</th>
                <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-12 text-end pe-20">Adviser Action</th>
              </tr>
            </thead>
            <tbody>
              <tr 
                v-for="sub in enrollmentStore.adviserSubmissions" 
                :key="sub.studentId"
                class="hover-bg-neutral-50"
              >
                <!-- Student -->
                <td class="ps-20 py-14">
                  <div class="d-flex align-items-center gap-12">
                    <img 
                      :src="sub.avatar || '/assets/images/thumbs/user-img1.png'" 
                      alt="Student Avatar" 
                      class="w-40-px h-40-px rounded-circle object-fit-cover border border-neutral-200 flex-shrink-0"
                      @error="(e) => e.target.src = '/assets/images/thumbs/user-img1.png'"
                    />
                    <div>
                      <span class="d-block text-xs fw-bold text-neutral-900 mb-2">{{ sub.name }}</span>
                      <span class="d-block font-monospace text-xxs text-secondary-light">{{ sub.matricNumber }}</span>
                    </div>
                  </div>
                </td>

                <!-- Level & CGPA -->
                <td>
                  <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-6 py-2 radius-4 fw-semibold mb-2 d-inline-block">
                    {{ sub.level }}
                  </span>
                  <div class="d-flex align-items-center gap-6">
                    <span class="text-xxs text-secondary-light">CGPA:</span>
                    <strong class="text-xs font-monospace text-success-700">{{ sub.cgpa?.toFixed(2) }}</strong>
                  </div>
                </td>

                <!-- Load Units -->
                <td>
                  <div class="d-flex align-items-center gap-6">
                    <strong class="text-xs font-monospace text-primary-600">{{ sub.totalCreditUnits }} Units</strong>
                    <span class="text-xxs text-secondary-light">({{ sub.coursesCount }} courses)</span>
                  </div>
                  <span 
                    v-if="sub.isUnderload" 
                    class="badge bg-warning-100 text-warning-800 text-xxs px-6 py-1 radius-4 d-inline-flex align-items-center gap-2 mt-2"
                  >
                    <i class="ri-alert-line"></i> Senate Underload Concession
                  </span>
                </td>

                <!-- Carryovers -->
                <td>
                  <div v-if="sub.hasCarryovers" class="d-flex align-items-center gap-6">
                    <span class="badge bg-danger-50 text-danger-700 border border-danger-200 text-xxs px-6 py-2 radius-4 fw-bold">
                      <i class="ri-lock-2-fill"></i> {{ sub.carryoverUnits }}u Carryover Enrolled
                    </span>
                  </div>
                  <div v-else>
                    <span class="badge bg-success-50 text-success-700 border border-success-200 text-xxs px-6 py-2 radius-4 fw-semibold">
                      <i class="ri-check-line"></i> Clean Standing
                    </span>
                  </div>
                </td>

                <!-- Review Status -->
                <td>
                  <span 
                    class="badge text-xxs px-10 py-4 radius-6 fw-bold d-inline-flex align-items-center gap-4"
                    :class="getStatusBadgeClass(sub.approvalStatus)"
                  >
                    <i :class="getStatusIcon(sub.approvalStatus)"></i>
                    {{ sub.approvalStatus }}
                  </span>
                  <span v-if="sub.adviserRemarks" class="d-block text-xxs text-secondary-light text-truncate mt-2" style="max-width: 180px;" :title="sub.adviserRemarks">
                    "{{ sub.adviserRemarks }}"
                  </span>
                </td>

                <!-- Actions -->
                <td class="text-end pe-20">
                  <button 
                    type="button" 
                    class="btn btn-outline-primary btn-xs radius-6 d-inline-flex align-items-center gap-4 px-12 py-6 fw-semibold"
                    @click="handleReview(sub.studentId)"
                  >
                    <i class="ri-eye-line text-xs"></i>
                    <span>Review Docket</span>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- 4. Review & Approval Modal -->
    <div 
      v-if="enrollmentStore.isReviewModalOpen && selectedDocket" 
      class="modal fade show d-block" 
      tabindex="-1" 
      style="background: rgba(0, 0, 0, 0.5); z-index: 1050;"
    >
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content border-0 radius-16 shadow-2">
          <!-- Modal Header -->
          <div class="modal-header p-20 border-bottom border-neutral-200">
            <div class="d-flex align-items-center gap-10">
              <span class="badge bg-primary-600 text-white rounded-circle p-8">
                <i class="ri-shield-user-fill text-lg"></i>
              </span>
              <div>
                <h6 class="modal-title text-md fw-bold text-neutral-900 mb-2">
                  Level Adviser Academic Docket Review
                </h6>
                <span class="text-xxs text-secondary-light">
                  {{ selectedDocket.student?.program }} • {{ selectedDocket.student?.level }}
                </span>
              </div>
            </div>
            <button 
              type="button" 
              class="btn-close text-xs" 
              @click="enrollmentStore.isReviewModalOpen = false"
            ></button>
          </div>

          <!-- Modal Body -->
          <div class="modal-body p-20 p-md-24 max-h-500-px overflow-y-auto">
            <!-- Student Header Dossier -->
            <div class="p-16 radius-12 bg-neutral-50 border border-neutral-200 d-flex flex-column flex-sm-row align-items-sm-center justify-content-between gap-16 mb-20">
              <div class="d-flex align-items-center gap-12">
                <img 
                  :src="selectedDocket.student?.avatar || '/assets/images/thumbs/user-img1.png'" 
                  alt="Student Passport" 
                  class="w-48-px h-48-px rounded-circle object-fit-cover border border-neutral-300"
                  @error="(e) => e.target.src = '/assets/images/thumbs/user-img1.png'"
                />
                <div>
                  <h6 class="text-sm fw-bold text-neutral-900 mb-2">{{ selectedDocket.student?.name }}</h6>
                  <div class="d-flex align-items-center gap-8 text-xxs text-secondary-light font-monospace">
                    <span>{{ selectedDocket.student?.matricNumber }}</span>
                    <span>•</span>
                    <span>CGPA: <strong class="text-success-700 font-monospace">{{ selectedDocket.student?.cgpa?.toFixed(2) }}</strong></span>
                  </div>
                </div>
              </div>

              <div>
                <span 
                  class="badge text-xs px-10 py-4 radius-6 fw-bold d-inline-flex align-items-center gap-4"
                  :class="getStatusBadgeClass(selectedDocket.approvalStatus)"
                >
                  <i :class="getStatusIcon(selectedDocket.approvalStatus)"></i>
                  {{ selectedDocket.approvalStatus }}
                </span>
              </div>
            </div>

            <!-- Underload Concession Box (if applicable) -->
            <div v-if="selectedDocket.isUnderload" class="p-14 radius-10 bg-warning-50 border border-warning-300 mb-20">
              <div class="d-flex align-items-start gap-8">
                <i class="ri-alert-fill text-warning-700 text-lg flex-shrink-0 mt-2"></i>
                <div>
                  <div class="d-flex align-items-center gap-8 mb-2">
                    <span class="text-xs fw-bold text-warning-900">Senate Underload Concession Request</span>
                    <span class="badge bg-neutral-900 text-white font-monospace text-xxs px-6 py-1 radius-4">
                      {{ selectedDocket.concessionReference }}
                    </span>
                  </div>
                  <p class="text-xxs text-warning-900 mb-0">
                    <strong>Justification Reason:</strong> {{ selectedDocket.underloadReason || 'Final Year Clearance / Special Pacing' }}
                  </p>
                </div>
              </div>
            </div>

            <!-- Enrolled Courses Breakdown -->
            <div class="mb-20">
              <div class="d-flex align-items-center justify-content-between mb-8">
                <span class="text-xs fw-bold text-neutral-800 text-uppercase">
                  Registered Modules ({{ selectedDocket.coursesCount }} Courses • {{ selectedDocket.totalCreditUnits }} Credit Units)
                </span>
                <span class="badge bg-primary-50 text-primary-700 text-xxs px-8 py-2 radius-4 fw-bold">
                  {{ selectedDocket.totalCreditUnits }} / 24 Units
                </span>
              </div>

              <div class="table-responsive">
                <table class="table bordered-table mb-0 align-middle">
                  <thead class="bg-neutral-100">
                    <tr>
                      <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-8">Code</th>
                      <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-8">Course Title</th>
                      <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-8">Units</th>
                      <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-8">Category</th>
                      <th scope="col" class="text-xxs text-uppercase fw-bold text-neutral-700 py-8 text-end">Lecturer</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr 
                      v-for="c in selectedDocket.courses" 
                      :key="c.code"
                      :class="{ 'bg-danger-50 bg-opacity-25': c.isCarryover }"
                    >
                      <td>
                        <span class="font-monospace fw-bold text-xs" :class="c.isCarryover ? 'text-danger-700' : 'text-neutral-900'">
                          {{ c.code }}
                        </span>
                      </td>
                      <td class="text-xs text-neutral-800 fw-medium">{{ c.title }}</td>
                      <td>
                        <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-6 py-2 radius-4 font-monospace">
                          {{ c.creditUnits }}u
                        </span>
                      </td>
                      <td>
                        <span 
                          class="badge text-xxs px-6 py-2 radius-4 fw-bold"
                          :class="c.isCarryover ? 'bg-danger-600 text-white' : 'bg-primary-50 text-primary-700'"
                        >
                          {{ c.isCarryover ? 'Mandatory Carryover' : c.category }}
                        </span>
                      </td>
                      <td class="text-end text-xxs text-secondary-light">{{ c.lecturer }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Adviser Decision & Remarks Form -->
            <div class="p-16 radius-12 bg-base border border-neutral-300">
              <label class="form-label text-xs fw-bold text-neutral-900 mb-4 d-flex align-items-center justify-content-between">
                <span>Level Adviser Endorsement / Correction Remarks:</span>
                <span class="text-xxs text-secondary-light">Required for disapproval</span>
              </label>
              <textarea 
                v-model="reviewRemarks"
                rows="3"
                placeholder="e.g., Registration approved. Verified prerequisites and carryover courses are satisfied."
                class="form-control text-xs radius-8 border-neutral-300 mb-8"
              ></textarea>
              <span class="text-xxs text-secondary-light d-block">
                These remarks will be printed on the student's Course Slip and displayed on their dashboard.
              </span>
            </div>
          </div>

          <!-- Modal Footer Actions -->
          <div class="modal-footer p-16 border-top border-neutral-200 d-flex align-items-center justify-content-between">
            <button 
              type="button" 
              class="btn btn-outline-secondary btn-sm radius-8 px-14 py-8 text-xs"
              @click="enrollmentStore.isReviewModalOpen = false"
            >
              Cancel
            </button>

            <div class="d-flex align-items-center gap-10">
              <!-- Disapprove Button -->
              <button 
                type="button" 
                class="btn btn-outline-danger btn-sm radius-8 d-inline-flex align-items-center gap-6 px-16 py-8 text-xs fw-bold"
                :disabled="isProcessing"
                @click="handleDisapprove"
              >
                <i class="ri-close-circle-line text-sm"></i>
                <span>Disapprove & Request Changes</span>
              </button>

              <!-- Approve Button -->
              <button 
                type="button" 
                class="btn btn-success btn-sm radius-8 d-inline-flex align-items-center gap-6 px-18 py-8 text-xs fw-bold shadow-sm"
                :disabled="isProcessing"
                @click="handleApprove"
              >
                <span v-if="isProcessing" class="spinner-border spinner-border-sm" role="status"></span>
                <i v-else class="ri-checkbox-circle-fill text-sm"></i>
                <span>Approve & Sign Registration</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: 'AdviserApprovalConsole',
  setup() {
    const enrollmentStore = useEnrollmentStore();
    const reviewRemarks = ref('');
    const isProcessing = ref(false);

    const selectedDocket = computed(() => enrollmentStore.selectedSubmissionForReview);

    onMounted(async () => {
      await loadSubmissions();
    });

    const loadSubmissions = async () => {
      await enrollmentStore.fetchAdviserSubmissions();
    };

    const handleSearch = () => {
      loadSubmissions();
    };

    const handleFilterChange = () => {
      loadSubmissions();
    };

    const handleReview = async (studentId) => {
      reviewRemarks.value = '';
      await enrollmentStore.openReviewModal(studentId);
      if (selectedDocket.value?.adviserRemarks) {
        reviewRemarks.value = selectedDocket.value.adviserRemarks;
      }
    };

    const handleApprove = async () => {
      if (!selectedDocket.value) return;
      isProcessing.value = true;
      try {
        await enrollmentStore.approveRegistration(
          selectedDocket.value.student.id,
          reviewRemarks.value
        );
      } finally {
        isProcessing.value = false;
      }
    };

    const handleDisapprove = async () => {
      if (!selectedDocket.value) return;
      isProcessing.value = true;
      try {
        await enrollmentStore.rejectRegistration(
          selectedDocket.value.student.id,
          reviewRemarks.value
        );
      } finally {
        isProcessing.value = false;
      }
    };

    const getStatusBadgeClass = (status) => {
      if (!status) return 'bg-neutral-100 text-neutral-800';
      if (status === 'Approved') return 'bg-success-100 text-success-800 border border-success-200';
      if (status === 'Disapproved') return 'bg-danger-100 text-danger-800 border border-danger-200';
      return 'bg-warning-100 text-warning-800 border border-warning-200';
    };

    const getStatusIcon = (status) => {
      if (status === 'Approved') return 'ri-checkbox-circle-fill';
      if (status === 'Disapproved') return 'ri-close-circle-fill';
      return 'ri-time-fill';
    };

    return {
      enrollmentStore,
      selectedDocket,
      reviewRemarks,
      isProcessing,
      loadSubmissions,
      handleSearch,
      handleFilterChange,
      handleReview,
      handleApprove,
      handleDisapprove,
      getStatusBadgeClass,
      getStatusIcon
    };
  }
};
</script>

<style scoped>
.max-h-500-px {
  max-height: 500px;
}
.w-40-px {
  width: 40px;
}
.h-40-px {
  height: 40px;
}
.w-48-px {
  width: 48px;
}
.h-48-px {
  height: 48px;
}
.btn-xs {
  padding: 4px 8px;
  font-size: 0.75rem;
}
</style>
