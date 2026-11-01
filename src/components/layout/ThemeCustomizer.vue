<template>
  <!-- Floating Configuration Button and Drawer (Restricted ONLY to Super Admin) -->
  <div v-if="isAuthorizedToRender" class="super-admin-customizer-container">
    
    <!-- Floating Config Button -->
    <button 
      type="button" 
      @click="toggleCustomizer"
      class="theme-customization__button w-48-px h-48-px text-white rounded-circle d-flex justify-content-center align-items-center position-fixed end-0 bottom-0 mb-40 me-40 text-xl shadow-lg border-2 border-white z-999"
      style="background: #0f172a;"
      title="Institutional Appearance (Super Admin)"
      aria-label="Institutional Appearance Settings"
    >
      <i class="ri-palette-line text-white"></i>
    </button>

    <!-- Customization Drawer -->
    <div 
      class="theme-customization-sidebar w-100 bg-base h-100vh overflow-y-auto position-fixed end-0 top-0 z-999 shadow-24" 
      :class="{ 'active': isOpen }"
    >
      <!-- Drawer Header -->
      <div class="d-flex align-items-center gap-3 py-18 px-24 justify-content-between border-bottom bg-neutral-900 text-white">
        <div>
          <div class="d-flex align-items-center gap-8 mb-4">
            <span class="badge bg-primary-600 text-white text-xxs px-6 py-2 radius-4 fw-semibold text-uppercase">
              Super Admin
            </span>
            <span class="badge badge-translucent-white text-white text-xxs px-8 py-3 radius-4">
              Institution Palette & Appearance
            </span>
          </div>
          <h6 class="text-sm fw-bold text-white mb-0">Campus Branding & Appearance</h6>
          <p class="text-xxs text-neutral-300 mb-0">Customize institutional palette, dark mode & layout</p>
        </div>
        <button 
          type="button" 
          @click="toggleCustomizer"
          class="theme-customization-sidebar__close text-white bg-transparent hover-text-warning-main border-0 d-flex text-xl cursor-pointer"
        >
          <i class="ri-close-line"></i>
        </button>
      </div>

      <!-- Drawer Content -->
      <div class="d-flex flex-column gap-36 p-24 overflow-y-auto flex-grow-1">

        <!-- 1. Institutional Theme Mode -->
        <div class="theme-setting-item">
          <div class="d-flex align-items-center justify-content-between mb-8">
            <h6 class="fw-bold text-neutral-900 text-xs mb-0 text-uppercase letter-spacing-05">Interface Mode</h6>
            <span class="text-xxs text-secondary-light">System-wide contrast</span>
          </div>
          <div class="d-grid grid-cols-3 gap-10 dark-light-mode">
            <button 
              type="button"
              class="theme-btn theme-setting-item__btn d-flex flex-column align-items-center justify-content-center p-12 rounded-8 text-md border"
              :class="{ 'active border-primary-600 bg-primary-50 text-primary-600': themeMode === 'light' }"
              @click="setTheme('light')" 
              aria-label="Light Mode"
            >
              <i class="ri-sun-line text-lg mb-2"></i>
              <span class="text-xs fw-semibold">Light</span>
            </button>

            <button 
              type="button"
              class="theme-btn theme-setting-item__btn d-flex flex-column align-items-center justify-content-center p-12 rounded-8 text-md border"
              :class="{ 'active border-primary-600 bg-primary-50 text-primary-600': themeMode === 'dark' }"
              @click="setTheme('dark')" 
              aria-label="Dark Mode"
            >
              <i class="ri-moon-line text-lg mb-2"></i>
              <span class="text-xs fw-semibold">Dark</span>
            </button>

            <button 
              type="button"
              class="theme-btn theme-setting-item__btn d-flex flex-column align-items-center justify-content-center p-12 rounded-8 text-md border"
              :class="{ 'active border-primary-600 bg-primary-50 text-primary-600': themeMode === 'system' }"
              @click="setTheme('system')" 
              aria-label="System Mode"
            >
              <i class="ri-computer-line text-lg mb-2"></i>
              <span class="text-xs fw-semibold">System</span>
            </button>
          </div>
        </div>

        <!-- 2. University Primary Color Presets -->
        <div class="theme-setting-item">
          <div class="d-flex align-items-center justify-content-between mb-8">
            <h6 class="fw-bold text-neutral-900 text-xs mb-0 text-uppercase letter-spacing-05">University Palette</h6>
            <span class="text-xxs text-secondary-light">Institutional brand identity</span>
          </div>
          
          <div class="row g-2">
            <div 
              v-for="color in universityColors" 
              :key="color.key"
              class="col-4"
            >
              <button 
                type="button" 
                class="w-100 p-8 rounded-8 border text-center transition-all bg-white"
                :class="activeColor === color.key ? 'border-2 border-neutral-900 shadow-sm' : 'border-neutral-200'"
                @click="applyUniversityColor(color)"
              >
                <div class="h-28-px w-100 rounded-6 mb-4 shadow-xs" :style="{ backgroundColor: color.hex }"></div>
                <span class="d-block text-xxs fw-bold text-neutral-800 text-truncate">{{ color.name }}</span>
              </button>
            </div>
          </div>
        </div>

        <!-- 3. Custom University Brand Hex Code -->
        <div class="theme-setting-item p-16 rounded-12 bg-neutral-50 border border-neutral-200">
          <h6 class="fw-bold text-neutral-900 text-xs mb-4 text-uppercase letter-spacing-05">Custom Pantone Hex</h6>
          <p class="text-xxs text-secondary-light mb-12">Match any client university's official color guide</p>
          
          <div class="d-flex align-items-center gap-10">
            <input 
              type="color" 
              class="form-control form-control-color border-0 p-0 rounded-circle flex-shrink-0 cursor-pointer" 
              style="width: 38px; height: 38px;" 
              v-model="customHex"
            >
            <input 
              type="text" 
              class="form-control text-sm font-monospace radius-8 uppercase" 
              placeholder="#25A194" 
              v-model="customHex"
            >
            <button 
              type="button" 
              class="btn btn-primary-600 btn-sm radius-8 px-14 py-8 text-xs fw-bold text-white text-nowrap shadow-sm"
              @click="applyCustomColor"
            >
              Apply
            </button>
          </div>
        </div>

        <!-- 4. Layout Direction -->
        <div class="theme-setting-item">
          <div class="d-flex align-items-center justify-content-between mb-8">
            <h6 class="fw-bold text-neutral-900 text-xs mb-0 text-uppercase letter-spacing-05">Script Direction</h6>
            <span class="text-xxs text-secondary-light">LTR / RTL scripts</span>
          </div>
          <div class="d-grid grid-cols-2 gap-10">
            <button 
              type="button"
              class="theme-setting-item__btn ltr-mode-btn d-flex align-items-center justify-content-center gap-8 py-10 rounded-8 border text-xs fw-semibold"
              :class="{ 'active border-primary-600 bg-primary-50 text-primary-600': direction === 'ltr' }"
              @click="setDirection('ltr')" 
              aria-label="Left-to-Right"
            >
              <i class="ri-align-item-left-line text-sm"></i>
              <span>Left-to-Right (LTR)</span>
            </button>

            <button 
              type="button"
              class="theme-setting-item__btn rtl-mode-btn d-flex align-items-center justify-content-center gap-8 py-10 rounded-8 border text-xs fw-semibold"
              :class="{ 'active border-primary-600 bg-primary-50 text-primary-600': direction === 'rtl' }"
              @click="setDirection('rtl')" 
              aria-label="Right-to-Left"
            >
              <span>Right-to-Left (RTL)</span>
              <i class="ri-align-item-right-line text-sm"></i>
            </button>
          </div>
        </div>

        <!-- 5. Reset to Institutional Default -->
        <div class="pt-16 border-top">
          <button 
            type="button" 
            class="btn btn-outline-neutral-300 w-100 py-10 radius-8 text-xs fw-semibold text-secondary-light hover-text-neutral-900 d-flex align-items-center justify-content-center gap-6"
            @click="resetToDefault"
          >
            <i class="ri-restart-line"></i>
            Reset to Apex University Default (#25A194)
          </button>
        </div>

      </div>
    </div>

    <!-- Backdrop when Customizer is Open -->
    <div 
      v-if="isOpen" 
      class="customizer-backdrop position-fixed top-0 start-0 w-100 h-100 bg-black bg-opacity-50 z-998 duration-200" 
      @click="isOpen = false"
    ></div>

  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: "ThemeCustomizer",
  props: {
    isGlobal: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isSuperAdmin = computed(() => authStore.isSuperAdmin);
    const isAuthorizedToRender = computed(() => props.isGlobal && isSuperAdmin.value);

    const isOpen = ref(false);
    const themeMode = ref('light');
    const direction = ref('ltr');
    const activeColor = ref('teal');
    const customHex = ref('#25A194');

    const universityColors = [
      { key: 'teal', name: 'Apex Teal', hex: '#25A194', desc: 'Apex University Default' },
      { key: 'navy', name: 'Oxford Navy', hex: '#1e3a8a', desc: 'Collegiate Blue' },
      { key: 'crimson', name: 'Crimson Tech', hex: '#dc2626', desc: 'Medical & Science' },
      { key: 'indigo', name: 'Royal Indigo', hex: '#4338ca', desc: 'Computing & AI' },
      { key: 'emerald', name: 'Emerald', hex: '#059669', desc: 'Polytechnic & Agric' },
      { key: 'amber', name: 'Collegiate Gold', hex: '#d97706', desc: 'Business & Law' },
    ];

    const toggleCustomizer = () => {
      isOpen.value = !isOpen.value;
    };

    const setTheme = (mode) => {
      themeMode.value = mode;
      localStorage.setItem('theme', mode);
      
      if (mode === 'system') {
        const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
      } else {
        document.documentElement.setAttribute('data-theme', mode);
      }

      if (isSuperAdmin.value && isOpen.value) {
        toastStore.info(`Interface theme mode set to ${mode.toUpperCase()}.`, 'Appearance Updated');
      }
    };

    const setDirection = (dir) => {
      direction.value = dir;
      document.documentElement.setAttribute('dir', dir);
      localStorage.setItem('direction', dir);

      if (isSuperAdmin.value && isOpen.value) {
        toastStore.info(`Script direction set to ${dir.toUpperCase()}.`, 'Layout Updated');
      }
    };

    const applyHexToRoot = (hex) => {
      document.documentElement.style.setProperty("--primary-600", hex);
      document.documentElement.style.setProperty("--brand", hex);
      localStorage.setItem('campus_university_color', hex);
    };

    const applyUniversityColor = (color) => {
      activeColor.value = color.key;
      customHex.value = color.hex;
      applyHexToRoot(color.hex);
      localStorage.setItem('color', color.key);

      if (isSuperAdmin.value && isOpen.value) {
        toastStore.success(`Applied ${color.name} (${color.hex}) as the university primary branding color.`, 'University Theme Applied');
      }
    };

    const applyCustomColor = () => {
      if (!customHex.value || !customHex.value.startsWith('#')) {
        toastStore.error('Please specify a valid hex color code (e.g. #25A194).', 'Invalid Color');
        return;
      }
      activeColor.value = 'custom';
      applyHexToRoot(customHex.value);
      localStorage.setItem('color', 'custom');
      toastStore.success(`Applied custom university brand color ${customHex.value}.`, 'Custom Palette Live');
    };

    const resetToDefault = () => {
      applyUniversityColor(universityColors[0]);
    };

    onMounted(() => {
      // 1. Initialize Theme Mode
      const savedTheme = localStorage.getItem('theme') || 'light';
      setTheme(savedTheme);

      // 2. Initialize Direction
      const savedDir = localStorage.getItem('direction') || 'ltr';
      setDirection(savedDir);

      // 3. Initialize University Brand Color
      const savedHex = localStorage.getItem('campus_university_color');
      const savedColorKey = localStorage.getItem('color');

      if (savedHex) {
        customHex.value = savedHex;
        applyHexToRoot(savedHex);
        activeColor.value = savedColorKey || 'teal';
      } else {
        applyUniversityColor(universityColors[0]);
      }
    });

    return {
      isSuperAdmin,
      isAuthorizedToRender,
      isOpen,
      themeMode,
      direction,
      activeColor,
      customHex,
      universityColors,
      toggleCustomizer,
      setTheme,
      setDirection,
      applyUniversityColor,
      applyCustomColor,
      resetToDefault
    };
  }
}
</script>

<style scoped>
.z-999 {
  z-index: 99999;
}
.z-998 {
  z-index: 99998;
}
.theme-customization-sidebar {
  max-width: 380px;
  transform: translateX(100%);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
.theme-customization-sidebar.active {
  transform: translateX(0);
}
.text-xxs {
  font-size: 0.6875rem;
}
.shadow-24 {
  box-shadow: -10px 0 30px rgba(0, 0, 0, 0.15);
}
.h-28-px {
  height: 28px;
}
</style>
