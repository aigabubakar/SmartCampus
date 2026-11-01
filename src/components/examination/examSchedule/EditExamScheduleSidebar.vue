<template>
<div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isOpen, 'active-translate-0': isOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Exam Schedule</h5>
        <button type="button" @click="$emit('close')" class="close-edit-sidebar text-danger-600 text-lg d-flex">
            <i class="ri-close-large-line"></i>
        </button>
    </div>
    <form action="#" class="d-flex flex-column p-20">
        <div class="row g-3">
             <div class="col-sm-6">
                <div class="">
                    <label for="examNmEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Exam Name</label>
                    <select class="form-control form-select" id="examNmEdit">
                        <option value="" disabled>Select Exam</option>
                        <option value="Monthly Test">Monthly Test</option>
                        <option value="Mid Term">Mid Term</option>
                         <option value="Final Term">Final Term</option>
                    </select>
                </div>
            </div>
             <div class="col-sm-6">
                <div class="">
                    <label for="classSelectEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
                    <select class="form-control form-select" id="classSelectEdit">
                        <option value="" disabled>Select Class</option>
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
                    <label for="sectionEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section</label>
                    <select class="form-control form-select" id="sectionEdit">
                        <option value="" disabled>Select Section</option>
                        <option value="A">A</option>
                        <option value="B">B</option>
                        <option value="C">C</option>
                        <option value="D">D</option>
                    </select>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="examRoomEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Room</label>
                    <select class="form-control form-select" id="examRoomEdit" :value="scheduleData?.room">
                         <option value="" disabled>Select Room</option>
                        <option value="101">101</option>
                        <option value="102">102</option>
                        <option value="103">103</option>
                         <option value="104">104</option>
                        <option value="105">105</option>
                        <option value="106">106</option>
                         <option value="107">107</option>
                        <option value="108">108</option>
                        <option value="109">109</option>
                         <option value="110">110</option>
                    </select>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="selectsubjectEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Subject</label>
                    <select class="form-control form-select" id="selectsubjectEdit" :value="scheduleData?.subject">
                        <option value="" disabled>Select Subject</option>
                        <option value="English">English</option>
                        <option value="Bangla">Bangla</option>
                        <option value="Math">Math</option>
                        <option value="Mathematics">Mathematics</option>
                         <option value="Science">Science</option>
                        <option value="History">History</option>
                        <option value="Geography">Geography</option>
                         <option value="Computer">Computer</option>
                        <option value="Physics">Physics</option>
                        <option value="Chemistry">Chemistry</option>
                         <option value="Biology">Biology</option>
                    </select>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="examDateEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Exam Date</label>
                    <input type="date" class="form-control" id="examDateEdit" :value="formatDateForInput(scheduleData?.date)">
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="startTimeEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Start Time</label>
                    <input type="time" class="form-control" id="startTimeEdit" :value="convertTo24Hour(scheduleData?.startTime)">
                </div>
            </div>
            <div class="col-sm-6">
                <div class="">
                    <label for="endTimeEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">End Time</label>
                    <input type="time" class="form-control" id="endTimeEdit" :value="convertTo24Hour(scheduleData?.endTime)">
                </div>
            </div>
             <div class="col-sm-6">
                <div class="">
                    <label for="durationEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Duration</label>
                    <input type="text" class="form-control" id="durationEdit" placeholder="e.g. 3 Hours" :value="scheduleData?.duration">
                </div>
            </div>
            <div class="col-12">
                <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
                    <button type="button" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="$emit('close')">Cancel</button>
                    <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">Update</button>
                </div>
            </div>
        </div>
    </form>
</div>
</template>
<script>
export default {
    name: "EditExamScheduleSidebar",
    props: {
        isOpen: Boolean,
        scheduleData: Object
    },
    emits: ['close'],
    setup() {
         const formatDateForInput = (dateStr) => {
            if (!dateStr) return '';
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
