<template>
  <div class="card h-100">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Personal Info</h6>
    </div>
    <div class="card-body p-20">
      <div class="row gy-3">
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="teacherID" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Teacher
              ID* <span class="text-danger-600">* </span> </label>
            <input type="text" class="form-control" id="teacherID" placeholder="Enter Teacher ID">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="fullName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Full Name
              <span class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="fullName" placeholder="Enter your Full Name">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="teacherSubject" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Subject
            </label>
            <select id="teacherSubject" class="form-control form-select">
              <option value="Select a Subject" disabled selected>Select a Subject</option>
              <option value="English">English</option>
              <option value="Mathematics">Mathematics</option>
              <option value="Physics">Physics</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="teacherClasses" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Classes
            </label>
            <select id="teacherClasses" class="form-control form-select">
              <option value="Select a Class" disabled selected>Select a Class</option>
              <option value="1 (A)">1 (A)</option>
              <option value="2 (A)">2 (A)</option>
              <option value="3 (A)">3 (A)</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="gender" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Gender</label>
            <select id="gender" class="form-control form-select">
              <option value="Select section" disabled selected>Select Gender</option>
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="dateOfBirth" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Date Of
              Birth <span class="text-danger-600">*</span> </label>
            <input type="date" class="form-control" id="dateOfBirth">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="fathersName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Fathers
              Name </label>
            <input type="text" class="form-control" id="fathersName" placeholder="Enter Fathers Name">
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
            <label for="meritalStatus" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Merital
              Status</label>
            <select id="meritalStatus" class="form-control form-select">
              <option value="Select a Merital Status" disabled selected>Select a Merital Status
              </option>
              <option value="Married">Married</option>
              <option value="Unmarried">Unmarried</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="contractType" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Contract
              Type</label>
            <select id="contractType" class="form-control form-select">
              <option value="Select a Contract Type" disabled selected>Select a Contract Type
              </option>
              <option value="Contractual">Contractual</option>
              <option value="Hourly">Hourly</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="teacherShift" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Shift</label>
            <select id="teacherShift" class="form-control form-select">
              <option value="Select a shift" disabled selected>Select a shift</option>
              <option value="Day Shift">Day Shift</option>
              <option value="Night Shift">Night Shift</option>
            </select>
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="workLocation" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Work
              Location </label>
            <input type="text" class="form-control" id="workLocation" placeholder="Enter work location">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="joinDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Join
              Date</label>
            <input type="date" class="form-control" id="joinDate">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="phoneNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Phone
              Number <span class="text-danger-600">*</span> </label>
            <input type="tel" class="form-control" id="phoneNumber" placeholder="Enter your Phone Number">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="teacherEmails" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Email
              <span class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="teacherEmails" placeholder="Enter your Email">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="wordExperience" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Experience
              <span class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="wordExperience" placeholder="Enter experience">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label for="wordQualification" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Qualification
              <span class="text-danger-600">*</span> </label>
            <input type="text" class="form-control" id="wordQualification" placeholder="Enter Qualification">
          </div>
        </div>
        <div class="col-xxl-3 col-xl-4 col-sm-6">
          <div class="">
            <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Teacher
              Photo <span class="text-danger-600">*</span> </label>
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
  name: "PersonalInfo"
}
</script>
