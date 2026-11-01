<template>
  <div class="card h-100">
    <div class="card-body p-24">
      <div class="d-flex gap-32 flex-md-row flex-column">
        <div class="max-w-300-px w-100 text-center">
          <figure
            class="mb-24 w-120-px h-120-px mx-auto rounded-circle overflow-hidden shadow-sm border border-3 border-primary-100 bg-neutral-100 position-relative cursor-pointer group"
            @click="$emit('edit')"
            title="Click to update academic photograph"
          >
            <img :src="studentAvatar" alt="Student Scholar Portrait" class="w-100 h-100 object-fit-cover">
            <span class="position-absolute bottom-0 start-0 end-0 bg-dark bg-opacity-50 text-white text-2xs py-4 text-center">
              <i class="ri-camera-fill me-2"></i>Change
            </span>
          </figure>
          <h2 class="h6 text-primary-light mb-8 fw-semibold">{{ studentName }}</h2>
          <span class="badge bg-success-50 text-success-700 border border-success-200 px-12 py-4 rounded-pill text-xs fw-semibold mb-12">
            Undergraduate Scholar
          </span>
          <p class="mb-4 text-xs text-secondary-light">
            Matric No: <span class="text-primary-600 fw-semibold">{{ studentMatric }}</span>
          </p>
          <p class="mb-0 text-xs text-secondary-light">
            Program: <span class="text-primary-light fw-semibold">{{ studentProgram }}</span>
          </p>

          <div class="mt-24 d-flex gap-12 w-100 justify-content-center">
            <button
              v-if="isAdmin"
              type="button"
              class="btn border fw-medium border-danger-600 bg-hover-danger-50 text-danger-600 text-xs d-flex justify-content-center align-items-center gap-6 flex-grow-1 px-12 py-8 radius-8"
            >
              <i class="ri-forbid-line"></i>
              Academic Suspension
            </button>
            <button
              type="button"
              class="btn btn-primary-600 text-xs d-flex justify-content-center align-items-center gap-6 flex-grow-1 px-12 py-8 radius-8 fw-semibold"
              @click="$emit('edit')"
            >
              <i class="ri-edit-line"></i>
              Edit Profile
            </button>
          </div>
        </div>

        <div>
          <span class="h-100 w-1-px bg-neutral-200 d-none d-md-block"></span>
        </div>

        <div class="flex-grow-1">
          <div class="pb-16 border-bottom d-flex align-items-center justify-content-between gap-20">
            <h3 class="h6 text-primary-light text-lg mb-0 fw-semibold">Academic Dossier & Standing</h3>
            <span class="px-16 py-4 radius-4 fw-medium text-xs" :class="standingClass">
              {{ standingText }} (CGPA {{ Number(studentCgpa).toFixed(2) }})
            </span>
          </div>

          <div class="mt-16 d-flex flex-column gap-12">
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Faculty</span>
              <span class="fw-normal text-xs text-secondary-light">: {{ studentFaculty }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Degree Program</span>
              <span class="fw-normal text-xs text-secondary-light">: {{ studentProgram }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Academic Level</span>
              <span class="fw-normal text-xs text-secondary-light">: {{ studentLevel }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Matriculation ID</span>
              <span class="fw-normal text-xs text-secondary-light">: {{ studentMatric }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Institutional Email</span>
              <span class="fw-normal text-xs text-primary-600">: {{ studentEmail }}</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Academic Session</span>
              <span class="fw-normal text-xs text-secondary-light">: 2026/2027 • Harmattan Semester</span>
            </div>
            <div class="d-flex gap-4">
              <span class="fw-semibold text-xs text-primary-light w-140-px">Hall of Residence</span>
              <span class="fw-normal text-xs text-secondary-light">: {{ studentHall }}</span>
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
  name: "StudentProfileCard",
  props: {
    student: {
      type: Object,
      default: null,
    },
  },
  emits: ['edit'],
  setup(props) {
    const authStore = useAuthStore();
    const currentUser = computed(() => authStore.currentUser);
    const isStudent = computed(() => authStore.isStudent);
    const isAdmin = computed(() => authStore.isAdmin || authStore.isSuperAdmin);

    const studentName = computed(() => {
      return props.student?.name || (isStudent.value && currentUser.value?.name) || 'Sophia Chen';
    });

    const studentMatric = computed(() => {
      return props.student?.matricNumber || (isStudent.value && currentUser.value?.matricNumber) || 'SCI/2026/0491';
    });

    const studentProgram = computed(() => {
      return props.student?.program || (isStudent.value && currentUser.value?.program) || 'B.Sc Computer Science';
    });

    const studentFaculty = computed(() => {
      return props.student?.faculty || 'Faculty of Computing & Information Systems';
    });

    const studentLevel = computed(() => {
      return props.student?.level || '300 Level (Undergraduate)';
    });

    const studentEmail = computed(() => {
      return props.student?.email || (isStudent.value && currentUser.value?.email) || 'sophia.chen@student.campus.edu';
    });

    const studentAvatar = computed(() => {
      return props.student?.avatar || (isStudent.value && currentUser.value?.avatar) || '/assets/images/thumbs/user-img1.png';
    });

    const studentHall = computed(() => {
      return props.student?.hallOfResidence || 'Queen Idia Hall, Block C, Room 14';
    });

    const studentCgpa = computed(() => {
      if (props.student?.cgpa !== undefined && props.student?.cgpa !== null) {
        return props.student.cgpa;
      }
      if (isStudent.value && currentUser.value?.cgpa !== undefined && currentUser.value?.cgpa !== null) {
        return currentUser.value.cgpa;
      }
      return 3.85;
    });

    const standingText = computed(() => {
      const gpa = Number(studentCgpa.value);
      if (gpa >= 3.5) return 'First Class Honours';
      if (gpa >= 2.4) return 'Second Class Upper';
      if (gpa >= 1.5) return 'Good Standing';
      return 'Academic Probation';
    });

    const standingClass = computed(() => {
      const gpa = Number(studentCgpa.value);
      if (gpa >= 3.5) return 'bg-success-100 text-success-700';
      if (gpa >= 2.4) return 'bg-primary-100 text-primary-700';
      if (gpa >= 1.5) return 'bg-warning-100 text-warning-700';
      return 'bg-danger-100 text-danger-700';
    });

    return {
      isAdmin,
      isStudent,
      studentName,
      studentMatric,
      studentProgram,
      studentFaculty,
      studentLevel,
      studentEmail,
      studentAvatar,
      studentHall,
      studentCgpa,
      standingText,
      standingClass,
    };
  },
};
</script>
