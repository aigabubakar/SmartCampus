<template>
  <div class="card h-100">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Student Details</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-sm-12">
          <div class="">
            <label for="moreDetails" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Details
            </label>
            <textarea id="moreDetails" class="form-control" placeholder="Enter details"></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentDetails"
}
</script>
