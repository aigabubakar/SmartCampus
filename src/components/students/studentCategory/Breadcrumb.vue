<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h6 class="fw-semibold mb-4">Student Categories</h6>
      <div class="">
        <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard</router-link>
        <span class="text-secondary-light">/ Student Categories</span>
      </div>
    </div>
    <button type="button" class="my-sidebar-btn btn btn-primary-600 d-flex align-items-center gap-6" @click="$emit('openSidebar')">
      <span class="d-flex text-md">
        <i class="ri-add-large-line"></i>
      </span>
      New Category
    </button>
  </div>
</template>

<script>
export default {
  name: 'Breadcrumb',
  emits: ['openSidebar']
}
</script>
