<template>
  <div>
    <ThemeCustomizer />
    
    <!-- Overlay -->
    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300"></div>

    <div class="d-lg-flex bg-white">
      <!-- Left Image -->
      <div class="w-50 d-lg-block d-none overflow-hidden d-flex">
        <img src="/assets/images/thumbs/login-img.png" alt="Register Image" class="w-100 h-100 object-fit-cover">
      </div>

      <!-- Right Form -->
      <div class="lg-w-50 px-24 py-40 d-flex justify-content-center align-items-center">
        <div class="max-w-540-px mx-auto w-100">

          <router-link to="/">
            <img src="/assets/images/logo.png" alt="Logo">
          </router-link>

          <div class="mt-48 mb-32">
            <h1 class="h6 fw-bold text-primary-light">Create Your Account 🚀</h1>
            <p class="text-sm text-secondary-light">
              Fill in the details to get started
            </p>
          </div>

          <form @submit.prevent="handleRegister" class="d-flex flex-column gap-24">

            <!-- Full Name -->
            <div>
              <label class="text-sm fw-semibold text-primary-light mb-8">
                Full Name <span class="text-danger-600">*</span>
              </label>
              <input type="text" class="form-control" placeholder="Enter your full name" v-model="formData.fullName" required>
            </div>

            <!-- Email -->
            <div>
              <label class="text-sm fw-semibold text-primary-light mb-8">
                Email Address <span class="text-danger-600">*</span>
              </label>
              <input type="email" class="form-control" placeholder="Enter your email" v-model="formData.email" required>
            </div>

            <!-- Password -->
            <div>
              <label for="password" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                Password
                <span class="text-danger-600">*</span>
              </label>
              <div class="position-relative">
                <input :type="showPassword ? 'text' : 'password'" id="password" class="form-control" placeholder="Enter your password" v-model="formData.password" required>
                <button type="button" @click="togglePassword" class="toggle-password btn p-0 border-0 bg-transparent position-absolute end-0 top-50 translate-middle-y me-16 text-secondary-light cursor-pointer" :class="showPassword ? 'ri-eye-off-line' : 'ri-eye-line'" aria-label="Toggle password visibility">
                </button>
              </div>
            </div>

            <!-- Confirm Password -->
            <div>
              <label for="confirmPassword" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                Confirm Password
                <span class="text-danger-600">*</span>
              </label>
              <div class="position-relative">
                <input :type="showConfirmPassword ? 'text' : 'password'" id="confirmPassword" class="form-control" placeholder="Confirm your password" v-model="formData.confirmPassword" required>
                <button type="button" @click="toggleConfirmPassword" class="toggle-password btn p-0 border-0 bg-transparent position-absolute end-0 top-50 translate-middle-y me-16 text-secondary-light cursor-pointer" :class="showConfirmPassword ? 'ri-eye-off-line' : 'ri-eye-line'" aria-label="Toggle password visibility">
                </button>
              </div>
            </div>

            <!-- Role Select -->
            <div>
              <label class="text-sm fw-semibold text-primary-light mb-8">
                Select Role
              </label>
              <select class="form-select" v-model="formData.role">
                <option value="">Choose your role</option>
                <option value="student">Student</option>
                <option value="teacher">Teacher</option>
                <option value="guardian">Guardian</option>
                <option value="admin">Admin</option>
              </select>
            </div>

            <!-- Terms -->
            <div class="form-check style-check d-flex align-items-center">
              <input class="form-check-input border border-neutral-400" type="checkbox" v-model="formData.agreeToTerms" id="agreeToTerms">
              <label class="form-check-label" for="agreeToTerms"> I agree to the <a href="#" class="text-primary-600 text-decoration-underline">Terms & Conditions</a> </label>
            </div>

            <!-- Submit -->
            <button type="submit" class="btn btn-primary-600 w-100 py-16 radius-8 text-sm fw-semibold">
              Create Account
            </button>

          </form>

          <!-- Login Link -->
          <div class="mt-24 text-center text-sm">
            Already have an account?
            <router-link to="/login" class="text-primary-600 fw-semibold text-decoration-underline">
              Log In
            </router-link>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';

export default {
  name: "RegisterPage",
  components: {
    ThemeCustomizer
  },
  setup() {
    const router = useRouter();
    const showPassword = ref(false);
    const showConfirmPassword = ref(false);

    const formData = ref({
      fullName: '',
      email: '',
      password: '',
      confirmPassword: '',
      role: '',
      agreeToTerms: false
    });

    const togglePassword = () => {
      showPassword.value = !showPassword.value;
    };

    const toggleConfirmPassword = () => {
      showConfirmPassword.value = !showConfirmPassword.value;
    };

    const handleRegister = () => {
      if (formData.value.password !== formData.value.confirmPassword) {
        alert('Passwords do not match!');
        return;
      }

      if (!formData.value.agreeToTerms) {
        alert('Please agree to the Terms & Conditions');
        return;
      }

      console.log('Register attempt with:', formData.value);
      // Add your registration logic here
      // After successful registration, redirect to login or dashboard
      // router.push('/login');
    };

    return {
      formData,
      showPassword,
      showConfirmPassword,
      togglePassword,
      toggleConfirmPassword,
      handleRegister
    };
  }
}
</script>

<style scoped>
.lg-w-50 {
  width: 100%;
}

@media (min-width: 992px) {
  .lg-w-50 {
    width: 50%;
  }
}

.max-w-540-px {
  max-width: 540px;
}
</style>
