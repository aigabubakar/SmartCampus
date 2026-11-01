<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Fees Collect</h1>
      <div class="">
        <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard</router-link>
        <span class="text-secondary-light"> / Fees Collect</span>
      </div>
    </div>
    <button type="button" class="my-sidebar-btn btn btn-primary-600 d-flex align-items-center gap-6" @click="$emit('openAddSidebar')">
      <span class="d-flex text-md">
        <i class="ri-wallet-3-line"></i>
      </span>
      Collect Fees
    </button>
  </div>
</template>

<script>
export default {
  name: "Breadcrumb",
  emits: ['openAddSidebar']
}
</script>
