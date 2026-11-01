<template>
  <div class="card radius-12 bg-base h-100 overflow-hidden shadow-1">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Parent & Guardian Info </h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="fathersName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Fathers
              Name </label>
            <input type="text" class="form-control" id="fathersName" placeholder="Enter Fathers Name">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="fathersPhoneNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Phone
              Number </label>
            <input type="tel" class="form-control" id="fathersPhoneNumber" placeholder="Enter Fathers Number">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="fathersFatherOccupation"
              class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Father
              Occupation </label>
            <input type="text" class="form-control" id="fathersFatherOccupation" placeholder="Enter Father Occupation">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Fathers
              Photo <span class="text-danger-600">*</span> </label>
            <div
              class="drop-zone height-44-px p-4 d-flex justify-content-center align-items-center text-center fw-medium text-md cursor-pointer border border-neutral-400 radius-8 border-dashed bg-hover-neutral-200">
              <span class="drop-zone__prompt">Darg & drop a file here or click</span>
              <input type="file" name="myFile" class="drop-zone__input">
            </div>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="mothersName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Mothers
              Name </label>
            <input type="text" class="form-control" id="mothersName" placeholder="Enter mothers Name">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="mothersPhoneNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Phone
              Number </label>
            <input type="tel" class="form-control" id="mothersPhoneNumber" placeholder="Enter mothers Number">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="mothersFatherOccupation"
              class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Father
              Occupation </label>
            <input type="text" class="form-control" id="mothersFatherOccupation" placeholder="Enter Father Occupation">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Mothers
              Photo <span class="text-danger-600">*</span> </label>
            <div
              class="drop-zone height-44-px p-4 d-flex justify-content-center align-items-center text-center fw-medium text-md cursor-pointer border border-neutral-400 radius-8 border-dashed bg-hover-neutral-200">
              <span class="drop-zone__prompt">Darg & drop a file here or click</span>
              <input type="file" name="myFile" class="drop-zone__input">
            </div>
          </div>
        </div>
        <div class="col-12">
          <div class="mt-24">
            <span class="text-lg fw-bold text-primary-light d-inline-block mb-8">Select a
              Guardian </span>
            <div class="d-flex align-items-center flex-wrap gap-28">
              <div class="form-check checked-primary d-flex align-items-center gap-2">
                <input class="form-check-input" type="radio" name="radio" id="selectFather">
                <label class="form-check-label line-height-1 fw-medium text-secondary-light" for="selectFather"> Father
                </label>
              </div>
              <div class="form-check checked-secondary d-flex align-items-center gap-2">
                <input class="form-check-input" type="radio" name="radio" id="selectMother">
                <label class="form-check-label line-height-1 fw-medium text-secondary-light" for="selectMother"> Mother
                </label>
              </div>
              <div class="form-check checked-success d-flex align-items-center gap-2">
                <input class="form-check-input" type="radio" name="radio" id="selectOthers">
                <label class="form-check-label line-height-1 fw-medium text-secondary-light" for="selectOthers"> Others
                </label>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="guardianName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Guardian
              Name </label>
            <input type="text" class="form-control" id="guardianName" placeholder="Enter Guardian Name">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="guardianEmailTwo" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Guardian
              Email </label>
            <input type="email" class="form-control" id="guardianEmailTwo" placeholder="Enter Guardian Email">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="guardianPhoneNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Phone
              Number </label>
            <input type="tel" class="form-control" id="guardianPhoneNumber" placeholder="Enter Guardian Number">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="guardianFatherOccupation"
              class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Father
              Occupation </label>
            <input type="text" class="form-control" id="guardianFatherOccupation" placeholder="Enter Father Occupation">
          </div>
        </div>
        <div class="col-xl-9 col-sm-6">
          <div class="">
            <label for="guardianGuardianAddress"
              class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Guardian
              Address </label>
            <input type="text" class="form-control" id="guardianGuardianAddress" placeholder="Enter Guardian Address">
          </div>
        </div>
        <div class="col-xl-3 col-sm-6">
          <div class="">
            <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Guardian
              Photo <span class="text-danger-600">*</span> </label>
            <div
              class="drop-zone height-44-px p-4 d-flex justify-content-center align-items-center text-center fw-medium text-md cursor-pointer border border-neutral-400 radius-8 border-dashed bg-hover-neutral-200">
              <span class="drop-zone__prompt">Darg & drop a file here or click</span>
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
  name: "ParentGuardianInfo"
}
</script>
