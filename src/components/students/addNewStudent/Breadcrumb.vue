<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h6 class="fw-semibold mb-4 text-primary-light">Add New Student</h6>
      <div class="">
        <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard </router-link>
        <router-link to="/student-list" class="text-secondary-light hover-text-primary hover-underline "> /
          Student</router-link>
        <span class="text-secondary-light"> / Add New Student</span>
      </div>
    </div>
    <router-link to="/add-new-student" class="btn btn-primary-600 d-flex align-items-center gap-6 d-none">
      <span class="d-flex text-md">
        <i class="ri-add-large-line"></i>
      </span>
      Add Student
    </router-link>
  </div>
</template>

<script>
export default {
  name: "Breadcrumb"
}
</script>
