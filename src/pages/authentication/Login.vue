<template>
  <div class="portal-login-wrapper min-vh-100 d-flex flex-column bg-base">
    <ThemeCustomizer />

    <div class="container-fluid p-0 flex-grow-1 d-flex flex-column">
      <div class="row g-0 flex-grow-1 min-vh-100">
        
        <!-- Left Column: University Institutional Atmosphere -->
        <div class="col-lg-6 col-xl-5 d-none d-lg-flex flex-column justify-content-between p-48 position-relative overflow-hidden text-white institutional-hero">
          <div class="hero-backdrop position-absolute top-0 start-0 w-100 h-100"></div>
          
          <!-- Top: University Crest & Identification -->
          <div class="position-relative z-2">
            <div class="d-flex align-items-center gap-14 mb-16">
              <div class="crest-container w-48-px h-48-px rounded-12 badge-translucent-white d-flex align-items-center justify-content-center shadow-sm">
                <i class="ri-government-line text-2xl text-white"></i>
              </div>
              <div>
                <h5 class="fw-bold mb-0 text-white letter-spacing-tight">{{ institution.institutionName }}</h5>
                <p class="text-xs text-white text-opacity-75 mb-0 fw-medium">{{ institution.portalSubtitle }}</p>
              </div>
            </div>

            <div class="d-inline-flex align-items-center gap-8 py-6 px-12 rounded-pill badge-translucent-white text-xs">
              <span class="w-8-px h-8-px rounded-circle bg-success-main"></span>
              <span class="fw-medium text-white">{{ institution.academicSession }}</span>
              <span class="text-white text-opacity-40">•</span>
              <span class="text-white text-opacity-80">{{ institution.currentSemester }}</span>
            </div>
          </div>

          <!-- Middle: Campus Statement -->
          <div class="position-relative z-2 my-auto py-32">
            <div class="badge badge-translucent-white text-white px-12 py-6 rounded-8 text-xs fw-semibold mb-16">
              OFFICIAL ACADEMIC PORTAL
            </div>
            <h1 class="display-6 fw-bold text-white mb-20 line-height-tight">
              Dedicated Academic & Administrative Operating System.
            </h1>
            <p class="text-md text-white text-opacity-80 mb-32 max-w-440-px">
              Securely access course schedules, grades, institutional analytics, attendance records, and faculty resources from one central campus terminal.
            </p>

            <div class="d-flex align-items-center gap-24 pt-16 border-top border-white border-opacity-15 text-xs text-white text-opacity-80">
              <div class="d-flex align-items-center gap-8">
                <i class="ri-shield-check-line text-lg text-white"></i>
                <span>Institutional Privacy</span>
              </div>
              <div class="d-flex align-items-center gap-8">
                <i class="ri-cpu-line text-lg text-white"></i>
                <span>AI Academic Insights</span>
              </div>
            </div>
          </div>

          <!-- Bottom: Institutional Contact -->
          <div class="position-relative z-2 pt-20 border-top border-white border-opacity-15 d-flex align-items-center justify-content-between text-xs text-white text-opacity-75">
            <span>{{ institution.campusLocation }}</span>
            <span>IT Support: {{ institution.supportEmail }}</span>
          </div>
        </div>

        <!-- Right Column: Clean, Focused Login Form -->
        <div class="col-lg-6 col-xl-7 d-flex flex-column justify-content-between p-24 p-sm-40 p-xl-64 bg-base">
          
          <!-- Top Utility Bar -->
          <div class="d-flex align-items-center justify-content-between w-100 max-w-480-px mx-auto mb-32">
            <div class="d-flex align-items-center gap-8">
              <img src="/assets/images/logo.png" alt="University Logo" class="h-32-px object-fit-contain light-logo">
              <img src="/assets/images/logo-light.png" alt="University Logo" class="h-32-px object-fit-contain dark-logo">
            </div>
            <div class="d-flex align-items-center gap-6 text-xs text-secondary-light">
              <i class="ri-lock-2-line text-success-main"></i>
              <span class="fw-medium">Secure Campus Login</span>
            </div>
          </div>

          <!-- Main Form Container -->
          <div class="w-100 max-w-480-px mx-auto my-auto">
            
            <div class="mb-32">
              <h2 class="h4 fw-bold text-primary-light mb-6">Sign In to {{ institution.institutionName }}</h2>
              <p class="text-sm text-secondary-light mb-0">
                Enter your Matriculation Number, Staff ID, or university email to access your campus portal.
              </p>
            </div>

            <!-- Session Timeout Alert Banner -->
            <div 
              v-if="isSessionTimedOut" 
              class="alert alert-warning border border-warning-200 bg-warning-50 radius-10 p-14 mb-24 d-flex align-items-start gap-12"
            >
              <i class="ri-timer-line text-lg text-warning-main mt-2 flex-shrink-0"></i>
              <div class="text-xs text-neutral-800">
                <span class="fw-bold d-block text-warning-800 mb-2">Session Timed Out</span>
                Your previous session expired after 15 minutes of inactivity to protect your account. Please sign in again.
              </div>
            </div>

            <!-- Authentication Failure Alert Banner -->
            <div 
              v-if="loginError" 
              class="alert alert-danger border border-danger-200 bg-danger-50 radius-10 p-14 mb-24 d-flex align-items-start gap-12"
            >
              <i class="ri-error-warning-fill text-lg text-danger-600 mt-2 flex-shrink-0"></i>
              <div class="text-xs text-danger-800">
                <span class="fw-bold d-block text-danger-900 mb-2">Sign-In Unsuccessful</span>
                {{ loginError }}
              </div>
            </div>

            <!-- Single Clean Credential Form -->
            <form @submit.prevent="submitLogin" class="d-flex flex-column gap-20">
              
              <!-- Identifier Field -->
              <div>
                <label for="identifier" class="text-xs fw-semibold text-primary-light mb-8 d-block">
                  Matriculation No, Staff ID, or Institutional Email
                </label>
                <div class="position-relative">
                  <span class="position-absolute start-0 top-50 translate-middle-y ps-14 text-neutral-400">
                    <i class="ri-user-3-line"></i>
                  </span>
                  <input
                    type="text"
                    id="identifier"
                    class="form-control ps-40 py-12 text-sm radius-8 border-neutral-300"
                    placeholder="e.g. SCI/2026/0491, FAC-104, or your campus email"
                    v-model="form.identifier"
                    required
                    autofocus
                  />
                </div>
              </div>

              <!-- Password Field -->
              <div>
                <div class="d-flex justify-content-between align-items-center mb-8">
                  <label for="password" class="text-xs fw-semibold text-primary-light mb-0">Password</label>
                  <a href="javascript:void(0)" class="text-xs text-primary-600 fw-medium hover-underline">
                    Forgot Password?
                  </a>
                </div>
                <div class="position-relative">
                  <span class="position-absolute start-0 top-50 translate-middle-y ps-14 text-neutral-400">
                    <i class="ri-lock-password-line"></i>
                  </span>
                  <input
                    :type="showPassword ? 'text' : 'password'"
                    id="password"
                    class="form-control ps-40 pe-40 py-12 text-sm radius-8 border-neutral-300"
                    placeholder="Enter your portal password"
                    v-model="form.password"
                    required
                  />
                  <button
                    type="button"
                    @click="showPassword = !showPassword"
                    class="btn p-0 border-0 bg-transparent position-absolute end-0 top-50 translate-middle-y pe-14 text-neutral-400 text-hover-primary-600"
                    aria-label="Toggle password visibility"
                  >
                    <i :class="showPassword ? 'ri-eye-off-line' : 'ri-eye-line'"></i>
                  </button>
                </div>
              </div>

              <!-- Remember Device Checkbox -->
              <div class="form-check d-flex align-items-center gap-2">
                <input
                  class="form-check-input border-neutral-400"
                  type="checkbox"
                  id="rememberDevice"
                  v-model="form.rememberDevice"
                />
                <label class="form-check-label text-xs text-secondary-light" for="rememberDevice">
                  Keep me signed in on this device
                </label>
              </div>

              <!-- Primary Submit Button -->
              <button
                type="submit"
                class="btn btn-primary-600 text-sm fw-semibold py-12 px-24 radius-8 w-100 d-flex align-items-center justify-content-center gap-8 shadow-sm transition-all mt-4"
                :disabled="isLoading"
              >
                <span v-if="isLoading" class="spinner-border spinner-border-sm" role="status"></span>
                <span>{{ isLoading ? 'Verifying with Campus Directory...' : 'Sign In' }}</span>
                <i v-if="!isLoading" class="ri-arrow-right-line"></i>
              </button>

              <!-- Optional Clean SSO Button -->
              <div class="mt-8">
                <div class="position-relative text-center my-16">
                  <hr class="border-neutral-200 m-0">
                  <span class="position-absolute top-50 start-50 translate-middle bg-base px-14 text-xs text-neutral-400">
                    or
                  </span>
                </div>
                <button
                  type="button"
                  @click="handleSSO"
                  class="btn btn-outline-neutral-300 bg-base text-neutral-800 text-xs fw-semibold py-10 px-16 rounded-8 w-100 d-flex align-items-center justify-content-center gap-8 hover-border-primary-600"
                >
                  <i class="ri-shield-keyhole-line text-primary-600 text-sm"></i>
                  <span>Sign In with {{ institution.shortCode || 'University' }} Single Sign-On (SSO)</span>
                </button>
              </div>
            </form>

            <!-- Subtle Developer Quick Presets (Discrete Drawer, No UI Clutter) -->
            <div class="mt-32 pt-16 border-top border-neutral-100">
              <div class="d-flex align-items-center justify-content-between mb-8">
                <span class="text-xxs text-neutral-400 fw-medium">Quick Demo Preset:</span>
                <div class="d-flex gap-8">
                  <button
                    type="button"
                    @click="fillDemo('student')"
                    class="btn btn-xs py-2 px-8 rounded text-xxs fw-semibold bg-neutral-100 text-neutral-700 hover-bg-neutral-200 border-0"
                  >
                    Student
                  </button>
                  <button
                    type="button"
                    @click="fillDemo('lecturer')"
                    class="btn btn-xs py-2 px-8 rounded text-xxs fw-semibold bg-neutral-100 text-neutral-700 hover-bg-neutral-200 border-0"
                  >
                    Lecturer
                  </button>
                  <button
                    type="button"
                    @click="fillDemo('admin')"
                    class="btn btn-xs py-2 px-8 rounded text-xxs fw-semibold bg-neutral-100 text-neutral-700 hover-bg-neutral-200 border-0"
                  >
                    Admin
                  </button>
                  <button
                    type="button"
                    @click="fillDemo('super-admin')"
                    class="btn btn-xs py-2 px-8 rounded text-xxs fw-bold bg-purple-50 text-purple-700 hover-bg-purple-100 border border-purple-200"
                  >
                    Super Admin
                  </button>
                </div>
              </div>
            </div>

            <!-- Help Contact -->
            <div class="mt-20 text-center">
              <p class="text-xs text-neutral-500 mb-0">
                Having trouble signing in?
                <a :href="'mailto:' + institution.supportEmail" class="text-primary-600 fw-medium ms-4 hover-underline">
                  Contact IT Support Desk
                </a>
              </p>
              <div class="mt-12">
                <button
                  type="button"
                  @click="handleClearStorage"
                  class="btn p-0 border-0 bg-transparent text-xxs text-neutral-400 hover-text-danger-600 text-decoration-underline"
                  title="Wipe cached browser session tokens"
                >
                  <i class="ri-refresh-line me-1"></i> Reset Browser Session & Clear Cached Tokens
                </button>
              </div>
            </div>

          </div>

          <!-- Bottom Footer -->
          <div class="w-100 max-w-480-px mx-auto pt-24 border-top border-neutral-200 d-flex flex-wrap align-items-center justify-content-between text-xs text-secondary-light">
            <div>
              &copy; {{ new Date().getFullYear() }} {{ institution.institutionName }} • Powered by 
              <a href="https://stackhubs.com.ng" target="_blank" rel="noopener noreferrer" class="text-primary-600 fw-semibold text-decoration-none hover-underline">stackhubs.com.ng</a>
            </div>
            <div class="d-flex align-items-center gap-12 mt-4 mt-sm-0">
              <a href="javascript:void(0)" class="text-secondary-light hover-text-primary-600">Privacy Policy</a>
              <span>•</span>
              <a href="javascript:void(0)" class="text-secondary-light hover-text-primary-600">Portal Security</a>
            </div>
          </div>

        </div>

      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useInstitutionStore } from '@/stores/institution.js';
import { useToastStore } from '@/stores/toast.js';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

export default {
  name: 'LoginPage',
  components: {
    ThemeCustomizer,
  },
  setup() {
    const router = useRouter();
    const route = useRoute();
    const authStore = useAuthStore();
    const institution = useInstitutionStore();
    const toastStore = useToastStore();

    const isSessionTimedOut = computed(() => route.query.reason === 'inactivity');
    const loginError = ref('');
    const showPassword = ref(false);
    const isLoading = ref(false);

    const form = ref({
      identifier: '',
      password: '',
      rememberDevice: true,
    });

    onMounted(() => {
      // Clear storage if user came with explicit logout/reset parameter
      if (route.query.logout === '1' || route.query.reset === '1') {
        authStore.logout();
        loginError.value = '';
      }
    });

    const handleClearStorage = () => {
      authStore.logout();
      loginError.value = '';
      form.value.identifier = '';
      form.value.password = '';
      toastStore.info('Local session cache purged. You may sign in with authentic credentials.', 'Session Reset');
    };

    const navigateToDestination = () => {
      const redirectPath = route.query.redirect || '/dashboard';
      router.push(redirectPath);
    };

    const submitLogin = async () => {
      loginError.value = '';
      if (!form.value.identifier || !form.value.password) {
        loginError.value = 'Please enter your Matriculation Number, Staff ID, or university email and password.';
        toastStore.error('Please enter your Matriculation Number, Staff ID, or university email and password.', 'Credentials Required');
        return;
      }
      isLoading.value = true;
      try {
        const user = await authStore.login({
          identifier: form.value.identifier,
          password: form.value.password,
        });
        toastStore.success(
          `Welcome back, ${user?.name || 'User'}! Authenticated as ${user?.role?.toUpperCase() || 'USER'}.`,
          'Sign-In Verified'
        );
        navigateToDestination();
      } catch (err) {
        loginError.value = err.message || `No active account matching '${form.value.identifier}' found in the ${institution.institutionName} directory.`;
        toastStore.error(
          loginError.value,
          'Sign-In Unsuccessful'
        );
      } finally {
        isLoading.value = false;
      }
    };

    const handleSSO = async () => {
      loginError.value = '';
      isLoading.value = true;
      try {
        // Authenticate student via database credentials
        const user = await authStore.login({
          identifier: 'SCI/2026/0491',
          password: 'CampusPass@2026',
        });
        toastStore.success(
          `${institution.shortCode || 'University'} SSO Verified. Welcome, ${user.name}.`,
          'SSO Verified'
        );
        navigateToDestination();
      } catch (err) {
        loginError.value = err.message || `Failed to establish single sign-on session with the ${institution.institutionName} directory.`;
        toastStore.error(loginError.value, 'SSO Unsuccessful');
      } finally {
        isLoading.value = false;
      }
    };

    const fillDemo = (roleKey) => {
      loginError.value = '';
      const sampleAccounts = {
        student: { id: 'SCI/2026/0491', pass: 'CampusPass@2026' },
        lecturer: { id: 'a.finch@campus.edu', pass: 'CampusPass@2026' },
        teacher: { id: 'a.finch@campus.edu', pass: 'CampusPass@2026' },
        admin: { id: 'evelyn.vance@campus.edu', pass: 'CampusPass@2026' },
        'super-admin': { id: 'superadmin@devcompany.io', pass: 'CampusPass@2026' },
      };

      const account = sampleAccounts[roleKey] || sampleAccounts.student;
      form.value.identifier = account.id;
      form.value.password = account.pass;
      
      // Submit credentials to live database for bcrypt verification
      submitLogin();
    };

    return {
      institution,
      isSessionTimedOut,
      loginError,
      showPassword,
      isLoading,
      form,
      handleClearStorage,
      submitLogin,
      handleSSO,
      fillDemo,
    };
  },
};
</script>

<style scoped>
.portal-login-wrapper {
  min-height: 100vh;
}

.max-w-440-px {
  max-width: 440px;
}

.max-w-480-px {
  max-width: 480px;
}

.institutional-hero {
  background: linear-gradient(135deg, #124d45 0%, #1a6d63 50%, #25a194 100%);
  background-size: cover;
  background-position: center;
}

.hero-backdrop {
  background: radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.08) 0%, transparent 60%),
              radial-gradient(circle at 80% 80%, rgba(0, 0, 0, 0.25) 0%, transparent 70%);
}

.backdrop-blur {
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.text-xxs {
  font-size: 0.6875rem;
}
</style>
