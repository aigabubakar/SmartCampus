<template>
  <div class="modal fade" id="payslipModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-sm modal-dialog modal-dialog-centered max-w-600-px">
      <div class="modal-content radius-16 bg-base">
        <div class="modal-body p-24">
          <div class="text-center">
            <h6 class="mb-0">{{ schoolName }}</h6>
            <p class="text-secondary-light">{{ schoolAddress }}</p>
          </div>
          
          <div class="d-flex align-items-center justify-content-between gap-20 flex-wrap mt-24">
            <div class="d-flex flex-column">
              <div class="text-sm fw-medium d-flex">
                <span class="text-primary-light w-110-px text-start">Invoice No</span>
                <span class="text-primary-light">: {{ invoiceNo }}</span>
              </div>
              <div class="text-sm fw-medium d-flex">
                <span class="text-primary-light w-110-px text-start">Employee Name</span>
                <span class="text-primary-light">: {{ employeeName }}</span>
              </div>
              <div class="text-sm fw-medium d-flex">
                <span class="text-primary-light w-110-px text-start">Phone</span>
                <span class="text-primary-light">: {{ phone }}</span>
              </div>
            </div>
            <div class="d-flex flex-column">
              <div class="text-sm fw-medium d-flex">
                <span class="text-primary-light text-start">Payslip</span>
              </div>
              <div class="text-sm fw-medium d-flex">
                <span class="text-secondary-light text-start">Month: {{ month }}</span>
              </div>
              <div class="text-sm fw-medium d-flex">
                <span class="text-secondary-light text-start">Payment: {{ paymentDate }}</span>
              </div>
            </div>
          </div>

          <ul class="border mt-24 radius-8 overflow-hidden">
            <li class="py-10 px-20 d-flex align-items-center justify-content-between gap-20 bg-neutral-50 border-bottom">
              <span class="text-primary-light fw-semibold">Name</span>
              <span class="text-primary-light fw-semibold">Amount</span>
            </li>
            <li class="py-10 px-20 d-flex align-items-center justify-content-between gap-20 border-bottom">
              <span class="text-primary-light">Base Salary</span>
              <span class="text-primary-light">${{ baseSalary.toLocaleString() }}</span>
            </li>
            <li class="py-10 px-20 d-flex align-items-center justify-content-between gap-20 border-bottom">
              <span class="text-primary-light">Overtime Pay</span>
              <span class="text-primary-light">${{ overtimePay.toLocaleString() }}</span>
            </li>
            <li class="py-10 px-20 d-flex align-items-center justify-content-between gap-20 border-bottom">
              <span class="text-primary-light">Bonuses</span>
              <span class="text-primary-light">${{ bonuses.toLocaleString() }}</span>
            </li>
            <li class="py-10 px-20 d-flex align-items-center justify-content-between gap-20 border-bottom">
              <span class="text-primary-light">Gross Salary</span>
              <span class="text-primary-light">${{ grossSalary.toLocaleString() }}</span>
            </li>
            <li class="py-10 px-20 d-flex align-items-center justify-content-between gap-20 bg-neutral-50">
              <span class="text-primary-light fw-semibold text-lg">Total</span>
              <span class="text-primary-light fw-semibold text-lg">${{ total.toLocaleString() }}</span>
            </li>
          </ul>

          <div class="pt-28 ms-16 text-start">
            <p class="text-primary-light fw-medium mb-0">Payment type: {{ paymentType }}</p>
          </div>

          <div class="text-center mt-100-px">
            <h6 class="text-xl mb-4">Thanks</h6>
            <p class="text-secondary-light text-sm mb-0">
              If you need further assistance, please feel free to contact HR at 
              <span class="fw-semibold text-primary-light">{{ schoolName }}</span>
            </p>
          </div>

          <div class="text-center mt-100-px">
            <p class="text-secondary-light text-sm mb-0">
              Powered by <a href="https://stackhubs.com.ng" target="_blank" rel="noopener noreferrer" class="fw-semibold text-primary-600 text-decoration-none">stackhubs.com.ng</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';

export default {
  name: "PayslipModal",
  props: {
    employee: {
      type: Object,
      default: () => ({})
    }
  },
  setup(props) {
    const schoolName = 'School Name';
    const schoolAddress = 'Smithbroand, Unit 4, Holler Tower, San Diego';
    const invoiceNo = '#5695';
    const phone = '+112515474';
    const month = 'January 2025';
    const paymentDate = '15 Jan 2025';
    
    // Computed properties to handle potential null/undefined employee
    const employeeName = computed(() => props.employee?.name || 'Jon Dan');
    const paymentType = computed(() => props.employee?.paymentMethod || 'Bank');
    
    // Fallback salary values or calculations based on netSalary if available
    const baseSalary = computed(() => props.employee?.netSalary ? Math.floor(props.employee.netSalary * 0.4) : 2000);
    const overtimePay = computed(() => props.employee?.netSalary ? Math.floor(props.employee.netSalary * 0.2) : 1000);
    const bonuses = computed(() => props.employee?.netSalary ? Math.floor(props.employee.netSalary * 0.4) : 2000);
    const grossSalary = computed(() => baseSalary.value + overtimePay.value + bonuses.value);
    const total = computed(() => grossSalary.value);

    return {
      schoolName,
      schoolAddress,
      invoiceNo,
      employeeName,
      phone,
      month,
      paymentDate,
      baseSalary,
      overtimePay,
      bonuses,
      grossSalary,
      total,
      paymentType
    };
  }
}
</script>
