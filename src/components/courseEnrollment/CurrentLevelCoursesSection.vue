<template>
  <div class="card border-0 shadow-1 radius-16 mb-24">
    <div class="card-body p-20 p-md-24">
      <div class="d-flex flex-wrap align-items-center justify-content-between gap-12 pb-16 border-bottom border-neutral-200">
        <div>
          <div class="d-flex align-items-center gap-8">
            <h6 class="text-md fw-bold text-neutral-900 mb-0">
              2. Current Level Curriculum ({{ enrollmentStore.student?.level || '300 Level' }})
            </h6>
            <span class="badge bg-primary-100 text-primary-700 text-xxs px-8 py-2 rounded-pill fw-bold">
              {{ availableCourses.length }} Accredited Modules
            </span>
          </div>
          <span class="text-secondary-light text-xs">
            Select your Core and Elective modules up to the maximum 24 credit unit ceiling.
          </span>
        </div>

        <div class="d-flex align-items-center gap-8">
          <span class="text-xs text-secondary-light">
            Selected Current Units: <strong class="text-primary-600">{{ enrollmentStore.regularUnits }} Units</strong>
          </span>
        </div>
      </div>

      <!-- Core Compulsory Courses -->
      <div class="mt-20">
        <div class="d-flex align-items-center gap-8 mb-12">
          <span class="badge bg-neutral-900 text-white text-xxs px-8 py-2 radius-4 fw-bold text-uppercase">
            Core Compulsory Modules
          </span>
          <span class="text-secondary-light text-xxs">Mandatory for {{ enrollmentStore.student?.program }}</span>
        </div>

        <div class="d-flex flex-column gap-10">
          <div 
            v-for="course in coreCourses" 
            :key="course.id"
            class="course-card-row p-14 radius-10 border border-neutral-200 d-flex align-items-center justify-content-between gap-16 cursor-pointer"
            :class="{ 'course-selected': isSelected(course.id) }"
            @click="enrollmentStore.toggleCourse(course)"
          >
            <div class="d-flex align-items-center gap-14 min-w-0">
              <div class="form-check m-0" @click.stop>
                <input 
                  class="form-check-input course-checkbox" 
                  type="checkbox" 
                  :id="`course-${course.id}`"
                  :checked="isSelected(course.id)"
                  @change="enrollmentStore.toggleCourse(course)"
                />
              </div>

              <div class="min-w-0">
                <div class="d-flex flex-wrap align-items-center gap-8 mb-4">
                  <span class="fw-bold text-neutral-900 text-sm font-monospace">{{ course.code }}</span>
                  <span class="badge bg-primary-50 text-primary-600 text-xxs px-6 py-2 radius-4 fw-semibold">
                    {{ course.category }}
                  </span>
                  <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-6 py-2 radius-4 fw-semibold">
                    {{ course.creditUnits }} Units
                  </span>
                  <span v-if="course.prerequisiteCode" class="text-xxs text-secondary-light d-inline-flex align-items-center gap-2">
                    <i class="ri-git-branch-line"></i> Prereq: {{ course.prerequisiteCode }}
                    <span v-if="course.prerequisitePassed" class="text-success-600 fw-bold">(Passed)</span>
                    <span v-else class="text-danger-600 fw-bold">(Pending)</span>
                  </span>
                </div>

                <h6 class="text-xs fw-semibold text-neutral-800 mb-2 text-truncate">
                  {{ course.title }}
                </h6>

                <span class="text-xxs text-secondary-light d-inline-flex align-items-center gap-4">
                  <i class="ri-user-voice-line text-primary-500"></i> Lecturer: {{ course.lecturerName || 'Faculty Board' }}
                </span>
              </div>
            </div>

            <div class="flex-shrink-0 text-end">
              <span 
                class="badge text-xxs px-10 py-4 radius-6"
                :class="isSelected(course.id) ? 'bg-primary-600 text-white fw-bold' : 'bg-neutral-100 text-secondary-light'"
              >
                {{ isSelected(course.id) ? 'Queued' : '+ Add' }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Departmental Electives -->
      <div v-if="electiveCourses.length > 0" class="mt-24">
        <div class="d-flex align-items-center gap-8 mb-12">
          <span class="badge bg-purple-700 text-white text-xxs px-8 py-2 radius-4 fw-bold text-uppercase">
            Departmental Electives
          </span>
          <span class="text-secondary-light text-xxs">Specialization modules (Select as recommended by AI Advisor)</span>
        </div>

        <div class="d-flex flex-column gap-10">
          <div 
            v-for="course in electiveCourses" 
            :key="course.id"
            class="course-card-row p-14 radius-10 border border-neutral-200 d-flex align-items-center justify-content-between gap-16 cursor-pointer"
            :class="{ 'course-selected': isSelected(course.id) }"
            @click="enrollmentStore.toggleCourse(course)"
          >
            <div class="d-flex align-items-center gap-14 min-w-0">
              <div class="form-check m-0" @click.stop>
                <input 
                  class="form-check-input course-checkbox" 
                  type="checkbox" 
                  :id="`course-${course.id}`"
                  :checked="isSelected(course.id)"
                  @change="enrollmentStore.toggleCourse(course)"
                />
              </div>

              <div class="min-w-0">
                <div class="d-flex flex-wrap align-items-center gap-8 mb-4">
                  <span class="fw-bold text-neutral-900 text-sm font-monospace">{{ course.code }}</span>
                  <span class="badge bg-purple-50 text-purple-700 text-xxs px-6 py-2 radius-4 fw-semibold">
                    {{ course.category }}
                  </span>
                  <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-6 py-2 radius-4 fw-semibold">
                    {{ course.creditUnits }} Units
                  </span>
                  <span v-if="course.prerequisiteCode" class="text-xxs text-secondary-light d-inline-flex align-items-center gap-2">
                    <i class="ri-git-branch-line"></i> Prereq: {{ course.prerequisiteCode }}
                    <span v-if="course.prerequisitePassed" class="text-success-600 fw-bold">(Passed)</span>
                    <span v-else class="text-danger-600 fw-bold">(Pending)</span>
                  </span>
                </div>

                <h6 class="text-xs fw-semibold text-neutral-800 mb-2 text-truncate">
                  {{ course.title }}
                </h6>

                <span class="text-xxs text-secondary-light d-inline-flex align-items-center gap-4">
                  <i class="ri-user-voice-line text-purple-500"></i> Lecturer: {{ course.lecturerName || 'Faculty Board' }}
                </span>
              </div>
            </div>

            <div class="flex-shrink-0 text-end">
              <span 
                class="badge text-xxs px-10 py-4 radius-6"
                :class="isSelected(course.id) ? 'bg-purple-600 text-white fw-bold' : 'bg-neutral-100 text-secondary-light'"
              >
                {{ isSelected(course.id) ? 'Queued' : '+ Add' }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: 'CurrentLevelCoursesSection',
  setup() {
    const enrollmentStore = useEnrollmentStore();

    const availableCourses = computed(() => enrollmentStore.availableCourses);
    
    const coreCourses = computed(() => {
      return availableCourses.value.filter(c => 
        (c.category || '').toLowerCase().includes('core') || 
        (c.category || '').toLowerCase().includes('compulsory') ||
        (c.category || '').toLowerCase().includes('general')
      );
    });

    const electiveCourses = computed(() => {
      return availableCourses.value.filter(c => 
        (c.category || '').toLowerCase().includes('elective')
      );
    });

    const isSelected = (courseId) => {
      return enrollmentStore.selectedCourseIds.includes(courseId);
    };

    return {
      enrollmentStore,
      availableCourses,
      coreCourses,
      electiveCourses,
      isSelected
    };
  }
};
</script>

<style scoped>
.course-card-row {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  background-color: var(--bs-card-bg, #fff);
}

.course-card-row:hover {
  border-color: rgba(72, 127, 255, 0.4) !important;
  background-color: rgba(72, 127, 255, 0.03);
  transform: translateX(2px);
}

.course-card-row.course-selected {
  border-color: rgba(72, 127, 255, 0.6) !important;
  background-color: rgba(72, 127, 255, 0.06);
}

.course-checkbox {
  width: 18px;
  height: 18px;
  cursor: pointer;
}
</style>
