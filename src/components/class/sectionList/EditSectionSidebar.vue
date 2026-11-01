<template>
<div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isOpen, 'active-translate-0': isOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Section</h5>
        <button type="button" @click="$emit('close')" class="close-edit-sidebar text-danger-600 text-lg d-flex">
            <i class="ri-close-large-line"></i>
        </button>
    </div>
    <form action="#" class="d-flex flex-column p-20">
        <div class="row g-3">
            <div class="col-sm-12">
                <div class="">
                    <label for="sectionNameEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section Name</label>
                    <input type="text" class="form-control" id="sectionNameEdit" placeholder="Enter section name" :value="sectionData?.name">
                </div>
            </div>
            <div class="col-sm-12">
                <div class="">
                    <label for="sectionStatusEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                    <select id="sectionStatusEdit" class="form-control form-select" :value="sectionData?.status">
                        <option value="Select a subject" disabled>Select Status</option>
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
    name: "EditSectionSidebar",
    props: {
        isOpen: Boolean,
        sectionData: Object
    },
    emits: ['close']
}
</script>
