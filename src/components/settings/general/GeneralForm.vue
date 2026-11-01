<template>
  <div class="card p-0 radius-12 border-0 shadow-sm overflow-hidden mb-32">
    <!-- Header with Tab Navigation -->
    <div class="card-header bg-base border-bottom py-16 px-24 d-flex flex-wrap align-items-center justify-content-between gap-3">
      <ul class="nav nav-pills cms-nav-pills gap-8">
        <li class="nav-item">
          <button
            type="button"
            class="nav-link text-xs fw-semibold py-8 px-16 rounded-8 d-flex align-items-center gap-8 transition-all"
            :class="activeTab === 'identity' ? 'active bg-primary-600 text-white' : 'text-neutral-600 hover-bg-neutral-100'"
            @click="activeTab = 'identity'"
          >
            <i class="ri-government-line text-sm"></i>
            <span>Identity & Branding</span>
          </button>
        </li>
        <li class="nav-item">
          <button
            type="button"
            class="nav-link text-xs fw-semibold py-8 px-16 rounded-8 d-flex align-items-center gap-8 transition-all"
            :class="activeTab === 'calendar' ? 'active bg-primary-600 text-white' : 'text-neutral-600 hover-bg-neutral-100'"
            @click="activeTab = 'calendar'"
          >
            <i class="ri-calendar-event-line text-sm"></i>
            <span>Academic Calendar</span>
          </button>
        </li>
        <li class="nav-item">
          <button
            type="button"
            class="nav-link text-xs fw-semibold py-8 px-16 rounded-8 d-flex align-items-center gap-8 transition-all"
            :class="activeTab === 'modules' ? 'active bg-primary-600 text-white' : 'text-neutral-600 hover-bg-neutral-100'"
            @click="activeTab = 'modules'"
          >
            <i class="ri-apps-2-line text-sm"></i>
            <span>Subsystem Modules</span>
          </button>
        </li>
        <li class="nav-item">
          <button
            type="button"
            class="nav-link text-xs fw-semibold py-8 px-16 rounded-8 d-flex align-items-center gap-8 transition-all"
            :class="activeTab === 'ai' ? 'active bg-primary-600 text-white' : 'text-neutral-600 hover-bg-neutral-100'"
            @click="activeTab = 'ai'"
          >
            <i class="ri-scales-3-line text-sm"></i>
            <span>Senate Regulations & Academic Policy</span>
          </button>
        </li>
      </ul>

      <!-- Action Buttons -->
      <div class="d-flex align-items-center gap-8">
        <button
          type="button"
          @click="resetDefaults"
          class="btn btn-outline-neutral-300 text-neutral-700 text-xs fw-semibold py-8 px-14 rounded-8 d-flex align-items-center gap-6 hover-bg-neutral-100"
        >
          <i class="ri-restart-line"></i>
          <span>Reset Defaults</span>
        </button>
        <button
          type="button"
          @click="saveAllSettings"
          class="btn btn-primary-600 text-xs fw-semibold py-8 px-18 rounded-8 d-flex align-items-center gap-6 shadow-sm"
          :disabled="isSaving"
        >
          <span v-if="isSaving" class="spinner-border spinner-border-sm" role="status"></span>
          <i v-if="!isSaving" class="ri-save-3-line"></i>
          <span>{{ isSaving ? 'Saving Changes...' : 'Save Configuration' }}</span>
        </button>
      </div>
    </div>

    <!-- Alert Banner on Save -->
    <div v-if="saveSuccessMessage" class="alert alert-success d-flex align-items-center gap-12 m-24 mb-0 py-12 px-16 radius-8 border-0 bg-success-50 text-success-700 text-xs">
      <i class="ri-checkbox-circle-fill text-lg text-success-main"></i>
      <div class="flex-grow-1 fw-medium">{{ saveSuccessMessage }}</div>
      <button type="button" class="btn p-0 border-0 text-success-700" @click="saveSuccessMessage = ''">
        <i class="ri-close-line text-md"></i>
      </button>
    </div>

    <div class="card-body p-24 p-lg-32">
      <!-- ================= TAB 1: IDENTITY & BRANDING ================= -->
      <div v-show="activeTab === 'identity'">
        <div class="mb-24">
          <h6 class="fw-bold text-primary-light mb-4">University Identity & Visual Co-Branding</h6>
          <p class="text-xs text-secondary-light mb-0">
            Configure how the university identifies itself on the portal gateway, documents, and external interfaces.
          </p>
        </div>

        <div class="row g-4">
          <div class="col-md-8">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">University Legal Name <span class="text-danger-600">*</span></label>
              <input type="text" class="form-control text-sm radius-8" v-model="form.institutionName" placeholder="e.g. Apex Metropolitan University">
            </div>
          </div>
          <div class="col-md-4">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">University Short Code / Acronym <span class="text-danger-600">*</span></label>
              <input type="text" class="form-control text-sm radius-8" v-model="form.shortCode" placeholder="e.g. AMU">
            </div>
          </div>

          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Portal Subtitle / Motto</label>
              <input type="text" class="form-control text-sm radius-8" v-model="form.portalSubtitle" placeholder="e.g. Intelligent Academic Portal & SIS">
            </div>
          </div>
          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Primary Campus Designation</label>
              <input type="text" class="form-control text-sm radius-8" v-model="form.campusLocation" placeholder="e.g. Main Campus - University City">
            </div>
          </div>

          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">IT Helpdesk Support Email <span class="text-danger-600">*</span></label>
              <input type="email" class="form-control text-sm radius-8" v-model="form.supportEmail" placeholder="helpdesk@amu.edu">
            </div>
          </div>
          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Support Hotline / Phone</label>
              <input type="text" class="form-control text-sm radius-8" v-model="form.supportPhone" placeholder="+1 (555) 019-4820">
            </div>
          </div>

          <div class="col-12">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Physical Campus Address</label>
              <input type="text" class="form-control text-sm radius-8" v-model="form.physicalAddress" placeholder="100 University Avenue, Tech Corridor, CA 94105">
            </div>
          </div>

          <div class="col-md-6">
            <div class="p-16 rounded-10 bg-neutral-50 border border-neutral-200">
              <label class="form-label text-xs fw-semibold text-primary-light mb-8 d-block">Light Theme Logo Asset Path</label>
              <input type="text" class="form-control text-xs font-monospace radius-8 mb-12" v-model="form.logoUrl">
              <div class="p-12 bg-white rounded-8 border text-center">
                <img :src="form.logoUrl" alt="Logo Preview" class="h-36-px object-fit-contain">
              </div>
            </div>
          </div>

          <div class="col-md-6">
            <div class="p-16 rounded-10 bg-neutral-900 text-white border border-neutral-800">
              <label class="form-label text-xs fw-semibold text-white mb-8 d-block">Dark Theme Logo Asset Path</label>
              <input type="text" class="form-control text-xs font-monospace radius-8 mb-12 bg-neutral-800 text-white border-neutral-700" v-model="form.logoDarkUrl">
              <div class="p-12 bg-neutral-950 rounded-8 border border-neutral-800 text-center">
                <img :src="form.logoDarkUrl" alt="Dark Logo Preview" class="h-36-px object-fit-contain">
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= TAB 2: ACADEMIC CALENDAR ================= -->
      <div v-show="activeTab === 'calendar'">
        <div class="mb-24">
          <h6 class="fw-bold text-primary-light mb-4">Academic Session & Term Governance</h6>
          <p class="text-xs text-secondary-light mb-0">
            Set the active session, semester dates, and operational windows across all academic departments.
          </p>
        </div>

        <div class="row g-4">
          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Active Academic Session <span class="text-danger-600">*</span></label>
              <select class="form-select text-sm radius-8" v-model="form.academicSession">
                <option value="2025/2026 Academic Session">2025/2026 Academic Session</option>
                <option value="2026/2027 Academic Session">2026/2027 Academic Session</option>
                <option value="2027/2028 Academic Session">2027/2028 Academic Session</option>
              </select>
            </div>
          </div>

          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Current Active Term / Semester <span class="text-danger-600">*</span></label>
              <select class="form-select text-sm radius-8" v-model="form.currentSemester">
                <option value="First Semester (Fall)">First Semester (Fall)</option>
                <option value="Second Semester (Spring)">Second Semester (Spring)</option>
                <option value="Summer Intensive Term">Summer Intensive Term</option>
              </select>
            </div>
          </div>

          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Term Start Date</label>
              <input type="date" class="form-control text-sm radius-8" v-model="form.semesterStartDate">
            </div>
          </div>

          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Term End Date</label>
              <input type="date" class="form-control text-sm radius-8" v-model="form.semesterEndDate">
            </div>
          </div>

          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Faculty Grade Submission Deadline</label>
              <input type="date" class="form-control text-sm radius-8" v-model="form.gradeSubmissionDeadline">
            </div>
          </div>

          <div class="col-md-6">
            <div class="p-16 rounded-10 bg-neutral-50 border border-neutral-200 d-flex align-items-center justify-content-between mb-20">
              <div>
                <h6 class="text-xs fw-bold text-primary-light mb-2">Student Course Registration Window</h6>
                <p class="text-xxs text-secondary-light mb-0">Allow undergraduate & postgraduate students to add/drop courses</p>
              </div>
              <div class="form-check form-switch m-0">
                <input class="form-check-input text-lg cursor-pointer" type="checkbox" v-model="form.courseRegistrationOpen">
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= TAB 3: SUBSYSTEM MODULES ================= -->
      <div v-show="activeTab === 'modules'">
        <div class="mb-24">
          <h6 class="fw-bold text-primary-light mb-4">Campus Subsystem Modules & Feature Flags</h6>
          <p class="text-xs text-secondary-light mb-0">
            Enable or disable specific university modules. Disabled modules will automatically hide from the navigation.
          </p>
        </div>

        <div class="row g-3">
          <div class="col-md-6" v-for="(enabled, modKey) in form.modules" :key="modKey">
            <div class="p-16 rounded-10 border transition-all d-flex align-items-center justify-content-between"
              :class="enabled ? 'bg-base border-primary-200' : 'bg-neutral-50 border-neutral-200 opacity-75'">
              <div class="d-flex align-items-center gap-12">
                <div class="w-36-px h-36-px rounded-8 d-flex align-items-center justify-content-center"
                  :class="enabled ? 'bg-primary-50 text-primary-600' : 'bg-neutral-200 text-neutral-500'">
                  <i :class="getModuleIcon(modKey)" class="text-lg"></i>
                </div>
                <div>
                  <h6 class="text-xs fw-bold text-primary-light mb-2">{{ getModuleTitle(modKey) }}</h6>
                  <p class="text-xxs text-secondary-light mb-0">{{ getModuleDescription(modKey) }}</p>
                </div>
              </div>
              <div class="form-check form-switch m-0">
                <input class="form-check-input text-md cursor-pointer" type="checkbox" v-model="form.modules[modKey]">
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ================= TAB 4: SENATE REGULATIONS & ACADEMIC POLICY ================= -->
      <div v-show="activeTab === 'ai'">
        <div class="mb-24">
          <h6 class="fw-bold text-primary-light mb-4">Senate Regulations, Academic Policy & Thresholds</h6>
          <p class="text-xs text-secondary-light mb-0">
            Define statutory academic compliance cutoffs, attendance requirements for exam entry, grading ratios, and handbook policies.
          </p>
        </div>

        <div class="row g-4">
          <div class="col-md-6">
            <div class="p-16 rounded-10 bg-neutral-50 border border-neutral-200">
              <div class="d-flex justify-content-between align-items-center mb-8">
                <label class="text-xs fw-bold text-primary-light mb-0">Minimum Lecture Attendance for Examination Eligibility</label>
                <span class="badge bg-warning-50 text-warning-main border border-warning-200 text-xs fw-bold px-8 py-4 rounded">
                  &ge; {{ form.ai.atRiskAttendanceThreshold }}% Required
                </span>
              </div>
              <input type="range" class="form-range" min="50" max="90" step="5" v-model.number="form.ai.atRiskAttendanceThreshold">
              <p class="text-xxs text-secondary-light mb-0 mt-4">
                Statutory Senate requirement: Students falling below this attendance percentage are barred from writing semester examinations without formal Dean dispensation.
              </p>
            </div>
          </div>

          <div class="col-md-6">
            <div class="p-16 rounded-10 bg-neutral-50 border border-neutral-200">
              <div class="d-flex justify-content-between align-items-center mb-8">
                <label class="text-xs fw-bold text-primary-light mb-0">Academic Probation CGPA Cutoff</label>
                <span class="badge bg-danger-50 text-danger-main border border-danger-200 text-xs fw-bold px-8 py-4 rounded">
                  &lt; {{ form.ai.atRiskGpaThreshold }} CGPA
                </span>
              </div>
              <input type="range" class="form-range" min="1.00" max="2.50" step="0.10" v-model.number="form.ai.atRiskGpaThreshold">
              <p class="text-xxs text-secondary-light mb-0 mt-4">
                Undergraduate benchmark: Students whose cumulative grade point average drops below this cutoff are placed on academic probation watch.
              </p>
            </div>
          </div>

          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Continuous Assessment (CAT) Component Weight</label>
              <select class="form-select text-sm radius-8" v-model="form.ai.catWeight">
                <option value="30">30% (Standard Senate Tertiary Baseline)</option>
                <option value="40">40% (Continuous Assessment Intensive)</option>
                <option value="20">20% (Examination Heavy)</option>
              </select>
              <span class="text-xxs text-secondary-light mt-4 d-block">Weight allocated to tests, quizzes, practicals, and assignments.</span>
            </div>
          </div>

          <div class="col-md-6">
            <div class="mb-20">
              <label class="form-label text-xs fw-semibold text-primary-light">Final Examination Component Weight</label>
              <select class="form-select text-sm radius-8" v-model="form.ai.examWeight">
                <option value="70">70% (Standard End-of-Semester Exam)</option>
                <option value="60">60% (Extended CAT Ratio)</option>
                <option value="80">80% (Final Exam Weighted)</option>
              </select>
              <span class="text-xxs text-secondary-light mt-4 d-block">Weight allocated to the invigilated semester exam paper.</span>
            </div>
          </div>

          <div class="col-12">
            <div class="p-16 rounded-10 bg-primary-50 border border-primary-200 d-flex align-items-center justify-content-between">
              <div>
                <h6 class="text-xs fw-bold text-primary-600 mb-2">Mandatory Senate & Faculty Board Grade Moderation</h6>
                <p class="text-xxs text-neutral-600 mb-0">
                  All semester examination results and CAT score amendments require Departmental Board vetting and Senate Business Committee approval before publishing.
                </p>
              </div>
              <div class="form-check form-switch m-0">
                <input class="form-check-input text-lg cursor-pointer" type="checkbox" v-model="form.ai.requireHumanInTheLoop">
              </div>
            </div>
          </div>

          <div class="col-12">
            <div class="mb-10">
              <label class="form-label text-xs fw-semibold text-primary-light">Institutional Academic Regulations & Faculty Handbook Directives</label>
              <textarea class="form-control text-xs radius-8 font-monospace" rows="3" v-model="form.ai.policyDirectives" placeholder="Statutory academic directives complying with University Senate guidelines"></textarea>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { ref, reactive } from 'vue';
import { useInstitutionStore } from '@/stores/institution.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: "GeneralForm",
  setup() {
    const institution = useInstitutionStore();
    const toastStore = useToastStore();

    const activeTab = ref('identity');
    const isSaving = ref(false);
    const saveSuccessMessage = ref('');

    // Clone state into reactive local form
    const form = reactive({
      institutionName: institution.institutionName,
      shortCode: institution.shortCode,
      portalSubtitle: institution.portalSubtitle,
      campusLocation: institution.campusLocation,
      logoUrl: institution.logoUrl,
      logoDarkUrl: institution.logoDarkUrl,
      supportEmail: institution.supportEmail,
      supportPhone: institution.supportPhone,
      physicalAddress: institution.physicalAddress,

      academicSession: institution.academicSession,
      currentSemester: institution.currentSemester,
      semesterStartDate: institution.semesterStartDate,
      semesterEndDate: institution.semesterEndDate,
      courseRegistrationOpen: institution.courseRegistrationOpen,
      examPeriodActive: institution.examPeriodActive,
      gradeSubmissionDeadline: institution.gradeSubmissionDeadline,

      modules: { ...institution.modules },
      ai: { ...institution.ai },
    });

    const getModuleTitle = (key) => {
      const titles = {
        aiAdvisory: 'Academic Standing & Retention Advisory',
        studentAdmissions: 'Online Admissions & Enrollment',
        attendance: 'Lecture Attendance & Biometric Registers',
        examination: 'Examinations, Schedules & Results',
        feeCollections: 'Fees, Tuition & Payments',
        library: 'Digital Library & Circulation',
        accounts: 'University Accounting & Expenses',
        hrm: 'Human Resources & Faculty Payroll',
        leaves: 'Leave Management & Approvals',
        noticeBoard: 'Official Campus Notice Board',
      };
      return titles[key] || key;
    };

    const getModuleDescription = (key) => {
      const desc = {
        aiAdvisory: 'Audits student attendance compliance (< 75%), probation watchlists (CGPA < 1.50), and academic standing',
        studentAdmissions: 'Student application tracking, vetting, and identity verification',
        attendance: 'Daily lecture attendance registers, biometric logs, and Senate 75% examination eligibility tracking',
        examination: 'Exam hall seating, invigilation rosters, and grading sheets',
        feeCollections: 'Tuition collection, receipts, and fee discount groups',
        library: 'Book cataloging, member cards, and borrowing history',
        accounts: 'Institutional income heads, expenditure audits, and ledgers',
        hrm: 'Employee records, designations, department rosters, and payroll',
        leaves: 'Faculty and staff leave requests and balance tracking',
        noticeBoard: 'Campus-wide announcements and emergency broadcasts',
      };
      return desc[key] || 'Campus subsystem component';
    };

    const getModuleIcon = (key) => {
      const icons = {
        aiAdvisory: 'ri-scales-3-line',
        studentAdmissions: 'ri-user-add-line',
        attendance: 'ri-calendar-check-line',
        examination: 'ri-file-list-3-line',
        feeCollections: 'ri-bank-card-line',
        library: 'ri-book-read-line',
        accounts: 'ri-wallet-3-line',
        hrm: 'ri-team-line',
        leaves: 'ri-time-line',
        noticeBoard: 'ri-notification-3-line',
      };
      return icons[key] || 'ri-function-line';
    };

    const saveAllSettings = () => {
      isSaving.value = true;
      setTimeout(() => {
        institution.saveConfig({
          institutionName: form.institutionName,
          shortCode: form.shortCode,
          portalSubtitle: form.portalSubtitle,
          campusLocation: form.campusLocation,
          logoUrl: form.logoUrl,
          logoDarkUrl: form.logoDarkUrl,
          supportEmail: form.supportEmail,
          supportPhone: form.supportPhone,
          physicalAddress: form.physicalAddress,

          academicSession: form.academicSession,
          currentSemester: form.currentSemester,
          semesterStartDate: form.semesterStartDate,
          semesterEndDate: form.semesterEndDate,
          courseRegistrationOpen: form.courseRegistrationOpen,
          examPeriodActive: form.examPeriodActive,
          gradeSubmissionDeadline: form.gradeSubmissionDeadline,

          modules: { ...form.modules },
          ai: { ...form.ai },
        });

        isSaving.value = false;
        saveSuccessMessage.value = `Institutional configuration saved! Changes are now live across ${form.institutionName}.`;
        toastStore.success(
          `Configuration saved! Branding, session parameters, and active modules are now live across ${form.institutionName}.`,
          'Campus Settings Saved'
        );

        setTimeout(() => {
          saveSuccessMessage.value = '';
        }, 5000);
      }, 400);
    };

    const resetDefaults = () => {
      if (confirm('Are you sure you want to restore default university configuration presets?')) {
        institution.resetToDefaults();
        Object.assign(form, {
          institutionName: institution.institutionName,
          shortCode: institution.shortCode,
          portalSubtitle: institution.portalSubtitle,
          campusLocation: institution.campusLocation,
          logoUrl: institution.logoUrl,
          logoDarkUrl: institution.logoDarkUrl,
          supportEmail: institution.supportEmail,
          supportPhone: institution.supportPhone,
          physicalAddress: institution.physicalAddress,

          academicSession: institution.academicSession,
          currentSemester: institution.currentSemester,
          semesterStartDate: institution.semesterStartDate,
          semesterEndDate: institution.semesterEndDate,
          courseRegistrationOpen: institution.courseRegistrationOpen,
          examPeriodActive: institution.examPeriodActive,
          gradeSubmissionDeadline: institution.gradeSubmissionDeadline,

          modules: { ...institution.modules },
          ai: { ...institution.ai },
        });

        saveSuccessMessage.value = 'Configuration reset to factory defaults.';
        toastStore.info(
          'Institutional settings and branding restored to university default presets.',
          'Presets Restored'
        );

        setTimeout(() => {
          saveSuccessMessage.value = '';
        }, 4000);
      }
    };

    return {
      institution,
      activeTab,
      form,
      isSaving,
      saveSuccessMessage,
      getModuleTitle,
      getModuleDescription,
      getModuleIcon,
      saveAllSettings,
      resetDefaults,
    };
  },
};
</script>

<style scoped>
.cms-nav-pills .nav-link {
  border: 1px solid transparent;
}
.cms-nav-pills .nav-link:not(.active):hover {
  background-color: var(--neutral-100, #f8fafc);
}
.text-xxs {
  font-size: 0.6875rem;
}
.h-36-px {
  height: 36px;
}
</style>
