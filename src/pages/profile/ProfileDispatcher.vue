<template>
  <component :is="resolvedProfile" />
</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth.js';

import StudentDetails from '@/pages/students/studentDetails.vue';
import TeacherDetails from '@/pages/teachers/teacherDetails.vue';
import EmployeeDetails from '@/pages/hrm/EmployeeDetails.vue';
import GuardianDetails from '@/pages/guardians/guardianDetails.vue';

export default {
  name: 'ProfileDispatcher',
  components: {
    StudentDetails,
    TeacherDetails,
    EmployeeDetails,
    GuardianDetails,
  },
  setup() {
    const authStore = useAuthStore();

    const resolvedProfile = computed(() => {
      const role = authStore.currentRole || authStore.user?.role;

      switch (role) {
        case 'student':
          return StudentDetails;
        case 'lecturer':
        case 'teacher':
          return TeacherDetails; // Lecturer Academic Dossier
        case 'guardian':
        case 'parent':
          return GuardianDetails;
        case 'admin':
        case 'super-admin':
        default:
          return EmployeeDetails; // University Admin / Staff Dossier
      }
    });

    return {
      resolvedProfile,
    };
  },
};
</script>
