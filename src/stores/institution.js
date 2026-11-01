import { defineStore } from 'pinia';
import { institutionApi } from '../services/api.js';

const STORAGE_KEY = 'campus_institution_config';

const DEFAULT_CONFIG = {
  // Identity & Branding
  institutionName: 'Apex Metropolitan University',
  name: 'Apex Metropolitan University',
  motto: 'Excellence, Integrity & Innovation',
  shortCode: 'AMU',
  portalSubtitle: 'Intelligent Academic Portal & SIS',
  campusLocation: 'Main Campus - University City',
  logoUrl: '/assets/images/logo.png',
  logoDarkUrl: '/assets/images/logo-light.png',
  crestUrl: '/assets/images/logo-icon.png',
  supportEmail: 'helpdesk@amu.edu',
  supportPhone: '+1 (555) 019-4820',
  physicalAddress: '100 University Avenue, Tech Corridor, CA 94105',
  websiteUrl: 'https://amu.edu',

  // Academic Calendar & Governance
  academicSession: '2026/2027 Academic Session',
  currentAcademicYear: '2026/2027 Academic Session',
  currentSemester: 'First Semester (Fall)',
  semesterStartDate: '2026-09-01',
  semesterEndDate: '2027-01-22',
  courseRegistrationOpen: true,
  examPeriodActive: false,
  gradeSubmissionDeadline: '2027-02-05',

  // Campus Subsystem Modules (Feature Flags)
  modules: {
    aiAdvisory: true,
    studentAdmissions: true,
    attendance: true,
    examination: true,
    feeCollections: true,
    library: true,
    accounts: true,
    hrm: true,
    leaves: true,
    noticeBoard: true,
  },

  // Senate Regulations & Academic Policy Parameters
  ai: {
    provider: 'senate-policy-engine',
    atRiskAttendanceThreshold: 75, // Minimum lecture attendance for exam clearance (< 75% flagged)
    atRiskGpaThreshold: 1.50, // Academic probation warning cutoff (CGPA < 1.50)
    requireHumanInTheLoop: true, // Mandatory Senate & Faculty Board grade moderation
    aiProctoringSensitivity: 'standard', // Examination invigilation compliance level
    policyDirectives:
      'All academic standing classifications and examination approvals are governed by the 2026/2027 Senate Regulations and Faculty Handbook. Examination eligibility mandates minimum 75% verified lecture attendance.',
  },

  // Security & Access
  ssoEnabled: true,
  ssoProviderName: 'University Single Sign-On (SSO)',
  sessionTimeoutMinutes: 60,
  maintenanceMode: false,
};

function loadStoredConfig() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return DEFAULT_CONFIG;
    const parsed = JSON.parse(raw);
    const resolvedName = parsed.name || parsed.institutionName || DEFAULT_CONFIG.institutionName;
    const resolvedSession = parsed.academicSession || parsed.currentAcademicYear || DEFAULT_CONFIG.academicSession;
    return {
      ...DEFAULT_CONFIG,
      ...parsed,
      institutionName: resolvedName,
      name: resolvedName,
      motto: parsed.motto || DEFAULT_CONFIG.motto,
      academicSession: resolvedSession,
      currentAcademicYear: parsed.currentAcademicYear || resolvedSession,
      modules: { ...DEFAULT_CONFIG.modules, ...(parsed.modules || {}) },
      ai: { ...DEFAULT_CONFIG.ai, ...(parsed.ai || {}) },
    };
  } catch {
    return DEFAULT_CONFIG;
  }
}

export const useInstitutionStore = defineStore('institution', {
  state: () => loadStoredConfig(),

  getters: {
    isModuleEnabled: (state) => (moduleName) => {
      return state.modules?.[moduleName] !== false;
    },
    formattedSession: (state) => `${state.academicSession} • ${state.currentSemester}`,
  },

  actions: {
    updateConfig(newConfig) {
      Object.assign(this.$state, newConfig);
      this.persist();
    },

    saveConfig(updatedData) {
      if (updatedData) {
        if (updatedData.modules) {
          this.modules = { ...this.modules, ...updatedData.modules };
          delete updatedData.modules;
        }
        if (updatedData.ai) {
          this.ai = { ...this.ai, ...updatedData.ai };
          delete updatedData.ai;
        }
        Object.assign(this.$state, updatedData);
      }
      this.persist();
      this.syncWithBackend();
    },

    toggleModule(moduleKey) {
      if (this.modules && typeof this.modules[moduleKey] !== 'undefined') {
        this.modules[moduleKey] = !this.modules[moduleKey];
        this.persist();
      }
    },

    resetToDefaults() {
      Object.assign(this.$state, JSON.parse(JSON.stringify(DEFAULT_CONFIG)));
      this.persist();
      this.syncWithBackend();
    },

    persist() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(this.$state));
      } catch (err) {
        console.error('Failed to save institutional config to localStorage:', err);
      }
    },

    async fetchLiveConfig() {
      try {
        const live = await institutionApi.getConfig();
        if (live && (live.institutionName || live.name)) {
          const resolvedName = live.institutionName || live.name || this.institutionName;
          const resolvedSession = live.academicSession || live.currentAcademicYear || this.academicSession;
          const merged = {
            ...live,
            institutionName: resolvedName,
            name: resolvedName,
            motto: live.motto || this.motto || DEFAULT_CONFIG.motto,
            academicSession: resolvedSession,
            currentAcademicYear: live.currentAcademicYear || resolvedSession,
          };
          Object.assign(this.$state, merged);
          this.persist();
        }
      } catch (e) {
        // Fallback to local cache
      }
    },

    async syncWithBackend() {
      try {
        await institutionApi.updateConfig(this.$state);
      } catch (e) {
        // Backend might be offline in frontend-only development mode; continue gracefully
        console.warn('Backend sync deferred (running local cache mode):', e.message);
      }
    },
  },
});

export const useTenantStore = useInstitutionStore;
