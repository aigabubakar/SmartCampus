<template>
  <form @submit.prevent="handleSubmit" class="mt-24">
          <div class="row gy-3">
            <!-- Personal Info -->
            <div class="col-lg-12">
              <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                  <h6 class="text-lg fw-semibold mb-0">Personal Info</h6>
                </div>
                <div class="card-body p-20">
                  <div class="row gy-3">
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="employeeID" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                        Employee ID <span class="text-danger-600">*</span>
                      </label>
                      <input type="text" class="form-control" id="employeeID" v-model="formData.employeeID" placeholder="Enter Employee ID" required>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="fullName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                        Full Name <span class="text-danger-600">*</span>
                      </label>
                      <input type="text" class="form-control" id="fullName" v-model="formData.fullName" placeholder="Enter your Full Name" required>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="employeeDepartment" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Department</label>
                      <select id="employeeDepartment" class="form-control form-select" v-model="formData.department">
                        <option value="">Select a Department</option>
                        <option value="English">English</option>
                        <option value="Mathematics">Mathematics</option>
                        <option value="Physics">Physics</option>
                      </select>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="employeeDesignation" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Designation</label>
                      <select id="employeeDesignation" class="form-control form-select" v-model="formData.designation">
                        <option value="">Select a Designation</option>
                        <option value="Team Lead">Team Lead</option>
                        <option value="Software Engineer">Software Engineer</option>
                        <option value="Frontend Developer">Frontend Developer</option>
                        <option value="Backend Developer">Backend Developer</option>
                        <option value="Full Stack Developer">Full Stack Developer</option>
                      </select>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="gender" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Gender</label>
                      <select id="gender" class="form-control form-select" v-model="formData.gender">
                        <option value="">Select Gender</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                      </select>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="dateOfBirth" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                        Date Of Birth <span class="text-danger-600">*</span>
                      </label>
                      <input type="date" class="form-control" id="dateOfBirth" v-model="formData.dateOfBirth" required>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="fathersName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Fathers Name</label>
                      <input type="text" class="form-control" id="fathersName" v-model="formData.fathersName" placeholder="Enter Fathers Name">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="mothersName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Mothers Name</label>
                      <input type="text" class="form-control" id="mothersName" v-model="formData.mothersName" placeholder="Enter mothers Name">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="maritalStatus" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Marital Status</label>
                      <select id="maritalStatus" class="form-control form-select" v-model="formData.maritalStatus">
                        <option value="">Select a Marital Status</option>
                        <option value="Married">Married</option>
                        <option value="Unmarried">Unmarried</option>
                      </select>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="contractType" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Contract Type</label>
                      <select id="contractType" class="form-control form-select" v-model="formData.contractType">
                        <option value="">Select a Contract Type</option>
                        <option value="Contractual">Contractual</option>
                        <option value="Hourly">Hourly</option>
                      </select>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="employeeShift" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Shift</label>
                      <select id="employeeShift" class="form-control form-select" v-model="formData.shift">
                        <option value="">Select a shift</option>
                        <option value="Day Shift">Day Shift</option>
                        <option value="Night Shift">Night Shift</option>
                      </select>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="workLocation" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Work Location</label>
                      <input type="text" class="form-control" id="workLocation" v-model="formData.workLocation" placeholder="Enter work location">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="joinDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Join Date</label>
                      <input type="date" class="form-control" id="joinDate" v-model="formData.joinDate">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="phoneNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                        Phone Number <span class="text-danger-600">*</span>
                      </label>
                      <input type="tel" class="form-control" id="phoneNumber" v-model="formData.phoneNumber" placeholder="Enter your Phone Number" required>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="employeeEmail" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                        Email <span class="text-danger-600">*</span>
                      </label>
                      <input type="email" class="form-control" id="employeeEmail" v-model="formData.email" placeholder="Enter your Email" required>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                        Employee Photo <span class="text-danger-600">*</span>
                      </label>
                      <input type="file" class="form-control" @change="handlePhotoUpload" accept="image/*">
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Medical Details -->
            <div class="col-lg-12">
              <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                  <h6 class="text-lg fw-semibold mb-0">Medical Details</h6>
                </div>
                <div class="card-body p-20">
                  <div class="row gy-3">
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="bloodGroup" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Blood Group</label>
                      <select id="bloodGroup" class="form-control form-select" v-model="formData.bloodGroup">
                        <option value="">Select blood group</option>
                        <option value="A+">A+</option>
                        <option value="AB+">AB+</option>
                        <option value="A-">A-</option>
                        <option value="AB-">AB-</option>
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                      </select>
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="medicalHeight" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Height</label>
                      <input type="text" class="form-control" id="medicalHeight" v-model="formData.height" placeholder="Enter height">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="medicalWeight" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Weight</label>
                      <input type="text" class="form-control" id="medicalWeight" v-model="formData.weight" placeholder="Enter Weight">
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Bank Details -->
            <div class="col-lg-12">
              <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                  <h6 class="text-lg fw-semibold mb-0">Bank Details</h6>
                </div>
                <div class="card-body p-20">
                  <div class="row gy-3">
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="bankAccountNumber" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Bank Account Number</label>
                      <input type="text" class="form-control" id="bankAccountNumber" v-model="formData.bankAccountNumber" placeholder="Enter bank account number">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="bankName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Bank Name</label>
                      <input type="text" class="form-control" id="bankName" v-model="formData.bankName" placeholder="Enter bank name">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="ifscCode" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">IFSC Code</label>
                      <input type="text" class="form-control" id="ifscCode" v-model="formData.ifscCode" placeholder="Enter IFSC Code">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="nationalId" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">National Identification Number</label>
                      <input type="text" class="form-control" id="nationalId" v-model="formData.nationalId" placeholder="Enter national identification number">
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Upload Documents -->
            <div class="col-xxl-12">
              <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                  <h6 class="text-lg fw-semibold mb-0">Upload Documents</h6>
                </div>
                <div class="card-body p-20">
                  <div class="row gy-3">
                    <div class="col-sm-6">
                      <label for="docName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Doc Name</label>
                      <input type="text" class="form-control" id="docName" v-model="formData.docName" placeholder="Enter Doc Name">
                    </div>
                    <div class="col-sm-6">
                      <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Upload File</label>
                      <input type="file" class="form-control" @change="handleDocumentUpload">
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Previous School Details -->
            <div class="col-xxl-6">
              <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                  <h6 class="text-lg fw-semibold mb-0">Previous School Details</h6>
                </div>
                <div class="card-body p-20">
                  <div class="row gy-3">
                    <div class="col-sm-6">
                      <label for="previousSchool" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">School Name</label>
                      <input type="text" class="form-control" id="previousSchool" v-model="formData.previousSchool" placeholder="Enter School Name">
                    </div>
                    <div class="col-sm-6">
                      <label for="previousSchoolAddress" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Address</label>
                      <input type="text" class="form-control" id="previousSchoolAddress" v-model="formData.previousSchoolAddress" placeholder="Enter Address">
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Address -->
            <div class="col-xxl-6">
              <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                  <h6 class="text-lg fw-semibold mb-0">Address</h6>
                </div>
                <div class="card-body p-20">
                  <div class="row gy-3">
                    <div class="col-sm-6">
                      <label for="currentAddress" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Current Address</label>
                      <input type="text" class="form-control" id="currentAddress" v-model="formData.currentAddress" placeholder="Enter Current Address">
                    </div>
                    <div class="col-sm-6">
                      <label for="permanentAddress" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Permanent Address</label>
                      <input type="text" class="form-control" id="permanentAddress" v-model="formData.permanentAddress" placeholder="Enter Permanent Address">
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Social Media -->
            <div class="col-xl-12">
              <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                  <h6 class="text-lg fw-semibold mb-0">Social Media</h6>
                </div>
                <div class="card-body p-20">
                  <div class="row gy-3">
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="facebookLink" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Facebook</label>
                      <input type="text" id="facebookLink" class="form-control" v-model="formData.facebook" placeholder="Enter your facebook link">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="linkedInLink" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">LinkedIn</label>
                      <input type="text" id="linkedInLink" class="form-control" v-model="formData.linkedin" placeholder="Enter your LinkedIn link">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="instagramLink" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Instagram</label>
                      <input type="text" id="instagramLink" class="form-control" v-model="formData.instagram" placeholder="Enter your Instagram link">
                    </div>
                    <div class="col-xxl-3 col-xl-4 col-sm-6">
                      <label for="youTubeLink" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">YouTube</label>
                      <input type="text" id="youTubeLink" class="form-control" v-model="formData.youtube" placeholder="Enter your YouTube link">
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Login Details -->
            <div class="col-xl-12">
              <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
                <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                  <h6 class="text-lg fw-semibold mb-0">Login Details</h6>
                </div>
                <div class="card-body p-20">
                  <div class="row gy-3">
                    <div class="col-sm-6">
                      <label for="loginEmail" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                        Email <span class="text-danger-600">*</span>
                      </label>
                      <input type="email" class="form-control" id="loginEmail" v-model="formData.loginEmail" placeholder="Enter Email" required>
                    </div>
                    <div class="col-sm-6">
                      <label for="loginPassword" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">
                        Password <span class="text-danger-600">*</span>
                      </label>
                      <div class="position-relative">
                        <input :type="showPassword ? 'text' : 'password'" id="loginPassword" class="form-control" v-model="formData.password" placeholder="Enter your password" required>
                        <span class="toggle-password ri-eye-line cursor-pointer position-absolute end-0 top-50 translate-middle-y me-16 text-secondary-light" :class="{ 'ri-eye-off-line': showPassword }" @click="showPassword = !showPassword"></span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Submit Buttons -->
            <div class="col-12">
              <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
                <button type="reset" @click="resetForm" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8">
                  Reset
                </button>
                <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8">
                  Save Changes
                </button>
              </div>
            </div>
          </div>
        </form>
</template>

<script>
import { ref } from 'vue';
export default {
  setup() {
    const showPassword = ref(false);
    
    const formData = ref({
      employeeID: '',
      fullName: '',
      department: '',
      designation: '',
      gender: '',
      dateOfBirth: '',
      fathersName: '',
      mothersName: '',
      maritalStatus: '',
      contractType: '',
      shift: '',
      workLocation: '',
      joinDate: '',
      phoneNumber: '',
      email: '',
      photo: null,
      bloodGroup: '',
      height: '',
      weight: '',
      bankAccountNumber: '',
      bankName: '',
      ifscCode: '',
      nationalId: '',
      docName: '',
      document: null,
      previousSchool: '',
      previousSchoolAddress: '',
      currentAddress: '',
      permanentAddress: '',
      facebook: '',
      linkedin: '',
      instagram: '',
      youtube: '',
      loginEmail: '',
      password: ''
    });

    const handlePhotoUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        formData.value.photo = file;
      }
    };

    const handleDocumentUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        formData.value.document = file;
      }
    };

    const handleSubmit = () => {
      console.log('Form submitted:', formData.value);
      // Add your form submission logic here
      alert('Employee added successfully!');
    };

    const resetForm = () => {
      formData.value = {
        employeeID: '',
        fullName: '',
        department: '',
        designation: '',
        gender: '',
        dateOfBirth: '',
        fathersName: '',
        mothersName: '',
        maritalStatus: '',
        contractType: '',
        shift: '',
        workLocation: '',
        joinDate: '',
        phoneNumber: '',
        email: '',
        photo: null,
        bloodGroup: '',
        height: '',
        weight: '',
        bankAccountNumber: '',
        bankName: '',
        ifscCode: '',
        nationalId: '',
        docName: '',
        document: null,
        previousSchool: '',
        previousSchoolAddress: '',
        currentAddress: '',
        permanentAddress: '',
        facebook: '',
        linkedin: '',
        instagram: '',
        youtube: '',
        loginEmail: '',
        password: ''
      };
    };

    return {
      showPassword,
      formData,
      handlePhotoUpload,
      handleDocumentUpload,
      handleSubmit,
      resetForm
    };
  }
};
</script>