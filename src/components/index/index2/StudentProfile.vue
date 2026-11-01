<template>
  <div class="card radius-16 border-0 shadow-1 h-100 overflow-hidden">
    <div class="card-body p-24 d-flex gap-20 flex-sm-nowrap flex-wrap">
      
      <!-- Left: Student Academic Identity Card -->
      <div
        class="radius-12 overflow-hidden position-relative z-1 py-28 px-20 text-center d-flex justify-content-center align-items-center flex-grow-1"
        style="background: linear-gradient(135deg, #134e48 0%, #25A194 100%); min-width: 240px;"
      >
        <div>
          <div class="position-relative d-inline-block mb-12">
            <router-link to="/edit-student" title="Change Academic Photograph" class="d-block position-relative text-decoration-none">
              <img 
                :src="studentUser?.avatar || '/assets/images/thumbs/user-img1.png'" 
                alt="Student Avatar"
                class="w-80-px h-80-px rounded-circle object-fit-cover border border-3 border-white shadow"
              >
              <span class="position-absolute bottom-0 end-0 bg-primary-700 text-white border border-2 border-white rounded-circle w-26-px h-26-px d-flex justify-content-center align-items-center text-xs shadow-sm" title="Upload or Change Photograph">
                <i class="ri-camera-fill text-2xs"></i>
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
              class="btn btn-light btn-sm radius-8 px-12 py-6 text-xs fw-bold text-neutral-900 d-inline-flex align-items-center gap-6 shadow-sm"
              data-bs-toggle="modal"
              data-bs-target="#studentExamPassModal"
            >
              <iconify-icon icon="solar:ticket-bold" class="text-primary-600 text-sm"></iconify-icon>
              Exam Pass
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
      <div class="d-flex flex-column gap-16 flex-grow-1 justify-content-between">
        
        <!-- Cumulative GPA -->
        <div class="radius-10 py-16 px-20 d-flex align-items-center justify-content-between bg-primary-50 border border-primary-100">
          <div class="d-flex align-items-center gap-12">
            <div class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-primary-600 text-white text-xl flex-shrink-0">
              <iconify-icon icon="solar:award-bold"></iconify-icon>
            </div>
            <div>
              <span class="text-secondary-light text-xs fw-semibold d-block">Cumulative GPA (CGPA)</span>
              <h4 class="text-primary-light fw-bold mb-0">3.82 <span class="text-xs fw-normal text-secondary-light">/ 5.00</span></h4>
            </div>
          </div>
          <span class="badge bg-success-subtle text-success-800 text-xs px-8 py-4 radius-6 fw-bold">
            First Class Standing
          </span>
        </div>

        <!-- Earned Credits -->
        <div class="radius-10 py-16 px-20 d-flex align-items-center justify-content-between bg-purple-50 border border-purple-100">
          <div class="d-flex align-items-center gap-12">
            <div class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-purple-600 text-white text-xl flex-shrink-0">
              <iconify-icon icon="solar:book-bookmark-bold"></iconify-icon>
            </div>
            <div>
              <span class="text-secondary-light text-xs fw-semibold d-block">Accumulated Credits</span>
              <h4 class="text-primary-light fw-bold mb-0">84 <span class="text-xs fw-normal text-secondary-light">/ 120 Units</span></h4>
            </div>
          </div>
          <span class="badge bg-purple-subtle text-purple-800 text-xs px-8 py-4 radius-6 fw-semibold">
            18 Units Enrolled
          </span>
        </div>

        <!-- Attendance Clearance -->
        <div class="radius-10 py-16 px-20 d-flex align-items-center justify-content-between bg-success-50 border border-success-100">
          <div class="d-flex align-items-center gap-12">
            <div class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-success-600 text-white text-xl flex-shrink-0">
              <iconify-icon icon="solar:fingerprint-bold"></iconify-icon>
            </div>
            <div>
              <span class="text-secondary-light text-xs fw-semibold d-block">Lecture Attendance Compliance</span>
              <h4 class="text-primary-light fw-bold mb-0">88.4%</h4>
            </div>
          </div>
          <span class="badge bg-success text-white text-xs px-8 py-4 radius-6 fw-bold">
            Exam Cleared (>75%)
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
