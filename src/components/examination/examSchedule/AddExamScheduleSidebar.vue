<template>
<div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isOpen, 'active-translate-0': isOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add New Exam Schedule</h5>
        <button type="button" @click="$emit('close')" class="close-my-sidebar text-danger-600 text-lg d-flex">
            <i class="ri-close-large-line"></i>
        </button>
    </div>
    <form action="#" class="d-flex flex-column p-20">
        <div class="row g-3">
             <div class="col-sm-6">
                <div class="">
                    <label for="examNm" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Exam Name</label>
                    <select class="form-control form-select" id="examNm">
                        <option value="" selected disabled>Select Exam</option>
                        <option value="Monthly Test">Monthly Test</option>
                        <option value="Mid Term">Mid Term</option>
                         <option value="Final Term">Final Term</option>
                    </select>
                </div>
            </div>
             <div class="col-sm-6">
                <div class="">
                    <label for="classSelect" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
                    <select class="form-control form-select" id="classSelect">
                        <option value="" selected disabled>Select Class</option>
                        <option value="One">One</option>
                        <option value="Two">Two</option>
                        <option value="Three">Three</option>
                         <option value="Four">Four</option>
                        <option value="Five">Five</option>
                    </select>
                </div>
            </div>
             <div class="col-sm-6">
                <div class="">
                    <label for="section" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section</label>
                    <select class="form-control form-select" id="section">
                        <option value="" selected disabled>Select Section</option>
                        <option value="A">A</option>
                        <option value="B">B</option>
                        <option value="C">C</option>
                        <option value="D">D</option>
                    </select>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="examRoom" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Room</label>
                    <select class="form-control form-select" id="examRoom">
                        <option value="" selected disabled>Select Room</option>
                        <option value="101">101</option>
                        <option value="102">102</option>
                        <option value="103">103</option>
                    </select>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="selectsubject" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Subject</label>
                    <select class="form-control form-select" id="selectsubject">
                        <option value="" selected disabled>Select Subject</option>
                        <option value="English">English</option>
                        <option value="Bangla">Bangla</option>
                        <option value="Math">Math</option>
                    </select>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="examDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Exam Date</label>
                    <input type="date" class="form-control" id="examDate">
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="startTime" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Start Time</label>
                    <input type="time" class="form-control" id="startTime">
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="endTime" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">End Time</label>
                    <input type="time" class="form-control" id="endTime">
                </div>
            </div>
             <div class="col-sm-6">
                <div class="">
                    <label for="duration" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Duration</label>
                    <input type="text" class="form-control" id="duration" placeholder="e.g. 3 Hours">
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
    name: "AddExamScheduleSidebar",
    props: {
        isOpen: Boolean
    },
    emits: ['close']
}
</script>
