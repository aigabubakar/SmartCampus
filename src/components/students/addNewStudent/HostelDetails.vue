<template>
  <div class="card radius-12 bg-base h-100 overflow-hidden shadow-1">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Hostel Details</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-sm-6">
          <div class="">
            <label for="hostel" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Hostel
            </label>
            <input type="text" class="form-control" id="hostel" placeholder="Enter Hostel">
          </div>
        </div>
        <div class="col-sm-6">
          <div class="">
            <label for="roomNo" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Room No
            </label>
            <input type="text" class="form-control" id="roomNo" placeholder="Enter Room No">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HostelDetails"
}
</script>
