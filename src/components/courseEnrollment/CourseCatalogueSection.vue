<template>
  <div class="card border-0 shadow-1 radius-16 mb-24 course-catalogue-card">
    <div class="card-body p-20 p-md-24">
      <!-- Section Header -->
      <div class="d-flex flex-wrap align-items-center justify-content-between gap-12 pb-16 border-bottom border-neutral-200">
        <div>
          <div class="d-flex align-items-center gap-8">
            <h6 class="text-md fw-bold text-neutral-900 mb-0">
              Course Catalogue — Add Fresh Courses
            </h6>
            <span class="badge bg-primary-100 text-primary-700 text-xxs px-8 py-2 rounded-pill fw-bold">
              {{ enrollmentStore.student?.level || '300 Level' }} Curriculum
            </span>
          </div>
          <span class="text-secondary-light text-xs">
            Browse and select accredited modules to add to your semester registration docket.
          </span>
        </div>

        <!-- Add from other departments button -->
        <button 
          type="button" 
          class="btn btn-outline-primary btn-xs radius-8 d-inline-flex align-items-center gap-6 px-12 py-6 fw-semibold"
          @click="enrollmentStore.isInterDeptModalOpen = true"
        >
          <i class="ri-search-eye-line text-sm"></i>
          <span>+ Add from Other Departments</span>
        </button>
      </div>

      <!-- Search & Category Filters -->
      <div class="mt-16 d-flex flex-wrap align-items-center justify-content-between gap-12">
        <!-- Search Input -->
        <div class="flex-grow-1 position-relative" style="min-width: 240px; max-width: 400px;">
          <input 
            type="text" 
            class="form-control form-control-sm ps-36 radius-8 text-xs" 
            placeholder="Search course code or title (e.g. CSC 301, AI, Systems)..." 
            v-model="searchFilter"
          />
          <i class="ri-search-line position-absolute top-50 start-0 translate-middle-y ms-12 text-secondary-light text-sm"></i>
          <button 
            v-if="searchFilter" 
            type="button" 
            class="btn p-0 position-absolute top-50 end-0 translate-middle-y me-10 text-secondary-light border-0 bg-transparent"
            @click="searchFilter = ''"
          >
            <i class="ri-close-line"></i>
          </button>
        </div>

        <!-- Category Pills -->
        <div class="d-flex align-items-center gap-6 bg-neutral-100 p-3 radius-8">
          <button 
            v-for="cat in categoryTabs" 
            :key="cat"
            type="button" 
            class="btn btn-xs radius-6 px-10 py-4 fw-semibold transition-2"
            :class="activeCategory === cat ? 'bg-base text-neutral-900 shadow-xs' : 'text-secondary-light bg-transparent'"
            @click="activeCategory = cat"
          >
            {{ cat }}
          </button>
        </div>
      </div>

      <!-- Course Cards List -->
      <div class="mt-20 d-flex flex-column gap-12">
        <div 
          v-for="course in filteredCourses" 
          :key="course.id"
          class="catalogue-course-card p-16 radius-12 border border-neutral-200 transition-2"
          :class="{
            'is-in-docket': isInDocket(course.id),
            'is-carryover': enrollmentStore.isCarryoverLocked(course.id)
          }"
        >
          <div class="d-flex flex-column flex-md-row align-items-md-center justify-content-between gap-16">
            <!-- Left: Course Details -->
            <div class="min-w-0">
              <div class="d-flex flex-wrap align-items-center gap-8 mb-6">
                <span class="fw-bold font-monospace text-sm text-neutral-900">{{ course.code }}</span>
                <span 
                  class="badge text-xxs px-8 py-2 radius-4 fw-bold"
                  :class="getCategoryBadgeClass(course.category)"
                >
                  {{ course.category }}
                </span>
                <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-8 py-2 radius-4 fw-semibold">
                  {{ course.creditUnits }} Credit Units
                </span>
                <span class="badge bg-neutral-100 text-secondary-light text-xxs px-8 py-2 radius-4">
                  {{ course.level }}
                </span>
                <!-- Prerequisite indicator -->
                <span v-if="course.prerequisiteCode" class="text-xxs text-secondary-light d-inline-flex align-items-center gap-4">
                  <i class="ri-git-branch-line"></i> Prereq: {{ course.prerequisiteCode }}
                  <span v-if="course.prerequisitePassed" class="text-success-600 fw-bold">(Passed ✓)</span>
                  <span v-else class="text-danger-600 fw-bold">(Pending)</span>
                </span>
              </div>

              <h6 class="text-sm fw-bold text-neutral-900 mb-4">
                {{ course.title }}
              </h6>

              <p v-if="course.description" class="text-secondary-light text-xs mb-6 text-line-2">
                {{ course.description }}
              </p>

              <div class="d-flex flex-wrap align-items-center gap-12 text-xxs text-secondary-light">
                <span class="d-inline-flex align-items-center gap-4">
                  <i class="ri-user-voice-line text-primary-500"></i> Lecturer: {{ course.lecturerName || 'Faculty Board' }}
                </span>
                <span>•</span>
                <span class="d-inline-flex align-items-center gap-4">
                  <i class="ri-building-line text-secondary-light"></i> Dept of Computer Science
                </span>
              </div>
            </div>

            <!-- Right: Action Button -->
            <div class="flex-shrink-0 text-md-end">
              <!-- Case 1: Mandatory Carryover (Locked) -->
              <span 
                v-if="enrollmentStore.isCarryoverLocked(course.id)"
                class="badge bg-danger-100 text-danger-700 border border-danger-200 text-xs px-12 py-6 radius-8 d-inline-flex align-items-center gap-6 fw-bold"
              >
                <i class="ri-lock-2-fill"></i> Pre-Enrolled Carryover
              </span>

              <!-- Case 2: Already Added to Docket -->
              <div v-else-if="isInDocket(course.id)" class="d-flex align-items-center gap-8">
                <span class="badge bg-success-50 text-success-700 border border-success-200 text-xs px-10 py-6 radius-8 d-inline-flex align-items-center gap-4 fw-semibold">
                  <i class="ri-checkbox-circle-line"></i> In Docket
                </span>
                <button 
                  type="button" 
                  class="btn btn-outline-danger btn-xs radius-8 d-inline-flex align-items-center gap-4 px-10 py-6"
                  @click="enrollmentStore.removeCourse(course.id)"
                  title="Remove from docket"
                >
                  <i class="ri-delete-bin-line"></i> Remove
                </button>
              </div>

              <!-- Case 3: Available to Add -->
              <button 
                v-else
                type="button" 
                class="btn btn-primary btn-sm radius-8 d-inline-flex align-items-center gap-6 px-16 py-8 shadow-xs fw-semibold"
                :disabled="isExceedingUnits(course.creditUnits)"
                @click="enrollmentStore.addCourse(course)"
              >
                <i class="ri-add-line text-sm"></i>
                <span>+ Add to Docket</span>
              </button>
            </div>
          </div>
        </div>

        <!-- No matching courses -->
        <div v-if="filteredCourses.length === 0" class="text-center py-36">
          <i class="ri-search-2-line text-3xl text-neutral-400 d-block mb-8"></i>
          <h6 class="text-sm fw-bold text-neutral-800 mb-4">No matching courses found</h6>
          <p class="text-secondary-light text-xs mb-8">
            Try adjusting your search query or category filter.
          </p>
          <button 
            type="button" 
            class="btn btn-outline-secondary btn-xs radius-6"
            @click="searchFilter = ''; activeCategory = 'All'"
          >
            Reset Filters
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useEnrollmentStore } from '@/stores/enrollment.js';

export default {
  name: 'CourseCatalogueSection',
  setup() {
    const enrollmentStore = useEnrollmentStore();

    const searchFilter = ref('');
    const activeCategory = ref('All');
    const categoryTabs = ['All', 'Core', 'Elective'];

    const filteredCourses = computed(() => {
      let list = enrollmentStore.availableCourses;

      // Filter by category
      if (activeCategory.value === 'Core') {
        list = list.filter(c => 
          (c.category || '').toLowerCase().includes('core') || 
          (c.category || '').toLowerCase().includes('compulsory') ||
          (c.category || '').toLowerCase().includes('general')
        );
      } else if (activeCategory.value === 'Elective') {
        list = list.filter(c => (c.category || '').toLowerCase().includes('elective'));
      }

      // Filter by text search
      if (searchFilter.value.trim()) {
        const query = searchFilter.value.toLowerCase().trim();
        list = list.filter(c => 
          c.code.toLowerCase().includes(query) ||
          c.title.toLowerCase().includes(query) ||
          (c.description || '').toLowerCase().includes(query) ||
          (c.lecturerName || '').toLowerCase().includes(query)
        );
      }

      return list;
    });

    const isInDocket = (courseId) => {
      return enrollmentStore.selectedCourseIds.includes(courseId);
    };

    const isExceedingUnits = (units) => {
      return (enrollmentStore.totalSelectedUnits + units) > 24;
    };

    const getCategoryBadgeClass = (category) => {
      const cat = (category || '').toLowerCase();
      if (cat.includes('core') || cat.includes('compulsory')) {
        return 'bg-neutral-900 text-white';
      }
      if (cat.includes('elective')) {
        return 'bg-purple-100 text-purple-700 border border-purple-200';
      }
      return 'bg-info-100 text-info-700';
    };

    return {
      enrollmentStore,
      searchFilter,
      activeCategory,
      categoryTabs,
      filteredCourses,
      isInDocket,
      isExceedingUnits,
      getCategoryBadgeClass
    };
  }
};
</script>

<style scoped>
.catalogue-course-card {
  background-color: var(--bs-card-bg, #fff);
}

.catalogue-course-card:hover {
  border-color: rgba(72, 127, 255, 0.4) !important;
  background-color: rgba(72, 127, 255, 0.02);
  transform: translateY(-1px);
}

.catalogue-course-card.is-in-docket {
  border-color: rgba(72, 127, 255, 0.5) !important;
  background-color: rgba(72, 127, 255, 0.04);
}

.catalogue-course-card.is-carryover {
  border-color: rgba(239, 68, 68, 0.3) !important;
  background-color: rgba(239, 68, 68, 0.02);
}

.text-line-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.btn-xs {
  padding: 4px 10px;
  font-size: 0.75rem;
}
</style>
