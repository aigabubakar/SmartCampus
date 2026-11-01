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
                    <div class="dropdown">
                        <button type="button"
                            class="px-12 py-5-px border border-neutral-300 radius-8 d-flex align-items-center gap-20"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            <span class="d-flex align-items-center gap-1 text-secondary-light text-sm">
                                Filter
                            </span>
                            <span class="">
                                <i class="ri-arrow-down-s-line"></i>
                            </span>
                        </button>
                        <div class="dropdown-menu border bg-base shadow dropdown-menu-lg p-0">
                            <div class="d-flex align-items-center justify-content-between border-bottom py-8 px-16">
                                <span class="fw-semibold text-lg text-primary-light">Filter</span>
                                <button type="button">
                                    <i class="ri-close-large-line"></i>
                                </button>
                            </div>

                            <form action="#" class="p-16 d-grid grid-cols-2 gap-16">
                                <div class="">
                                    <label for="class" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Class</label>
                                    <select id="class" class="form-control form-select">
                                        <option value="Select" disabled>Select Class</option>
                                        <option value="Primary">Primary</option>
                                        <option value="SSC">SSC</option>
                                        <option value="HSC">HSC</option>
                                        <option value="Hons">Hons</option>
                                        <option value="Masters">Masters</option>
                                    </select>
                                </div>
                                <div class="">
                                    <label for="sectionEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Section</label>
                                    <select id="sectionEdit" class="form-control form-select">
                                        <option value="Select">Select Section</option>
                                        <option value="Arts">Arts</option>
                                        <option value="Science">Science</option>
                                        <option value="Commerce">Commerce</option>
                                    </select>
                                </div>
                                <div class="">
                                    <label for="gender" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Gender</label>
                                    <select id="gender" class="form-control form-select">
                                        <option value="Select">Select Gender</option>
                                        <option value="Male">Male</option>
                                        <option value="Female">Female</option>
                                    </select>
                                </div>
                                <div class="">
                                    <label for="status" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                                    <select id="status" class="form-control form-select">
                                        <option value="Select">Select Status</option>
                                        <option value="Active">Active</option>
                                        <option value="Inactive">Inactive</option>
                                    </select>
                                </div>
                                <div class="">
                                    <button type="reset" class="btn btn-danger-200 text-danger-600 w-100">Reset</button>
                                </div>
                                <div class="">
                                    <button type="submit" class="btn btn-primary-600 w-100">Apply</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
                <div class="d-flex align-items-center gap-8 text-secondary-light">
                    <span class="">Rows per page:</span>
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
                                <th scope="col">Amount</th>
                                <th scope="col">Paid</th>
                                <th scope="col">Due</th>
                                <th scope="col">Date</th>
                                <th scope="col">Status</th>
                                <th scope="col">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(student, index) in students" :key="index">
                                <td>
                                    <div class="form-check style-check d-flex align-items-center">
                                        <input class="form-check-input" type="checkbox" v-model="selectedItems" :value="student.id">
                                        <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                                    </div>
                                </td>
                                <td><span class="text-primary-600">{{ student.admissionNo }}</span></td>
                                <td>
                                    <div class="d-flex align-items-center">
                                        <img :src="student.avatar" alt="Image" class="flex-shrink-0 me-12 radius-8">
                                        <div class="">
                                            <h6 class="text-md mb-0 fw-medium flex-grow-1">{{ student.name }}</h6>
                                        </div>
                                    </div>
                                </td>
                                <td>{{ student.rollNo }}</td>
                                <td>{{ student.class }}</td>
                                <td>${{ student.amount }}</td>
                                <td>${{ student.paid }}</td>
                                <td>${{ student.due }}</td>
                                <td>{{ student.date }}</td>
                                <td>
                                    <span :class="getStatusClass(student.status)" class="px-16 py-2 radius-4 fw-medium text-sm">
                                        {{ student.status }}
                                    </span>
                                </td>
                                <td>
                                    <div class="btn-group">
                                        <button type="button" class="text-primary-light text-xl"
                                            data-bs-toggle="dropdown" data-bs-display="static" aria-expanded="false">
                                            <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                                        </button>
                                        <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                                            <li>
                                                <button type="button"
                                                    class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                                                    @click="viewDetails(student)">
                                                    <i class="ri-eye-line"></i>
                                                    View Details
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
    name: "FeesCollectionTable",
    emits: ['viewDetails'],
    setup(props, { emit }) {
        const selectAll = ref(false);
        const selectedItems = ref([]);

        const students = ref([
            { id: 1, admissionNo: 'AD52365', name: 'Kathryn Murphy', avatar: 'assets/images/thumbs/avatar-img1.png', rollNo: '12', class: 'Class 1 (A)', amount: 700.50, paid: 700.50, due: 0, date: '12 May 2025', status: 'Paid' },
            { id: 2, admissionNo: 'AD52366', name: 'Jerome Bell', avatar: 'assets/images/thumbs/avatar-img2.png', rollNo: '08', class: 'Class 2 (B)', amount: 850.00, paid: 450.00, due: 400.00, date: '10 May 2025', status: 'Partial' },
            { id: 3, admissionNo: 'AD52367', name: 'Theresa Webb', avatar: 'assets/images/thumbs/avatar-img3.png', rollNo: '19', class: 'Class 3 (A)', amount: 920.75, paid: 0, due: 920.75, date: '08 May 2025', status: 'Unpaid' },
            { id: 4, admissionNo: 'AD52368', name: 'Cody Fisher', avatar: 'assets/images/thumbs/avatar-img4.png', rollNo: '10', class: 'Class 4 (C)', amount: 750.00, paid: 750.00, due: 0, date: '05 May 2025', status: 'Paid' },
            { id: 5, admissionNo: 'AD52369', name: 'Annette Black', avatar: 'assets/images/thumbs/avatar-img5.png', rollNo: '16', class: 'Class 5 (B)', amount: 630.20, paid: 500.00, due: 130.20, date: '03 May 2025', status: 'Partial' },
            { id: 6, admissionNo: 'AD52370', name: 'Jenny Wilson', avatar: 'assets/images/thumbs/avatar-img6.png', rollNo: '09', class: 'Class 6 (A)', amount: 800.00, paid: 800.00, due: 0, date: '01 May 2025', status: 'Paid' },
            { id: 7, admissionNo: 'AD52371', name: 'Darlene Robertson', avatar: 'assets/images/thumbs/avatar-img7.png', rollNo: '11', class: 'Class 7 (A)', amount: 950.00, paid: 400.00, due: 550.00, date: '28 Apr 2025', status: 'Partial' },
            { id: 8, admissionNo: 'AD52372', name: 'Wade Warren', avatar: 'assets/images/thumbs/avatar-img8.png', rollNo: '18', class: 'Class 8 (B)', amount: 880.00, paid: 880.00, due: 0, date: '25 Apr 2025', status: 'Paid' },
            { id: 9, admissionNo: 'AD52373', name: 'Esther Howard', avatar: 'assets/images/thumbs/avatar-img9.png', rollNo: '13', class: 'Class 9 (C)', amount: 990.00, paid: 0, due: 990.00, date: '22 Apr 2025', status: 'Unpaid' },
            { id: 10, admissionNo: 'AD52374', name: 'Guy Hawkins', avatar: 'assets/images/thumbs/avatar-img10.png', rollNo: '15', class: 'Class 10 (A)', amount: 1020.00, paid: 1020.00, due: 0, date: '20 Apr 2025', status: 'Paid' },
            { id: 11, admissionNo: 'AD52375', name: 'Robert Fox', avatar: 'assets/images/thumbs/avatar-img1.png', rollNo: '24', class: 'Class 12 (B)', amount: 1200.00, paid: 600.00, due: 600.00, date: '18 Apr 2025', status: 'Partial' },
            { id: 12, admissionNo: 'AD52376', name: 'Jacob Jones', avatar: 'assets/images/thumbs/avatar-img2.png', rollNo: '05', class: 'Class 8 (C)', amount: 1100.00, paid: 1100.00, due: 0, date: '15 Apr 2025', status: 'Paid' }
        ]);

        const getStatusClass = (status) => {
            switch (status) {
                case 'Paid':
                    return 'bg-success-100 text-success-600';
                case 'Partial':
                    return 'bg-warning-100 text-warning-600';
                case 'Unpaid':
                    return 'bg-danger-100 text-danger-600';
                default:
                    return 'bg-secondary-100 text-secondary-600';
            }
        };

        const toggleAll = () => {
            if (selectAll.value) {
                selectedItems.value = students.value.map(s => s.id);
            } else {
                selectedItems.value = [];
            }
        };

        const viewDetails = (student) => {
            emit('viewDetails', student);
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
            students,
            selectAll,
            selectedItems,
            toggleAll,
            getStatusClass,
            viewDetails
        };
    }
}
</script>
