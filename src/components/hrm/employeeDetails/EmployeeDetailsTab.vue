<template>
  <div class="row gy-4">
    <!-- Profile Detail -->
    <div class="col-md-12">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Profile Detail</h6>
        </div>
        <div class="card-body p-0">
          <div class="p-20">
            <div class="row gy-4">
              <div class="col-md-3 col-sm-6">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Date of Birth</h6>
                  <span class="">{{ details.dateOfBirth }}</span>
                </div>
              </div>
              <div class="col-md-3 col-sm-6">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Martial Status</h6>
                  <span class="">{{ details.maritalStatus }}</span>
                </div>
              </div>
              <div class="col-md-3 col-sm-6">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Qualification</h6>
                  <span class="">{{ details.qualification }}</span>
                </div>
              </div>
              <div class="col-md-3 col-sm-6">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Experience</h6>
                  <span class="">{{ details.experience }}</span>
                </div>
              </div>
              <div class="col-md-3 col-sm-6">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Father Name</h6>
                  <span class="">{{ details.fatherName }}</span>
                </div>
              </div>
              <div class="col-md-3 col-sm-6">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Mother Name</h6>
                  <span class="">{{ details.motherName }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Previous School Details -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Previous School Details</h6>
        </div>
        <div class="card-body p-0">
          <div class="p-20">
            <div class="row gy-4">
              <div class="col-sm-12">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Previous School Name</h6>
                  <span class="">{{ details.previousSchool }}</span>
                </div>
              </div>
              <div class="col-sm-12">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Current School Name</h6>
                  <span class="">{{ details.currentSchool }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Address -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Address</h6>
        </div>
        <div class="card-body p-0">
          <div class="p-20">
            <div class="row gy-4">
              <div class="col-sm-12">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Current Address</h6>
                  <span class="">{{ details.currentAddress }}</span>
                </div>
              </div>
              <div class="col-sm-12">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Permanent Address</h6>
                  <span class="">{{ details.permanentAddress }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bank Details -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Bank Details</h6>
        </div>
        <div class="card-body p-0">
          <div class="p-20">
            <div class="row gy-4">
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Bank Name</h6>
                  <span class="">{{ details.bankName }}</span>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Branch</h6>
                  <span class="">{{ details.branch }}</span>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">IFSC Code</h6>
                  <span class="">{{ details.ifscCode }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Medical Details -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Medical Details</h6>
        </div>
        <div class="card-body p-0">
          <div class="p-20">
            <div class="row gy-4">
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Blood Group</h6>
                  <span class="">{{ details.bloodGroup }}</span>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Height</h6>
                  <span class="">{{ details.height }}</span>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Weight</h6>
                  <span class="">{{ details.weight }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Documents -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Documents</h6>
        </div>
        <div class="card-body p-20">
          <div class="p-10 border radius-8" v-for="doc in details.documents" :key="doc.name">
            <div class="d-flex align-items-center justify-content-between gap-20 mb-12">
              <div class="d-flex align-items-center gap-12">
                <span class="w-36-px h-36-px radius-4 bg-neutral-50 d-flex justify-content-center align-items-center text-xl">
                  <i class="ri-file-text-line"></i>
                </span>
                <span class="text-md text-secondary-light">{{ doc.name }}</span>
              </div>
              <button type="button"
                class="w-36-px h-36-px radius-4 bg-primary-50 bg-hover-primary-100 text-primary-600 d-flex justify-content-center align-items-center text-xl">
                <i class="ri-download-2-line"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Social Media -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Social Media</h6>
        </div>
        <div class="card-body p-0">
          <div class="p-20">
            <div class="row gy-4">
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Facebook</h6>
                  <span class="">{{ details.facebook }}</span>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">LinkedIn</h6>
                  <span class="">{{ details.linkedin }}</span>
                </div>
              </div>
              <div class="col-sm-4">
                <div class="">
                  <h6 class="text-md mb-2 fw-medium flex-grow-1">Instagram</h6>
                  <span class="">{{ details.instagram }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EmployeeDetailsTab",
  props: {
    details: {
      type: Object,
      required: true
    }
  }
}
</script>
