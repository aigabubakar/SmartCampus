<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb />
      <form action="#" class="mt-24">
        <div class="row gy-3">
          <div class="col-lg-12">
            <PersonalInfo />
          </div>
          <div class="col-lg-12">
            <MedicalDetails />
          </div>
          <div class="col-lg-12">
            <BankDetails />
          </div>
          <div class="col-xxl-12">
            <UploadDocuments />
          </div>
          <div class="col-xxl-6">
            <PreviousSchoolDetails />
          </div>
          <div class="col-xxl-6">
            <AddressDetails />
          </div>
          <div class="col-xl-12">
            <TeacherBio />
          </div>
          <div class="col-xl-12">
            <SocialLinks />
          </div>
          <div class="col-xl-12">
            <LoginDetails />
          </div>
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
              <button type="reset"
                class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8">
                Reset
              </button>
              <button type="submit"
                class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8">
                Save Changes
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
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/teachers/editTeacher/Breadcrumb.vue';
import PersonalInfo from '@/components/teachers/editTeacher/PersonalInfo.vue';
import MedicalDetails from '@/components/teachers/editTeacher/MedicalDetails.vue';
import BankDetails from '@/components/teachers/editTeacher/BankDetails.vue';
import UploadDocuments from '@/components/teachers/editTeacher/UploadDocuments.vue';
import PreviousSchoolDetails from '@/components/teachers/editTeacher/PreviousSchoolDetails.vue';
import AddressDetails from '@/components/teachers/editTeacher/AddressDetails.vue';
import TeacherBio from '@/components/teachers/editTeacher/TeacherBio.vue';
import SocialLinks from '@/components/teachers/editTeacher/SocialLinks.vue';
import LoginDetails from '@/components/teachers/editTeacher/LoginDetails.vue';

import { onMounted } from 'vue';

export default {
  name: "EditTeacher",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    PersonalInfo,
    MedicalDetails,
    BankDetails,
    UploadDocuments,
    PreviousSchoolDetails,
    AddressDetails,
    TeacherBio,
    SocialLinks,
    LoginDetails
  },
  setup() {
    onMounted(() => {
     // ========================== Drag & Drop Upload photo Js start ========================
        document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
            const dropZoneElement = inputElement.closest(".drop-zone");

            dropZoneElement.addEventListener("click", (e) => {
                inputElement.click();
            });

            inputElement.addEventListener("change", (e) => {
                if (inputElement.files.length) {
                    updateThumbnail(dropZoneElement, inputElement.files[0]);
                }
            });

            dropZoneElement.addEventListener("dragover", (e) => {
                e.preventDefault();
                dropZoneElement.classList.add("drop-zone--over");
            });

            ["dragleave", "dragend"].forEach((type) => {
                dropZoneElement.addEventListener(type, (e) => {
                    dropZoneElement.classList.remove("drop-zone--over");
                });
            });

            dropZoneElement.addEventListener("drop", (e) => {
                e.preventDefault();

                if (e.dataTransfer.files.length) {
                    inputElement.files = e.dataTransfer.files;
                    updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
                }

                dropZoneElement.classList.remove("drop-zone--over");
            });
        });

        /**
         * Updates the thumbnail on a drop zone element.
         *
         * @param {HTMLElement} dropZoneElement
         * @param {File} file
         */
        function updateThumbnail(dropZoneElement, file) {
            let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");

            // First time - remove the prompt
            if (dropZoneElement.querySelector(".drop-zone__prompt")) {
                dropZoneElement.querySelector(".drop-zone__prompt").remove();
            }

            // First time - there is no thumbnail element, so lets create it
            if (!thumbnailElement) {
                thumbnailElement = document.createElement("div");
                thumbnailElement.classList.add("drop-zone__thumb");
                dropZoneElement.appendChild(thumbnailElement);
            }

            thumbnailElement.dataset.label = file.name;

            // Show thumbnail for image files
            if (file.type.startsWith("image/")) {
                const reader = new FileReader();

                reader.readAsDataURL(file);
                reader.onload = () => {
                    thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
                };
            } else {
                thumbnailElement.style.backgroundImage = null;
            }
        }
        // ========================== Drag & Drop Upload photo Js end ========================
    });
  }
}
</script>
