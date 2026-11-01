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
                            <option value="10">10</option>
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
                                <th scope="col">Course Code</th>
                                <th scope="col">Course Title</th>
                                <th scope="col">Credit Units</th>
                                <th scope="col">Department</th>
                                <th scope="col">Assigned Lecturer</th>
                                <th scope="col">Status</th>
                                <th scope="col">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(subject, index) in subjects" :key="index">
                                <td>
                                    <div class="form-check style-check d-flex align-items-center">
                                        <input class="form-check-input" type="checkbox" v-model="selectedItems"
                                            :value="subject.id">
                                        <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                                    </div>
                                </td>
                                <td><span class="text-primary-600 fw-semibold">{{ subject.code }}</span></td>
                                <td><span class="fw-medium">{{ subject.name }}</span></td>
                                <td><span class="badge bg-neutral-100 text-neutral-800 px-10 py-4 radius-4">{{ subject.creditUnits }} Units</span></td>
                                <td>{{ subject.department }}</td>
                                <td><span class="text-secondary-light">{{ subject.lecturerName || 'Faculty Board' }}</span></td>
                                <td>
                                    <span :class="subject.status === 'Active' ? 'bg-success-100 text-success-600' : 'bg-danger-100 text-danger-600'" class="px-24 py-4 radius-4 fw-medium text-sm">
                                        {{ subject.status }}
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
                                                    @click="$emit('openEditSidebar', subject)">
                                                    <i class="ri-edit-2-line"></i>
                                                    Edit
                                                </button>
                                            </li>
                                            <li>
                                                <button
                                                    class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                                                    type="button" data-bs-toggle="modal"
                                                    data-bs-target="#exampleModalDelete">
                                                    <i class="ri-delete-bin-6-line"></i>
                                                    Delete
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

    <!-- Modal Delete Event start -->
    <div class="modal fade" id="exampleModalDelete" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-sm modal-dialog modal-dialog-centered max-w-340-px">
            <div class="modal-content radius-16 bg-base">
                <div class="modal-body pt-32 px-36 pb-24 text-center">
                    <span class="mb-16 fs-1 line-height-1 text-danger">
                        <iconify-icon icon="fluent:delete-24-regular" class="menu-icon"></iconify-icon>
                    </span>
                    <h6 class="text-lg fw-semibold text-primary-light mb-0">Are your sure you want to Delete this subject?</h6>
                    <div class="d-flex align-items-center justify-content-center gap-3 mt-24">
                        <button type="reset" class="flex-grow-1 border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-24 py-11 radius-8" data-bs-dismiss="modal">
                            Cancel
                        </button>
                        <button type="button" class="flex-grow-1 btn btn-primary-600 border border-primary-600 text-md px-16 py-12 radius-8" data-bs-dismiss="modal">
                            Yes, Delete
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Modal Delete Event end -->
</template>

<script>
import { ref, onMounted, nextTick } from 'vue';
import { coursesApi } from '@/services/api.js';

export default {
    name: "SubjectTable",
    emits: ['openEditSidebar'],
    setup() {
        const selectAll = ref(false);
        const selectedItems = ref([]);
        const isLoading = ref(false);

        const defaultCourses = [
            { id: 1, name: 'Structured Programming & Algorithms', code: 'CSC 301', creditUnits: 3, department: 'Department of Computer Science', lecturerName: 'Prof. Alex Finch', status: 'Active' },
            { id: 2, name: 'Operating Systems & Concurrency', code: 'CSC 303', creditUnits: 3, department: 'Department of Computer Science', lecturerName: 'Dr. Angela Davis', status: 'Active' },
            { id: 3, name: 'Software Verification & QA', code: 'SEN 305', creditUnits: 3, department: 'Department of Software Engineering', lecturerName: 'Engr. Marcus Vance', status: 'Active' },
            { id: 4, name: 'Engineering Mathematics & Stats', code: 'ENG 203', creditUnits: 2, department: 'Department of Mathematical Sciences', lecturerName: 'Dr. Angela Davis', status: 'Active' },
        ];

        const subjects = ref(defaultCourses);

        const toggleAll = () => {
            if (selectAll.value) {
                selectedItems.value = subjects.value.map(s => s.id);
            } else {
                selectedItems.value = [];
            }
        };

        const mapApiCourse = (c) => ({
            id: c.id,
            name: c.title,
            code: c.code,
            creditUnits: c.creditUnits || 3,
            department: c.department || 'Department of Computer Science',
            lecturerName: c.lecturerName || 'Faculty Board',
            status: 'Active'
        });

        const initDataTable = () => {
            if (typeof $ !== 'undefined' && $.fn.DataTable) {
                 $('.data-table').each(function () {
                    const $table = $(this);
                     
                    if ($table.hasClass('dataTable-initialized')) return;

                    let tableInstance = $table.DataTable({
                        pageLength: 10,
                        columnDefs: [{ orderable: false, targets: [0, 6] }]
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
        };

        onMounted(async () => {
            isLoading.value = true;
            try {
                const records = await coursesApi.listCourses();
                if (Array.isArray(records) && records.length > 0) {
                    subjects.value = records.map(mapApiCourse);
                }
            } catch (err) {
                console.warn("Using fallback course catalog:", err);
            } finally {
                isLoading.value = false;
                await nextTick();
                initDataTable();
            }
        });

        return {
            subjects,
            selectAll,
            selectedItems,
            isLoading,
            toggleAll
        };
    }
}
</script>
