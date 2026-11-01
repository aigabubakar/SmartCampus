<template>
  <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active-translate-0': isActive }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
      <h5 class="text-lg mb-0">Edit Language </h5>
      <button type="button" class="close-edit-sidebar text-danger-600 text-lg d-flex" @click="$emit('close')">
        <i class="ri-close-large-line"></i>
      </button>
    </div>
    <form action="#" class="d-flex flex-column p-20" @submit.prevent="update">
      <div class="row g-3">
        <div class="col-sm-12">
          <div class="">
            <label for="languageNameEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Language Name</label>
            <input type="text" class="form-control" id="languageNameEdit" placeholder="Enter Language Name" v-model="localData.name">
          </div>
        </div>
        <div class="col-12">
          <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
            <button type="button" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="$emit('close')">
              Cancel
            </button>
            <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
              Update
            </button>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "EditLanguageSidebar",
  props: {
    isActive: {
      type: Boolean,
      default: false
    },
    languageData: {
      type: Object,
      default: () => ({ name: '' })
    }
  },
  emits: ['close', 'update'],
  data() {
    return {
      localData: { ...this.languageData }
    }
  },
  watch: {
    languageData: {
      handler(newVal) {
        this.localData = { ...newVal };
      },
      deep: true
    }
  },
  methods: {
    update() {
      this.$emit('update', this.localData);
    }
  }
}
</script>
