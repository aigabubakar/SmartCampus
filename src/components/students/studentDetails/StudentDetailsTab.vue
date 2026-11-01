<template>
  <div class="row gy-4">
    <!-- Parent & Guardian Information -->
    <div class="col-12">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Parent & Guardian Academic Sponsor</h6>
          <span class="badge bg-primary-50 text-primary-700 border border-primary-200 px-12 py-4 rounded-pill text-xs fw-semibold">
            Verified Sponsor
          </span>
        </div>
        <div class="card-body p-0">
          <div class="p-20">
            <div class="row g-4 align-items-center">
              <div class="col-md-4">
                <div class="d-flex align-items-center gap-12">
                  <figure class="w-48-px h-48-px rounded-circle overflow-hidden mb-0 border border-neutral-200 flex-shrink-0 bg-neutral-100">
                    <img src="@/assets/images/thumbs/guardian-img1.png" alt="Guardian Image" class="w-100 h-100 object-fit-cover">
                  </figure>
                  <div>
                    <h6 class="text-md mb-2 fw-semibold text-primary-light">
                      {{ student?.guardianName || 'Eleanor Vance-Chen' }}
                    </h6>
                    <span class="text-xs text-secondary-light">Primary Guardian & Academic Sponsor</span>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div>
                  <span class="text-xs text-secondary-light d-block mb-4">Official Contact Phone</span>
                  <h6 class="text-sm mb-0 fw-medium text-primary-light">
                    {{ student?.guardianPhone || '+1 (555) 304-9912' }}
                  </h6>
                </div>
              </div>
              <div class="col-md-4">
                <div>
                  <span class="text-xs text-secondary-light d-block mb-4">Institutional Correspondence Email</span>
                  <h6 class="text-sm mb-0 fw-medium text-primary-600">
                    {{ student?.guardianEmail || 'eleanor.vance@family.org' }}
                  </h6>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Contact & Residential Address -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Residential & Contact Details</h6>
          <i class="ri-map-pin-user-line text-primary-600 text-lg"></i>
        </div>
        <div class="card-body p-20">
          <div class="d-flex flex-column gap-16">
            <div>
              <span class="text-xs text-secondary-light d-block mb-4">Current Domicile / Residential Address</span>
              <p class="text-sm text-primary-light mb-0 fw-medium">
                {{ student?.address || 'Plot 14, Academic Hills, University City' }}
              </p>
            </div>
            <div>
              <span class="text-xs text-secondary-light d-block mb-4">Personal Contact Phone</span>
              <p class="text-sm text-primary-light mb-0 fw-medium">
                {{ student?.phone || '+1 (555) 234-8901' }}
              </p>
            </div>
            <div>
              <span class="text-xs text-secondary-light d-block mb-4">Verified University Email</span>
              <p class="text-sm text-primary-600 mb-0 fw-medium">
                {{ student?.email || 'sophia.chen@student.campus.edu' }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Campus Accommodation / Hall of Residence -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Campus Hall of Residence</h6>
          <i class="ri-hotel-bed-line text-primary-600 text-lg"></i>
        </div>
        <div class="card-body p-20">
          <div class="d-flex flex-column gap-16">
            <div>
              <span class="text-xs text-secondary-light d-block mb-4">Allocated Hall & Room</span>
              <p class="text-sm text-primary-light mb-0 fw-medium">
                {{ student?.hallOfResidence || 'Queen Idia Hall, Block C, Room 14' }}
              </p>
            </div>
            <div>
              <span class="text-xs text-secondary-light d-block mb-4">Accommodation Category</span>
              <p class="text-sm text-primary-light mb-0 fw-medium">
                On-Campus Collegiate Residence (Undergraduate Wing)
              </p>
            </div>
            <div>
              <span class="text-xs text-secondary-light d-block mb-4">Allocation Status</span>
              <span class="badge bg-success-50 text-success-700 border border-success-200 px-12 py-4 rounded-pill text-xs fw-semibold">
                Cleared & Active for 2026/2027 Session
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Medical & Health Services -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Health & University Clinic Record</h6>
          <i class="ri-heart-pulse-line text-danger-600 text-lg"></i>
        </div>
        <div class="card-body p-20">
          <div class="row gy-3">
            <div class="col-sm-6">
              <span class="text-xs text-secondary-light d-block mb-4">Blood Group</span>
              <span class="badge bg-danger-50 text-danger-700 border border-danger-200 px-12 py-6 rounded-8 text-sm fw-bold">
                {{ student?.bloodGroup || 'O+' }}
              </span>
            </div>
            <div class="col-sm-6">
              <span class="text-xs text-secondary-light d-block mb-4">Emergency Contact Phone</span>
              <p class="text-sm text-primary-light mb-0 fw-medium">
                {{ student?.emergencyContact || student?.guardianPhone || '+1 (555) 304-9912' }}
              </p>
            </div>
            <div class="col-12 pt-8 border-top">
              <span class="text-xs text-secondary-light d-block mb-4">Clinical Clearance</span>
              <span class="badge bg-success-50 text-success-700 border border-success-200 px-12 py-4 rounded-pill text-xs fw-semibold">
                Verified by Apex University Health Centre
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Academic Candidacy & Standing -->
    <div class="col-md-6">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Academic Registry & Standing</h6>
          <i class="ri-shield-check-line text-success-600 text-lg"></i>
        </div>
        <div class="card-body p-20">
          <div class="row gy-3">
            <div class="col-sm-6">
              <span class="text-xs text-secondary-light d-block mb-2">Faculty</span>
              <p class="text-sm text-primary-light mb-0 fw-medium">{{ student?.faculty || 'Faculty of Computing & Information Systems' }}</p>
            </div>
            <div class="col-sm-6">
              <span class="text-xs text-secondary-light d-block mb-2">Academic Department</span>
              <p class="text-sm text-primary-light mb-0 fw-medium">{{ student?.department || 'Department of Computer Science' }}</p>
            </div>
            <div class="col-sm-6">
              <span class="text-xs text-secondary-light d-block mb-2">Cumulative Grade Point (CGPA)</span>
              <span class="badge bg-success-50 text-success-700 border border-success-200 px-12 py-6 rounded-8 text-sm fw-bold">
                {{ Number(student?.cgpa || 3.85).toFixed(2) }} / 4.00
              </span>
            </div>
            <div class="col-sm-6">
              <span class="text-xs text-secondary-light d-block mb-2">Academic Session & Level</span>
              <p class="text-sm text-primary-light mb-0 fw-medium">{{ student?.level || '300 Level' }} • Year {{ student?.admissionYear || '2023' }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Scholar Statement & Academic Bio -->
    <div class="col-12">
      <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
          <h6 class="text-lg fw-semibold mb-0">Scholar Profile & Academic Statement</h6>
          <i class="ri-quill-pen-line text-primary-600 text-lg"></i>
        </div>
        <div class="card-body p-20">
          <p class="text-secondary-light mb-0 line-height-lg">
            {{ student?.bio || 'Undergraduate Scholar majoring in Computer Science with a focus on Distributed Systems and Software Architecture. Demonstrates consistent academic distinction, active research participation, and exemplary adherence to university codes of conduct.' }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "StudentDetailsTab",
  props: {
    student: {
      type: Object,
      default: () => ({}),
    },
  },
};
</script>
