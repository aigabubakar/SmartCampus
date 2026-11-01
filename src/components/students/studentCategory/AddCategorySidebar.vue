<template>
  <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{'active': isOpen}" @click="$emit('close')">
  </div>
  <div
    class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300 active-translate-0" :class="{'active': isOpen}">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add New Student Category</h5>
        <button type="button" class="close-my-sidebar text-danger-600 text-lg d-flex" @click="$emit('close')">
            <i class="ri-close-large-line"></i>
        </button>
    </div>
    <form action="#" class="d-flex flex-column gap-20 p-20">
        <div class="">
            <label for="studentCategoryName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Student
                Category Name </label>
            <input type="text" class="form-control" id="studentCategoryName" placeholder="Enter Student Category Name">
        </div>
        <div class="">
            <label for="studentStatus" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
            <select id="studentStatus" class="form-control form-select">
                <option value="Select a class" disabled>Select a Status</option>
                <option value="Active">Active</option>
                <option value="Inactive">Inactive</option>
            </select>
        </div>
        <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
            <button type="reset"
                class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="$emit('close')">
                Cancel
            </button>
            <button type="submit" class="btn btn-primary-600 text-md px-48 py-12 radius-8">
                Save
            </button>
        </div>
    </form>
</div>
</template>

<script>
export default {
  name: "AddCategorySidebar",
  props: {
    isOpen: {
        type: Boolean,
        default: false
    }
  },
  emits: ['close']
}
</script>
