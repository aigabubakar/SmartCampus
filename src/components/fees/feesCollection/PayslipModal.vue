<template>
    <div class="modal fade" id="payslipModal" tabindex="-1" aria-hidden="true">
       <div class="modal-dialog modal-sm modal-dialog modal-dialog-centered max-w-600-px">
           <div class="modal-content radius-16 bg-base">
               <div class="modal-body p-24">
                   <div class="text-center">
                       <h6 class="mb-0">School Name</h6>            
                       <p class="text-secondary-light">Smithbroand, Unit 4, Holler Tower, San Diego</p>
                   </div>
                   <div class="d-flex align-items-center justify-content-between gap-20 flex-wrap mt-24 ">
                       <div class="d-flex flex-column">
                           <div class="text-sm fw-medium d-flex">
                               <span class="text-primary-light w-110-px text-start">Student Name</span>
                               <span class="text-primary-light">: {{ details?.name }}</span>
                           </div>
                           <div class="text-sm fw-medium d-flex">
                               <span class="text-primary-light w-110-px text-start">Class</span>
                               <span class="text-primary-light">: {{ details?.class }}</span>
                           </div>
                           <div class="text-sm fw-medium d-flex">
                               <span class="text-primary-light w-110-px text-start">Roll No.</span>
                               <span class="text-primary-light">: {{ details?.rollNo }}</span>
                           </div>
                       </div>
                       <div class="d-flex flex-column">
                           <div class="text-sm fw-medium d-flex">
                               <span class="text-primary-light text-start">Date: {{ details?.date }}</span>
                           </div>
                           <div class="text-sm fw-medium d-flex">
                               <span class="text-primary-light text-start">Collected By: Admin</span>
                           </div>
                           <div class="text-sm fw-medium d-flex">
                               <span class="text-primary-light text-start">Payment By: Cash</span>
                           </div>
                       </div>
                   </div>
                   <ul class="border mt-24 radius-8 overflow-hidden">
                       <li class="py-10 px-20 d-flex align-items-center justify-content-between gap-20 bg-neutral-50 border-bottom">
                           <span class="text-primary-light fw-semibold">Amount</span>
                           <span class="text-primary-light fw-semibold">Paid</span>
                           <span class="text-primary-light fw-semibold">Balance</span>
                       </li>
                       <li class="py-10 px-20 d-flex align-items-center justify-content-between gap-20 ">
                           <span class="text-primary-light">${{ details?.amount }}</span>
                           <span class="text-primary-light">${{ details?.paid }}</span>
                           <span class="text-primary-light">${{ details?.due }}</span>
                       </li>
                   </ul>
                   <div class="text-center mt-100-px">
                       <h6 class="text-xl mb-4">Thanks</h6>
                       <p class="text-secondary-light text-sm mb-0">This receipt is computer generated hence on signature is required</p>
                   </div>
                   <div class="text-center mt-100-px">
                       <p class="text-secondary-light text-sm mb-0">Powered by <a href="https://stackhubs.com.ng" target="_blank" rel="noopener noreferrer" class="fw-semibold text-primary-600 text-decoration-none">stackhubs.com.ng</a></p>
                   </div>
               </div>
           </div>
       </div>
   </div>
</template>

<script>
export default {
    name: "PayslipModal",
    props: {
        details: {
            type: Object,
            default: () => ({})
        }
    }
}
</script>
