<template>
    <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300"
        :class="{ 'active-translate-0': isOpen, 'active': isOpen }">
        <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
            <h5 class="text-lg mb-0">Edit Fees Group</h5>
            <button type="button" class="close-edit-sidebar text-danger-600 text-lg d-flex" @click="$emit('close')">
                <i class="ri-close-large-line"></i>
            </button>
        </div>
        <form @submit.prevent="submitForm" class="d-flex flex-column p-20">
            <div class="row g-3">
                 <div class="col-sm-12">
                    <div class="">
                        <label for="editGroupName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Group Name</label>
                        <input type="text" class="form-control" id="editGroupName" placeholder="Enter Group Name" v-model="form.name">
                    </div>
                </div>
                <div class="col-sm-12">
                    <div class="">
                        <label for="editFeesType" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Fees Type</label>
                        <select id="editFeesType" class="form-control form-select" v-model="form.feesType">
                            <option value="" disabled>Select fees type</option>
                            <option value="May month fees">May month fees</option>
                            <option value="Admission fees">Admission fees</option>
                            <option value="Exam fees">Exam fees</option>
                            <!-- Note: The mock data has a comma separated string, but the select can only pick one. 
                                 In a real scenario, this would handle multi-select properly or parse the string.
                                 For now, we'll just bind whatever is possible or defaulting -->
                        </select>
                    </div>
                </div>
                <div class="col-sm-12">
                    <div class="">
                        <label for="editGroupStatus" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                        <select id="editGroupStatus" class="form-control form-select" v-model="form.status">
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
                            class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8">
                            Update
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
    name: "EditFeesGroupSidebar",
    props: {
        isOpen: {
            type: Boolean,
            default: false
        },
        feesGroup: {
            type: Object,
            default: () => ({ name: '', feesType: '', status: '' })
        }
    },
    emits: ['close', 'update'],
    setup(props, { emit }) {
        const form = reactive({
            name: '',
            feesType: '',
            status: ''
        });

        watch(() => props.feesGroup, (newVal) => {
            if (newVal) {
                form.name = newVal.name;
                // Simple handling for feesType - in real app, might need to split ID or array
                // For this mock, we'll just try to match if it's a single value, or default to first part if multi
                form.feesType = newVal.feesType.split(',')[0].trim() || ''; 
                form.status = newVal.status;
            }
        }, { immediate: true, deep: true });

        const submitForm = () => {
             if (!form.name || !form.feesType || !form.status) {
                 alert('Please fill all fields');
                 return;
             }
             emit('update', { ...form });
             emit('close');
        };

        return {
            form,
            submitForm
        };
    }
}
</script>
