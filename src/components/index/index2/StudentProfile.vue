<template>
  <div class="card radius-16 border-0 shadow-1 h-100 overflow-hidden">
    <div class="card-body p-24 d-flex gap-20 flex-sm-nowrap flex-wrap">
      
      <!-- Left: Student Academic Identity Card -->
      <div
        class="radius-12 overflow-hidden position-relative z-1 py-24 px-20 text-center d-flex justify-content-center align-items-center flex-shrink-0"
        style="background: linear-gradient(135deg, #134e48 0%, #25A194 100%); width: 255px; min-width: 240px; max-width: 270px;"
      >
        <div class="w-100 d-flex flex-column align-items-center">
          <!-- Prominent Circular Portrait Container -->
          <div class="position-relative d-inline-block mb-14" style="width: 112px; height: 112px;">
            <router-link to="/edit-student" title="Change Academic Photograph" class="d-block position-relative text-decoration-none w-100 h-100">
              <figure
                class="rounded-circle overflow-hidden shadow-sm border border-3 border-white mb-0 bg-white d-flex justify-content-center align-items-center"
                style="width: 112px; height: 112px; min-width: 112px; min-height: 112px; max-width: 112px; max-height: 112px; border-radius: 50% !important; margin: 0 auto;"
              >
                <img 
                  :src="studentUser?.avatar || '/assets/images/thumbs/user-img1.png'" 
                  alt="Student Avatar"
                  class="rounded-circle"
                  style="width: 100% !important; height: 100% !important; min-width: 100% !important; min-height: 100% !important; max-width: 100% !important; max-height: 100% !important; object-fit: cover !important; object-position: center !important; aspect-ratio: 1 / 1 !important; display: block;"
                  @error="(e) => e.target.src = '/assets/images/thumbs/user-img1.png'"
                >
              </figure>
              <span 
                class="position-absolute bottom-0 end-0 bg-primary-700 text-white border border-2 border-white rounded-circle d-flex justify-content-center align-items-center shadow-sm"
                style="width: 32px; height: 32px; font-size: 15px;"
                title="Upload or Change Photograph"
              >
                <i class="ri-camera-fill"></i>
              </span>
            </router-link>
          </div>

          <h5 class="text-white fw-bold mb-2">{{ studentUser?.name || 'Sophia Chen' }}</h5>
          <span class="text-white text-opacity-80 text-xs d-block font-monospace mb-6">
            {{ studentUser?.matricNumber || 'SCI/2026/0491' }}
          </span>
          <span class="badge badge-translucent-white text-white px-10 py-4 radius-6 text-xs fw-semibold mb-12 d-inline-block">
            {{ studentUser?.program || 'B.Sc. Computer Science' }}
          </span>

          <div class="mt-4 d-flex justify-content-center gap-8 flex-wrap">
            <button 
              type="button" 
              class="btn btn-light btn-sm radius-8 px-12 py-6 text-xs fw-bold d-inline-flex align-items-center gap-6 shadow-sm"
              style="background-color: #ffffff !important; color: #111827 !important; border: 1px solid #ffffff !important;"
              data-bs-toggle="modal"
              data-bs-target="#studentExamPassModal"
            >
              <i class="ri-shield-check-fill text-primary-600 text-sm"></i>
              <span style="color: #111827 !important;">Exam Pass</span>
            </button>
            <router-link
              to="/edit-student"
              class="btn btn-outline-light btn-sm radius-8 px-12 py-6 text-xs fw-semibold text-white d-inline-flex align-items-center gap-4"
              title="Update Academic Portrait & Profile"
            >
              <i class="ri-camera-lens-line"></i>
              Photo
            </router-link>
          </div>
        </div>
      </div>

      <!-- Right: Academic Progress & Compliance Overview -->
      <div class="d-flex flex-column gap-14 flex-grow-1 justify-content-between min-w-0">
        
        <!-- Cumulative GPA -->
        <div class="radius-10 py-16 px-20 d-flex flex-wrap align-items-center justify-content-between gap-12 bg-primary-50 border border-primary-100">
          <div class="d-flex align-items-center gap-12 flex-grow-1 min-w-0">
            <div class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-primary-600 text-white text-xl flex-shrink-0">
              <iconify-icon icon="solar:award-bold"></iconify-icon>
            </div>
            <div class="min-w-0">
              <span class="text-secondary-light text-xs fw-semibold d-block text-truncate mb-2">Cumulative GPA (CGPA)</span>
              <h4 class="text-primary-light fw-bold mb-0 line-height-1">3.82 <span class="text-xs fw-normal text-secondary-light">/ 5.00</span></h4>
            </div>
          </div>
          <span class="badge bg-success-subtle text-success-800 text-xs px-10 py-6 radius-6 fw-bold flex-shrink-0 text-nowrap">
            First Class Standing
          </span>
        </div>

        <!-- Earned Credits -->
        <div class="radius-10 py-16 px-20 d-flex flex-wrap align-items-center justify-content-between gap-12 bg-purple-50 border border-purple-100 accumulated-credits-card">
          <div class="d-flex align-items-center gap-12 flex-grow-1 min-w-0">
            <div class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-purple-600 text-white text-xl flex-shrink-0">
              <i class="ri-book-marked-fill text-xl text-white"></i>
            </div>
            <div class="min-w-0">
              <span class="text-secondary-light text-xs fw-semibold d-block text-truncate mb-2">Accumulated Credits</span>
              <h4 class="text-primary-light fw-bold mb-0 line-height-1">84 <span class="text-xs fw-normal text-secondary-light">/ 120 Units</span></h4>
            </div>
          </div>
          <span class="badge bg-purple-subtle text-purple-800 border border-purple-200 text-xs px-10 py-6 radius-6 fw-semibold flex-shrink-0 text-nowrap accumulated-credits-badge">
            18 Units Enrolled
          </span>
        </div>

        <!-- Attendance Clearance -->
        <div class="radius-10 py-16 px-20 d-flex flex-wrap align-items-center justify-content-between gap-12 bg-success-50 border border-success-100">
          <div class="d-flex align-items-center gap-12 flex-grow-1 min-w-0">
            <div class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-success-600 text-white text-xl flex-shrink-0">
              <iconify-icon icon="solar:fingerprint-bold"></iconify-icon>
            </div>
            <div class="min-w-0">
              <span class="text-secondary-light text-xs fw-semibold d-block text-truncate mb-2">Lecture Attendance Compliance</span>
              <h4 class="text-primary-light fw-bold mb-0 line-height-1">88.4%</h4>
            </div>
          </div>
          <span class="badge bg-success text-white text-xs px-10 py-6 radius-6 fw-bold flex-shrink-0 text-nowrap">
            Exam Cleared (&gt;75%)
          </span>
        </div>

      </div>

    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth.js';

export default {
  name: "StudentProfile",
  setup() {
    const authStore = useAuthStore();
    const studentUser = computed(() => authStore.currentUser);

    return {
      studentUser
    };
  }
}
</script>

<style scoped>
.accumulated-credits-card {
  transition: background-color 0.2s ease, border-color 0.2s ease;
}

:global([data-theme="dark"]) .accumulated-credits-card,
:global([data-bs-theme="dark"]) .accumulated-credits-card {
  background-color: rgba(168, 85, 247, 0.1) !important;
  border-color: rgba(168, 85, 247, 0.25) !important;
}

:global([data-theme="dark"]) .accumulated-credits-badge,
:global([data-bs-theme="dark"]) .accumulated-credits-badge {
  background-color: rgba(168, 85, 247, 0.22) !important;
  color: #E9D8FD !important;
  border-color: rgba(168, 85, 247, 0.4) !important;
}
</style>
