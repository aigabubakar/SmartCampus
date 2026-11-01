<template>
  <div class="card radius-12 border-0 h-100 shadow-sm">
    <div class="card-body p-24">
      <div class="row g-3">
        <div class="col-md-5">
          <div
            class="radius-8 overflow-hidden position-relative z-1 h-100 py-32 px-20 text-center d-flex justify-content-center align-items-center"
            style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 60%, #4338ca 100%);"
          >
            <div>
              <span class="mb-12 d-inline-block">
                <img
                  :src="lecturerAvatar"
                  alt="Lecturer"
                  class="rounded-circle object-fit-cover w-72-px h-72-px border border-3 border-white shadow-sm"
                />
              </span>
              <h6 class="text-white mb-4 fw-bold">{{ lecturerName }}</h6>
              <span class="badge badge-translucent-white text-white text-xs px-10 py-4 rounded-pill mb-6 d-inline-block">
                {{ lecturerRank }}
              </span>
              <span class="text-white text-opacity-80 text-xs d-block mb-16">
                Courses: {{ assignedCoursesText }}
              </span>
              <div>
                <router-link
                  to="/teacher-list"
                  class="btn btn-sm px-16 py-6 text-white badge-translucent-white hover-bg-white hover-text-primary-600 radius-6 fw-semibold text-xs border border-white border-opacity-30"
                >
                  <i class="ri-team-line me-4"></i> Faculty Roster
                </router-link>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-7">
          <div class="row g-3">
            <div class="col-sm-6 col-xs-6">
              <div class="radius-8 py-20 px-16 text-center bg-purple-50 border border-purple-100">
                <span
                  class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-purple-100 text-purple-700 text-xl"
                >
                  <i class="ri-graduation-cap-line"></i>
                </span>
                <span class="text-secondary-light fw-medium d-block mt-8 text-xs">Enrolled Students</span>
                <h5 class="text-primary-light mb-0 fw-bold">428</h5>
              </div>
            </div>
            <div class="col-sm-6 col-xs-6">
              <div class="radius-8 py-20 px-16 text-center bg-success-50 border border-success-100">
                <span
                  class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-success-100 text-success-700 text-xl"
                >
                  <i class="ri-book-open-line"></i>
                </span>
                <span class="text-secondary-light fw-medium d-block mt-8 text-xs">Assigned Modules</span>
                <h5 class="text-primary-light mb-0 fw-bold">{{ assignedModulesCount }}</h5>
              </div>
            </div>
            <div class="col-sm-6 col-xs-6">
              <div class="radius-8 py-20 px-16 text-center bg-info-50 border border-info-100">
                <span
                  class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-info-100 text-info-700 text-xl"
                >
                  <i class="ri-time-line"></i>
                </span>
                <span class="text-secondary-light fw-medium d-block mt-8 text-xs">Weekly Teaching Load</span>
                <h5 class="text-primary-light mb-0 fw-bold">12 Hours</h5>
              </div>
            </div>
            <div class="col-sm-6 col-xs-6">
              <div class="radius-8 py-20 px-16 text-center bg-warning-50 border border-warning-100">
                <span
                  class="w-44-px h-44-px d-inline-flex justify-content-center align-items-center rounded-circle bg-warning-100 text-warning-700 text-xl"
                >
                  <i class="ri-award-line"></i>
                </span>
                <span class="text-secondary-light fw-medium d-block mt-8 text-xs">CAT / Exam Pass Rate</span>
                <h5 class="text-primary-light mb-0 fw-bold">89.4%</h5>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { lecturersApi } from '@/services/api.js';

export default {
  name: "TeacherProfile",
  setup() {
    const authStore = useAuthStore();
    const currentUser = computed(() => authStore.currentUser);
    const isLecturer = computed(() => authStore.isLecturer || authStore.isTeacher);
    const profileData = ref(null);

    onMounted(async () => {
      try {
        const ident = authStore.currentUser?.userId || authStore.currentUser?.staffId || 'FAC-104';
        const data = await lecturersApi.getLecturerDetails(ident);
        if (data) {
          profileData.value = data;
        }
      } catch (err) {
        // Fallback gracefully to store or mock data
      }
    });

    const lecturerName = computed(() => {
      if (profileData.value?.name) return profileData.value.name;
      if (isLecturer.value && currentUser.value?.name) {
        return currentUser.value.name;
      }
      return 'Prof. Alex Finch';
    });

    const lecturerRank = computed(() => {
      if (profileData.value?.rank) return profileData.value.rank;
      if (isLecturer.value && currentUser.value?.rank) {
        return currentUser.value.rank;
      }
      return 'Professor of Computer Science';
    });

    const lecturerAvatar = computed(() => {
      if (profileData.value?.avatar) return profileData.value.avatar;
      if (isLecturer.value && currentUser.value?.avatar) {
        return currentUser.value.avatar;
      }
      return '/assets/images/users/user1.png';
    });

    const assignedCoursesText = computed(() => {
      if (profileData.value?.assignedCourses?.length) {
        return profileData.value.assignedCourses.join(', ');
      }
      return 'CSC 301, CSC 303, SEN 305';
    });

    const assignedModulesCount = computed(() => {
      if (profileData.value?.assignedCourses?.length) {
        return `${profileData.value.assignedCourses.length} Courses`;
      }
      return '3 Courses';
    });

    return {
      lecturerName,
      lecturerRank,
      lecturerAvatar,
      assignedCoursesText,
      assignedModulesCount,
      profileData
    };
  },
};
</script>
