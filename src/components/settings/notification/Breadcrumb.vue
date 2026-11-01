<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Notification</h1>
      <div class="">
        <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard </router-link>
        <router-link to="/general" class="text-secondary-light hover-text-primary hover-underline "> /
          Settings</router-link>
        <span class="text-secondary-light">/ Notification</span>
      </div>
    </div>
    <a href="javascript:void(0)" class="btn btn-primary-600 d-flex align-items-center gap-6 d-none">
      <span class="d-flex text-md">
        <i class="ri-add-large-line"></i>
      </span>
      Notification
    </a>
  </div>
</template>

<script>
export default {
  name: "NotificationBreadcrumb"
}
</script>
