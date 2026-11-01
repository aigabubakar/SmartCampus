<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Student Attendance</h1>
      <div class="">
        <a href="javascript:void(0)" class="text-secondary-light hover-text-primary hover-underline">Dashboard</a>
        <span class="text-secondary-light"> / Student Attendance</span>
      </div>
    </div>
    <!-- Add Teacher button was hidden in the HTML (d-none), keeping it hidden or removing it implies adherence to design. I will keep it consistent with the request but if it's hidden I might leave it out or hide it. -->
  </div>
</template>

<script>
export default {
  name: "Breadcrumb"
}
</script>
