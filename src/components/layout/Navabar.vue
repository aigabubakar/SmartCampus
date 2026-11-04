<template>
  <div class="navbar-header shadow-1">
    <div class="row align-items-center justify-content-between">
      <div class="col-auto">
        <div class="d-flex flex-wrap align-items-center gap-4">
          <button type="button" class="sidebar-mobile-toggle" aria-label="Sidebar Mobile Toggler Button" @click="toggleMobileSidebar">
            <iconify-icon icon="heroicons:bars-3-solid" class="icon"></iconify-icon>
          </button>
          <form class="navbar-search">
            <input type="text" class="bg-transparent" name="search" placeholder="Search">
            <iconify-icon icon="ion:search-outline" class="icon"></iconify-icon>
          </form>
        </div>
      </div>
      <div class="col-auto">
        <div class="d-flex flex-wrap align-items-center gap-3">
          <!-- 1. Theme Toggle Button -->
          <button type="button" 
            class="navbar-action-btn navbar-theme-btn w-40-px h-40-px rounded-circle d-flex justify-content-center align-items-center text-white border-0 cursor-pointer"
            :class="isDark ? 'navbar-theme-dark' : 'navbar-theme-light'"
            aria-label="Dark & Light Mode Button" 
            :title="isDark ? 'Switch to Day Light Mode' : 'Switch to Night Dark Mode'" 
            @click="toggleTheme">
             <i class="text-lg text-white" :class="isDark ? 'ri-moon-line' : 'ri-sun-line'"></i>
          </button>

          <!-- 2. Lock Workstation Button -->
          <button type="button" 
            class="navbar-action-btn navbar-lock-btn w-40-px h-40-px rounded-circle d-flex justify-content-center align-items-center text-white border-0 cursor-pointer"
            aria-label="Lock Workstation" 
            title="Lock Workstation Session" 
            @click="handleLockScreen">
             <i class="ri-lock-2-line text-lg text-white"></i>
          </button>

          <div class="dropdown">
            <button
              class="navbar-action-btn navbar-notif-btn has-indicator w-40-px h-40-px rounded-circle d-flex justify-content-center align-items-center position-relative text-white border-0 cursor-pointer"
              type="button" data-bs-toggle="dropdown" aria-label="Notification Button" title="Campus Circulars & Notifications">
              <i class="ri-notification-3-line text-lg text-white"></i>
              <span class="w-10-px h-10-px bg-danger-600 border border-white border-2 position-absolute end-0 top-0 rounded-circle mt-1 me-1"></span>
            </button>
            <div class="dropdown-menu to-top dropdown-menu-lg p-0">
              <div
                class="m-16 py-12 px-16 radius-8 bg-primary-50 mb-16 d-flex align-items-center justify-content-between gap-2">
                <div>
                  <h6 class="text-lg text-primary-light fw-semibold mb-0">Notifications</h6>
                </div>
                <span
                  class="text-primary-600 fw-semibold text-lg w-40-px h-40-px rounded-circle bg-base d-flex justify-content-center align-items-center">05</span>
              </div>

              <div class="max-h-400-px overflow-y-auto scroll-sm pe-4">
                <a href="javascript:void(0)"
                  class="px-24 py-12 d-flex align-items-start gap-3 mb-2 justify-content-between">
                  <div class="text-black hover-bg-transparent hover-text-primary d-flex align-items-center gap-3">
                    <span
                      class="w-44-px h-44-px bg-success-subtle text-success-main rounded-circle d-flex justify-content-center align-items-center flex-shrink-0">
                      <iconify-icon icon="bitcoin-icons:verify-outline" class="icon text-xxl"></iconify-icon>
                    </span>
                    <div>
                      <h6 class="text-md fw-semibold mb-4">Congratulations</h6>
                      <p class="mb-0 text-sm text-secondary-light text-w-200-px">Your profile has been Verified. Your
                        profile has been Verified</p>
                    </div>
                  </div>
                  <span class="text-sm text-secondary-light flex-shrink-0">23 Mins ago</span>
                </a>

                <a href="javascript:void(0)"
                  class="px-24 py-12 d-flex align-items-start gap-3 mb-2 justify-content-between bg-neutral-50">
                  <div class="text-black hover-bg-transparent hover-text-primary d-flex align-items-center gap-3">
                    <span
                      class="w-44-px h-44-px bg-success-subtle text-success-main rounded-circle d-flex justify-content-center align-items-center flex-shrink-0">
                      <img src="/assets/images/notification/profile-1.png" alt="Image">
                    </span>
                    <div>
                      <h6 class="text-md fw-semibold mb-4">Ronald Richards</h6>
                      <p class="mb-0 text-sm text-secondary-light text-w-200-px">You can stitch between artboards</p>
                    </div>
                  </div>
                  <span class="text-sm text-secondary-light flex-shrink-0">23 Mins ago</span>
                </a>

                <a href="javascript:void(0)"
                  class="px-24 py-12 d-flex align-items-start gap-3 mb-2 justify-content-between">
                  <div class="text-black hover-bg-transparent hover-text-primary d-flex align-items-center gap-3">
                    <span
                      class="w-44-px h-44-px bg-info-subtle text-info-main rounded-circle d-flex justify-content-center align-items-center flex-shrink-0">
                      AM
                    </span>
                    <div>
                      <h6 class="text-md fw-semibold mb-4">Arlene McCoy</h6>
                      <p class="mb-0 text-sm text-secondary-light text-w-200-px">Invite you to prototyping</p>
                    </div>
                  </div>
                  <span class="text-sm text-secondary-light flex-shrink-0">23 Mins ago</span>
                </a>

                <a href="javascript:void(0)"
                  class="px-24 py-12 d-flex align-items-start gap-3 mb-2 justify-content-between bg-neutral-50">
                  <div class="text-black hover-bg-transparent hover-text-primary d-flex align-items-center gap-3">
                    <span
                      class="w-44-px h-44-px bg-success-subtle text-success-main rounded-circle d-flex justify-content-center align-items-center flex-shrink-0">
                      <img src="/assets/images/notification/profile-2.png" alt="Image">
                    </span>
                    <div>
                      <h6 class="text-md fw-semibold mb-4">Robiul Hasan</h6>
                      <p class="mb-0 text-sm text-secondary-light text-w-200-px">Invite you to prototyping</p>
                    </div>
                  </div>
                  <span class="text-sm text-secondary-light flex-shrink-0">23 Mins ago</span>
                </a>

                <a href="javascript:void(0)"
                  class="px-24 py-12 d-flex align-items-start gap-3 mb-2 justify-content-between">
                  <div class="text-black hover-bg-transparent hover-text-primary d-flex align-items-center gap-3">
                    <span
                      class="w-44-px h-44-px bg-info-subtle text-info-main rounded-circle d-flex justify-content-center align-items-center flex-shrink-0">
                      DR
                    </span>
                    <div>
                      <h6 class="text-md fw-semibold mb-4">Darlene Robertson</h6>
                      <p class="mb-0 text-sm text-secondary-light text-w-200-px">Invite you to prototyping</p>
                    </div>
                  </div>
                  <span class="text-sm text-secondary-light flex-shrink-0">23 Mins ago</span>
                </a>
              </div>

              <div class="text-center py-12 px-16">
                <a href="javascript:void(0)" class="text-primary-600 fw-semibold text-md hover-underline">See All
                  Notification</a>
              </div>

            </div>
          </div><!-- Notification dropdown end -->

          <!-- 4. Quick Logout Button -->
          <button type="button" 
            class="navbar-action-btn navbar-logout-btn w-40-px h-40-px rounded-circle d-flex justify-content-center align-items-center text-white border-0 cursor-pointer"
            aria-label="Sign Out" 
            title="Sign Out / Log Out" 
            @click="handleLogout">
             <i class="ri-logout-box-r-line text-lg text-white"></i>
          </button>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: "Navabar",
  data() {
    return {
      isDark: false
    }
  },
  methods: {
    handleLockScreen() {
      const authStore = useAuthStore();
      authStore.lockScreen(this.$route.fullPath);
      this.$router.push('/lock-screen');
    },
    handleLogout() {
      const authStore = useAuthStore();
      const toastStore = useToastStore();
      authStore.logout();
      toastStore.info('Your active session has been securely closed.', 'Signed Out');
      this.$router.push('/login');
    },
    toggleTheme() {
      this.isDark = !this.isDark;
      const theme = this.isDark ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
    },
    toggleMobileSidebar() {
      const sidebar = document.querySelector('.sidebar');
      const overlay = document.querySelector('.overlay');
      if (sidebar && overlay) {
        sidebar.classList.toggle('sidebar-open');
        if (sidebar.classList.contains('sidebar-open')) {
          sidebar.classList.add('open');
          overlay.classList.remove('visibility-hidden', 'opacity-0');
          overlay.classList.add('visibility-visible', 'opacity-100');
        } else {
          sidebar.classList.remove('open');
          overlay.classList.remove('visibility-visible', 'opacity-100');
          overlay.classList.add('visibility-hidden', 'opacity-0');
        }
      }
    }
  },
  mounted() {
    // Check local storage for theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
      this.isDark = savedTheme === 'dark';
    }
    
    // Check local storage for system preference if no theme saved? 
    // Usually system usage is separate, but here we just check if previously set.
  }
}
</script>

<style scoped>
/* Base action button micro-interactions */
.navbar-action-btn {
  transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
}

.navbar-action-btn:hover {
  transform: translateY(-2px) scale(1.05);
}

.navbar-action-btn:active {
  transform: translateY(0) scale(0.97);
}

/* 1. Theme Toggle Button (Amber in light mode, Twilight Indigo in dark mode) */
.navbar-theme-light {
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
  box-shadow: 0 2px 8px rgba(245, 158, 11, 0.38);
}
.navbar-theme-light:hover {
  background: linear-gradient(135deg, #fbbf24 0%, #d97706 100%) !important;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.55);
}

.navbar-theme-dark {
  background: linear-gradient(135deg, #6366f1 0%, #4338ca 100%) !important;
  box-shadow: 0 2px 8px rgba(99, 102, 241, 0.4);
}
.navbar-theme-dark:hover {
  background: linear-gradient(135deg, #818cf8 0%, #4f46e5 100%) !important;
  box-shadow: 0 4px 14px rgba(99, 102, 241, 0.58);
}

/* 2. Lock Workstation Button (Security Tangerine / Orange) */
.navbar-lock-btn {
  background: linear-gradient(135deg, #f97316 0%, #ea580c 100%) !important;
  box-shadow: 0 2px 8px rgba(249, 115, 22, 0.38);
}
.navbar-lock-btn:hover {
  background: linear-gradient(135deg, #fb923c 0%, #c2410c 100%) !important;
  box-shadow: 0 4px 14px rgba(249, 115, 22, 0.55);
}

/* 3. Notifications Button (Royal Azure Blue) */
.navbar-notif-btn {
  background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
  box-shadow: 0 2px 8px rgba(37, 99, 235, 0.38);
}
.navbar-notif-btn:hover {
  background: linear-gradient(135deg, #60a5fa 0%, #1e40af 100%) !important;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.55);
}

/* 4. Quick Logout Button (Emergency Crimson Red) */
.navbar-logout-btn {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
  box-shadow: 0 2px 8px rgba(220, 38, 38, 0.38);
}
.navbar-logout-btn:hover {
  background: linear-gradient(135deg, #f87171 0%, #b91c1c 100%) !important;
  box-shadow: 0 4px 14px rgba(220, 38, 38, 0.55);
}
</style>

