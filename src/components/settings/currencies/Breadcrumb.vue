<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Currencies </h1>
      <div class="">
        <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard </router-link>
        <router-link to="/general" class="text-secondary-light hover-text-primary hover-underline "> /
          Settings</router-link>
        <span class="text-secondary-light">/ Currencies</span>
      </div>
    </div>
    <button type="button" class="my-sidebar-btn btn btn-primary-600 d-flex align-items-center gap-6" @click="$emit('open-add-sidebar')">
      <span class="d-flex text-md">
        <i class="ri-add-large-line"></i>
      </span>
      Add Currencies
    </button>
  </div>
</template>

<script>
export default {
  name: "CurrenciesBreadcrumb",
  emits: ['open-add-sidebar']
}
</script>
