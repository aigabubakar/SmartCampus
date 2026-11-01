import { defineStore } from 'pinia';
import { useAuthStore } from './auth';
import { noticesApi } from '../services/api.js';

const NOTICES_STORAGE_KEY = 'campus_institutional_notices';

const DEFAULT_NOTICES = [
  {
    id: 1,
    title: 'Senate Approval of 2026/2027 Academic Calendar & Exam Schedule',
    description: 'The University Senate at its 348th Regular Session approved the official timeline for Harmattan Semester examinations commencing March 16, 2027. All faculties are advised to adhere strictly to the lecture period.',
    sender: 'Office of the Registrar',
    senderIcon: 'solar:document-text-bold',
    senderColor: 'bg-primary-50 text-primary-600',
    audience: 'all',
    priority: 'Urgent',
    priorityClass: 'bg-danger-subtle text-danger-700',
    date: '28 Oct 2026',
    date_raw: '2026-10-28',
    selected: false
  },
  {
    id: 2,
    title: 'National Accreditation Peer-Review Visit for College of AI & Computing',
    description: 'External accreditation panel from the National Universities Commission (NUC) is scheduled to evaluate computing laboratories, research outputs, and faculty credentials from November 12 to 15.',
    sender: 'Academic Planning Directorate',
    senderIcon: 'solar:diploma-bold',
    senderColor: 'bg-warning-50 text-warning-700',
    audience: 'faculty',
    priority: 'Important',
    priorityClass: 'bg-warning-subtle text-warning-800',
    date: '27 Oct 2026',
    date_raw: '2026-10-27',
    selected: false
  },
  {
    id: 3,
    title: 'Final Notice: Harmattan Semester Course Registration & Tuition Settlement',
    description: 'Late course registration and bursary tuition clearance will permanently close at midnight on Friday. Biometric digital examination passes will only be generated for 100% cleared students.',
    sender: 'University Bursary',
    senderIcon: 'solar:wallet-money-bold',
    senderColor: 'bg-danger-50 text-danger-600',
    audience: 'students',
    priority: 'Urgent',
    priorityClass: 'bg-danger-subtle text-danger-700',
    date: '25 Oct 2026',
    date_raw: '2026-10-25',
    selected: false
  },
  {
    id: 4,
    title: 'Annual University Research Exhibition & Tech Innovation Challenge 2026',
    description: 'Registration is now open for students and faculty research groups to present interdisciplinary research and software engineering projects at the Senate Exhibition Hall.',
    sender: 'Dean of Student Affairs',
    senderIcon: 'solar:cup-star-bold',
    senderColor: 'bg-success-50 text-success-700',
    audience: 'all',
    priority: 'Event',
    priorityClass: 'bg-success-subtle text-success-800',
    date: '22 Oct 2026',
    date_raw: '2026-10-22',
    selected: false
  },
  {
    id: 5,
    title: 'Continuous Assessment Test (CAT 1) Hall & CBT Terminal Allocations',
    description: 'All 200L to 400L students are required to verify their biometric CBT terminal seating allocations before Monday morning. Bring valid physical or digital institutional ID cards.',
    sender: 'Examinations & Records Board',
    senderIcon: 'solar:laptop-bold',
    senderColor: 'bg-cyan-50 text-cyan-700',
    audience: 'students',
    priority: 'Important',
    priorityClass: 'bg-warning-subtle text-warning-800',
    date: '20 Oct 2026',
    date_raw: '2026-10-20',
    selected: false
  },
  {
    id: 6,
    title: 'Call for International Research Fellowship & Conference Travel Grants',
    description: 'The Directorate of Research & International Collaborations invites applications from academic staff and post-doctoral fellows for the 2027 Global Innovation Travel Grant. Deadline is December 5.',
    sender: 'Directorate of Research',
    senderIcon: 'solar:globus-bold',
    senderColor: 'bg-purple-50 text-purple-700',
    audience: 'faculty',
    priority: 'General',
    priorityClass: 'bg-primary-subtle text-primary-700',
    date: '18 Oct 2026',
    date_raw: '2026-10-18',
    selected: false
  },
  {
    id: 7,
    title: 'Parent & Guardian Portal Access: Mid-Semester Progress Review',
    description: 'Ward grade reports and continuous assessment breakdown are now accessible via the Parent Gateway. Guardians can review academic standing and communicate directly with academic advisors.',
    sender: 'Registry / Public Relations',
    senderIcon: 'solar:users-group-two-rounded-bold',
    senderColor: 'bg-blue-50 text-blue-700',
    audience: 'guardians',
    priority: 'General',
    priorityClass: 'bg-neutral-200 text-neutral-800',
    date: '15 Oct 2026',
    date_raw: '2026-10-15',
    selected: false
  }
];

function loadNotices() {
  try {
    const raw = localStorage.getItem(NOTICES_STORAGE_KEY);
    if (!raw) return DEFAULT_NOTICES;
    return JSON.parse(raw);
  } catch {
    return DEFAULT_NOTICES;
  }
}

export const useNoticeStore = defineStore('notices', {
  state: () => ({
    notices: loadNotices(),
    searchQuery: '',
    selectedAudienceFilter: 'all'
  }),

  getters: {
    allNotices: (state) => state.notices,

    studentNotices: (state) => {
      return state.notices.filter(n => n.audience === 'all' || n.audience === 'students');
    },

    facultyNotices: (state) => {
      return state.notices.filter(n => n.audience === 'all' || n.audience === 'faculty');
    },

    guardianNotices: (state) => {
      return state.notices.filter(n => n.audience === 'all' || n.audience === 'guardians');
    },

    noticesForCurrentUser: (state) => {
      const authStore = useAuthStore();
      const role = authStore.currentRole || authStore.user?.role;

      if (role === 'student') {
        return state.notices.filter(n => n.audience === 'all' || n.audience === 'students');
      } else if (role === 'teacher') {
        return state.notices.filter(n => n.audience === 'all' || n.audience === 'faculty');
      } else if (role === 'guardian' || role === 'parent') {
        return state.notices.filter(n => n.audience === 'all' || n.audience === 'guardians');
      }
      return state.notices; // Admins and Super Admins see all notices
    }
  },

  actions: {
    persist() {
      localStorage.setItem(NOTICES_STORAGE_KEY, JSON.stringify(this.notices));
    },

    async fetchNotices() {
      try {
        const live = await noticesApi.getNotices();
        if (Array.isArray(live) && live.length > 0) {
          this.notices = live.map((n) => ({
            id: n.id,
            title: n.title,
            description: n.description,
            sender: n.sender || 'Office of the Registrar',
            senderIcon: n.priority === 'Urgent' ? 'solar:wallet-money-bold' : 'solar:document-text-bold',
            senderColor: n.priority === 'Urgent' ? 'bg-danger-50 text-danger-600' : 'bg-primary-50 text-primary-600',
            audience: n.audience || 'all',
            priority: n.priority || 'General',
            priorityClass:
              n.priority === 'Urgent'
                ? 'bg-danger-subtle text-danger-700'
                : n.priority === 'Important'
                ? 'bg-warning-subtle text-warning-800'
                : n.priority === 'Event'
                ? 'bg-success-subtle text-success-800'
                : 'bg-primary-subtle text-primary-700',
            date: n.date || 'Today',
            date_raw: n.date || new Date().toISOString().split('T')[0],
            selected: false,
          }));
          this.persist();
        }
      } catch (e) {
        // Fallback to local cache
      }
    },

    async addNotice(payload) {
      let createdId = this.notices.length > 0 ? Math.max(...this.notices.map((n) => n.id)) + 1 : 1;

      try {
        const res = await noticesApi.createNotice({
          title: payload.title,
          description: payload.description,
          sender: payload.sender || 'Office of the Registrar',
          audience: payload.audience || 'all',
          priority: payload.priority || 'General',
          date: payload.date || new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }),
        });
        if (res && res.id) {
          createdId = res.id;
        }
      } catch (e) {
        // Fallback to local ID
      }

      const newNotice = {
        id: createdId,
        title: payload.title,
        description: payload.description,
        sender: payload.sender || 'Office of the Registrar',
        senderIcon: payload.senderIcon || 'solar:document-text-bold',
        senderColor: payload.senderColor || 'bg-primary-50 text-primary-600',
        audience: payload.audience || 'all',
        priority: payload.priority || 'General',
        priorityClass:
          payload.priority === 'Urgent'
            ? 'bg-danger-subtle text-danger-700'
            : payload.priority === 'Important'
            ? 'bg-warning-subtle text-warning-800'
            : payload.priority === 'Event'
            ? 'bg-success-subtle text-success-800'
            : 'bg-primary-subtle text-primary-700',
        date: payload.date || new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }),
        date_raw: payload.date_raw || new Date().toISOString().split('T')[0],
        selected: false,
      };

      this.notices.unshift(newNotice);
      this.persist();
      return newNotice;
    },

    updateNotice(id, updates) {
      const index = this.notices.findIndex((n) => n.id === id);
      if (index !== -1) {
        this.notices[index] = {
          ...this.notices[index],
          ...updates,
        };
        this.persist();
      }
    },

    async deleteNotice(id) {
      try {
        await noticesApi.deleteNotice(id);
      } catch (e) {
        // Backend sync deferred
      }
      this.notices = this.notices.filter((n) => n.id !== id);
      this.persist();
    },
  },
});
