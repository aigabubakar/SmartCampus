<template>
  <div class="lock-screen-wrapper min-vh-100 d-flex flex-column justify-content-between position-relative overflow-hidden bg-base">
    <ThemeCustomizer />

    <!-- Ambient Institutional Background Decorative Glows -->
    <div class="glow-sphere glow-sphere-1 position-absolute top-0 start-0 pointer-events-none"></div>
    <div class="glow-sphere glow-sphere-2 position-absolute bottom-0 end-0 pointer-events-none"></div>

    <!-- Top Header Bar -->
    <header class="w-100 px-24 px-sm-40 py-20 d-flex align-items-center justify-content-between position-relative z-2">
      <div class="d-flex align-items-center gap-12">
        <div class="crest-container w-40-px h-40-px rounded-12 bg-primary-600 text-white d-flex align-items-center justify-content-center shadow-sm">
          <i class="ri-government-line text-xl"></i>
        </div>
        <div>
          <h6 class="fw-bold mb-0 text-primary-light letter-spacing-tight">{{ institution.institutionName }}</h6>
          <span class="text-xxs text-secondary-light fw-medium">{{ institution.portalSubtitle }}</span>
        </div>
      </div>

      <div class="d-flex align-items-center gap-8">
        <span class="badge bg-warning-50 text-warning-700 border border-warning-200 px-12 py-6 rounded-pill text-xs fw-semibold d-inline-flex align-items-center gap-6">
          <span class="w-8-px h-8-px rounded-circle bg-warning-main animate-pulse"></span>
          Workstation Locked
        </span>
      </div>
    </header>

    <!-- Main Centered Lock Card -->
    <main class="container py-24 my-auto position-relative z-2">
      <div class="row justify-content-center">
        <div class="col-12 col-sm-10 col-md-8 col-lg-5 col-xl-4">
          <div class="card border border-neutral-200 radius-16 shadow-lg bg-base overflow-hidden">
            <!-- Decorative Card Header Gradient -->
            <div class="card-hero-banner p-24 text-center text-white position-relative">
              <div class="position-relative z-2">
                <div class="position-relative d-inline-block mb-12">
                  <img
                    :src="userAvatar"
                    :alt="currentUser?.name || 'User'"
                    class="w-88-px h-88-px rounded-circle object-fit-cover border border-3 border-white shadow-md bg-white"
                    @error="onAvatarError"
                  />
                  <span class="position-absolute bottom-0 end-0 w-28-px h-28-px rounded-circle bg-warning-main text-white d-flex align-items-center justify-content-center shadow-sm border border-2 border-white">
                    <i class="ri-lock-2-fill text-xs"></i>
                  </span>
                </div>

                <h5 class="fw-bold mb-4 text-white line-height-tight">{{ currentUser?.name || 'Academic User' }}</h5>
                <p class="text-xs text-white text-opacity-80 mb-8">{{ currentUser?.email || institution.supportEmail }}</p>

                <div class="d-inline-flex align-items-center gap-6 px-12 py-5 rounded-pill badge-translucent-white text-xxs fw-bold uppercase letter-spacing-1 text-white shadow-sm">
                  <i :class="roleBadgeIcon"></i>
                  <span>{{ formatRoleTitle(currentUser?.role) }}</span>
                </div>
              </div>
            </div>

            <!-- Card Body: Password Entry -->
            <div class="card-body p-24 p-sm-32">
              <div class="text-center mb-20">
                <h6 class="text-md fw-bold text-primary-light mb-4">Resume Protected Session</h6>
                <p class="text-xs text-secondary-light mb-0">
                  Enter your account password to resume your workspace right where you paused.
                </p>
              </div>

              <!-- Error Alert -->
              <div v-if="errorMessage" class="alert alert-danger border border-danger-200 bg-danger-50 radius-8 p-12 mb-16 text-xs text-danger-700 d-flex align-items-center gap-8">
                <i class="ri-error-warning-line text-base flex-shrink-0"></i>
                <span>{{ errorMessage }}</span>
              </div>

              <!-- Unlock Form -->
              <form @submit.prevent="handleUnlock">
                <div class="mb-20">
                  <label for="lockPassword" class="form-label text-xs fw-semibold text-primary-light d-flex justify-content-between align-items-center">
                    <span>Account Password</span>
                    <button
                      type="button"
                      @click="autofillDemoPassword"
                      class="btn p-0 text-xxs text-primary-600 hover-text-primary-800 fw-semibold border-0 text-decoration-underline"
                    >
                      Autofill Demo
                    </button>
                  </label>
                  <div class="position-relative">
                    <input
                      id="lockPassword"
                      ref="passwordInputRef"
                      v-model="password"
                      :type="showPassword ? 'text' : 'password'"
                      class="form-control radius-8 pe-48 text-sm"
                      placeholder="••••••••••••"
                      autocomplete="current-password"
                      required
                      :disabled="isSubmitting"
                    />
                    <button
                      type="button"
                      class="position-absolute end-0 top-50 translate-middle-y me-12 text-secondary-light hover-text-primary border-0 bg-transparent"
                      @click="showPassword = !showPassword"
                      tabindex="-1"
                      aria-label="Toggle password visibility"
                    >
                      <i :class="showPassword ? 'ri-eye-off-line' : 'ri-eye-line'" class="text-md"></i>
                    </button>
                  </div>
                </div>

                <button
                  type="submit"
                  class="btn btn-primary text-sm btn-sm px-16 py-12 w-100 radius-8 d-flex align-items-center justify-content-center gap-8 fw-semibold shadow-sm"
                  :disabled="isSubmitting || !password"
                >
                  <span v-if="isSubmitting" class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                  <i v-else class="ri-lock-unlock-line text-lg"></i>
                  <span>{{ isSubmitting ? 'Verifying Credentials...' : 'Unlock Workstation' }}</span>
                </button>
              </form>

              <!-- Account Switcher / Logout Option -->
              <div class="pt-20 mt-20 border-top border-neutral-200 text-center">
                <p class="text-xs text-secondary-light mb-12">
                  Not <strong class="text-primary-light">{{ currentUser?.name || 'you' }}</strong> or need a different account?
                </p>
                <button
                  type="button"
                  @click="handleSwitchAccount"
                  class="btn btn-outline-neutral text-xs py-8 px-16 radius-8 w-100 d-inline-flex align-items-center justify-content-center gap-6"
                >
                  <i class="ri-user-shared-line"></i>
                  <span>Switch Account / Sign In as Different User</span>
                </button>
              </div>

              <!-- Session Security Status -->
              <div class="mt-16 text-center">
                <span class="text-xxs text-neutral-400 d-inline-flex align-items-center gap-4">
                  <i class="ri-shield-check-line text-success-main"></i>
                  Session Secured &bull; {{ institution.institutionName }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>

    <!-- Bottom Institutional & Provider Footer -->
    <footer class="w-100 px-24 px-sm-40 py-16 position-relative z-2 border-top border-neutral-200 bg-base">
      <div class="container-fluid p-0 d-flex flex-column flex-sm-row align-items-center justify-content-between gap-12 text-xs text-secondary-light">
        <div>
          &copy; {{ currentYear }} {{ institution.institutionName }} • All Rights Reserved.
        </div>
        <div>
          Powered by
          <a
            href="https://stackhubs.com.ng"
            target="_blank"
            rel="noopener noreferrer"
            class="text-primary-600 fw-semibold text-decoration-none hover-underline ms-4"
          >
            stackhubs.com.ng
          </a>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import { ref, computed, onMounted, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useInstitutionStore } from '@/stores/institution.js';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

export default {
  name: 'LockScreen',
  components: {
    ThemeCustomizer,
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const institution = useInstitutionStore();

    const password = ref('');
    const showPassword = ref(false);
    const isSubmitting = ref(false);
    const errorMessage = ref('');
    const passwordInputRef = ref(null);
    const avatarFallbackTriggered = ref(false);

    const currentUser = computed(() => authStore.currentUser);
    const currentYear = new Date().getFullYear();

    const userAvatar = computed(() => {
      if (avatarFallbackTriggered.value) {
        return '/assets/images/users/user1.png';
      }
      return currentUser.value?.avatar || '/assets/images/users/user1.png';
    });

    const onAvatarError = () => {
      avatarFallbackTriggered.value = true;
    };

    const roleBadgeIcon = computed(() => {
      const role = currentUser.value?.role;
      switch (role) {
        case 'super-admin':
          return 'ri-shield-star-line';
        case 'admin':
          return 'ri-admin-line';
        case 'lecturer':
        case 'teacher':
          return 'ri-book-read-line';
        case 'student':
          return 'ri-graduation-cap-line';
        default:
          return 'ri-user-line';
      }
    });

    const formatRoleTitle = (role) => {
      if (!role) return 'ACADEMIC USER';
      if (role === 'teacher' || role === 'lecturer') return 'LECTURER';
      return role.replace('-', ' ').toUpperCase();
    };

    const sessionDigest = computed(() => {
      const token = authStore.token || 'CAMPUS-ACTIVE-SESSION';
      return token.substring(0, 14) + '...';
    });

    const autofillDemoPassword = () => {
      password.value = 'CampusSecure2026!';
      errorMessage.value = '';
      if (passwordInputRef.value) {
        passwordInputRef.value.focus();
      }
    };

    const handleUnlock = async () => {
      errorMessage.value = '';
      if (!password.value || password.value.trim().length < 4) {
        errorMessage.value = 'Please enter your password (minimum 4 characters).';
        return;
      }

      isSubmitting.value = true;
      try {
        await new Promise((resolve) => setTimeout(resolve, 350)); // smooth micro-interaction
        authStore.unlockScreen(password.value);
        const destination = authStore.lockedRedirect || '/dashboard';
        router.push(destination);
      } catch (err) {
        errorMessage.value = err.message || 'Authentication failed. Please verify your password.';
      } finally {
        isSubmitting.value = false;
      }
    };

    const handleSwitchAccount = () => {
      authStore.logout();
      router.push('/login');
    };

    onMounted(() => {
      // If user is not authenticated, navigate to login
      if (!authStore.isAuthenticated) {
        router.replace('/login');
        return;
      }

      // If user is not locked, navigate to dashboard
      if (!authStore.isLocked) {
        router.replace(authStore.lockedRedirect || '/dashboard');
        return;
      }

      nextTick(() => {
        if (passwordInputRef.value) {
          passwordInputRef.value.focus();
        }
      });
    });

    return {
      institution,
      currentUser,
      password,
      showPassword,
      isSubmitting,
      errorMessage,
      passwordInputRef,
      userAvatar,
      onAvatarError,
      roleBadgeIcon,
      formatRoleTitle,
      sessionDigest,
      currentYear,
      autofillDemoPassword,
      handleUnlock,
      handleSwitchAccount,
    };
  },
};
</script>

<style scoped>
.lock-screen-wrapper {
  background-color: var(--bs-body-bg, #f4f6fa);
}

.card-hero-banner {
  background: linear-gradient(135deg, #124d45 0%, #1a6d63 50%, #25a194 100%);
}

.glow-sphere {
  width: 480px;
  height: 480px;
  border-radius: 50%;
  filter: blur(120px);
  opacity: 0.15;
}

.glow-sphere-1 {
  background: #1a6d63;
  transform: translate(-30%, -30%);
}

.glow-sphere-2 {
  background: #25a194;
  transform: translate(30%, 30%);
}

.pointer-events-none {
  pointer-events: none;
}

.backdrop-blur {
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
}

.text-xxs {
  font-size: 0.6875rem;
}

.w-88-px {
  width: 88px;
}

.h-88-px {
  height: 88px;
}

.radius-16 {
  border-radius: 16px;
}

.hover-underline:hover {
  text-decoration: underline !important;
}
</style>
