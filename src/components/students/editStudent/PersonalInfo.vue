<template>
  <div class="card h-100">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Personal Info</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="academicYear" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Academic Year
              <span class="text-danger-600">* </span> </label>
            <select id="academicYear" class="form-control form-select">
              <option value="Jun 2025/2026">Jun 2025/2026</option>
              <option value="Jun 2026/2027">Jun 2026/2027</option>
              <option value="Jun 2027/2028">Jun 2027/2028</option>
              <option value="Jun 2028/2029">Jun 2028/2029</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="classSelection" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class <span
                class="text-danger-600">* </span> </label>
            <select id="classSelection" class="form-control form-select">
              <option value="Select a class" disabled>Select a class</option>
              <option value="Primary">Primary</option>
              <option value="High school">High school</option>
              <option value="College">College</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="section" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section <span
                class="text-danger-600">* </span> </label>
            <select id="section" class="form-control form-select">
              <option value="Select section" disabled>Select section</option>
              <option value="Science">Science</option>
              <option value="Art">Art</option>
              <option value="Commerce">Commerce</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="rollNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Roll Number
            </label>
            <input type="text" class="form-control" id="rollNumber" placeholder="Enter your rollNumber">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="admissionNo" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Admission No
              <span class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="admissionNo" placeholder="Enter admission number">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="fullName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Full Name <span
                class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="fullName" placeholder="Enter your Full Name">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="category" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Category <span
                class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="category" placeholder="Select a Category">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="gender" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Gender</label>
            <select id="gender" class="form-control form-select">
              <option value="Select section" disabled>Select Gender</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="dateOfBirth" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Date Of Birth
              <span class="text-danger-600">*</span> </label>
            <input type="date" class="form-control" id="dateOfBirth">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="phoneNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Phone Number
              <span class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="phoneNumber" placeholder="Enter your Phone Number">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="studentEmail" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Email <span
                class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="studentEmail" placeholder="Enter your Email">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Student Photo <span
                class="text-danger-600">*</span> </label>
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
  name: "PersonalInfo"
}
</script>
