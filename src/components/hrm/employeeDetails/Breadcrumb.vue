<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Employee Details</h1>
      <div class="">
        <a href="index.html" class="text-secondary-light hover-text-primary hover-underline">Dashboard</a>
        <a href="employee-list.html" class="text-secondary-light hover-text-primary hover-underline"> / HRM</a>
        <span class="text-secondary-light">/ Employee Details</span>
      </div>
    </div>
    <button type="button"
      class="btn btn-primary-600 d-flex align-items-center gap-6 bg-base text-primary-light bg-hover-primary-600"
      @click="$emit('open-login-details')">
      <span class="d-flex text-md">
        <i class="ri-lock-2-line"></i>
      </span>
      Login Details
    </button>
  </div>
</template>

<script>
export default {
  name: "Breadcrumb",
  emits: ['open-login-details']
}
</script>
