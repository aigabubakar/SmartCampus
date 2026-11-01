<template>
  <div class="card h-100">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Login Details</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-sm-6">
          <div class="">
            <label for="myEmail" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Email <span
                class="text-danger-600">*</span>
            </label>
            <input type="email" class="form-control" id="myEmail" placeholder="Enter Email">
          </div>
        </div>
        <div class="col-sm-6">
          <div class="">
            <label for="your-password" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Password <span
                class="text-danger-600">*</span>
            </label>
            <div class="position-relative">
              <input type="password" id="your-password" class="form-control" placeholder="Enter Password">
              <span class="toggle-password ri-eye-line cursor-pointer position-absolute end-0 top-50 translate-middle-y me-16 text-secondary-light" @click="togglePassword"></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginDetails",
  methods: {
    togglePassword(event) {
        const icon = event.target;
        const input = icon.previousElementSibling;

        if (input.type === 'password') {
            input.type = 'text';
            icon.classList.remove('ri-eye-line');
            icon.classList.add('ri-eye-off-line');
        } else {
            input.type = 'password';
             icon.classList.remove('ri-eye-off-line');
            icon.classList.add('ri-eye-line');
        }
    }
  }
}
</script>
