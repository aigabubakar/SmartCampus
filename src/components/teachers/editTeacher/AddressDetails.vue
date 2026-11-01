<template>
  <div class="card h-100">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Address</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-sm-6">
          <div class="">
            <label for="currentAddress" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Current
              Address </label>
            <input type="text" class="form-control" id="currentAddress" placeholder="Enter Current Address">
          </div>
        </div>
        <div class="col-sm-6">
          <div class="">
            <label for="permanentAddress" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Permanent
              Address </label>
            <input type="text" class="form-control" id="permanentAddress" placeholder="Enter Permanent Address">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddressDetails"
}
</script>
