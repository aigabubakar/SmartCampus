<template>
  <div v-if="isAuthorized">
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb />

        <div class="mt-24">
          <div class="card h-100 p-0 radius-12 overflow-hidden mt-24">
            <div class="card-body p-40">
              <div class="row justify-content-center">
                <div class="col-xxl-10">
                  <div class="text-center">
                    <h4 class="mb-0">Simple, Transparent Pricing</h4>
                  </div>

                  <div class="pricing-tab">
                    <div class="form-switch switch-primary d-flex align-items-center gap-3 mt-28 justify-content-center">
                      <label class="form-check-label line-height-1 fw-medium text-secondary-light" for="yes">Monthly</label>
                      <input 
                        class="form-check-input choose-plan-input" 
                        type="checkbox" 
                        role="switch" 
                        id="yes"
                        v-model="isAnnually"
                      >
                      <label class="form-check-label line-height-1 fw-medium text-secondary-light" for="yes">Annually</label>
                    </div>
                  </div>

                  <div class="row gy-4">
                    <div class="col-xxl-4 col-sm-6" v-for="(plan, index) in plans" :key="index">
                      <div 
                        class="pricing-plan position-relative radius-24 overflow-hidden border"
                        :class="[
                          plan.isPopular ? 'bg-primary-600 text-white z-1 featured-item' : 'bg-base'
                        ]"
                      >
                        <img v-if="plan.isPopular" src="@/assets/images/icons/pricing-shape.png" alt="Image" class="position-absolute end-0 top-10 z-n1">
                        <span v-if="plan.isPopular" class="bg-white text-primary-600 fw-bold radius-24 py-8 px-24 text-sm position-absolute end-0 top-0 z-1 rounded-start-top-0 rounded-end-bottom-0 shadow-sm">Popular</span>
                        
                        <div class="d-flex align-items-center gap-16">
                          <span 
                            class="w-72-px h-72-px d-flex justify-content-center align-items-center radius-16"
                            :class="plan.isPopular ? 'bg-base' : 'bg-primary-50'"
                          >
                            <img :src="plan.icon" alt="Image">
                          </span>
                          <div class="">
                            <span class="fw-medium text-md" :class="plan.isPopular ? 'text-white' : 'text-secondary-light'">{{ plan.subtitle }}</span>
                            <h6 class="mb-0" :class="{'text-white': plan.isPopular}">{{ plan.title }}</h6>
                          </div>
                        </div>
                        
                        <p class="mt-16 mb-0 mb-28" :class="plan.isPopular ? 'text-white' : 'text-secondary-light'">{{ plan.description }}</p>
                        
                        <h3 class="mb-24" :class="{'text-white': plan.isPopular}">
                          $<span class="price-range">{{ isAnnually ? plan.price * 10 : plan.price }}</span>
                          <span class="fw-medium text-md" :class="plan.isPopular ? 'text-white' : 'text-secondary-light'">/{{ isAnnually ? 'yearly' : 'monthly' }}</span>
                        </h3>
                        
                        <span class="mb-20 fw-medium">What's included</span>
                        <ul>
                          <li class="d-flex align-items-center gap-16 mb-16" v-for="(feature, idx) in plan.features" :key="idx">
                            <span 
                              class="w-24-px h-24-px d-flex justify-content-center align-items-center rounded-circle"
                              :class="plan.isPopular ? 'bg-white text-primary-600' : 'bg-primary-600'"
                            >
                              <iconify-icon icon="iconamoon:check-light" class="text-lg" :class="{'text-white': !plan.isPopular}"></iconify-icon>
                            </span>
                            <span class="text-lg" :class="plan.isPopular ? 'text-white' : 'text-secondary-light'">{{ feature }}</span>
                          </li>
                        </ul>

                        <button 
                          type="button" 
                          class="text-center text-sm btn-sm px-12 py-10 w-100 radius-8 mt-28"
                          :class="plan.isPopular ? 'bg-white text-primary-600 border border-white' : 'bg-primary-600 bg-hover-primary-700 text-white border border-primary-600'"
                          data-bs-toggle="modal" data-bs-target="#exampleModal"
                        >
                          Get started
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <Footer />
    </main>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import Breadcrumb from '@/components/subscriptionPlan/Breadcrumb.vue';
import priceIcon1 from '@/assets/images/icons/price-icon1.png';
import priceIcon2 from '@/assets/images/icons/price-icon2.png';
import priceIcon3 from '@/assets/images/icons/price-icon3.png';

export default {
  name: "SubscriptionPlan",
  components: {
    Sidebar,
    Navbar,
    Footer,
    Breadcrumb
  },
  setup() {
    const router = useRouter();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isAuthorized = computed(() => authStore.isSuperAdmin);

    onMounted(() => {
      if (!isAuthorized.value) {
        toastStore.error(
          'Security Interception: Subscription & Tenant Plan Configuration is restricted to the Super Administrator.',
          '403 Forbidden'
        );
        router.replace('/403');
      }
    });

    const isAnnually = ref(false);

    const plans = [
      {
        title: 'Basic',
        subtitle: 'For individuals',
        price: 99,
        description: 'Lorem ipsum dolor sit amet doloroli sitiol conse ctetur adipiscing elit.',
        icon: priceIcon1,
        isPopular: false,
        features: [
          'All analytics features',
          'Up to 250,000 tracked visits',
          'Normal support',
          'Up to 3 team members'
        ]
      },
      {
        title: 'Pro',
        subtitle: 'For startups',
        price: 199,
        description: 'Lorem ipsum dolor sit amet doloroli sitiol conse ctetur adipiscing elit.',
        icon: priceIcon2,
        isPopular: true,
        features: [
          'All analytics features',
          'Up to 250,000 tracked visits',
          'Normal support',
          'Up to 3 team members'
        ]
      },
      {
        title: 'Enterprise',
        subtitle: 'For big companies',
        price: 399,
        description: 'Lorem ipsum dolor sit amet doloroli sitiol conse ctetur adipiscing elit.',
        icon: priceIcon3,
        isPopular: false,
        features: [
          'All analytics features',
          'Up to 250,000 tracked visits',
          'Normal support',
          'Up to 3 team members'
        ]
      }
    ];

    return {
      isAuthorized,
      isAnnually,
      plans
    };
  }
}
</script>
