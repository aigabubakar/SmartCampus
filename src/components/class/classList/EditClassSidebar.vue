<template>
<div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isOpen, 'active-translate-0': isOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Class</h5>
        <button type="button" @click="$emit('close')" class="close-edit-sidebar text-danger-600 text-lg d-flex">
            <i class="ri-close-large-line"></i>
        </button>
    </div>
    <form action="#" class="d-flex flex-column p-20">
        <div class="row g-3">
            <div class="col-sm-12">
                <div class="">
                    <label for="classNameEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class Name</label>
                    <input type="text" class="form-control" id="classNameEdit" placeholder="Enter Class name" :value="classData?.name">
                </div>
            </div>
             <div class="col-sm-12">
                <div class="">
                    <label for="classSectionEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section</label>
                     <select id="classSectionEdit" class="form-control form-select">
                        <option value="" disabled>Select Section</option>
                        <option value="A">A</option>
                        <option value="B">B</option>
                        <option value="C">C</option>
                        <option value="D">D</option>
                    </select>
                </div>
            </div>
            <div class="col-sm-12">
                <div class="">
                    <label for="classStatusEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                    <select id="classStatusEdit" class="form-control form-select" :value="classData?.status">
                        <option value="" disabled>Select Status</option>
                        <option value="Active">Active</option>
                        <option value="Inactive">Inactive</option>
                    </select>
                </div>
            </div>
            <div class="col-12">
                <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
                    <button type="button" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="$emit('close')">Cancel</button>
                    <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8">Update</button>
                </div>
            </div>
        </div>
    </form>
</div>
</template>
<script>
export default {
    name: "EditClassSidebar",
    props: {
        isOpen: Boolean,
        classData: Object
    },
    emits: ['close']
}
</script>
