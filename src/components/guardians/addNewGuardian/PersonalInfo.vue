<template>
    <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
            <h6 class="text-lg fw-semibold mb-0">Personal Info</h6>
        </div>
        <div class="card-body p-20">
            <div class="row gy-3">
                <div class="col-xl-4 col-sm-6">
                    <div class="">
                        <label for="guardianType"
                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Guardian
                            Type
                        </label>
                        <select id="guardianType" class="form-control form-select">
                            <option value="Select Guardian" disabled selected>Select Guardian</option>
                            <option value="Father">Father</option>
                            <option value="Mother">Mother</option>
                            <option value="Brother">Brother</option>
                            <option value="Sister">Sister</option>
                            <option value="Uncle">Uncle</option>
                        </select>
                    </div>
                </div>
                <div class="col-xl-4 col-sm-6">
                    <div class="">
                        <label for="guardianName"
                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Guardian
                            Name
                        </label>
                        <input type="text" id="guardianName" class="form-control"
                            placeholder="Enter guardian name">
                    </div>
                </div>
                <div class="col-xl-4 col-sm-6">
                    <div class="">
                        <label for="phoneNumber"
                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Instagram
                        </label>
                        <input type="tel" id="phoneNumber" class="form-control" placeholder="Enter phone number">
                    </div>
                </div>
                <div class="col-xl-4 col-sm-6">
                    <div class="">
                        <label for="occupation"
                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Occupation
                        </label>
                        <input type="text" id="occupation" class="form-control" placeholder="Enter occupation">
                    </div>
                </div>
                <div class="col-xl-4 col-sm-6">
                    <div class="">
                        <label for="guardianAddress"
                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Guardian
                            Address
                        </label>
                        <input type="text" id="guardianAddress" class="form-control"
                            placeholder="Enter guardian address">
                    </div>
                </div>
                <div class="col-xl-4 col-sm-6">
                    <div class="">
                        <label class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Teacher
                            Photo <span class="text-danger-600">*</span> </label>
                        <div
                            class="drop-zone height-44-px p-4 d-flex justify-content-center align-items-center text-center fw-medium text-md cursor-pointer border border-neutral-400 radius-8 border-dashed bg-hover-neutral-200"
                            :class="{ 'drop-zone--over': isDragging }" @click="triggerFileInput"
                            @dragover.prevent="isDragging = true" @dragleave="isDragging = false" @drop.prevent="handleDrop">
                            <span class="drop-zone__prompt" v-if="!file">Darg & drop a file here or click</span>
                            <div class="drop-zone__thumb" v-if="file" :style="{ backgroundImage: `url(${file.url})` }"
                                :data-label="file.name"></div>
                            <input type="file" ref="fileInput" name="myFile" class="drop-zone__input"
                                @change="handleFileChange" style="display: none;">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    name: "PersonalInfo",
    setup() {
        const file = ref(null);
        const isDragging = ref(false);
        const fileInput = ref(null);

        const triggerFileInput = () => {
            fileInput.value.click();
        };

        const handleFileChange = (e) => {
            const selectedFile = e.target.files[0];
            if (selectedFile) {
                processFile(selectedFile);
            }
        };

        const handleDrop = (e) => {
            isDragging.value = false;
            const droppedFile = e.dataTransfer.files[0];
            if (droppedFile) {
                processFile(droppedFile);
            }
        };

        const processFile = (fileObj) => {
            if (fileObj.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.readAsDataURL(fileObj);
                reader.onload = () => {
                    file.value = {
                        name: fileObj.name,
                        url: reader.result
                    };
                };
            } else {
                file.value = {
                    name: fileObj.name,
                    url: null
                };
            }
        };

        return {
            file,
            isDragging,
            fileInput,
            triggerFileInput,
            handleFileChange,
            handleDrop
        };
    }
}
</script>
