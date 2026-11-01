<template>
  <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active-translate-0': isOpen }">
    <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
      <h5 class="text-lg mb-0">Add Payment</h5>
      <button type="button" class="close-my-sidebar text-danger-600 text-lg d-flex" @click="$emit('close')">
        <i class="ri-close-large-line"></i>
      </button>
    </div>
    
    <form @submit.prevent="handleSubmit" class="d-flex flex-column p-20">
      <div class="row g-3">
        <div class="col-sm-6">
          <div class="">
            <label for="employeeName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
              Employee Name
            </label>
            <input type="text" class="form-control" id="employeeName" v-model="formData.employeeName" placeholder="Enter Employee Name">
          </div>
        </div>
        
        <div class="col-sm-6">
          <div class="">
            <label for="paymentAmount" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
              Payment Amount ($)
            </label>
            <input type="text" class="form-control" id="paymentAmount" v-model="formData.paymentAmount" placeholder="Enter Payment Amount ($)">
          </div>
        </div>
        
        <div class="col-sm-6">
          <div class="">
            <label for="month" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
              Month
            </label>
            <select id="month" class="form-control form-select" v-model="formData.month">
              <option value="" disabled>Select Month</option>
              <option value="January 2026">January 2026</option>
              <option value="February 2026">February 2026</option>
              <option value="March 2026">March 2026</option>
              <option value="April 2026">April 2026</option>
              <option value="May 2026">May 2026</option>
              <option value="June 2026">June 2026</option>
              <option value="July 2026">July 2026</option>
              <option value="August 2026">August 2026</option>
              <option value="September 2026">September 2026</option>
              <option value="October 2026">October 2026</option>
              <option value="November 2026">November 2026</option>
              <option value="December 2026">December 2026</option>
            </select>
          </div>
        </div>
        
        <div class="col-sm-6">
          <div class="">
            <label for="paymentType" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
              Payment Type
            </label>
            <select id="paymentType" class="form-control form-select" v-model="formData.paymentType">
              <option value="" disabled>Select Payment Type</option>
              <option value="Cash">Cash</option>
              <option value="Bank">Bank</option>
              <option value="Card">Card</option>
              <option value="Cheque">Cheque</option>
            </select>
          </div>
        </div>
        
        <div class="col-sm-12">
          <div class="">
            <label for="paymentDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
              Date
            </label>
            <input type="date" class="form-control" id="paymentDate" v-model="formData.paymentDate">
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
              Save
            </button>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: "PaymentSidebar",
  props: {
    isOpen: {
      type: Boolean,
      default: false
    }
  },
  emits: ['close', 'submit'],
  setup(props, { emit }) {
    const formData = ref({
      employeeName: '',
      paymentAmount: '',
      month: '',
      paymentType: '',
      paymentDate: '',
      description: ''
    });

    const handleSubmit = () => {
      emit('submit', formData.value);
      resetForm();
      emit('close');
    };

    const handleCancel = () => {
      resetForm();
      emit('close');
    };

    const resetForm = () => {
      formData.value = {
        employeeName: '',
        paymentAmount: '',
        month: '',
        paymentType: '',
        paymentDate: '',
        description: ''
      };
    };

    return {
      formData,
      handleSubmit,
      handleCancel
    };
  }
}
</script>
