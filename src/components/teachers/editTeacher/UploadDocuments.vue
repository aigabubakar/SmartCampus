<template>
  <div class="card h-100">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Upload Documents</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-sm-6">
          <div class="">
            <label for="docName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Doc Name
            </label>
            <input type="text" class="form-control" id="docName" placeholder="Enter Doc Name">
          </div>
        </div>
        <div class="col-sm-6">
          <div class="">
            <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Upload File</label>
            <div
              class="drop-zone height-44-px p-4 d-flex justify-content-center align-items-center text-center fw-medium text-md cursor-pointer border border-neutral-400 radius-8 border-dashed bg-hover-neutral-200">
              <span class="drop-zone__prompt">Drag & drop a file here or click</span>
              <input type="file" name="myFile" class="drop-zone__input">
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UploadDocuments"
}
</script>
