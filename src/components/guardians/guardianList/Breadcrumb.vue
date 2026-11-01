<template>
    <div class="breadcrumb d-flex flex-wrap align-items-center justify-content-between gap-3 mb-24">
        <div class="">
            <h1 class="fw-semibold mb-4 h6 text-primary-light">Guardian List</h1>
            <div class="">
                <router-link to="/" class="text-secondary-light hover-text-primary hover-underline">Dashboard </router-link>
                <span class="text-secondary-light">/ Guardian List</span>
            </div>
        </div>
        <router-link to="/add-new-guardian" class="btn btn-primary-600 d-flex align-items-center gap-6 ">
            <span class="d-flex text-md">
                <i class="ri-add-large-line"></i>
            </span>
            Add Guardian
        </router-link>
    </div>
</template>

<script>
export default {
    name: "Breadcrumb"
}
</script>
