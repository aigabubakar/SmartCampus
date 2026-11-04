<template>
  <div class="card h-100 shadow-1 radius-16 border-0">
    <div class="card-body p-0 d-flex flex-column">
      <div class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <div>
          <div class="d-flex align-items-center gap-8">
            <h6 class="text-lg mb-0 fw-bold text-neutral-900">Campus Notices & Circulars</h6>
            <span v-if="shouldRollOver" class="badge bg-primary-50 text-primary-600 text-xxs px-8 py-2 rounded-pill d-inline-flex align-items-center gap-4">
              <span class="w-6-px h-6-px bg-primary-600 rounded-circle pulse-dot"></span> Live Rollover
            </span>
          </div>
          <span class="text-secondary-light text-xs">Real-time Senate, Registry & Faculty Dispatches</span>
        </div>
        <router-link to="/notice-board" class="text-primary-600 text-xs fw-semibold d-flex align-items-center gap-4">
          View All Circulars
          <iconify-icon icon="solar:arrow-right-linear"></iconify-icon>
        </router-link>
      </div>

      <div class="px-20 pt-16 pb-16 flex-grow-1">
        <div class="notice-rollover-wrapper" :class="{ 'has-rollover': shouldRollOver }">
          <div :class="shouldRollOver ? 'notice-rollover-track' : 'd-flex flex-column gap-14'">
            <div 
              v-for="(notice, idx) in displayNotices" 
              :key="`${notice.id}-${idx}`"
              class="notice-card-item d-flex align-items-start gap-14 pb-14 border-bottom border-neutral-100 last-border-0"
            >
              <div 
                class="w-36-px h-36-px rounded-circle d-flex align-items-center justify-content-center flex-shrink-0 text-base"
                :class="notice.senderColor || 'bg-primary-50 text-primary-600'"
              >
                <iconify-icon :icon="notice.senderIcon || 'solar:document-text-bold'"></iconify-icon>
              </div>
              
              <div class="flex-grow-1 min-w-0">
                <div class="d-flex align-items-center justify-content-between flex-wrap gap-6 mb-4">
                  <span class="badge bg-neutral-100 text-neutral-800 text-xxs px-6 py-2 radius-4 fw-semibold text-truncate" style="max-width: 150px;">
                    {{ notice.sender }}
                  </span>
                  <div class="d-flex align-items-center gap-6">
                    <span class="badge radius-4 px-6 py-2 text-xxs fw-bold" :class="notice.priorityClass">
                      {{ notice.priority }}
                    </span>
                    <span class="text-secondary-light text-xxs">{{ notice.date }}</span>
                  </div>
                </div>

                <h6 class="mb-4 mt-4 text-xs fw-bold text-neutral-900 text-truncate">
                  {{ notice.title }}
                </h6>
                <p class="notice-details-text text-secondary-light text-xxs mb-0">
                  {{ notice.description }}
                </p>
              </div>
            </div>

            <div v-if="notices.length === 0" class="text-center py-24 text-secondary-light">
              <p class="text-xs mb-0">No active notices at this time.</p>
            </div>
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
  name: "NoticeBoard",
  setup() {
    const noticeStore = useNoticeStore();
    const notices = computed(() => noticeStore.noticesForCurrentUser);
    const shouldRollOver = computed(() => notices.value.length > 2);
    const displayNotices = computed(() => {
      if (shouldRollOver.value) {
        return [...notices.value, ...notices.value];
      }
      return notices.value;
    });

    return {
      notices,
      displayNotices,
      shouldRollOver
    };
  }
}
</script>

<style scoped>
.notice-rollover-wrapper {
  height: 380px;
  max-height: 380px;
  overflow: hidden;
  position: relative;
}

.notice-rollover-wrapper.has-rollover {
  mask-image: linear-gradient(to bottom, transparent 0%, black 5%, black 95%, transparent 100%);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 5%, black 95%, transparent 100%);
}

.notice-rollover-track {
  display: flex;
  flex-direction: column;
  gap: 14px;
  animation: rollOverMarquee 28s linear infinite;
  will-change: transform;
}

.notice-rollover-wrapper:hover .notice-rollover-track {
  animation-play-state: paused;
}

@keyframes rollOverMarquee {
  0% {
    transform: translateY(0);
  }
  100% {
    transform: translateY(-50%);
  }
}

.notice-card-item {
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  padding: 8px 10px;
  border-radius: 8px;
  cursor: pointer;
}

.notice-card-item:hover {
  background-color: rgba(72, 127, 255, 0.06);
  transform: translateX(3px);
}

.notice-details-text {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.45;
  transition: all 0.25s ease-in-out;
}

.notice-card-item:hover .notice-details-text {
  -webkit-line-clamp: 5;
  color: var(--neutral-800) !important;
}

.pulse-dot {
  animation: pulseDotAnim 2s infinite ease-in-out;
}

@keyframes pulseDotAnim {
  0%, 100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(0.7);
    opacity: 0.4;
  }
}
</style>
