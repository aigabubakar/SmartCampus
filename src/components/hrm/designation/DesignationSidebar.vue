<template>
  <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active-translate-0': isOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
      <h5 class="text-lg mb-0">{{ isEditMode ? 'Edit Designation' : 'Add Designation' }}</h5>
      <button type="button" class="text-danger-600 text-lg d-flex" @click="handleClose">
        <i class="ri-close-large-line"></i>
      </button>
    </div>
    
    <form @submit.prevent="handleSubmit" class="d-flex flex-column p-20">
      <div class="row g-3">
        <div class="col-sm-12">
          <div class="">
            <label for="designationName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
              Designation Name
            </label>
            <input type="text" class="form-control" id="designationName" v-model="formData.name" placeholder="Enter designation name" required>
          </div>
        </div>
        
        <div class="col-sm-12">
          <div class="">
            <label for="description" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
              Description
            </label>
            <textarea class="form-control" id="description" v-model="formData.description" placeholder="Enter Description" rows="4"></textarea>
          </div>
        </div>
        
        <div class="col-12">
          <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
            <button type="button" @click="handleCancel" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8">
              Cancel
            </button>
            <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
              {{ isEditMode ? 'Update' : 'Save' }}
            </button>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  name: "DesignationSidebar",
  props: {
    isOpen: {
      type: Boolean,
      default: false
    },
    designation: {
      type: Object,
      default: null
    }
  },
  emits: ['close', 'submit'],
  setup(props, { emit }) {
    const formData = ref({
      name: '',
      description: ''
    });

    const isEditMode = ref(false);

    // Watch for designation prop changes (for edit mode)
    watch(() => props.designation, (newVal) => {
      if (newVal) {
        isEditMode.value = true;
        formData.value = {
          id: newVal.id,
          name: newVal.name,
          description: newVal.description
        };
      } else {
        isEditMode.value = false;
        resetForm();
      }
    }, { immediate: true });

    const handleSubmit = () => {
      console.log('Designation submitted:', formData.value);
      emit('submit', { ...formData.value, isEdit: isEditMode.value });
      resetForm();
      emit('close');
    };

    const handleCancel = () => {
      resetForm();
      emit('close');
    };

    const handleClose = () => {
      resetForm();
      emit('close');
    };

    const resetForm = () => {
      formData.value = {
        name: '',
        description: ''
      };
      isEditMode.value = false;
    };

    return {
      formData,
      isEditMode,
      handleSubmit,
      handleCancel,
      handleClose
    };
  }
}
</script>
