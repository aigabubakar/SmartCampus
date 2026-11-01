<template>
    <div class="card h-100">
        <div class="card-body p-0 dataTable-wrapper">
            <div class="d-flex align-items-center justify-content-between flex-wrap gap-16 px-20 py-12 border-bottom border-neutral-200">
                <div class="d-flex flex-wrap align-items-center gap-16">
                    <div class="dropdown">
                        <button type="button"
                            class="px-12 py-5-px border border-neutral-300 radius-8 d-flex align-items-center gap-20 "
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <span class="d-flex align-items-center gap-1 text-secondary-light text-sm">
                                <i class="ri-file-upload-line text-md line-height-1"></i>
                                Export
                            </span>
                            <span class="">
                                <i class="ri-arrow-down-s-line"></i>
                            </span>
                        </button>
                        <ul class="dropdown-menu p-12 border bg-base shadow">
                            <li>
                                <button type="button"
                                    class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10"
                                    data-bs-toggle="modal" data-bs-target="#exampleModalView">
                                    <i class="ri-file-3-line"></i>
                                    PDF
                                </button>
                            </li>
                            <li>
                                <button type="button"
                                    class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10"
                                    data-bs-toggle="modal" data-bs-target="#exampleModalEdit">
                                    <i class="ri-file-excel-line"></i>
                                    Excel
                                </button>
                            </li>
                        </ul>
                    </div>
                    <form class="navbar-search dt-search m-0">
                        <input type="text" class="dt-input bg-transparent radius-4" aria-controls="dataTable"
                            name="search" placeholder="Search...">
                        <iconify-icon icon="ion:search-outline" class="icon"></iconify-icon>
                    </form>
                </div>
                <div class="d-flex align-items-center gap-8 text-secondary-light">
                    <span class="">
                        Rows per page:
                    </span>
                    <div class="dt-length">
                        <select name="dataTable_length" aria-controls="dataTable"
                            class="dt-input form-control form-select">
                            <option value="5">5</option>
                            <option value="10" selected>10</option>
                            <option value="25">25</option>
                            <option value="50">50</option>
                            <option value="100">100</option>
                        </select>
                    </div>
                </div>
            </div>

            <div class="p-0">
                <div class="table-responsive">
                    <table class="table bordered-table mb-0 data-table" id="dataTable">
                        <thead>
                            <tr>
                                <th scope="col">
                                    <div class="form-check style-check d-flex align-items-center">
                                        <input class="form-check-input" type="checkbox" v-model="selectAll" @change="toggleAll">
                                        <label class="form-check-label">S.L</label>
                                    </div>
                                </th>
                                <th scope="col">Admission No</th>
                                <th scope="col">Name</th>
                                <th scope="col">Roll No</th>
                                <th scope="col">Class</th>
                                <th scope="col">Exam</th>
                                <th scope="col">Grand Total</th>
                                <th scope="col">Percent (%)</th>
                                <th scope="col">Grade</th>
                                <th scope="col">Result</th>
                                <th scope="col">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(result, index) in results" :key="index">
                                <td>
                                    <div class="form-check style-check d-flex align-items-center">
                                        <input class="form-check-input" type="checkbox" v-model="selectedItems"
                                            :value="result.id">
                                        <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                                    </div>
                                </td>
                                <td><span class="text-primary-600">{{ result.admissionNo }}</span></td>
                                <td>
                                    <div class="d-flex align-items-center">
                                        <img :src="result.avatar" alt="Image"
                                            class="flex-shrink-0 me-12 radius-8">
                                        <div class="">
                                            <h6 class="text-md mb-0 fw-medium flex-grow-1">{{ result.name }}</h6>
                                        </div>
                                    </div>
                                </td>
                                <td>{{ result.rollNo }}</td>
                                <td>{{ result.class }}</td>
                                <td>{{ result.exam }}</td>
                                <td>{{ result.grandTotal }}</td>
                                <td>{{ result.percent }}</td>
                                <td>{{ result.grade }}</td>
                                <td>
                                    <span :class="result.isPass ? 'bg-success-100 text-success-600' : 'bg-danger-100 text-danger-600'" 
                                          class="px-16 py-2 radius-4 fw-medium text-sm">
                                        {{ result.isPass ? 'Pass' : 'Fail' }}
                                    </span>
                                </td>
                                <td>
                                    <div class="btn-group">
                                        <button type="button" class="text-primary-light text-xl"
                                            data-bs-toggle="dropdown" aria-expanded="false">
                                            <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                                        </button>
                                        <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                                            <li>
                                                <button type="button"
                                                    class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                                                    @click="$emit('viewResult', result)">
                                                    <i class="ri-eye-line"></i>
                                                    View
                                                </button>
                                            </li>
                                        </ul>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, onMounted, nextTick } from 'vue';

export default {
    name: "ExamResultTable",
    emits: ['viewResult'],
    setup() {
        const selectAll = ref(false);
        const selectedItems = ref([]);

        // Mocks for avatars using provided assets path structure, though exact resolution might need adjustment if using different assets
        const results = ref([
            { id: 1, admissionNo: 'AD52365', name: 'Kathryn Murphy', avatar: 'assets/images/thumbs/avatar-img1.png', rollNo: '12', class: 'Class 1 (A)', exam: 'Monthly Test', grandTotal: 644, percent: 92, grade: 'A+', isPass: true },
            { id: 2, admissionNo: 'AD52366', name: 'Jerome Bell', avatar: 'assets/images/thumbs/avatar-img2.png', rollNo: '14', class: 'Class 2 (B)', exam: 'Final Exam', grandTotal: 578, percent: 82, grade: 'A', isPass: true },
            { id: 3, admissionNo: 'AD52367', name: 'Theresa Webb', avatar: 'assets/images/thumbs/avatar-img3.png', rollNo: '16', class: 'Class 3 (C)', exam: 'Mid Term', grandTotal: 430, percent: 70, grade: 'B+', isPass: true },
            { id: 4, admissionNo: 'AD52368', name: 'Cody Fisher', avatar: 'assets/images/thumbs/avatar-img4.png', rollNo: '19', class: 'Class 4 (A)', exam: 'Quarterly Test', grandTotal: 380, percent: 64, grade: 'B', isPass: false },
            { id: 5, admissionNo: 'AD52369', name: 'Annette Black', avatar: 'assets/images/thumbs/avatar-img5.png', rollNo: '10', class: 'Class 5 (B)', exam: 'Final Exam', grandTotal: 698, percent: 96, grade: 'A+', isPass: true },
            { id: 6, admissionNo: 'AD52370', name: 'Jenny Wilson', avatar: 'assets/images/thumbs/avatar-img6.png', rollNo: '07', class: 'Class 6 (A)', exam: 'Half Yearly', grandTotal: 612, percent: 89, grade: 'A', isPass: true },
            { id: 7, admissionNo: 'AD52371', name: 'Darlene Robertson', avatar: 'assets/images/thumbs/avatar-img7.png', rollNo: '18', class: 'Class 7 (C)', exam: 'Monthly Test', grandTotal: 325, percent: 58, grade: 'C', isPass: false },
            { id: 8, admissionNo: 'AD52372', name: 'Wade Warren', avatar: 'assets/images/thumbs/avatar-img8.png', rollNo: '22', class: 'Class 8 (A)', exam: 'Final Exam', grandTotal: 510, percent: 75, grade: 'B+', isPass: true },
            { id: 9, admissionNo: 'AD52373', name: 'Esther Howard', avatar: 'assets/images/thumbs/avatar-img9.png', rollNo: '09', class: 'Class 9 (B)', exam: 'Mid Term', grandTotal: 285, percent: 46, grade: 'D', isPass: false },
            { id: 10, admissionNo: 'AD52374', name: 'Guy Hawkins', avatar: 'assets/images/thumbs/avatar-img10.png', rollNo: '11', class: 'Class 10 (C)', exam: 'Final Exam', grandTotal: 715, percent: 98, grade: 'A+', isPass: true },
            { id: 11, admissionNo: 'AD52375', name: 'Black Marvin', avatar: 'assets/images/thumbs/avatar-img1.png', rollNo: '13', class: 'Class 11 (B)', exam: 'Terminal', grandTotal: 500, percent: 85, grade: 'B+', isPass: true },
            { id: 12, admissionNo: 'AD52376', name: 'Eleanor Pena', avatar: 'assets/images/thumbs/avatar-img2.png', rollNo: '25', class: 'Class 12 (A)', exam: 'Final', grandTotal: 750, percent: 99, grade: 'A+', isPass: true },
        ]);

        const toggleAll = () => {
             if (selectAll.value) {
                selectedItems.value = results.value.map(r => r.id);
            } else {
                selectedItems.value = [];
            }
        };

        onMounted(async () => {
             await nextTick();
            if (typeof $ !== 'undefined' && $.fn.DataTable) {
                 $('.data-table').each(function () {
                    const $table = $(this);
                    
                    if ($table.hasClass('dataTable-initialized')) return;

                    let tableInstance = $table.DataTable({
                        pageLength: 10,
                        columnDefs: [{ orderable: false, targets: [10] }] // Disable sorting on action column
                    });

                    $table.addClass('dataTable-initialized');

                    $table.closest('.dataTable-wrapper').find('.dt-search .dt-input').on('keyup', function () {
                        tableInstance.search(this.value).draw();
                    });

                    $table.closest('.dataTable-wrapper').find('.dt-length .dt-input').on('change', function () {
                        const value = $(this).val();
                        tableInstance.page.len(value).draw();
                    });
                 });
            }
        });

        return {
            results,
            selectAll,
            selectedItems,
            toggleAll
        };
    }
}
</script>
