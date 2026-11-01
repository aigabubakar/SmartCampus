import { defineStore } from 'pinia';
import { useToastStore } from './toast.js';
import { authApi } from '../services/api.js';

const ADMIN_STORAGE_KEY = 'campus_admin_users';

const DEFAULT_ADMIN_USERS = [
  {
    id: 'ADM-001',
    name: 'System Super Administrator',
    email: 'superadmin@devcompany.io',
    staffId: 'ROOT-SYS-001',
    role: 'super-admin',
    scope: 'Platform Owner / Absolute Root Control',
    department: 'Software Engineering & Managed Systems',
    status: 'Active',
    dateCreated: '01 Jan 2026',
    isRoot: true,
    avatar: '/assets/images/thumbs/leave-request-img2.png',
    permissions: ['all_access', 'manage_admins', 'system_cms', 'ai_governance', 'database_control'],
  },
  {
    id: 'ADM-002',
    name: 'Dr. Evelyn Vance',
    email: 'evelyn.vance@campus.edu',
    staffId: 'STAFF-ADM-01',
    role: 'admin',
    scope: 'Full Campus Operations',
    department: 'Vice Chancellor / Executive Office',
    status: 'Active',
    dateCreated: '12 Jan 2026',
    isRoot: false,
    avatar: '/assets/images/thumbs/leave-request-img1.png',
    permissions: ['curriculum', 'admissions', 'grading_approvals', 'ai_override', 'staff_management'],
  },
  {
    id: 'ADM-003',
    name: 'Marcus Holloway',
    email: 'm.holloway@campus.edu',
    staffId: 'STAFF-REG-04',
    role: 'admin',
    scope: 'Academic & Examinations',
    department: 'Academic Registrar Office',
    status: 'Active',
    dateCreated: '18 Feb 2026',
    isRoot: false,
    avatar: '/assets/images/thumbs/user-img1.png',
    permissions: ['curriculum', 'grading_approvals', 'transcripts', 'exam_schedules'],
  },
  {
    id: 'ADM-004',
    name: 'Linda Kowalski',
    email: 'l.kowalski@campus.edu',
    staffId: 'STAFF-FIN-09',
    role: 'admin',
    scope: 'Finance & Bursary',
    department: 'University Bursary & Collections',
    status: 'Active',
    dateCreated: '05 Mar 2026',
    isRoot: false,
    avatar: '/assets/images/thumbs/user-img2.png',
    permissions: ['fee_structures', 'payroll', 'accounts_audit', 'fee_discounts'],
  },
  {
    id: 'ADM-005',
    name: 'Darius Sterling',
    email: 'd.sterling@campus.edu',
    staffId: 'STAFF-ADM-12',
    role: 'admin',
    scope: 'Admissions & Student Affairs',
    department: 'Undergraduate Admissions Board',
    status: 'Suspended',
    dateCreated: '20 Apr 2026',
    isRoot: false,
    avatar: '/assets/images/thumbs/user-img3.png',
    permissions: ['admissions', 'student_records'],
  },
];

function loadAdminUsers() {
  try {
    const raw = localStorage.getItem(ADMIN_STORAGE_KEY);
    if (!raw) return DEFAULT_ADMIN_USERS;
    return JSON.parse(raw);
  } catch {
    return DEFAULT_ADMIN_USERS;
  }
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('campus_user') || 'null'),
    token: localStorage.getItem('campus_token') || null,
    role: localStorage.getItem('campus_role') || null,
    isAuthenticated: !!localStorage.getItem('campus_token'),
    adminUsers: loadAdminUsers(),

    // Inactivity Session Management (15 minutes threshold, 60s warning)
    lastActiveTime: Number(localStorage.getItem('campus_last_active')) || Date.now(),
    sessionTimeoutMs: 15 * 60 * 1000,
    warningThresholdMs: 60 * 1000,
    isWarningModalOpen: false,
    secondsRemaining: 60,

    // Locked Screen Security
    isLocked: localStorage.getItem('campus_screen_locked') === 'true',
    lockedRedirect: localStorage.getItem('campus_locked_redirect') || '/dashboard',
  }),

  getters: {
    currentUser: (state) => state.user,
    currentRole: (state) => state.role,
    isSuperAdmin: (state) => state.role === 'super-admin' || state.user?.isRoot === true,
    isAdmin: (state) => state.role === 'admin' || state.role === 'super-admin',
    canManageAdmins: (state) => state.role === 'super-admin' || state.user?.isRoot === true,
    isLecturer: (state) => state.role === 'lecturer' || state.role === 'teacher',
    isTeacher: (state) => state.role === 'teacher' || state.role === 'lecturer',
    isStudent: (state) => state.role === 'student',
    isGuardian: (state) => state.role === 'guardian' || state.role === 'parent',
    allAdmins: (state) => state.adminUsers,

    isSessionExpired: (state) => {
      if (!state.isAuthenticated) return false;
      const lastActive = state.lastActiveTime || Number(localStorage.getItem('campus_last_active')) || 0;
      return (Date.now() - lastActive) >= state.sessionTimeoutMs;
    },
    idleTimeMs: (state) => Math.max(0, Date.now() - (state.lastActiveTime || Date.now())),
  },

  actions: {
    setAuthSession({ user, token, role }) {
      this.user = user;
      this.token = token;
      this.role = role || user?.role || 'student';
      this.isAuthenticated = true;
      this.lastActiveTime = Date.now();
      this.isWarningModalOpen = false;

      localStorage.setItem('campus_user', JSON.stringify(this.user));
      localStorage.setItem('campus_token', this.token);
      localStorage.setItem('campus_role', this.role);
      localStorage.setItem('campus_last_active', String(this.lastActiveTime));
    },

    async quickLogin(roleType) {
      // Live backend database authentication only
      try {
        const res = await authApi.quickLogin(roleType);
        if (res && res.user && res.access_token) {
          const profile = {
            ...res.user,
            matricNumber: res.user.matric_number || res.user.matricNumber,
            staffId: res.user.staff_id || res.user.staffId,
          };
          this.setAuthSession({
            user: profile,
            token: res.access_token,
            role: profile.role,
          });
          return profile;
        }
        throw new Error(`Failed to retrieve authentic credentials for role ${roleType}.`);
      } catch (err) {
        const errorDetail = err.response?.data?.detail || err.message || 'Live database quick-login unavailable.';
        throw new Error(errorDetail);
      }
    },

    async login({ identifier, password, role = null }) {
      if (!identifier || !identifier.trim()) {
        throw new Error('Please enter your Matriculation Number, Staff ID, or university email.');
      }
      if (!password) {
        throw new Error('Please enter your portal password.');
      }

      try {
        const res = await authApi.login({
          identifier: identifier.trim(),
          password: password,
          audience: role || 'student',
        });
        if (res && res.user && res.access_token) {
          const profile = {
            ...res.user,
            matricNumber: res.user.matric_number || res.user.matricNumber,
            staffId: res.user.staff_id || res.user.staffId,
          };
          this.setAuthSession({
            user: profile,
            token: res.access_token,
            role: profile.role,
          });
          return profile;
        }
        throw new Error('Unexpected response from the university authentication service.');
      } catch (err) {
        const errorDetail = err.response?.data?.detail || err.message || 'Unable to verify credentials with the university directory.';
        throw new Error(errorDetail);
      }
    },

    async verifySession() {
      if (!this.token) return false;
      try {
        const userProfile = await authApi.getMe();
        if (userProfile) {
          this.user = {
            ...userProfile,
            matricNumber: userProfile.matric_number || userProfile.matricNumber,
            staffId: userProfile.staff_id || userProfile.staffId,
          };
          this.role = userProfile.role;
          localStorage.setItem('campus_user', JSON.stringify(this.user));
          localStorage.setItem('campus_role', this.role);
          return true;
        }
      } catch (err) {
        if (err.response && (err.response.status === 401 || err.response.status === 403)) {
          this.logout();
          return false;
        }
      }
      return true;
    },

    updateUserProfile(updates) {
      if (!this.user) return;
      this.user = {
        ...this.user,
        ...updates,
      };
      try {
        localStorage.setItem('campus_user', JSON.stringify(this.user));
      } catch (err) {
        console.error('Failed to update local user session:', err);
      }
    },

    logout() {
      this.user = null;
      this.token = null;
      this.role = null;
      this.isAuthenticated = false;
      this.isLocked = false;
      this.isWarningModalOpen = false;

      localStorage.removeItem('campus_user');
      localStorage.removeItem('campus_token');
      localStorage.removeItem('campus_role');
      localStorage.removeItem('campus_last_active');
      localStorage.removeItem('campus_screen_locked');
      localStorage.removeItem('campus_locked_redirect');
    },

    // ================= INACTIVITY & SESSION TIMEOUT MANAGEMENT =================

    recordUserActivity(force = false) {
      if (!this.isAuthenticated) return;
      const now = Date.now();
      // Throttle updates: avoid writing to localStorage more than once every 5 seconds unless forced
      if (!force && now - this.lastActiveTime < 5000) return;

      this.lastActiveTime = now;
      this.isWarningModalOpen = false;
      try {
        localStorage.setItem('campus_last_active', String(now));
      } catch {
        // quota or private mode fallback
      }
    },

    extendSession() {
      this.recordUserActivity(true);
      this.isWarningModalOpen = false;
      try {
        const toastStore = useToastStore();
        toastStore.info('Your active working session has been extended by 15 minutes.', 'Session Extended');
      } catch {
        // ignore if not ready
      }
    },

    checkInactivity() {
      if (!this.isAuthenticated) return false;

      // Cross-tab synchronization check: if another tab was active more recently, respect it
      const storedLastActive = Number(localStorage.getItem('campus_last_active') || 0);
      if (storedLastActive > this.lastActiveTime) {
        this.lastActiveTime = storedLastActive;
      }

      const elapsed = Date.now() - this.lastActiveTime;

      // 1. Fully expired (>= 15 minutes)
      if (elapsed >= this.sessionTimeoutMs) {
        this.handleSessionTimeout('inactivity');
        return true;
      }

      // 2. Approaching expiration (< 60 seconds remaining)
      if (elapsed >= (this.sessionTimeoutMs - this.warningThresholdMs)) {
        this.isWarningModalOpen = true;
        this.secondsRemaining = Math.max(0, Math.ceil((this.sessionTimeoutMs - elapsed) / 1000));
      } else {
        this.isWarningModalOpen = false;
      }

      return false;
    },

    handleSessionTimeout(reason = 'inactivity') {
      this.isWarningModalOpen = false;
      this.logout();
      try {
        const toastStore = useToastStore();
        toastStore.warning(
          'Your session expired due to 15 minutes of inactivity. Please log in again to continue.',
          'Session Expired'
        );
      } catch {
        // ignore
      }
    },

    // ================= WORKSTATION LOCK SCREEN ACTIONS =================

    lockScreen(redirectPath = '/dashboard') {
      if (!this.isAuthenticated) return;

      this.isLocked = true;
      this.lockedRedirect = redirectPath || '/dashboard';
      this.isWarningModalOpen = false;

      try {
        localStorage.setItem('campus_screen_locked', 'true');
        localStorage.setItem('campus_locked_redirect', this.lockedRedirect);
      } catch {
        // quota fallback
      }

      try {
        const toastStore = useToastStore();
        toastStore.info(
          'Workstation Secured: Re-enter your credentials to resume your session.',
          'Screen Locked'
        );
      } catch {
        // ignore
      }
    },

    async unlockScreen(password) {
      if (!password || !password.trim()) {
        throw new Error('Please enter your account password.');
      }

      const identifier = this.user?.email || this.user?.matricNumber || this.user?.staffId || this.user?.id;
      if (identifier) {
        // Authenticate password with backend database
        await this.login({ identifier, password, role: this.role });
      }

      this.isLocked = false;
      this.recordUserActivity(true);

      try {
        localStorage.removeItem('campus_screen_locked');
        localStorage.removeItem('campus_locked_redirect');
      } catch {
        // quota fallback
      }

      try {
        const toastStore = useToastStore();
        const userName = this.user?.name ? ` ${this.user.name}` : '';
        toastStore.success(`Session Restored — Welcome back${userName}!`, 'Screen Unlocked');
      } catch {
        // ignore
      }

      return true;
    },

    // ================= SUPER ADMIN GOVERNANCE ACTIONS =================

    async fetchAdmins() {
      try {
        const liveAdmins = await authApi.listAdmins();
        if (Array.isArray(liveAdmins) && liveAdmins.length > 0) {
          this.adminUsers = liveAdmins;
          this.persistAdmins();
          return liveAdmins;
        }
      } catch (err) {
        // Offline resilience
      }
      return this.adminUsers;
    },

    async createUniversityAdmin(payload) {
      if (!this.canManageAdmins) {
        throw new Error('Access Denied: Only Super Admin can provision new university administrators.');
      }

      let created = null;
      try {
        created = await authApi.createAdmin({
          name: payload.name,
          email: payload.email,
          role: payload.role || 'admin',
          department: payload.department || 'Academic Administration',
          permissions: payload.permissions || ['curriculum', 'admissions'],
          password: payload.password || 'CampusPass@2026',
        });
      } catch (err) {
        // fallback
      }

      const newAdmin = {
        id: created?.id || `ADM-00${this.adminUsers.length + 1}`,
        name: created?.name || payload.name,
        email: created?.email || payload.email,
        staffId: created?.id || payload.staffId || `STAFF-ADM-${Math.floor(10 + Math.random() * 90)}`,
        role: created?.role || 'admin',
        scope: payload.scope || 'Academic Operations',
        department: created?.department || payload.department || 'Academic Administration',
        status: created?.status || 'Active',
        dateCreated: new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }),
        isRoot: false,
        avatar: '/assets/images/thumbs/leave-request-img1.png',
        permissions: created?.permissions || payload.permissions || ['curriculum', 'admissions'],
      };

      this.adminUsers.unshift(newAdmin);
      this.persistAdmins();
      return newAdmin;
    },

    updateAdminUser(id, updates) {
      const admin = this.adminUsers.find((a) => a.id === id);
      if (!admin) return false;

      if (admin.isRoot && updates.role && updates.role !== 'super-admin') {
        throw new Error('Root Super Administrator privileges cannot be downgraded.');
      }

      Object.assign(admin, updates);
      this.persistAdmins();
      return admin;
    },

    toggleAdminStatus(id) {
      const admin = this.adminUsers.find((a) => a.id === id);
      if (!admin) return false;

      if (admin.isRoot) {
        throw new Error('Root Super Administrator cannot be suspended.');
      }

      admin.status = admin.status === 'Active' ? 'Suspended' : 'Active';
      this.persistAdmins();
      return admin;
    },

    async deleteAdminUser(id) {
      const adminIndex = this.adminUsers.findIndex((a) => a.id === id);
      if (adminIndex === -1) return false;

      if (this.adminUsers[adminIndex].isRoot) {
        throw new Error('Root Super Administrator is immutable and cannot be deleted.');
      }

      try {
        await authApi.deleteAdmin(id);
      } catch (err) {
        // ignore offline error
      }

      this.adminUsers.splice(adminIndex, 1);
      this.persistAdmins();
      return true;
    },

    persistAdmins() {
      try {
        localStorage.setItem(ADMIN_STORAGE_KEY, JSON.stringify(this.adminUsers));
      } catch (err) {
        console.error('Failed to persist admin users:', err);
      }
    },
  },
});
