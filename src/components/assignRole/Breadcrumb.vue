<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Assign Role </h1>
      <div class="">
        <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard </router-link>
        <router-link to="/employee-list" class="text-secondary-light hover-text-primary hover-underline "> /
          HRM</router-link>
        <span class="text-secondary-light">/ Assign Role</span>
      </div>
    </div>
    <button type="button" class="my-sidebar-btn btn btn-primary-600 d-flex align-items-center gap-6">
      <span class="d-flex text-md">
        <i class="ri-add-large-line"></i>
      </span>
      Add Assign Role
    </button>
  </div>
</template>

<script>
export default {
  name: "Breadcrumb"
}
</script>
