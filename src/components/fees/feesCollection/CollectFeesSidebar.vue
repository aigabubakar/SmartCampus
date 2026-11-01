<template>
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 duration-300" :class="{ 'active-translate-0': isOpen, 'translate-x-full': !isOpen }">
        <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
            <h5 class="text-lg mb-0">Collect Fees</h5>
            <button type="button" class="close-my-sidebar text-danger-600 text-lg d-flex" @click="$emit('close')">
                <i class="ri-close-large-line"></i>
            </button>
        </div>
        <form action="#" class="d-flex flex-column p-20">
            <div class="row g-3">
                <div class="col-sm-6">
                    <div class="">
                        <label for="className" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class
                        </label>
                        <select class="form-control form-select" id="className">
                            <option value="Select a class" selected disabled>Select a class</option>
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
                        <label for="section" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section
                        </label>
                        <select class="form-control form-select" id="section">
                            <option value="Select a class" selected disabled>Select a Section</option>
                            <option value="A">A</option>
                            <option value="B">B</option>
                            <option value="C">C</option>
                            <option value="D">D</option>
                        </select>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="">
                        <label for="rollNo" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Roll No
                        </label>
                        <input type="text" class="form-control" id="rollNo" placeholder="Enter roll no.">
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="">
                        <label for="collectDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Date
                        </label>
                        <input type="date" class="form-control" id="collectDate">
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="">
                        <div class="d-flex align-items-center justify-content-between gap-4">
                            <label for="collectAmount" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Amount
                            </label>
                            <span class="text-sm fw-semibold text-warning-600">Due: 2000</span>
                        </div>
                        <input type="text" class="form-control" id="collectAmount" placeholder="$1500">
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class="">
                        <label for="colDiscount" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Discount
                        </label>
                        <select class="form-control form-select" id="colDiscount">
                            <option value="Select a class" selected disabled>Select a Discount</option>
                            <option value="10%">10%</option>
                            <option value="20%">20%</option>
                            <option value="30%">30%</option>
                            <option value="50%">50%</option>
                        </select>
                    </div>
                </div>
                <div class="col-sm-12">
                    <div class="">
                        <label for="paymentType" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Payment Type
                        </label>
                        <select class="form-control form-select" id="paymentType">
                            <option value="Cash" selected>Cash</option>
                            <option value="bKash">bKash</option>
                            <option value="Bank">Bank</option>
                        </select>
                    </div>
                </div>
                <div class="col-sm-12">
                    <div class="">
                        <label for="noteType" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Note
                        </label>
                        <textarea class="form-control" id="noteType" placeholder="Enter note..."></textarea>
                    </div>
                </div>
                <div class="col-12">
                    <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
                        <button type="button" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="$emit('close')">
                            Cancel
                        </button>
                        <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "CollectFeesSidebar",
    props: {
        isOpen: {
            type: Boolean,
            default: false
        }
    },
    emits: ['close']
}
</script>
