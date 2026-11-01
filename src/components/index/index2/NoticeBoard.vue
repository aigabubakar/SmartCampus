<template>
  <div class="card h-100 shadow-1 radius-16 border-0">
    <div class="card-body p-0">
      <div class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <div>
          <h6 class="text-lg mb-0 fw-bold text-neutral-900">Student Bulletins & Campus Notices</h6>
          <span class="text-secondary-light text-xs">Official Registry, Examination & Senate Circulars</span>
        </div>
        <router-link to="/notice-board" class="text-primary-600 text-xs fw-semibold d-flex align-items-center gap-4">
          View All Bulletins
          <iconify-icon icon="solar:arrow-right-linear"></iconify-icon>
        </router-link>
      </div>

      <div class="ps-20 pt-20 pb-20">
        <div class="pe-20 d-flex flex-column gap-20 max-h-490-px overflow-y-auto scroll-sm">
          <div 
            v-for="notice in notices" 
            :key="notice.id"
            class="d-flex align-items-start gap-16 pb-16 border-bottom border-neutral-100 last-border-0"
          >
            <div 
              class="w-40-px h-40-px rounded-circle d-flex align-items-center justify-content-center flex-shrink-0 text-lg"
              :class="notice.senderColor || 'bg-primary-50 text-primary-600'"
            >
              <iconify-icon :icon="notice.senderIcon || 'solar:document-text-bold'"></iconify-icon>
            </div>
            
            <div class="flex-grow-1">
              <div class="d-flex align-items-center justify-content-between flex-wrap gap-6 mb-4">
                <span class="badge bg-neutral-100 text-neutral-800 text-xs px-8 py-2 radius-4 fw-semibold">
                  {{ notice.sender }}
                </span>
                <div class="d-flex align-items-center gap-6">
                  <span class="badge radius-4 px-6 py-2 text-xxs fw-bold" :class="notice.priorityClass">
                    {{ notice.priority }}
                  </span>
                  <span class="text-secondary-light text-xs">{{ notice.date }}</span>
                </div>
              </div>

              <h6 class="mb-4 mt-6 text-sm fw-bold text-neutral-900">
                {{ notice.title }}
              </h6>
              <p class="text-secondary-light text-xs mb-0 line-clamp-2">
                {{ notice.description }}
              </p>
            </div>
          </div>

          <div v-if="notices.length === 0" class="text-center py-24 text-secondary-light">
            <iconify-icon icon="solar:document-medicine-bold-duotone" class="text-3xl text-neutral-300 d-block mx-auto mb-6"></iconify-icon>
            <p class="text-xs mb-0">No active student notices at this time.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useNoticeStore } from '@/stores/notices.js';

export default {
  name: "NoticeBoard2",
  setup() {
    const noticeStore = useNoticeStore();
    const notices = computed(() => noticeStore.noticesForCurrentUser);

    return {
      notices
    };
  }
}
</script>
