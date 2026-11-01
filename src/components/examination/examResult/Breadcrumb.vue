<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Exam Result</h1>
      <div class="">
        <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard</router-link>
        <span class="text-secondary-light"> / Exam Result</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: "Breadcrumb"
}
</script>
