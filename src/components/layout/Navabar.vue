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
          <button type="button" 
            class="w-40-px h-40-px bg-neutral-200 rounded-circle d-flex justify-content-center align-items-center"
            aria-label="Dark & Light Mode Button" @click="toggleTheme">
             <i class="text-xl" :class="isDark ? 'ri-moon-line' : 'ri-sun-line'"></i>
          </button>
          <button type="button" 
            class="w-40-px h-40-px bg-neutral-200 rounded-circle d-flex justify-content-center align-items-center text-secondary-light hover-text-warning-600"
            aria-label="Lock Workstation" 
            title="Lock Workstation" 
            @click="handleLockScreen">
             <i class="ri-lock-2-line text-xl"></i>
          </button>
          <!-- Quick Logout Button -->
          <button type="button" 
            class="navbar-logout-btn w-40-px h-40-px rounded-circle d-flex justify-content-center align-items-center text-white border-0 cursor-pointer"
            aria-label="Sign Out" 
            title="Sign Out / Log Out" 
            @click="handleLogout">
             <i class="ri-logout-box-r-line text-lg text-white"></i>
          </button>

          <div class="dropdown">
            <button
              class="has-indicator w-40-px h-40-px bg-neutral-200 rounded-circle d-flex justify-content-center align-items-center position-relative"
              type="button" data-bs-toggle="dropdown" aria-label="Notification Button">
              <iconify-icon icon="iconoir:bell" class="text-primary-light text-xl"></iconify-icon>
              <span class="w-8-px h-8-px bg-danger-600 position-absolute end-0 top-0 rounded-circle mt-2 me-2"></span>
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
.navbar-logout-btn {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
  box-shadow: 0 2px 8px rgba(220, 38, 38, 0.35);
  transition: all 0.2s ease-in-out;
  border: 1px solid rgba(255, 255, 255, 0.2) !important;
}

.navbar-logout-btn:hover {
  background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%) !important;
  box-shadow: 0 4px 14px rgba(220, 38, 38, 0.55);
  transform: translateY(-1px) scale(1.05);
}

.navbar-logout-btn:active {
  transform: translateY(0) scale(0.97);
  box-shadow: 0 1px 4px rgba(220, 38, 38, 0.4);
}
</style>

