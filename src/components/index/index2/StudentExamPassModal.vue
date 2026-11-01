<template>
  <div class="modal fade" id="studentExamPassModal" tabindex="-1" aria-labelledby="studentExamPassModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg modal-dialog-centered">
      <div class="modal-content border-0 radius-16 shadow-lg overflow-hidden">
        
        <!-- Header with Academic Seal -->
        <div class="modal-header py-16 px-24 text-white" style="background: linear-gradient(135deg, #134e48 0%, #25A194 100%);">
          <div class="d-flex align-items-center gap-12">
            <img :src="institution.crestUrl" alt="Crest" class="w-48-px h-48-px rounded-circle bg-white p-2 shadow-sm object-fit-contain">
            <div>
              <h5 class="modal-title fw-bold text-white mb-0" id="studentExamPassModalLabel">
                Digital Examination Clearance Hall Pass
              </h5>
              <span class="text-white text-opacity-80 text-xs">
                {{ institution.name }} • {{ institution.currentAcademicYear }} {{ institution.currentSemester }}
              </span>
            </div>
          </div>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>

        <!-- Body: Verifiable Student Examination Pass -->
        <div class="modal-body p-24">
          <div class="card border border-neutral-300 radius-12 p-20 bg-neutral-50 mb-20">
            <div class="d-flex flex-wrap align-items-center justify-content-between gap-16">
              
              <!-- Student Photo & Identification -->
              <div class="d-flex align-items-center gap-16">
                <img 
                  :src="studentUser?.avatar || '/assets/images/thumbs/user-img1.png'" 
                  alt="Student" 
                  class="w-64-px h-64-px rounded-circle object-fit-cover border border-2 border-primary-600 shadow-sm"
                >
                <div>
                  <h5 class="fw-bold text-neutral-900 mb-2">{{ studentUser?.name || 'Sophia Chen' }}</h5>
                  <div class="text-xs text-secondary-light">Matriculation No: <strong class="text-primary-light font-monospace">{{ studentUser?.matricNumber || 'SCI/2026/0491' }}</strong></div>
                  <div class="text-xs text-secondary-light">Degree Program: <strong class="text-neutral-800">{{ studentUser?.program || 'B.Sc. Computer Science' }}</strong></div>
                  <div class="text-xs text-secondary-light">Faculty: <span class="text-neutral-800">{{ studentUser?.department || 'Faculty of Natural Sciences' }}</span></div>
                </div>
              </div>

              <!-- Clearance Stamp & QR Code -->
              <div class="text-center bg-white p-12 radius-8 border border-neutral-200 shadow-xs">
                <div class="w-80-px h-80-px bg-neutral-100 rounded d-flex align-items-center justify-content-center mx-auto mb-6">
                  <iconify-icon icon="solar:qr-code-bold" class="text-5xl text-neutral-900"></iconify-icon>
                </div>
                <span class="badge bg-success-subtle text-success-800 border border-success-subtle text-xs px-8 py-2 radius-4 fw-bold">
                  VERIFIED CLEAR
                </span>
                <span class="text-xxs text-secondary-light d-block mt-2 font-monospace">TOKEN: #EX-89024</span>
              </div>

            </div>
          </div>

          <!-- Academic Clearances Matrix -->
          <h6 class="text-sm fw-bold text-neutral-900 mb-12">Institutional Clearance Audit</h6>
          <div class="row g-3 mb-20">
            <div class="col-sm-4">
              <div class="p-12 radius-8 bg-success-50 border border-success-subtle d-flex align-items-center gap-10">
                <iconify-icon icon="solar:check-circle-bold" class="text-success-600 text-2xl flex-shrink-0"></iconify-icon>
                <div>
                  <span class="text-secondary-light text-xxs d-block">Lecture Attendance</span>
                  <strong class="text-success-700 text-sm">88.4% (Threshold &gt; 75%)</strong>
                </div>
              </div>
            </div>
            <div class="col-sm-4">
              <div class="p-12 radius-8 bg-success-50 border border-success-subtle d-flex align-items-center gap-10">
                <iconify-icon icon="solar:check-circle-bold" class="text-success-600 text-2xl flex-shrink-0"></iconify-icon>
                <div>
                  <span class="text-secondary-light text-xxs d-block">Tuition Settlement</span>
                  <strong class="text-success-700 text-sm">100% Cleared (Bursary)</strong>
                </div>
              </div>
            </div>
            <div class="col-sm-4">
              <div class="p-12 radius-8 bg-success-50 border border-success-subtle d-flex align-items-center gap-10">
                <iconify-icon icon="solar:check-circle-bold" class="text-success-600 text-2xl flex-shrink-0"></iconify-icon>
                <div>
                  <span class="text-secondary-light text-xxs d-block">Course Registration</span>
                  <strong class="text-success-700 text-sm">Signed Off by Advisor</strong>
                </div>
              </div>
            </div>
          </div>

          <!-- Registered Courses Admitted for Exam -->
          <h6 class="text-sm fw-bold text-neutral-900 mb-12">Accredited Examination Schedule (Harmattan 2026/2027)</h6>
          <div class="table-responsive radius-8 border border-neutral-200">
            <table class="table table-sm align-middle mb-0 text-xs">
              <thead class="bg-neutral-100 text-secondary-light fw-semibold">
                <tr>
                  <th class="py-8 px-12">Course Code & Title</th>
                  <th class="py-8 px-12">Units</th>
                  <th class="py-8 px-12">Exam Date & Time</th>
                  <th class="py-8 px-12">Allocated Hall & Seat</th>
                  <th class="py-8 px-12 text-center">Eligibility</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="py-8 px-12 fw-semibold text-neutral-900">CSC 301 — Advanced Algorithms</td>
                  <td class="py-8 px-12">3</td>
                  <td class="py-8 px-12">16 Mar 2027 • 09:00 AM</td>
                  <td class="py-8 px-12"><span class="badge bg-neutral-200 text-neutral-800 font-monospace">Auditorium B • Desk #42</span></td>
                  <td class="py-8 px-12 text-center"><span class="badge bg-success-subtle text-success-800">Cleared</span></td>
                </tr>
                <tr>
                  <td class="py-8 px-12 fw-semibold text-neutral-900">AI 303 — Deep Neural Architectures</td>
                  <td class="py-8 px-12">3</td>
                  <td class="py-8 px-12">19 Mar 2027 • 02:00 PM</td>
                  <td class="py-8 px-12"><span class="badge bg-neutral-200 text-neutral-800 font-monospace">CBT Center 1 • Terminal #18</span></td>
                  <td class="py-8 px-12 text-center"><span class="badge bg-success-subtle text-success-800">Cleared</span></td>
                </tr>
                <tr>
                  <td class="py-8 px-12 fw-semibold text-neutral-900">ENG 201 — Engineering Mathematics III</td>
                  <td class="py-8 px-12">3</td>
                  <td class="py-8 px-12">23 Mar 2027 • 09:00 AM</td>
                  <td class="py-8 px-12"><span class="badge bg-neutral-200 text-neutral-800 font-monospace">Lecture Theatre 1 • Desk #89</span></td>
                  <td class="py-8 px-12 text-center"><span class="badge bg-success-subtle text-success-800">Cleared</span></td>
                </tr>
                <tr>
                  <td class="py-8 px-12 fw-semibold text-neutral-900">CSC 305 — Operating System Internals</td>
                  <td class="py-8 px-12">3</td>
                  <td class="py-8 px-12">26 Mar 2027 • 12:00 PM</td>
                  <td class="py-8 px-12"><span class="badge bg-neutral-200 text-neutral-800 font-monospace">Auditorium A • Desk #14</span></td>
                  <td class="py-8 px-12 text-center"><span class="badge bg-success-subtle text-success-800">Cleared</span></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="mt-16 text-neutral-500 text-xxs font-italic text-center">
            * This digital pass must be presented on mobile or printed for biometric admission at the examination entrance turnstiles.
          </div>
        </div>

        <!-- Footer -->
        <div class="modal-footer border-top border-neutral-200 py-12 px-24 bg-neutral-50 d-flex justify-content-between">
          <button type="button" class="btn btn-outline-neutral-300 btn-sm radius-8 px-16 py-6 text-xs" data-bs-dismiss="modal">
            Close
          </button>
          <button type="button" class="btn btn-primary-600 btn-sm radius-8 px-16 py-6 text-xs text-white d-flex align-items-center gap-6" @click="printPass">
            <iconify-icon icon="solar:printer-bold"></iconify-icon>
            Print Official Examination Slip
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useInstitutionStore } from '@/stores/institution.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: 'StudentExamPassModal',
  setup() {
    const authStore = useAuthStore();
    const institution = useInstitutionStore();
    const toastStore = useToastStore();

    const studentUser = computed(() => authStore.currentUser);

    const printPass = () => {
      toastStore.success('Biometric digital examination clearance pass prepared for printing.', 'Hall Pass Ready');
      window.print();
    };

    return {
      institution,
      studentUser,
      printPass
    };
  }
};
</script>
