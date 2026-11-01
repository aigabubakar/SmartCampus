<template>
  <div class="card h-100">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Bank Details</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="bankAccountNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Bank
              Account Number </label>
            <input type="text" class="form-control" id="bankAccountNumber" placeholder="Enter Bank Account Number">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="bankName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Bank Name
            </label>
            <input type="text" class="form-control" id="bankName" placeholder="Enter Bank Name">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="iFSCCode" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">IFSC Code
            </label>
            <input type="text" class="form-control" id="iFSCCode" placeholder="Enter IFSC Code">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="nationalIdentificationNumber"
              class="text-sm fw-semibold text-primary-light d-inline-block mb-8">National
              Identification Number</label>
            <input type="text" class="form-control" id="nationalIdentificationNumber"
              placeholder="Enter National Identification Number">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    name: "BankDetails"
}
</script>
