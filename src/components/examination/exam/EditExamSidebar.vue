<template>
<div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isOpen, 'active-translate-0': isOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Exam</h5>
        <button type="button" @click="$emit('close')" class="close-edit-sidebar text-danger-600 text-lg d-flex">
            <i class="ri-close-large-line"></i>
        </button>
    </div>
    <form action="#" class="d-flex flex-column p-20">
        <div class="row g-3">
            <div class="col-sm-12">
                <div class="">
                    <label for="examNmEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Exam Name</label>
                    <input type="text" class="form-control" id="examNmEdit" placeholder="Enter Exam name" :value="examData?.name">
                </div>
            </div>
             <div class="col-sm-6">
                <div class="">
                    <label for="examDateEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Exam Date</label>
                    <input type="date" class="form-control" id="examDateEdit" :value="formatDateForInput(examData?.date)">
                </div>
            </div>
             <div class="col-sm-6">
                <div class="">
                    <label for="startTimeEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Start Time</label>
                    <input type="time" class="form-control" id="startTimeEdit" :value="convertTo24Hour(examData?.startTime)">
                </div>
            </div>
             <div class="col-sm-6">
                <div class="">
                    <label for="endTimeEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">End Time</label>
                    <input type="time" class="form-control" id="endTimeEdit" :value="convertTo24Hour(examData?.endTime)">
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="examStatusEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                    <select id="examStatusEdit" class="form-control form-select" :value="examData?.status">
                        <option value="" disabled>Select Status</option>
                        <option value="Active">Active</option>
                         <option value="Pending">Pending</option>
                         <option value="Scheduled">Scheduled</option>
                         <option value="Closed">Closed</option>
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
    name: "EditExamSidebar",
    props: {
        isOpen: Boolean,
        examData: Object
    },
    emits: ['close'],
    setup() {
        // Helper date, time formats not implemented robustly here as we are mocking data
         const formatDateForInput = (dateStr) => {
            if (!dateStr) return '';
             // Assumes dateStr is like "05 Jun 2015" - basic parsing attempt or placeholder
            const date = new Date(dateStr);
            if(isNaN(date)) return '';
            
            return date.toISOString().split('T')[0];
        };

        const convertTo24Hour = (timeStr) => {
            if (!timeStr) return '';
            const [time, modifier] = timeStr.split(' ');
            let [hours, minutes] = time.split(':');
            if (hours === '12') {
                hours = '00';
            }
            if (modifier === 'PM') {
                hours = parseInt(hours, 10) + 12;
            }
            return `${hours}:${minutes}`;
        };

        return {
            formatDateForInput,
            convertTo24Hour
        }
    }
}
</script>
