<template>
  <div 
    v-if="enrollmentStore.isInterDeptModalOpen" 
    class="modal-backdrop-custom d-flex align-items-center justify-content-center p-16"
  >
    <div class="modal-dialog-custom bg-base radius-16 shadow-3 border border-neutral-200 overflow-hidden d-flex flex-column animate-fade-in">
      <!-- Modal Header -->
      <div class="px-24 py-18 border-bottom border-neutral-200 d-flex align-items-center justify-content-between bg-neutral-50">
        <div>
          <h6 class="text-md fw-bold text-neutral-900 mb-2 d-flex align-items-center gap-8">
            <i class="ri-building-4-line text-primary-600"></i>
            Add Inter-Departmental Elective
          </h6>
          <span class="text-secondary-light text-xs">
            Browse and add approved general electives and borrowed modules from any faculty.
          </span>
        </div>
        <button 
          type="button" 
          class="btn p-0 text-neutral-500 hover-text-neutral-900 border-0 bg-transparent text-xl line-height-1"
          @click="enrollmentStore.isInterDeptModalOpen = false"
        >
          <i class="ri-close-line"></i>
        </button>
      </div>

      <!-- Search & Department Filters -->
      <div class="p-20 border-bottom border-neutral-200 bg-base d-flex flex-wrap align-items-center gap-12">
        <!-- Search input -->
        <div class="flex-grow-1 position-relative" style="min-width: 200px;">
          <input 
            type="text" 
            class="form-control form-control-sm ps-36 radius-8 text-xs" 
            placeholder="Search all accredited courses (e.g. MTH, ENG, GST)..." 
            v-model="searchQuery"
          />
          <i class="ri-search-line position-absolute top-50 start-0 translate-middle-y ms-12 text-secondary-light text-sm"></i>
        </div>

        <!-- Level Filter -->
        <div style="min-width: 140px;">
          <select class="form-select form-select-sm radius-8 text-xs" v-model="selectedLevel">
            <option value="All Levels">All Levels</option>
            <option value="100 Level">100 Level</option>
            <option value="200 Level">200 Level</option>
            <option value="300 Level">300 Level</option>
          </select>
        </div>
      </div>

      <!-- Course List -->
      <div class="p-20 overflow-y-auto flex-grow-1 d-flex flex-column gap-12" style="max-height: 400px;">
        <div 
          v-for="course in filteredCourses" 
          :key="course.id"
          class="p-14 radius-10 border border-neutral-200 d-flex align-items-center justify-content-between gap-16 transition-2"
          :class="{ 'bg-primary-50 bg-opacity-25 border-primary-300': isAdded(course.id) }"
        >
          <div class="min-w-0">
            <div class="d-flex flex-wrap align-items-center gap-8 mb-4">
              <span class="fw-bold font-monospace text-xs text-neutral-900">{{ course.code }}</span>
              <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-6 py-2 radius-4">
                {{ course.creditUnits }} Units
              </span>
              <span class="badge bg-neutral-100 text-secondary-light text-xxs px-6 py-2 radius-4">
                {{ course.level }}
              </span>
              <span class="text-xxs text-secondary-light">
                {{ course.department }}
              </span>
            </div>

            <h6 class="text-xs fw-semibold text-neutral-800 mb-2 text-truncate">
              {{ course.title }}
            </h6>

            <span class="text-xxs text-secondary-light">
              Lecturer: {{ course.lecturerName || 'Faculty Board' }}
            </span>
          </div>

          <!-- Action Button -->
          <div class="flex-shrink-0">
            <span v-if="enrollmentStore.isCarryoverLocked(course.id)" class="badge bg-danger-100 text-danger-700 text-xxs px-8 py-4 radius-6">
              Carryover
            </span>
            <button 
              v-else-if="isAdded(course.id)"
              type="button" 
              class="btn btn-outline-danger btn-xs radius-6 d-inline-flex align-items-center gap-4 px-10 py-4"
              @click="enrollmentStore.removeCourse(course.id)"
            >
              <i class="ri-delete-bin-line"></i> Remove
            </button>
            <button 
              v-else
              type="button" 
              class="btn btn-primary btn-xs radius-6 d-inline-flex align-items-center gap-4 px-10 py-4"
              :disabled="enrollmentStore.totalSelectedUnits + course.creditUnits > 24"
              @click="enrollmentStore.addCourse(course)"
            >
              <i class="ri-add-line"></i> + Add
            </button>
          </div>
        </div>

        <div v-if="filteredCourses.length === 0" class="text-center py-32 text-secondary-light">
          <i class="ri-file-search-line text-3xl mb-6 d-block text-neutral-300"></i>
          <p class="text-xs mb-0">No matching courses found in the university database.</p>
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="px-24 py-14 bg-neutral-50 border-top border-neutral-200 d-flex align-items-center justify-content-between text-xs">
        <span class="text-secondary-light">
          Current Docket Load: <strong class="text-primary-600">{{ enrollmentStore.totalSelectedUnits }} / 24 Units</strong>
        </span>
        <button 
          type="button" 
          class="btn btn-secondary btn-sm radius-8 px-16 py-6"
          @click="enrollmentStore.isInterDeptModalOpen = false"
        >
          Done
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: 'InterDepartmentalModal',
  setup() {
    const enrollmentStore = useEnrollmentStore();

    const searchQuery = ref('');
    const selectedLevel = ref('All Levels');

    const filteredCourses = computed(() => {
      let list = enrollmentStore.allAccreditedCourses;

      if (selectedLevel.value !== 'All Levels') {
        list = list.filter(c => c.level === selectedLevel.value);
      }

      if (searchQuery.value.trim()) {
        const q = searchQuery.value.toLowerCase().trim();
        list = list.filter(c => 
          c.code.toLowerCase().includes(q) ||
          c.title.toLowerCase().includes(q) ||
          (c.department || '').toLowerCase().includes(q)
        );
      }

      return list;
    });

    const isAdded = (courseId) => {
      return enrollmentStore.selectedCourseIds.includes(courseId);
    };

    return {
      enrollmentStore,
      searchQuery,
      selectedLevel,
      filteredCourses,
      isAdded
    };
  }
};
</script>

<style scoped>
.modal-backdrop-custom {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.55);
  backdrop-filter: blur(4px);
  z-index: 1050;
}

.modal-dialog-custom {
  width: 100%;
  max-width: 680px;
  max-height: 90vh;
}

.btn-xs {
  padding: 4px 10px;
  font-size: 0.75rem;
}

.animate-fade-in {
  animation: modalFadeIn 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

@keyframes modalFadeIn {
  from {
    opacity: 0;
    transform: scale(0.96) translateY(-10px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}
</style>
