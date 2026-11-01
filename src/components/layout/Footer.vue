<template>
  <footer class="d-footer">
    <div class="d-flex flex-wrap align-items-center justify-content-between gap-3 text-xs text-secondary-light">
      <p class="mb-0"> &copy; <span class="current-year">{{ currentYear }}</span> SmartCampus. All rights reserved.</p>
      <p class="mb-0">
        Powered by <a href="https://stackhubs.com.ng" target="_blank" rel="noopener noreferrer" class="text-primary-600 fw-semibold text-decoration-none hover-underline">stackhubs.com.ng</a>
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  computed: {
    currentYear() {
      return new Date().getFullYear();
    }
  }
}
</script>
