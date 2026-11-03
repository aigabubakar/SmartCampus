<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />

      <!-- Loading State -->
      <div v-if="isLoading" class="card p-32 text-center my-24">
        <div class="spinner-border text-primary-600 mx-auto mb-16" role="status">
          <span class="visually-hidden">Loading student dossier...</span>
        </div>
        <p class="text-secondary-light mb-0">Retrieving student academic records from the institutional registry...</p>
      </div>

      <template v-else>
        <div class="mt-24">
          <StudentProfileCard :student="studentDossier" @edit="openEditModal" />
        </div>

        <div class="my-16">
          <ul class="nav nav-pills bordered-tab mb-3" id="pills-tab" role="tablist">
            <li class="nav-item" role="presentation">
              <button class="nav-link d-flex align-items-center gap-8 text-secondary-light fw-medium text-sm text-hover-primary-600 text-capitalize bg-transparent px-20 py-12 active" id="pills-studentDetails-tab" data-bs-toggle="pill" data-bs-target="#pills-studentDetails" type="button" role="tab" aria-controls="pills-studentDetails" aria-selected="true">
                <span class="d-flex tab-icon line-height-1 text-md">
                  <i class="ri-group-line"></i>
                </span>
                Academic Dossier & Details
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link d-flex align-items-center gap-8 text-secondary-light fw-medium text-sm text-hover-primary-600 text-capitalize bg-transparent px-20 py-12" id="pills-attendance-tab" data-bs-toggle="pill" data-bs-target="#pills-attendance" type="button" role="tab" aria-controls="pills-attendance" aria-selected="false">
                <span class="d-flex tab-icon line-height-1 text-md">
                  <i class="ri-calendar-check-line"></i>
                </span>
                Lecture Attendance
              </button>
            </li>
            <li class="nav-item" role="presentation">
              <button class="nav-link d-flex align-items-center gap-8 text-secondary-light fw-medium text-sm text-hover-primary-600 text-capitalize bg-transparent px-20 py-12" id="pills-courses-tab" data-bs-toggle="pill" data-bs-target="#pills-courses" type="button" role="tab" aria-controls="pills-courses" aria-selected="false">
                <span class="d-flex tab-icon line-height-1 text-md">
                  <i class="ri-book-read-line"></i>
                </span>
                Enrolled Modules & Grades
              </button>
            </li>
          </ul>

          <div class="tab-content" id="pills-tabContent">
            <!-- Student Details tab start -->
            <div class="tab-pane fade show active" id="pills-studentDetails" role="tabpanel" aria-labelledby="pills-studentDetails-tab" tabindex="0">
              <StudentDetailsTab :student="studentDossier" />
            </div>
            <!-- Student Details tab end -->

            <!-- Attendance tab start -->
            <div class="tab-pane fade" id="pills-attendance" role="tabpanel" aria-labelledby="pills-attendance-tab" tabindex="0">
              <StudentAttendanceTab :attendance="studentDossier?.attendanceStats" :records="studentDossier?.registeredCourses" />
            </div>
            <!-- Attendance tab end -->

            <!-- Courses & Assessment tab start -->
            <div class="tab-pane fade" id="pills-courses" role="tabpanel" aria-labelledby="pills-courses-tab" tabindex="0">
              <div class="card p-24">
                <h6 class="text-md fw-semibold mb-16 text-primary-light">Harmattan Semester Registered Courses & Senate Approvals</h6>
                <div class="table-responsive">
                  <table class="table basic-border-table mb-0">
                    <thead>
                      <tr>
                        <th>Course Code</th>
                        <th>Course Title</th>
                        <th>Credit Units</th>
                        <th>CA Score (30%)</th>
                        <th>Exam Score (70%)</th>
                        <th>Total</th>
                        <th>Letter Grade</th>
                        <th>Senate Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(g, idx) in studentDossier?.grades || []" :key="idx">
                        <td class="fw-semibold text-primary-600">{{ g.courseCode }}</td>
                        <td>{{ g.courseTitle }}</td>
                        <td>3 Units</td>
                        <td>{{ g.caScore }}</td>
                        <td>{{ g.examScore }}</td>
                        <td class="fw-bold">{{ g.totalScore }}</td>
                        <td>
                          <span class="badge bg-success-50 text-success-700 px-8 py-4 rounded-pill">{{ g.letterGrade }}</span>
                        </td>
                        <td>
                          <span v-if="g.senateApproved" class="badge bg-success-50 text-success-600 border border-success-200">Senate Approved</span>
                          <span v-else class="badge bg-warning-50 text-warning-600 border border-warning-200">Pending Review</span>
                        </td>
                      </tr>
                      <tr v-if="!studentDossier?.grades || studentDossier.grades.length === 0">
                        <td colspan="8" class="text-center py-20 text-secondary-light">
                          No official assessment grades ratified for this session yet.
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <!-- Courses tab end -->
          </div>
        </div>
      </template>

      <!-- Edit Profile Modal -->
      <div
        v-if="isEditModalOpen"
        class="modal fade show d-block"
        tabindex="-1"
        style="background: rgba(0, 0, 0, 0.6); z-index: 1060;"
        role="dialog"
      >
        <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
          <div class="modal-content radius-16 border-0 shadow">
            <div class="modal-header border-bottom py-16 px-24 bg-base">
              <div class="d-flex align-items-center gap-12">
                <div class="w-40-px h-40-px radius-8 bg-primary-50 text-primary-600 d-flex justify-content-center align-items-center text-xl">
                  <i class="ri-user-settings-line"></i>
                </div>
                <div>
                  <h6 class="modal-title text-lg fw-semibold mb-0">Update Student Profile Record</h6>
                  <p class="text-xs text-secondary-light mb-0">
                    Changes persist directly in the institutional relational database.
                  </p>
                </div>
              </div>
              <button
                type="button"
                class="btn-close"
                aria-label="Close"
                :disabled="isSaving"
                @click="closeEditModal"
              ></button>
            </div>

            <div class="modal-body p-24">
              <!-- Academic Locks Advisory Banner -->
              <div class="alert alert-primary bg-primary-50 border border-primary-100 radius-8 p-12 mb-20 d-flex gap-12 align-items-center">
                <i class="ri-lock-2-line text-primary-600 text-xl flex-shrink-0"></i>
                <div class="text-xs text-primary-900">
                  <strong>Senate Academic Integrity Lock:</strong>
                  Matriculation number, faculty, department, and CGPA are regulated by university senate policy and can only be modified by the Academic Registrar.
                </div>
              </div>

              <form @submit.prevent="saveProfileChanges">
                <div class="row gy-3">
                  <!-- Scholar Photograph Upload & Studio Section -->
                  <div class="col-12">
                    <div class="card border border-neutral-200 radius-12 bg-neutral-50 p-20 mb-8 shadow-none">
                      <div class="d-flex flex-sm-row flex-column align-items-sm-center justify-content-between pb-12 mb-16 border-bottom gap-8">
                        <div>
                          <h6 class="text-sm fw-bold text-primary-light mb-2">
                            <i class="ri-camera-lens-line text-primary-600 me-6"></i>Official Scholar Academic Portrait
                          </h6>
                          <p class="text-xs text-secondary-light mb-0">
                            Provide a formal tertiary passport photograph or choose from institutional scholar presets.
                          </p>
                        </div>
                        <span class="badge bg-primary-50 text-primary-700 border border-primary-200 text-xs px-10 py-4 align-self-sm-auto align-self-start">
                          Standard 1:1 Portrait
                        </span>
                      </div>

                      <div class="row g-20 align-items-center">
                        <!-- Portrait Preview & Current Status -->
                        <div class="col-sm-auto text-center">
                          <div class="position-relative d-inline-block">
                            <figure class="w-100-px h-100-px rounded-circle overflow-hidden shadow border border-3 border-white mb-0 bg-white position-relative">
                              <img
                                :src="editForm.avatar || defaultAvatar"
                                alt="Scholar Portrait"
                                class="w-100 h-100 object-fit-cover"
                                @error="(e) => e.target.src = defaultAvatar"
                              >
                              <!-- Loading overlay while reading file -->
                              <div v-if="isReadingPhoto" class="position-absolute top-0 start-0 w-100 h-100 bg-black bg-opacity-50 d-flex justify-content-center align-items-center text-white">
                                <span class="spinner-border spinner-border-sm" role="status"></span>
                              </div>
                            </figure>
                            <span
                              v-if="selectedFileName"
                              class="position-absolute bottom-0 end-0 bg-success-600 text-white rounded-circle w-26-px h-26-px d-flex justify-content-center align-items-center border border-2 border-white text-xs shadow-sm"
                              title="Custom Photograph Selected"
                            >
                              <i class="ri-check-line"></i>
                            </span>
                          </div>
                          <div class="mt-8">
                            <span v-if="selectedFileName" class="badge bg-success-100 text-success-800 text-2xs fw-semibold px-8 py-3">
                              New Photo Loaded
                            </span>
                            <span v-else-if="isPresetAvatar" class="badge bg-primary-100 text-primary-800 text-2xs fw-semibold px-8 py-3">
                              University Preset
                            </span>
                            <span v-else class="badge bg-neutral-200 text-neutral-800 text-2xs fw-medium px-8 py-3">
                              Current Dossier Photo
                            </span>
                          </div>
                        </div>

                        <!-- Drop & Browse Studio Area -->
                        <div class="col-sm flex-grow-1">
                          <!-- Drag & Drop Zone -->
                          <div
                            class="border-2 border-dashed radius-12 p-16 text-center transition-all cursor-pointer"
                            :class="[
                              isDragging ? 'border-primary-600 bg-primary-50' : 'border-neutral-300 bg-white hover-border-primary-500'
                            ]"
                            @dragover.prevent="isDragging = true"
                            @dragleave.prevent="isDragging = false"
                            @drop.prevent="handleAvatarDrop"
                            @click="triggerFileInput"
                          >
                            <input
                              ref="avatarFileInput"
                              type="file"
                              accept="image/*, image/jpeg, image/jpg, image/png, image/webp, .jpg, .jpeg, .png, .webp"
                              class="d-none"
                              @change="handleAvatarFileSelect"
                            >

                            <i class="ri-upload-cloud-2-line text-2xl text-primary-600 mb-4 d-block line-height-1"></i>
                            <p class="text-xs fw-semibold text-primary-light mb-2">
                              <span class="text-primary-600 hover-underline">Click to browse your device</span> or drag and drop image here
                            </p>
                            <p class="text-2xs text-secondary-light mb-0 font-monospace">
                              Defined Image Formats: JPG, JPEG, PNG, WebP • Max 5MB
                            </p>
                          </div>

                          <!-- Selected File Information Bar -->
                          <div v-if="selectedFileName" class="mt-10 p-8 px-12 radius-8 bg-success-50 border border-success-200 d-flex align-items-center justify-content-between gap-12">
                            <div class="d-flex align-items-center gap-8 overflow-hidden">
                              <i class="ri-file-image-line text-success-700 text-base flex-shrink-0"></i>
                              <span class="text-xs fw-semibold text-success-900 text-truncate font-monospace">{{ selectedFileName }}</span>
                              <span class="text-2xs text-success-700 flex-shrink-0">({{ selectedFileSize }})</span>
                            </div>
                            <button
                              type="button"
                              class="btn btn-sm btn-link text-danger-600 text-xs p-0 text-decoration-none fw-semibold flex-shrink-0"
                              @click.stop="resetAvatar"
                            >
                              <i class="ri-close-line me-2"></i>Clear
                            </button>
                          </div>
                        </div>
                      </div>

                      <!-- University Scholar Presets Row -->
                      <div class="mt-16 pt-12 border-top">
                        <div class="d-flex align-items-center justify-content-between mb-8">
                          <span class="text-xs fw-semibold text-secondary-light">
                            <i class="ri-sparkling-line text-warning-600 me-4"></i>Institutional Scholar Presets:
                          </span>
                          <button
                            v-if="editForm.avatar && editForm.avatar !== defaultAvatar"
                            type="button"
                            class="btn btn-link text-xs text-secondary-light hover-text-primary-600 p-0 text-decoration-none"
                            @click="resetAvatar"
                          >
                            <i class="ri-refresh-line me-2"></i>Reset to Default
                          </button>
                        </div>

                        <div class="d-flex gap-10 flex-wrap">
                          <button
                            v-for="preset in scholarPresets"
                            :key="preset"
                            type="button"
                            class="w-40-px h-40-px rounded-circle overflow-hidden p-0 transition-all cursor-pointer position-relative border"
                            :class="editForm.avatar === preset ? 'border-primary-600 border-2 shadow scale-105' : 'border-neutral-300 opacity-80 hover-opacity-100'"
                            @click="selectPreset(preset)"
                            :title="'Select Scholar Preset ' + preset"
                          >
                            <img :src="preset" alt="Scholar Preset" class="w-100 h-100 object-fit-cover">
                            <span
                              v-if="editForm.avatar === preset"
                              class="position-absolute top-0 start-0 w-100 h-100 bg-primary-600 bg-opacity-30 d-flex justify-content-center align-items-center text-white"
                            >
                              <i class="ri-check-line text-sm fw-bold"></i>
                            </span>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Scholar Name -->
                  <div class="col-md-6">
                    <label class="form-label text-xs fw-semibold text-primary-light">Full Legal Name</label>
                    <input
                      type="text"
                      v-model="editForm.name"
                      class="form-control"
                      placeholder="e.g. Sophia A. Chen"
                      required
                    >
                  </div>

                  <!-- Institutional Email (Read-Only) -->
                  <div class="col-md-6">
                    <label class="form-label text-xs fw-semibold text-secondary-light">
                      Institutional Email <i class="ri-lock-line ms-4"></i>
                    </label>
                    <input
                      type="email"
                      :value="studentDossier?.email"
                      class="form-control bg-neutral-100 text-secondary-light"
                      disabled
                      readonly
                    >
                  </div>

                  <!-- Contact Phone -->
                  <div class="col-md-6">
                    <label class="form-label text-xs fw-semibold text-primary-light">Contact Phone Number</label>
                    <input
                      type="text"
                      v-model="editForm.phone"
                      class="form-control"
                      placeholder="e.g. +1 (555) 234-8901"
                    >
                  </div>

                  <!-- Hall of Residence -->
                  <div class="col-md-6">
                    <label class="form-label text-xs fw-semibold text-primary-light">Campus Hall of Residence / Hostel</label>
                    <input
                      type="text"
                      v-model="editForm.hallOfResidence"
                      class="form-control"
                      placeholder="e.g. Queen Idia Hall, Block C, Room 14"
                    >
                  </div>

                  <!-- Residential Address -->
                  <div class="col-12">
                    <label class="form-label text-xs fw-semibold text-primary-light">Residential / Domicile Address</label>
                    <input
                      type="text"
                      v-model="editForm.address"
                      class="form-control"
                      placeholder="e.g. Plot 14, Academic Hills, University City"
                    >
                  </div>

                  <!-- Section Divider: Guardian Info -->
                  <div class="col-12 pt-8">
                    <h6 class="text-sm fw-semibold text-primary-600 mb-0 border-bottom pb-8">
                      Parent & Guardian Academic Sponsor Details
                    </h6>
                  </div>

                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Guardian Name</label>
                    <input
                      type="text"
                      v-model="editForm.guardianName"
                      class="form-control"
                      placeholder="e.g. Eleanor Vance-Chen"
                    >
                  </div>

                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Guardian Phone</label>
                    <input
                      type="text"
                      v-model="editForm.guardianPhone"
                      class="form-control"
                      placeholder="e.g. +1 (555) 304-9912"
                    >
                  </div>

                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Guardian Email</label>
                    <input
                      type="email"
                      v-model="editForm.guardianEmail"
                      class="form-control"
                      placeholder="e.g. eleanor.vance@family.org"
                    >
                  </div>

                  <!-- Section Divider: Medical / Health -->
                  <div class="col-12 pt-8">
                    <h6 class="text-sm fw-semibold text-primary-600 mb-0 border-bottom pb-8">
                      Health & Emergency Clinical Information
                    </h6>
                  </div>

                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Blood Group</label>
                    <select v-model="editForm.bloodGroup" class="form-control form-select">
                      <option value="O+">O+</option>
                      <option value="O-">O-</option>
                      <option value="A+">A+</option>
                      <option value="A-">A-</option>
                      <option value="B+">B+</option>
                      <option value="B-">B-</option>
                      <option value="AB+">AB+</option>
                      <option value="AB-">AB-</option>
                    </select>
                  </div>

                  <div class="col-md-8">
                    <label class="form-label text-xs fw-semibold text-primary-light">Emergency Contact Phone</label>
                    <input
                      type="text"
                      v-model="editForm.emergencyContact"
                      class="form-control"
                      placeholder="e.g. +1 (555) 304-9912"
                    >
                  </div>

                  <!-- Academic Statement / Bio -->
                  <div class="col-12 pt-8">
                    <h6 class="text-sm fw-semibold text-primary-600 mb-0 border-bottom pb-8">
                      Academic Bio & Scholar Statement
                    </h6>
                  </div>

                  <div class="col-12">
                    <label class="form-label text-xs fw-semibold text-primary-light">Research Focus & Profile Statement</label>
                    <textarea
                      v-model="editForm.bio"
                      rows="3"
                      class="form-control"
                      placeholder="Brief personal scholar statement..."
                    ></textarea>
                  </div>
                </div>

                <div class="d-flex justify-content-end gap-12 mt-24 pt-16 border-top">
                  <button
                    type="button"
                    class="btn btn-outline-secondary px-20 py-10 radius-8 text-sm"
                    :disabled="isSaving"
                    @click="closeEditModal"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    class="btn btn-primary-600 px-24 py-10 radius-8 text-sm fw-semibold d-flex align-items-center gap-8"
                    :disabled="isSaving"
                  >
                    <span v-if="isSaving" class="spinner-border spinner-border-sm" role="status"></span>
                    <i v-else class="ri-save-line"></i>
                    {{ isSaving ? 'Saving...' : 'Save Changes' }}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </main>
  <ThemeCustomizer />
</template>

<script>
import { ref, reactive, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';
import { studentsApi } from '@/services/api.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/students/studentDetails/Breadcrumb.vue';
import StudentProfileCard from '@/components/students/studentDetails/StudentProfileCard.vue';
import StudentDetailsTab from '@/components/students/studentDetails/StudentDetailsTab.vue';
import StudentAttendanceTab from '@/components/students/studentDetails/StudentAttendanceTab.vue';

export default {
  name: "StudentDetails",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    StudentProfileCard,
    StudentDetailsTab,
    StudentAttendanceTab
  },
  setup() {
    const route = useRoute();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const studentDossier = ref(null);
    const isLoading = ref(true);
    const isEditModalOpen = ref(false);
    const isSaving = ref(false);

    const defaultAvatar = '/assets/images/thumbs/user-img1.png';
    const avatarFileInput = ref(null);
    const isDragging = ref(false);
    const isReadingPhoto = ref(false);
    const selectedFileName = ref('');
    const selectedFileSize = ref('');

    const scholarPresets = [
      '/assets/images/thumbs/user-img1.png',
      '/assets/images/thumbs/user-img2.png',
      '/assets/images/thumbs/user-img3.png',
      '/assets/images/thumbs/avatar-img1.png',
      '/assets/images/thumbs/avatar-img2.png',
      '/assets/images/thumbs/avatar-img3.png',
      '/assets/images/thumbs/leave-request-img1.png',
      '/assets/images/thumbs/leave-request-img2.png',
    ];

    const editForm = reactive({
      name: '',
      avatar: defaultAvatar,
      phone: '',
      address: '',
      hallOfResidence: '',
      guardianName: '',
      guardianPhone: '',
      guardianEmail: '',
      bloodGroup: 'O+',
      emergencyContact: '',
      bio: '',
    });

    const isPresetAvatar = computed(() => scholarPresets.includes(editForm.avatar));

    const triggerFileInput = () => {
      avatarFileInput.value?.click();
    };

    const selectPreset = (preset) => {
      editForm.avatar = preset;
      selectedFileName.value = '';
      selectedFileSize.value = '';
      if (avatarFileInput.value) avatarFileInput.value.value = '';
    };

    const processPhotoFile = (file) => {
      if (!file) return;

      // Validate defined application types
      const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
      const ext = file.name.split('.').pop()?.toLowerCase();
      const validExts = ['jpg', 'jpeg', 'png', 'webp'];

      if (!file.type.startsWith('image/') && !validExts.includes(ext)) {
        toastStore.error('Please select a valid image file (JPG, JPEG, PNG, or WebP).', 'Unsupported Application Type');
        return;
      }

      if (file.size > 5 * 1024 * 1024) {
        toastStore.error('Photograph file size exceeds the 5MB institutional limit.', 'File Too Large');
        return;
      }

      // Format readable size
      const sizeKb = file.size / 1024;
      selectedFileSize.value = sizeKb > 1024 ? `${(sizeKb / 1024).toFixed(2)} MB` : `${Math.round(sizeKb)} KB`;
      selectedFileName.value = file.name;
      isReadingPhoto.value = true;

      const reader = new FileReader();
      reader.onload = (event) => {
        editForm.avatar = event.target.result;
        isReadingPhoto.value = false;
        toastStore.info(`Photograph "${file.name}" loaded successfully into preview.`, 'Portrait Staged');
      };
      reader.onerror = () => {
        isReadingPhoto.value = false;
        toastStore.error('Could not process selected image file. Please try another image.', 'Read Error');
      };
      reader.readAsDataURL(file);
    };

    const handleAvatarFileSelect = (e) => {
      const file = e.target.files?.[0];
      if (file) processPhotoFile(file);
    };

    const handleAvatarDrop = (e) => {
      isDragging.value = false;
      const file = e.dataTransfer?.files?.[0];
      if (file) processPhotoFile(file);
    };

    const resetAvatar = () => {
      editForm.avatar = defaultAvatar;
      selectedFileName.value = '';
      selectedFileSize.value = '';
      if (avatarFileInput.value) avatarFileInput.value.value = '';
    };

    const fetchDossier = async () => {
      isLoading.value = true;
      try {
        const queryMatric = route.query.matric || route.query.id;
        let data = null;

        if (queryMatric) {
          data = await studentsApi.getStudentDossier(queryMatric);
        } else if (authStore.isStudent) {
          data = await studentsApi.getMyDossier();
        } else {
          // If admin viewing without query, default to primary demo student
          data = await studentsApi.getStudentDossier('SCI/2026/0491');
        }

        if (data) {
          studentDossier.value = data;
        }
      } catch (err) {
        console.error('Failed to load student dossier:', err);
        // Fallback to local store user if available
        if (authStore.currentUser) {
          studentDossier.value = {
            name: authStore.currentUser.name,
            email: authStore.currentUser.email,
            matricNumber: authStore.currentUser.matricNumber || 'SCI/2026/0491',
            level: authStore.currentUser.level || '300 Level',
            program: authStore.currentUser.program || 'B.Sc Computer Science',
            faculty: 'Faculty of Computing & Information Systems',
            department: 'Department of Computer Science',
            cgpa: authStore.currentUser.cgpa || 3.85,
            admissionYear: '2023',
            status: 'Active',
            phone: authStore.currentUser.phone || '+1 (555) 234-8901',
            address: authStore.currentUser.address || 'Plot 14, Academic Hills, University City',
            hallOfResidence: 'Queen Idia Hall, Block C, Room 14',
            guardianName: 'Eleanor Vance-Chen',
            guardianPhone: '+1 (555) 304-9912',
            guardianEmail: 'eleanor.vance@family.org',
            bloodGroup: 'O+',
            emergencyContact: '+1 (555) 304-9912',
            bio: 'Undergraduate Scholar majoring in Computer Science with a focus on Distributed Systems and Software Architecture.',
          };
        }
      } finally {
        isLoading.value = false;
      }
    };

    const openEditModal = () => {
      const d = studentDossier.value || authStore.currentUser || {};
      editForm.name = d.name || '';
      editForm.avatar = d.avatar || defaultAvatar;
      editForm.phone = d.phone || '';
      editForm.address = d.address || '';
      editForm.hallOfResidence = d.hallOfResidence || '';
      editForm.guardianName = d.guardianName || '';
      editForm.guardianPhone = d.guardianPhone || '';
      editForm.guardianEmail = d.guardianEmail || '';
      editForm.bloodGroup = d.bloodGroup || 'O+';
      editForm.emergencyContact = d.emergencyContact || d.guardianPhone || '';
      editForm.bio = d.bio || '';
      selectedFileName.value = '';
      selectedFileSize.value = '';
      isEditModalOpen.value = true;
    };

    const closeEditModal = () => {
      isEditModalOpen.value = false;
    };

    const saveProfileChanges = async () => {
      isSaving.value = true;
      const delayPromise = new Promise((resolve) => setTimeout(resolve, 1500));
      try {
        const identifier = authStore.isStudent ? 'me' : (studentDossier.value?.matricNumber || 'me');
        const payload = {
          name: editForm.name,
          avatar: editForm.avatar,
          phone: editForm.phone,
          address: editForm.address,
          hallOfResidence: editForm.hallOfResidence,
          guardianName: editForm.guardianName,
          guardianPhone: editForm.guardianPhone,
          guardianEmail: editForm.guardianEmail,
          bloodGroup: editForm.bloodGroup,
          emergencyContact: editForm.emergencyContact,
          bio: editForm.bio,
        };

        const updated = authStore.isStudent
          ? await studentsApi.updateMyProfile(payload)
          : await studentsApi.updateStudent(identifier, payload);

        await delayPromise;

        if (updated) {
          studentDossier.value = updated;
          if (authStore.isStudent) {
            authStore.updateUserProfile({
              name: updated.name,
              avatar: updated.avatar,
              phone: updated.phone,
              address: updated.address,
              guardianName: updated.guardianName,
              guardianPhone: updated.guardianPhone,
              guardianEmail: updated.guardianEmail,
              hallOfResidence: updated.hallOfResidence,
              bio: updated.bio,
              bloodGroup: updated.bloodGroup,
              emergencyContact: updated.emergencyContact,
            });
          }
          toastStore.success(
            'Academic profile records updated and synchronized with the university registry.',
            'Profile Persisted'
          );
          closeEditModal();
        }
      } catch (err) {
        await delayPromise;
        const msg = err.response?.data?.detail || err.message || 'Failed to update student profile in database.';
        toastStore.error(msg, 'Update Failed');
      } finally {
        isSaving.value = false;
      }
    };

    onMounted(() => {
      fetchDossier();
    });

    return {
      studentDossier,
      isLoading,
      isEditModalOpen,
      isSaving,
      editForm,
      defaultAvatar,
      avatarFileInput,
      isDragging,
      isReadingPhoto,
      selectedFileName,
      selectedFileSize,
      isPresetAvatar,
      scholarPresets,
      triggerFileInput,
      selectPreset,
      handleAvatarFileSelect,
      handleAvatarDrop,
      resetAvatar,
      openEditModal,
      closeEditModal,
      saveProfileChanges,
    };
  }
};
</script>
