<template>
  <div class="card radius-12 bg-base h-100 overflow-hidden shadow-1">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Medical Details</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="bloodGroup" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Blood
              Group</label>
            <select id="bloodGroup" class="form-control form-select">
              <option value="Select blood group" disabled>Select blood group</option>
              <option value="A+">A+</option>
              <option value="AB+">AB+</option>
              <option value="A-">A-</option>
              <option value="AB-">AB-</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="medicalHeight" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Height
            </label>
            <input type="text" class="form-control" id="medicalHeight" placeholder="Enter height">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="medicalWeight" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Weight
            </label>
            <input type="text" class="form-control" id="medicalWeight" placeholder="Enter Weight">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MedicalDetails"
}
</script>
