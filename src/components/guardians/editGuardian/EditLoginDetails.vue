<template>
    <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
            <h6 class="text-lg fw-semibold mb-0">Login Details</h6>
        </div>
        <div class="card-body p-20">
            <div class="row gy-3">
                <div class="col-sm-6">
                    <div class="">
                        <label for="myEmail" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Email
                            <span class="text-danger-600">*</span>
                        </label>
                        <input type="email" class="form-control" id="myEmail" placeholder="Enter Email"
                            v-model="email">
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="">
                        <label for="your-password"
                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Password
                            <span class="text-danger-600">*</span>
                        </label>
                        <div class="position-relative">
                            <input :type="isPasswordVisible ? 'text' : 'password'" id="your-password"
                                class="form-control" placeholder="Enter your password" v-model="password">
                            <span
                                class="toggle-password ri-eye-line cursor-pointer position-absolute end-0 top-50 translate-middle-y me-16 text-secondary-light"
                                :class="{ 'ri-eye-off-line': isPasswordVisible }"
                                @click="togglePasswordVisibility"></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: "EditLoginDetails",
    setup() {
        const email = ref('');
        const password = ref(''); // Usually wouldn't pre-fill password, but for edits maybe blank or masked.
        const isPasswordVisible = ref(false);

        const togglePasswordVisibility = () => {
            isPasswordVisible.value = !isPasswordVisible.value;
        };

        return {
            email,
            password,
            isPasswordVisible,
            togglePasswordVisibility
        };
    }
}
</script>
