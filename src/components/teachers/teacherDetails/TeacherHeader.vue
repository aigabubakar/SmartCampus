<template>
  <div class="card h-100">
    <div class="card-body p-24">
      <div class="d-flex gap-32 flex-md-row flex-column">
        <div class="max-w-300-px w-100 text-center">
          <figure class="mb-24 w-120-px h-120-px mx-auto rounded-circle overflow-hidden shadow-sm border border-2 border-primary-100">
            <img :src="lecturerAvatar" alt="Lecturer Image" class="w-100 h-100 object-fit-cover">
          </figure>
          <h2 class="h6 text-primary-light mb-8 fw-semibold">{{ lecturerName }}</h2>
          <span class="badge bg-primary-50 text-primary-700 border border-primary-200 px-12 py-4 rounded-pill text-xs fw-semibold mb-12">
            {{ lecturerRank }}
          </span>
          <p class="mb-4 text-xs text-secondary-light">
            Staff ID: <span class="text-primary-600 fw-semibold">{{ lecturerStaffId }}</span>
          </p>
          <p class="mb-0 text-xs text-secondary-light">
            Department: <span class="text-primary-light fw-semibold">{{ lecturerDepartment }}</span>
          </p>

          <div class="mt-24 d-flex gap-12 w-100 justify-content-center">
            <button
              v-if="isAdmin"
              type="button"
              class="btn border fw-medium border-danger-600 bg-hover-danger-50 text-danger-600 text-xs d-flex justify-content-center align-items-center gap-6 flex-grow-1 px-12 py-8 radius-8"
              data-bs-toggle="modal"
              data-bs-target="#exampleModalDelete"
            >
              <i class="ri-forbid-line"></i>
              Suspend
            </button>
            <router-link
              to="/edit-lecturer"
              class="btn btn-primary-600 text-xs d-flex justify-content-center align-items-center gap-6 flex-grow-1 px-12 py-8 radius-8 fw-semibold"
            >
              <i class="ri-edit-line"></i>
              Edit Profile
            </router-link>
          </div>
        </div>

        <div>
          <span class="h-100 w-1-px bg-neutral-200 d-none d-md-block"></span>
        </div>

        <div class="flex-grow-1">
          <div class="pb-16 border-bottom d-flex align-items-center justify-content-between gap-20">
            <h3 class="h6 text-primary-light text-lg mb-0 fw-semibold">Academic & Faculty Dossier</h3>
            <span class="bg-success-100 text-success-600 px-16 py-4 radius-4 fw-medium text-xs">Active Academic Staff</span>
          </div>

          <div class="mt-16 d-flex flex-column gap-12">
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Faculty Division</span>
              <span class="fw-normal text-xs text-secondary-light">: Faculty of Natural & Applied Sciences</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Academic Rank</span>
              <span class="fw-normal text-xs text-secondary-light">: {{ lecturerRank }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Appointment Type</span>
              <span class="fw-normal text-xs text-secondary-light">: Tenured Academic Staff</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Faculty Office</span>
              <span class="fw-normal text-xs text-secondary-light">: Science Complex, Office 304</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Institutional Email</span>
              <span class="fw-normal text-xs text-primary-600">: {{ lecturerEmail }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Research Focus</span>
              <span class="fw-normal text-xs text-secondary-light">: Neural Networks, Deep Learning & Autonomous Systems</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Academic Session</span>
              <span class="fw-normal text-xs text-secondary-light">: 2026/2027 Academic Session</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth.js';

export default {
  name: 'TeacherHeader',
  setup() {
    const authStore = useAuthStore();
    const currentUser = computed(() => authStore.currentUser);
    const isLecturer = computed(() => authStore.isLecturer || authStore.isTeacher);
    const isAdmin = computed(() => authStore.isAdmin || authStore.isSuperAdmin);

    const lecturerName = computed(() => {
      if (isLecturer.value && currentUser.value?.name) {
        return currentUser.value.name;
      }
      return 'Prof. Alistair Finch';
    });

    const lecturerRank = computed(() => {
      if (isLecturer.value && currentUser.value?.rank) {
        return currentUser.value.rank;
      }
      return 'Professor of Computer Science';
    });

    const lecturerStaffId = computed(() => {
      if (isLecturer.value && currentUser.value?.id) {
        return currentUser.value.id;
      }
      return 'FAC-104';
    });

    const lecturerDepartment = computed(() => {
      if (isLecturer.value && currentUser.value?.department) {
        return currentUser.value.department;
      }
      return 'Department of Computer Science';
    });

    const lecturerEmail = computed(() => {
      if (isLecturer.value && currentUser.value?.email) {
        return currentUser.value.email;
      }
      return 'a.finch@campus.edu';
    });

    const lecturerAvatar = computed(() => {
      if (isLecturer.value && currentUser.value?.avatar) {
        return currentUser.value.avatar;
      }
      return '/assets/images/users/user1.png';
    });

    return {
      isAdmin,
      isLecturer,
      lecturerName,
      lecturerRank,
      lecturerStaffId,
      lecturerDepartment,
      lecturerEmail,
      lecturerAvatar,
    };
  },
};
</script>
