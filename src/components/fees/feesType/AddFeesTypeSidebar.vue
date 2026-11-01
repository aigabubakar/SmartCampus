<template>
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300"
        :class="{ 'active-translate-0': isOpen, 'active': isOpen }">
        <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
            <h5 class="text-lg mb-0">Add New Fees Type</h5>
            <button type="button" class="close-my-sidebar text-danger-600 text-lg d-flex" @click="$emit('close')">
                <i class="ri-close-large-line"></i>
            </button>
        </div>
        <form @submit.prevent="submitForm" class="d-flex flex-column p-20">
            <div class="row g-3">
                <div class="col-sm-12">
                    <div class="">
                        <label for="feesName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Fees Name</label>
                        <input type="text" class="form-control" id="feesName" placeholder="Enter Fees Type name" v-model="form.name">
                    </div>
                </div>
                <div class="col-sm-12">
                    <div class="">
                        <label for="feesStatus" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                        <select id="feesStatus" class="form-control form-select" v-model="form.status">
                            <option value="" disabled>Select Status</option>
                            <option value="Active">Active</option>
                            <option value="Inactive">Inactive</option>
                        </select>
                    </div>
                </div>
                <div class="col-12">
                    <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
                        <button type="button"
                            class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8"
                            @click="$emit('close')">
                            Cancel
                        </button>
                        <button type="submit"
                            class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import { reactive, watch } from 'vue';

export default {
    name: "AddFeesTypeSidebar",
    props: {
        isOpen: {
            type: Boolean,
            default: false
        }
    },
    emits: ['close', 'save'],
    setup(props, { emit }) {
        const form = reactive({
            name: '',
            status: ''
        });

        watch(() => props.isOpen, (newVal) => {
            if (!newVal) {
                form.name = '';
                form.status = '';
            }
        });

        const submitForm = () => {
             // Basic validation
             if (!form.name || !form.status) {
                 alert('Please fill all fields');
                 return;
             }
             emit('save', { ...form });
             emit('close');
        };

        return {
            form,
            submitForm
        };
    }
}
</script>
