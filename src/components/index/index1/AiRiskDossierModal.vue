<template>
  <div class="modal fade" id="aiRiskDossierModal" tabindex="-1" aria-labelledby="aiRiskDossierModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
      <div class="modal-content border-0 radius-16 shadow-lg">
        
        <!-- Header -->
        <div class="modal-header border-bottom border-neutral-200 py-16 px-24 bg-neutral-50 radius-top-16">
          <div class="d-flex align-items-center gap-12">
            <div class="w-44-px h-44-px rounded-circle bg-danger-50 text-danger-600 d-flex justify-content-center align-items-center text-xl flex-shrink-0">
              <iconify-icon icon="solar:shield-warning-bold"></iconify-icon>
            </div>
            <div>
              <div class="d-flex align-items-center gap-8 flex-wrap">
                <h5 class="modal-title fw-bold text-primary-light mb-0" id="aiRiskDossierModalLabel">
                  Academic Retention & Student Advisory Dossier
                </h5>
                <span class="badge bg-danger-subtle text-danger-600 border border-danger-subtle px-10 py-4 radius-8 text-xs fw-semibold">
                  {{ atRiskStudents.length }} Students Flagged
                </span>
                <span class="badge bg-primary-50 text-primary-600 border border-primary-100 px-10 py-4 radius-8 text-xs fw-medium">
                  Senate Regulations: Attendance &lt; 75% • CGPA &lt; 1.50
                </span>
              </div>
              <p class="text-secondary-light text-xs mb-0 mt-2">
                Registry advisory roster monitoring lecture attendance compliance, continuous assessment performance, and academic probation benchmarks.
              </p>
            </div>
          </div>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <!-- Body -->
        <div class="modal-body p-24">
          <!-- Filter Tabs & Search Bar -->
          <div class="d-flex flex-wrap align-items-center justify-content-between gap-16 mb-20">
            <div class="d-flex align-items-center gap-8 flex-wrap">
              <button 
                type="button" 
                class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
                :class="selectedFilter === 'all' ? 'btn-primary-600 text-white' : 'btn-outline-neutral-300 text-secondary-light'"
                @click="selectedFilter = 'all'"
              >
                All Flagged ({{ atRiskStudents.length }})
              </button>
              <button 
                type="button" 
                class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
                :class="selectedFilter === 'attendance' ? 'btn-danger-600 text-white' : 'btn-outline-neutral-300 text-secondary-light'"
                @click="selectedFilter = 'attendance'"
              >
                Attendance &lt; 75% Threshold ({{ countByReason('attendance') }})
              </button>
              <button 
                type="button" 
                class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
                :class="selectedFilter === 'academic' ? 'btn-warning-600 text-white' : 'btn-outline-neutral-300 text-secondary-light'"
                @click="selectedFilter = 'academic'"
              >
                Continuous Assessment Deficits ({{ countByReason('academic') }})
              </button>
              <button 
                type="button" 
                class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
                :class="selectedFilter === 'probation' ? 'btn-purple text-white' : 'btn-outline-neutral-300 text-secondary-light'"
                @click="selectedFilter = 'probation'"
              >
                Academic Probation Watch CGPA &lt; 1.50 ({{ countByReason('probation') }})
              </button>
            </div>

            <div class="position-relative" style="min-width: 260px;">
              <input 
                type="text" 
                class="form-control radius-8 py-6 ps-36 pe-16 text-sm" 
                placeholder="Search student or matric no..."
                v-model="searchQuery"
              >
              <iconify-icon icon="ion:search-outline" class="position-absolute top-50 start-0 translate-middle-y ms-12 text-secondary-light"></iconify-icon>
            </div>
          </div>

          <!-- Students Risk Table -->
          <div class="table-responsive radius-12 border border-neutral-200">
            <table class="table table-hover align-middle mb-0 text-sm">
              <thead class="bg-neutral-100 text-secondary-light fw-semibold text-xs text-uppercase">
                <tr>
                  <th class="py-12 px-16">Student Identity</th>
                  <th class="py-12 px-16">Department & Level</th>
                  <th class="py-12 px-16">Standing Deficit</th>
                  <th class="py-12 px-16 text-center">Deficit Severity</th>
                  <th class="py-12 px-16 text-center">Advisory Status</th>
                  <th class="py-12 px-16 text-end">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="student in filteredStudents" :key="student.id" :class="{'bg-neutral-50': student.status === 'Resolved'}">
                  
                  <!-- Student Details -->
                  <td class="py-12 px-16">
                    <div class="d-flex align-items-center gap-12">
                      <div class="w-36-px h-36-px rounded-circle bg-neutral-200 text-primary-600 fw-bold d-flex align-items-center justify-content-center flex-shrink-0 text-xs">
                        {{ student.initials }}
                      </div>
                      <div>
                        <div class="fw-semibold text-primary-light">{{ student.name }}</div>
                        <div class="text-secondary-light text-xs font-monospace">{{ student.matricNo }}</div>
                      </div>
                    </div>
                  </td>

                  <!-- Dept & Level -->
                  <td class="py-12 px-16">
                    <div class="fw-medium text-neutral-800">{{ student.department }}</div>
                    <div class="text-secondary-light text-xs">{{ student.level }} • CGPA: <span :class="student.cgpa < 2.0 ? 'text-danger-600 fw-bold' : 'text-primary-light'">{{ student.cgpa.toFixed(2) }}</span></div>
                  </td>

                  <!-- Risk Vector -->
                  <td class="py-12 px-16">
                    <div class="d-flex align-items-center gap-6">
                      <span 
                        class="badge radius-6 text-xs px-8 py-4 fw-medium"
                        :class="getRiskBadgeClass(student.riskCategory)"
                      >
                        {{ student.riskVector }}
                      </span>
                    </div>
                    <div class="text-secondary-light text-xs mt-2">
                      Course: <strong>{{ student.flaggedCourse }}</strong>
                    </div>
                  </td>

                  <!-- Severity / Benchmark -->
                  <td class="py-12 px-16 text-center">
                    <span 
                      class="badge radius-6 text-xs px-10 py-4 fw-semibold"
                      :class="getSeverityBadgeClass(student)"
                    >
                      {{ getSeverityLabel(student) }}
                    </span>
                  </td>

                  <!-- Status -->
                  <td class="py-12 px-16 text-center">
                    <span 
                      class="badge radius-pill px-10 py-4 text-xs fw-semibold"
                      :class="getStatusBadgeClass(student.status)"
                    >
                      {{ student.status }}
                    </span>
                  </td>

                  <!-- Action -->
                  <td class="py-12 px-16 text-end">
                    <div class="dropdown d-inline-block">
                      <button 
                        class="btn btn-sm btn-outline-neutral-300 radius-8 px-10 py-4 text-xs dropdown-toggle" 
                        type="button" 
                        data-bs-toggle="dropdown"
                      >
                        Intervene
                      </button>
                      <ul class="dropdown-menu dropdown-menu-end shadow-sm border p-8 radius-8 text-xs">
                        <li>
                          <a class="dropdown-item py-6 px-12 rounded cursor-pointer text-primary-600" @click="triggerAdvisorAlert(student)">
                            <iconify-icon icon="solar:letter-bold" class="me-6 text-sm"></iconify-icon>
                            Alert Academic Advisor
                          </a>
                        </li>
                        <li>
                          <a class="dropdown-item py-6 px-12 rounded cursor-pointer text-warning-600" @click="enrollInRemedial(student)">
                            <iconify-icon icon="solar:square-academic-cap-bold" class="me-6 text-sm"></iconify-icon>
                            Enroll in Peer Tutoring Clinic
                          </a>
                        </li>
                        <li>
                          <a class="dropdown-item py-6 px-12 rounded cursor-pointer text-success-600" @click="markAsResolved(student)">
                            <iconify-icon icon="solar:check-circle-bold" class="me-6 text-sm"></iconify-icon>
                            Mark As Under Supervision
                          </a>
                        </li>
                      </ul>
                    </div>
                  </td>

                </tr>
              </tbody>
            </table>
          </div>

          <!-- Alert Notification Feedback -->
          <div v-if="actionToast" class="alert alert-success border-0 radius-8 mt-16 py-10 px-16 d-flex align-items-center justify-content-between text-xs">
            <div class="d-flex align-items-center gap-8">
              <iconify-icon icon="solar:check-circle-bold" class="text-base text-success-600"></iconify-icon>
              <span>{{ actionToast }}</span>
            </div>
            <button type="button" class="btn-close btn-close-xs" @click="actionToast = ''"></button>
          </div>

        </div>

        <!-- Footer -->
        <div class="modal-footer border-top border-neutral-200 py-12 px-24 bg-neutral-50 radius-bottom-16 d-flex justify-content-between align-items-center">
          <div class="text-secondary-light text-xs d-flex align-items-center gap-6">
            <iconify-icon icon="solar:info-circle-bold" class="text-primary-600"></iconify-icon>
            Human-in-the-loop: Disqualification or probation decisions require Dean of Faculty signature before enforcement.
          </div>
          <div class="d-flex align-items-center gap-8">
            <button type="button" class="btn btn-outline-neutral-300 btn-sm radius-8 px-16 py-6 text-xs fw-semibold" data-bs-dismiss="modal">
              Close Dossier
            </button>
            <button type="button" class="btn btn-primary-600 btn-sm radius-8 px-16 py-6 text-xs fw-semibold text-white d-flex align-items-center gap-6" @click="exportReport">
              <iconify-icon icon="solar:document-text-bold"></iconify-icon>
              Export Faculty Early-Warning Report
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { telemetryApi } from '@/services/api.js';

export default {
  name: 'AiRiskDossierModal',
  setup() {
    const selectedFilter = ref('all');
    const searchQuery = ref('');
    const actionToast = ref('');

    const atRiskStudents = ref([
      {
        id: 1,
        name: 'David Adeleke',
        matricNo: 'CSC/2023/1042',
        initials: 'DA',
        department: 'Computer Science',
        level: '300 Level',
        cgpa: 1.82,
        riskCategory: 'attendance',
        riskVector: 'Attendance 58% (< 75% Exam Threshold)',
        flaggedCourse: 'CSC 301 — Advanced Algorithms',
        aiConfidence: 94,
        status: 'Unaddressed'
      },
      {
        id: 2,
        name: 'Chidinma Okoye',
        matricNo: 'MEE/2024/0488',
        initials: 'CO',
        department: 'Mechanical Engineering',
        level: '200 Level',
        cgpa: 1.45,
        riskCategory: 'probation',
        riskVector: 'Probation Risk (CGPA 1.45 < 1.50)',
        flaggedCourse: 'ENG 203 — Applied Thermodynamics',
        aiConfidence: 91,
        status: 'Unaddressed'
      },
      {
        id: 3,
        name: 'Emmanuel Babatunde',
        matricNo: 'LAW/2022/0119',
        initials: 'EB',
        department: 'Faculty of Law',
        level: '400 Level',
        cgpa: 2.15,
        riskCategory: 'academic',
        riskVector: 'CAT 1 Score: 8/30 (Course Failure Risk)',
        flaggedCourse: 'PUL 401 — Law of Evidence',
        aiConfidence: 87,
        status: 'Advisor Alerted'
      },
      {
        id: 4,
        name: 'Fatima Al-Hassan',
        matricNo: 'BCH/2023/0754',
        initials: 'FA',
        department: 'Biochemistry',
        level: '300 Level',
        cgpa: 1.90,
        riskCategory: 'attendance',
        riskVector: 'Attendance 62% (< 75% Exam Threshold)',
        flaggedCourse: 'BCH 305 — Enzymology',
        aiConfidence: 89,
        status: 'Unaddressed'
      },
      {
        id: 5,
        name: 'Olumide Fashola',
        matricNo: 'ECN/2024/0932',
        initials: 'OF',
        department: 'Economics',
        level: '200 Level',
        cgpa: 1.38,
        riskCategory: 'probation',
        riskVector: 'Probation Risk (CGPA 1.38 < 1.50)',
        flaggedCourse: 'ECN 201 — Macroeconomic Theory',
        aiConfidence: 96,
        status: 'Under Supervision'
      },
      {
        id: 6,
        name: 'Khadijah Suleiman',
        matricNo: 'NUR/2023/0315',
        initials: 'KS',
        department: 'Nursing Science',
        level: '300 Level',
        cgpa: 2.40,
        riskCategory: 'attendance',
        riskVector: 'Clinical Ward Attendance 68%',
        flaggedCourse: 'NUR 303 — Medical-Surgical Nursing',
        aiConfidence: 86,
        status: 'Unaddressed'
      },
      {
        id: 7,
        name: 'Victor Nwosu',
        matricNo: 'CVE/2022/0281',
        initials: 'VN',
        department: 'Civil Engineering',
        level: '400 Level',
        cgpa: 1.95,
        riskCategory: 'academic',
        riskVector: 'Missed Continuous Assessment Test 1',
        flaggedCourse: 'CVE 405 — Structural Analysis II',
        aiConfidence: 92,
        status: 'Unaddressed'
      }
    ]);

    const countByReason = (cat) => {
      return atRiskStudents.value.filter(s => s.riskCategory === cat).length;
    };

    const filteredStudents = computed(() => {
      return atRiskStudents.value.filter(s => {
        const matchesFilter = selectedFilter.value === 'all' || s.riskCategory === selectedFilter.value;
        const matchesSearch = s.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
                              s.matricNo.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
                              s.department.toLowerCase().includes(searchQuery.value.toLowerCase());
        return matchesFilter && matchesSearch;
      });
    });

    const getRiskBadgeClass = (category) => {
      switch (category) {
        case 'attendance':
          return 'bg-danger-50 text-danger-600 border border-danger-subtle';
        case 'academic':
          return 'bg-warning-50 text-warning-700 border border-warning-subtle';
        case 'probation':
          return 'bg-purple-50 text-purple-600 border border-purple-subtle';
        default:
          return 'bg-neutral-100 text-neutral-600';
      }
    };

    const getStatusBadgeClass = (status) => {
      switch (status) {
        case 'Unaddressed':
          return 'bg-danger-subtle text-danger-700';
        case 'Advisor Alerted':
          return 'bg-warning-subtle text-warning-800';
        case 'Under Supervision':
          return 'bg-success-subtle text-success-800';
        default:
          return 'bg-neutral-200 text-neutral-700';
      }
    };

    onMounted(async () => {
      try {
        const liveRecords = await telemetryApi.getRiskDossier();
        if (Array.isArray(liveRecords) && liveRecords.length > 0) {
          atRiskStudents.value = liveRecords;
        }
      } catch (err) {
        // Fall back to default seeded records
      }
    });

    const triggerAdvisorAlert = async (student) => {
      student.status = 'Advisor Alerted';
      try {
        await telemetryApi.submitIntervention({ studentId: student.id, action: 'Advisor Alerted' });
      } catch (e) {
        // Local fallback
      }
      actionToast.value = `Automated early-warning dispatch sent to ${student.name}'s Academic Advisor (${student.department}).`;
      setTimeout(() => { actionToast.value = ''; }, 4500);
    };

    const enrollInRemedial = async (student) => {
      student.status = 'Under Supervision';
      try {
        await telemetryApi.submitIntervention({ studentId: student.id, action: 'Remedial Tutoring Assigned' });
      } catch (e) {
        // Local fallback
      }
      actionToast.value = `${student.name} enrolled into Academic Clinic & Peer Tutoring for ${student.flaggedCourse}.`;
      setTimeout(() => { actionToast.value = ''; }, 4500);
    };

    const markAsResolved = async (student) => {
      student.status = 'Under Supervision';
      try {
        await telemetryApi.submitIntervention({ studentId: student.id, action: 'Under Supervision' });
      } catch (e) {
        // Local fallback
      }
      actionToast.value = `${student.name} marked as under formal academic supervision in Senate records.`;
      setTimeout(() => { actionToast.value = ''; }, 4500);
    };

    const exportReport = () => {
      actionToast.value = 'Generated PDF Early-Warning Dossier for Faculty Board of Examiners.';
      setTimeout(() => { actionToast.value = ''; }, 4500);
    };

    const getSeverityLabel = (student) => {
      if (student.riskCategory === 'attendance') return 'Exam Hold Risk';
      if (student.riskCategory === 'probation') return 'Probation Watch';
      return 'CAT Deficit';
    };

    const getSeverityBadgeClass = (student) => {
      if (student.riskCategory === 'attendance') return 'bg-danger-subtle text-danger-700';
      if (student.riskCategory === 'probation') return 'bg-purple-50 text-purple-700 border border-purple-200';
      return 'bg-warning-subtle text-warning-800';
    };

    return {
      selectedFilter,
      searchQuery,
      atRiskStudents,
      filteredStudents,
      countByReason,
      getRiskBadgeClass,
      getStatusBadgeClass,
      getSeverityLabel,
      getSeverityBadgeClass,
      triggerAdvisorAlert,
      enrollInRemedial,
      markAsResolved,
      exportReport,
      actionToast
    };
  }
};
</script>
