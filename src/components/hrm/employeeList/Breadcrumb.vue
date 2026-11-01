<template>
  <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
    <div class="">
      <h1 class="fw-semibold mb-4 h6 text-primary-light">Employee List</h1>
      <div class="">
        <a href="index.html" class="text-secondary-light hover-text-primary hover-underline">Dashboard</a>
        <a href="employee-list.html" class="text-secondary-light hover-text-primary hover-underline"> / HRM</a>
        <span class="text-secondary-light">/ Employee List</span>
      </div>
    </div>
    <button type="button" class="btn btn-primary-600 d-flex align-items-center gap-6" @click="navigateToAddEmployee">
      <span class="d-flex text-md">
        <i class="ri-add-large-line"></i>
      </span>
      Add Employee
    </button>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: "Breadcrumb",
  setup() {
    const router = useRouter();

    const navigateToAddEmployee = () => {
      router.push('/add-employee');
    };

    return {
      navigateToAddEmployee
    };
  }
}
</script>
