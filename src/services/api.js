import axios from 'axios';

const API_BASE_URL = import.meta.env?.VITE_API_BASE_URL || '/api/v1';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor: attach bearer token from localStorage
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('campus_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor: handle token expiration and unwrap response
apiClient.interceptors.response.use(
  (response) => response.data,
  (error) => {
    if (error.response && error.response.status === 401) {
      const requestUrl = error.config?.url || '';
      const isAuthApi = requestUrl.includes('/auth/login') || requestUrl.includes('/auth/quick-login');

      if (!isAuthApi && typeof window !== 'undefined') {
        const currentPath = window.location.pathname;
        const isAuthRoute = currentPath === '/' || currentPath === '/login' || currentPath === '/register' || currentPath === '/lock-screen';
        if (!isAuthRoute) {
          localStorage.removeItem('campus_token');
          localStorage.removeItem('campus_user');
          localStorage.removeItem('campus_role');
          window.location.href = '/login?reason=session_expired';
        }
      }
    }
    return Promise.reject(error);
  }
);

// Authentication & Tenant APIs
export const authApi = {
  getTenantInfo: () => apiClient.get('/auth/tenant-info'),
  login: (payload) => apiClient.post('/auth/login', payload),
  quickLogin: (role) => apiClient.post(`/auth/quick-login/${role}`),
  getMe: () => apiClient.get('/auth/me'),
  listAdmins: () => apiClient.get('/auth/admins'),
  createAdmin: (payload) => apiClient.post('/auth/admins', payload),
  deleteAdmin: (adminId) => apiClient.delete(`/auth/admins/${adminId}`),
};

// Institutional Configuration & CMS APIs
export const institutionApi = {
  getConfig: () => apiClient.get('/institution/config'),
  updateConfig: (payload) => apiClient.put('/institution/config', payload),
};

// Campus Notices & Circulars APIs
export const noticesApi = {
  getNotices: (audience) => apiClient.get('/notices', { params: audience ? { audience } : {} }),
  createNotice: (payload) => apiClient.post('/notices', payload),
  deleteNotice: (noticeId) => apiClient.delete(`/notices/${noticeId}`),
};

// Campus Telemetry & AI Early-Warning APIs
export const telemetryApi = {
  getOverview: () => apiClient.get('/telemetry/overview'),
  getRiskDossier: () => apiClient.get('/telemetry/ai-risk-dossier'),
  submitIntervention: (payload) => apiClient.post('/telemetry/intervene', payload),
};

// Academic Lecturers APIs
export const lecturersApi = {
  listLecturers: (params) => apiClient.get('/lecturers', { params }),
  getLecturerDetails: (id) => apiClient.get(`/lecturers/${id}`),
  createLecturer: (payload) => apiClient.post('/lecturers', payload),
};

// Student Academic Dossier APIs
export const studentsApi = {
  listStudents: (params) => apiClient.get('/students', { params }),
  getStudentDossier: (id) => apiClient.get(`/students/${id}`),
  getMyDossier: () => apiClient.get('/students/me'),
  enrollStudent: (payload) => apiClient.post('/students', payload),
  updateStudent: (id, payload) => apiClient.put(`/students/${id}`, payload),
  updateMyProfile: (payload) => apiClient.put('/students/me', payload),
  uploadAvatar: (id, formData) => apiClient.post(`/students/${id}/avatar`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  }),
};

// Courses & Examination APIs
export const coursesApi = {
  listCourses: (params) => apiClient.get('/courses', { params }),
  recordAttendance: (courseId, payload) => apiClient.post(`/courses/${courseId}/attendance`, payload),
  submitGrades: (courseId, payload) => apiClient.post(`/courses/${courseId}/grades`, payload),
};

// System Health & Diagnostics APIs
export const systemApi = {
  checkHealth: async () => {
    try {
      return await axios.get('/health', { timeout: 4000 });
    } catch {
      return await axios.get('http://127.0.0.1:8000/health', { timeout: 4000 });
    }
  },
};

export default apiClient;
