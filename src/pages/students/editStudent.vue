<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />

      <!-- Loading State -->
      <div v-if="isLoading" class="card p-32 text-center my-24">
        <div class="spinner-border text-primary-600 mx-auto mb-16" role="status">
          <span class="visually-hidden">Loading dossier...</span>
        </div>
        <p class="text-secondary-light mb-0">Loading student dossier from institutional registry...</p>
      </div>

      <form v-else @submit.prevent="handleSubmit" class="mt-24">
        <!-- Advisory Alert -->
        <div class="alert alert-primary bg-primary-50 border border-primary-100 radius-12 p-16 mb-24 d-flex gap-16 align-items-center">
          <div class="w-40-px h-40-px radius-8 bg-primary-600 text-white d-flex justify-content-center align-items-center text-xl flex-shrink-0">
            <i class="ri-shield-user-line"></i>
          </div>
          <div>
            <h6 class="text-sm fw-semibold text-primary-900 mb-2">Institutional Academic Record Modification</h6>
            <p class="text-xs text-primary-800 mb-0">
              Personal contact details, residence, guardian records, and scholar bio can be updated by the student.
              <span v-if="!isAdmin">
                Degree program, faculty, department, and matriculation number are immutable by Senate policy.
              </span>
              <span v-else class="fw-semibold text-primary-900">
                Administrator Mode Active: You possess clearance to adjust academic standing and program allocations.
              </span>
            </p>
          </div>
        </div>

        <div class="row gy-4">
          <!-- 1. Personal & Contact Information -->
          <div class="col-12">
            <div class="card h-100">
              <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                <h6 class="text-md fw-semibold mb-0 text-primary-light">
                  <i class="ri-user-3-line text-primary-600 me-8"></i>Personal & Contact Information
                </h6>
              </div>
              <div class="card-body p-24">
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
                                :src="form.avatar || defaultAvatar"
                                alt="Scholar Portrait"
                                class="w-100 h-100 object-fit-cover"
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
                            v-if="form.avatar && form.avatar !== defaultAvatar"
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
                            :class="form.avatar === preset ? 'border-primary-600 border-2 shadow scale-105' : 'border-neutral-300 opacity-80 hover-opacity-100'"
                            @click="selectPreset(preset)"
                            :title="'Select Scholar Preset ' + preset"
                          >
                            <img :src="preset" alt="Scholar Preset" class="w-100 h-100 object-fit-cover">
                            <span
                              v-if="form.avatar === preset"
                              class="position-absolute top-0 start-0 w-100 h-100 bg-primary-600 bg-opacity-30 d-flex justify-content-center align-items-center text-white"
                            >
                              <i class="ri-check-line text-sm fw-bold"></i>
                            </span>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="col-md-6">
                    <label class="form-label text-xs fw-semibold text-primary-light">Full Legal Name *</label>
                    <input
                      type="text"
                      v-model="form.name"
                      class="form-control"
                      placeholder="e.g. Sophia A. Chen"
                      required
                    >
                  </div>
                  <div class="col-md-6">
                    <label class="form-label text-xs fw-semibold text-secondary-light">
                      Institutional Email <i class="ri-lock-line ms-4"></i>
                    </label>
                    <input
                      type="email"
                      :value="form.email"
                      class="form-control bg-neutral-100 text-secondary-light"
                      disabled
                      readonly
                    >
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Contact Phone Number</label>
                    <input
                      type="text"
                      v-model="form.phone"
                      class="form-control"
                      placeholder="e.g. +1 (555) 234-8901"
                    >
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Gender</label>
                    <select v-model="form.gender" class="form-control form-select">
                      <option value="Female">Female</option>
                      <option value="Male">Male</option>
                      <option value="Other">Other</option>
                    </select>
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Date of Birth</label>
                    <input
                      type="date"
                      v-model="form.dateOfBirth"
                      class="form-control"
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 2. Academic Affiliation & Standing -->
          <div class="col-12">
            <div class="card h-100">
              <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                <h6 class="text-md fw-semibold mb-0 text-primary-light">
                  <i class="ri-graduation-cap-line text-primary-600 me-8"></i>Academic Candidacy & Institutional Standing
                </h6>
                <span v-if="!isAdmin" class="badge bg-neutral-100 text-secondary-light border text-xs">
                  <i class="ri-lock-line me-4"></i>Institutional Lock
                </span>
                <span v-else class="badge bg-success-50 text-success-700 border border-success-200 text-xs">
                  Admin Clearance Active
                </span>
              </div>
              <div class="card-body p-24">
                <div class="row gy-3">
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-secondary-light">
                      Matriculation Number <i class="ri-lock-line ms-4"></i>
                    </label>
                    <input
                      type="text"
                      :value="form.matricNumber"
                      class="form-control bg-neutral-100 text-secondary-light fw-semibold"
                      disabled
                      readonly
                    >
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">
                      Faculty {{ !isAdmin ? '(Locked)' : '' }}
                    </label>
                    <input
                      type="text"
                      v-model="form.faculty"
                      class="form-control"
                      :class="{ 'bg-neutral-100 text-secondary-light': !isAdmin }"
                      :disabled="!isAdmin"
                      :readonly="!isAdmin"
                    >
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">
                      Degree Program {{ !isAdmin ? '(Locked)' : '' }}
                    </label>
                    <input
                      type="text"
                      v-model="form.program"
                      class="form-control"
                      :class="{ 'bg-neutral-100 text-secondary-light': !isAdmin }"
                      :disabled="!isAdmin"
                      :readonly="!isAdmin"
                    >
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">
                      Academic Level {{ !isAdmin ? '(Locked)' : '' }}
                    </label>
                    <select
                      v-model="form.level"
                      class="form-control form-select"
                      :class="{ 'bg-neutral-100 text-secondary-light': !isAdmin }"
                      :disabled="!isAdmin"
                    >
                      <option value="100 Level">100 Level</option>
                      <option value="200 Level">200 Level</option>
                      <option value="300 Level">300 Level</option>
                      <option value="400 Level">400 Level</option>
                      <option value="500 Level">500 Level</option>
                      <option value="Postgraduate">Postgraduate</option>
                    </select>
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">
                      Cumulative GPA (CGPA) <i class="ri-lock-line ms-4"></i>
                    </label>
                    <input
                      type="text"
                      :value="Number(form.cgpa || 3.85).toFixed(2)"
                      class="form-control bg-neutral-100 text-secondary-light fw-bold"
                      disabled
                      readonly
                    >
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">
                      Academic Standing Status {{ !isAdmin ? '(Locked)' : '' }}
                    </label>
                    <select
                      v-model="form.status"
                      class="form-control form-select"
                      :class="{ 'bg-neutral-100 text-secondary-light': !isAdmin }"
                      :disabled="!isAdmin"
                    >
                      <option value="Active">Active (Good Standing)</option>
                      <option value="Probation">Academic Probation</option>
                      <option value="Suspended">Suspended</option>
                      <option value="Graduated">Graduated</option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 3. Residential & Campus Accommodation -->
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                <h6 class="text-md fw-semibold mb-0 text-primary-light">
                  <i class="ri-home-4-line text-primary-600 me-8"></i>Residence & Accommodation
                </h6>
              </div>
              <div class="card-body p-24">
                <div class="row gy-3">
                  <div class="col-12">
                    <label class="form-label text-xs fw-semibold text-primary-light">Residential / Domicile Address</label>
                    <input
                      type="text"
                      v-model="form.address"
                      class="form-control"
                      placeholder="e.g. Plot 14, Academic Hills, University City"
                    >
                  </div>
                  <div class="col-12">
                    <label class="form-label text-xs fw-semibold text-primary-light">Campus Hall of Residence / Hostel</label>
                    <input
                      type="text"
                      v-model="form.hallOfResidence"
                      class="form-control"
                      placeholder="e.g. Queen Idia Hall, Block C, Room 14"
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 4. Health & Emergency Contact -->
          <div class="col-md-6">
            <div class="card h-100">
              <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                <h6 class="text-md fw-semibold mb-0 text-primary-light">
                  <i class="ri-heart-pulse-line text-danger-600 me-8"></i>Health & Emergency Contact
                </h6>
              </div>
              <div class="card-body p-24">
                <div class="row gy-3">
                  <div class="col-md-5">
                    <label class="form-label text-xs fw-semibold text-primary-light">Blood Group</label>
                    <select v-model="form.bloodGroup" class="form-control form-select">
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
                  <div class="col-md-7">
                    <label class="form-label text-xs fw-semibold text-primary-light">Emergency Contact Phone</label>
                    <input
                      type="text"
                      v-model="form.emergencyContact"
                      class="form-control"
                      placeholder="e.g. +1 (555) 304-9912"
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 5. Parent & Guardian Sponsor Details -->
          <div class="col-12">
            <div class="card h-100">
              <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                <h6 class="text-md fw-semibold mb-0 text-primary-light">
                  <i class="ri-parent-line text-primary-600 me-8"></i>Parent & Guardian Academic Sponsor
                </h6>
              </div>
              <div class="card-body p-24">
                <div class="row gy-3">
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Guardian Full Name</label>
                    <input
                      type="text"
                      v-model="form.guardianName"
                      class="form-control"
                      placeholder="e.g. Eleanor Vance-Chen"
                    >
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Guardian Phone</label>
                    <input
                      type="text"
                      v-model="form.guardianPhone"
                      class="form-control"
                      placeholder="e.g. +1 (555) 304-9912"
                    >
                  </div>
                  <div class="col-md-4">
                    <label class="form-label text-xs fw-semibold text-primary-light">Guardian Email</label>
                    <input
                      type="email"
                      v-model="form.guardianEmail"
                      class="form-control"
                      placeholder="e.g. eleanor.vance@family.org"
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 6. Academic Statement & Scholar Bio -->
          <div class="col-12">
            <div class="card h-100">
              <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
                <h6 class="text-md fw-semibold mb-0 text-primary-light">
                  <i class="ri-quill-pen-line text-primary-600 me-8"></i>Scholar Statement & Research Bio
                </h6>
              </div>
              <div class="card-body p-24">
                <textarea
                  v-model="form.bio"
                  rows="3"
                  class="form-control"
                  placeholder="Outline your research focus, academic distinctions, and scholarly interests..."
                ></textarea>
              </div>
            </div>
          </div>

          <!-- Form Action Buttons -->
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-end gap-16 mt-8 mb-32">
              <button
                type="button"
                class="btn btn-outline-secondary text-md px-32 py-12 radius-8"
                @click="handleCancel"
                :disabled="isSubmitting"
              >
                Cancel
              </button>
              <button
                type="submit"
                class="btn btn-primary-600 text-md px-36 py-12 radius-8 fw-semibold d-flex align-items-center gap-8"
                :disabled="isSubmitting"
              >
                <span v-if="isSubmitting" class="spinner-border spinner-border-sm" role="status"></span>
                <i v-else class="ri-check-line"></i>
                {{ isSubmitting ? 'Saving...' : 'Save Changes' }}
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>
    <Footer />
  </main>
  <ThemeCustomizer />
</template>

<script>
import { ref, reactive, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';
import { studentsApi } from '@/services/api.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/students/editStudent/Breadcrumb.vue';

export default {
  name: "EditStudent",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isLoading = ref(true);
    const isSubmitting = ref(false);
    const isAdmin = computed(() => authStore.isAdmin || authStore.isSuperAdmin);

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

    const form = reactive({
      name: '',
      avatar: defaultAvatar,
      email: '',
      matricNumber: '',
      phone: '',
      gender: 'Female',
      dateOfBirth: '',
      faculty: '',
      program: '',
      level: '300 Level',
      cgpa: 3.85,
      status: 'Active',
      address: '',
      hallOfResidence: '',
      guardianName: '',
      guardianPhone: '',
      guardianEmail: '',
      bloodGroup: 'O+',
      emergencyContact: '',
      bio: '',
    });

    const isPresetAvatar = computed(() => scholarPresets.includes(form.avatar));

    const triggerFileInput = () => {
      avatarFileInput.value?.click();
    };

    const selectPreset = (preset) => {
      form.avatar = preset;
      selectedFileName.value = '';
      selectedFileSize.value = '';
      if (avatarFileInput.value) avatarFileInput.value.value = '';
    };

    const processPhotoFile = (file) => {
      if (!file) return;

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

      const sizeKb = file.size / 1024;
      selectedFileSize.value = sizeKb > 1024 ? `${(sizeKb / 1024).toFixed(2)} MB` : `${Math.round(sizeKb)} KB`;
      selectedFileName.value = file.name;
      isReadingPhoto.value = true;

      const reader = new FileReader();
      reader.onload = (event) => {
        form.avatar = event.target.result;
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
      form.avatar = defaultAvatar;
      selectedFileName.value = '';
      selectedFileSize.value = '';
      if (avatarFileInput.value) avatarFileInput.value.value = '';
    };

    const loadStudentData = async () => {
      isLoading.value = true;
      try {
        const queryMatric = route.query.matric || route.query.id;
        let data = null;

        if (queryMatric) {
          data = await studentsApi.getStudentDossier(queryMatric);
        } else if (authStore.isStudent) {
          data = await studentsApi.getMyDossier();
        } else {
          data = await studentsApi.getStudentDossier('SCI/2026/0491');
        }

        if (data) {
          form.name = data.name || '';
          form.avatar = data.avatar || defaultAvatar;
          form.email = data.email || '';
          form.matricNumber = data.matricNumber || '';
          form.phone = data.phone || '';
          form.gender = data.gender || 'Female';
          form.dateOfBirth = data.dateOfBirth || '';
          form.faculty = data.faculty || 'Faculty of Computing & Information Systems';
          form.program = data.program || 'B.Sc Computer Science';
          form.level = data.level || '300 Level';
          form.cgpa = data.cgpa || 3.85;
          form.status = data.status || 'Active';
          form.address = data.address || '';
          form.hallOfResidence = data.hallOfResidence || '';
          form.guardianName = data.guardianName || '';
          form.guardianPhone = data.guardianPhone || '';
          form.guardianEmail = data.guardianEmail || '';
          form.bloodGroup = data.bloodGroup || 'O+';
          form.emergencyContact = data.emergencyContact || data.guardianPhone || '';
          form.bio = data.bio || '';
        }
      } catch (err) {
        console.error('Failed to load student data:', err);
        // Fallback to current authenticated user
        if (authStore.currentUser) {
          const u = authStore.currentUser;
          form.name = u.name || '';
          form.avatar = u.avatar || defaultAvatar;
          form.email = u.email || '';
          form.matricNumber = u.matricNumber || 'SCI/2026/0491';
          form.phone = u.phone || '+1 (555) 234-8901';
          form.program = u.program || 'B.Sc Computer Science';
          form.level = u.level || '300 Level';
          form.cgpa = u.cgpa || 3.85;
          form.address = u.address || 'Plot 14, Academic Hills, University City';
          form.hallOfResidence = u.hallOfResidence || 'Queen Idia Hall, Block C, Room 14';
          form.guardianName = u.guardian_name || 'Eleanor Vance-Chen';
          form.guardianPhone = u.guardian_phone || '+1 (555) 304-9912';
          form.guardianEmail = u.guardian_email || 'eleanor.vance@family.org';
          form.bio = u.bio || '';
        }
      } finally {
        isLoading.value = false;
      }
    };

    const handleSubmit = async () => {
      isSubmitting.value = true;
      const delayPromise = new Promise((resolve) => setTimeout(resolve, 1500));
      try {
        const identifier = authStore.isStudent ? 'me' : (form.matricNumber || 'me');
        const payload = {
          name: form.name,
          avatar: form.avatar,
          phone: form.phone,
          gender: form.gender,
          dateOfBirth: form.dateOfBirth,
          address: form.address,
          hallOfResidence: form.hallOfResidence,
          guardianName: form.guardianName,
          guardianPhone: form.guardianPhone,
          guardianEmail: form.guardianEmail,
          bloodGroup: form.bloodGroup,
          emergencyContact: form.emergencyContact,
          bio: form.bio,
        };

        if (isAdmin.value) {
          payload.level = form.level;
          payload.program = form.program;
          payload.faculty = form.faculty;
          payload.status = form.status;
        }

        const updated = authStore.isStudent
          ? await studentsApi.updateMyProfile(payload)
          : await studentsApi.updateStudent(identifier, payload);

        await delayPromise;

        if (updated) {
          if (authStore.isStudent) {
            authStore.updateUserProfile({
              name: updated.name,
              avatar: updated.avatar,
              phone: updated.phone,
              address: updated.address,
              hallOfResidence: updated.hallOfResidence,
              guardianName: updated.guardianName,
              guardianPhone: updated.guardianPhone,
              guardianEmail: updated.guardianEmail,
              bloodGroup: updated.bloodGroup,
              emergencyContact: updated.emergencyContact,
              bio: updated.bio,
            });
          }

          toastStore.success(
            'Academic profile records saved and persisted to the institutional database.',
            'Record Updated'
          );

          // Route to student dossier
          if (authStore.isStudent) {
            router.push('/profile');
          } else {
            router.push(`/student-details?matric=${encodeURIComponent(form.matricNumber)}`);
          }
        }
      } catch (err) {
        await delayPromise;
        const errorMsg = err.response?.data?.detail || err.message || 'Unable to update student records in database.';
        toastStore.error(errorMsg, 'Update Failed');
      } finally {
        isSubmitting.value = false;
      }
    };

    const handleCancel = () => {
      if (window.history.length > 1) {
        router.back();
      } else {
        router.push(authStore.isStudent ? '/profile' : '/student-list');
      }
    };

    onMounted(() => {
      loadStudentData();
    });

    return {
      isLoading,
      isSubmitting,
      isAdmin,
      form,
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
      handleSubmit,
      handleCancel,
    };
  }
};
</script>
