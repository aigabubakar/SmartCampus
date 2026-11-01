<template>
<div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isOpen, 'active-translate-0': isOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add New Class Room</h5>
        <button type="button" @click="$emit('close')" class="close-my-sidebar text-danger-600 text-lg d-flex">
            <i class="ri-close-large-line"></i>
        </button>
    </div>
    <form action="#" class="d-flex flex-column p-20">
        <div class="row g-3">
            <div class="col-sm-12">
                <div class="">
                    <label for="roomName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Room Name</label>
                    <input type="text" class="form-control" id="roomName" placeholder="Enter Class Room name">
                </div>
            </div>
             <div class="col-sm-12">
                <div class="">
                    <label for="roomCapacity" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Capacity</label>
                    <input type="text" class="form-control" id="roomCapacity" placeholder="Enter room capacity">
                </div>
            </div>
            <div class="col-sm-12">
                <div class="">
                    <label for="roomStatus" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                    <select id="roomStatus" class="form-control form-select">
                        <option value="" selected disabled>Select Status</option>
                        <option value="Active">Active</option>
                        <option value="Inactive">Inactive</option>
                    </select>
                </div>
            </div>
            <div class="col-12">
                <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
                    <button type="button" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="$emit('close')">Cancel</button>
                    <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">Save</button>
                </div>
            </div>
        </div>
    </form>
</div>
</template>
<script>
export default {
    name: "AddClassRoomSidebar",
    props: {
        isOpen: Boolean
    },
    emits: ['close']
}
</script>
