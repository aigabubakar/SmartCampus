<template>
  <div 
    class="card shadow-1 radius-12 h-100 transition-all cursor-pointer" 
    :class="[gradientBg, { 'border border-primary-200': isHighlighted }]"
    :data-bs-toggle="modalTarget ? 'modal' : null"
    :data-bs-target="modalTarget || null"
    @click="handleClick"
  >
    <div class="card-body p-20 d-flex flex-column justify-content-between">
      
      <!-- Top row: Icon, Title & Badge -->
      <div>
        <div class="d-flex align-items-center justify-content-between gap-12 mb-12">
          <div class="d-flex align-items-center gap-12">
            <div 
              class="w-44-px h-44-px rounded-circle d-flex justify-content-center align-items-center text-white text-xl flex-shrink-0"
              :class="iconColor"
            >
              <iconify-icon v-if="isIconify" :icon="icon" class="text-xl"></iconify-icon>
              <img v-else :src="icon" alt="Icon" class="w-24-px h-24-px object-fit-contain">
            </div>
            <div>
              <p class="fw-semibold text-neutral-800 text-sm mb-0">{{ title }}</p>
              <span v-if="subtitle" class="text-secondary-light text-xs d-block">{{ subtitle }}</span>
            </div>
          </div>

          <span v-if="badge" class="badge radius-6 text-xs px-8 py-4 fw-semibold" :class="badgeClass">
            {{ badge }}
          </span>
        </div>

        <!-- Metric Value -->
        <h4 class="fw-bold text-neutral-900 mb-0 mt-8">{{ count }}</h4>
      </div>

      <!-- Trend & Subtext footer -->
      <div class="pt-12 mt-8 border-top border-neutral-200 border-opacity-50 d-flex align-items-center justify-content-between text-xs">
        <div class="d-flex align-items-center gap-6">
          <span 
            v-if="trendValue" 
            class="d-inline-flex align-items-center gap-2 fw-bold"
            :class="trendIsPositive ? 'text-success-600' : 'text-danger-600'"
          >
            {{ trendValue }}
            <iconify-icon :icon="trendIsPositive ? 'solar:arrow-up-linear' : 'solar:arrow-down-linear'" class="text-xs"></iconify-icon>
          </span>
          <span class="text-secondary-light">{{ trendLabel || 'vs Last Semester' }}</span>
        </div>
        
        <span v-if="modalTarget" class="text-primary-600 fw-semibold d-flex align-items-center gap-2">
          Inspect
          <iconify-icon icon="solar:arrow-right-linear" class="text-xs"></iconify-icon>
        </span>
      </div>

    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: "Widget",
  props: {
    gradientBg: {
      type: String,
      default: 'gradient-bg-end-1'
    },
    iconColor: {
      type: String,
      default: 'bg-primary-600'
    },
    icon: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    subtitle: {
      type: String,
      default: ''
    },
    count: {
      type: String,
      required: true
    },
    badge: {
      type: String,
      default: ''
    },
    badgeClass: {
      type: String,
      default: 'bg-primary-50 text-primary-600'
    },
    trendValue: {
      type: String,
      default: ''
    },
    trendIsPositive: {
      type: Boolean,
      default: true
    },
    trendLabel: {
      type: String,
      default: ''
    },
    to: {
      type: String,
      default: ''
    },
    modalTarget: {
      type: String,
      default: ''
    },
    isHighlighted: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const router = useRouter();

    const isIconify = computed(() => {
      return props.icon && (props.icon.includes(':') || !props.icon.includes('/'));
    });

    const handleClick = () => {
      if (props.to) {
        router.push(props.to);
      }
    };

    return {
      isIconify,
      handleClick
    };
  }
}
</script>
