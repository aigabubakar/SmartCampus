<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Student Details</h1>
      <div class="">
        <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard</router-link>
        <router-link to="/student-list" class="text-secondary-light hover-text-primary hover-underline"> / Student</router-link>
        <span class="text-secondary-light">/ Student Details</span>
      </div>
    </div>
    <button type="button" class="my-sidebar-btn btn btn-primary-600 d-flex align-items-center gap-6 bg-base text-primary-light bg-hover-primary-600">
      <span class="d-flex text-md">
        <i class="ri-lock-2-line"></i>
      </span>
      Login Details
    </button>
  </div>
</template>

<script>
export default {
  name: "Breadcrumb"
}
</script>
