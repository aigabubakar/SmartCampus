<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Transaction</h1>
      <div class="">
        <a href="index.html" class="text-secondary-light hover-text-primary hover-underline">Dashboard</a>
        <span class="text-secondary-light">/ Transaction</span>
      </div>
    </div>
    <button type="button" class="btn btn-primary-600 d-flex align-items-center gap-6" @click="$emit('open-add-sidebar')">
      <span class="d-flex text-md">
        <i class="ri-add-large-line"></i>
      </span>
      Add Transaction
    </button>
  </div>
</template>

<script>
export default {
  name: "Breadcrumb",
  emits: ['open-add-sidebar']
}
</script>
