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
                                <th scope="col">Exam Name</th>
                                <th scope="col">Exam Date</th>
                                <th scope="col">Start Time</th>
                                <th scope="col">End Time</th>
                                <th scope="col">Status</th>
                                <th scope="col">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(exam, index) in exams" :key="index">
                                <td>
                                    <div class="form-check style-check d-flex align-items-center">
                                        <input class="form-check-input" type="checkbox" v-model="selectedItems"
                                            :value="exam.id">
                                        <label class="form-check-label">{{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}</label>
                                    </div>
                                </td>
                                <td>{{ exam.name }}</td>
                                <td>{{ exam.date }}</td>
                                <td>{{ exam.startTime }}</td>
                                <td>{{ exam.endTime }}</td>
                                <td>
                                    <span :class="getStatusClass(exam.status)" class="px-24 py-4 radius-4 fw-medium text-sm">
                                        {{ exam.status }}
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
                                                    @click="$emit('openEditSidebar', exam)">
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
                    <h6 class="text-lg fw-semibold text-primary-light mb-0">Are your sure you want to Delete this exam?</h6>
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

export default {
    name: "ExamTable",
    emits: ['openEditSidebar'],
    setup() {
        const selectAll = ref(false);
        const selectedItems = ref([]);

        const exams = ref([
            { id: 1, name: 'Monthly Test', date: '05 Jun 2015', startTime: '10:00 AM', endTime: '01:00 PM', status: 'Active' },
            { id: 2, name: 'Weekly Assessment', date: '10 Jun 2015', startTime: '09:00 AM', endTime: '11:00 AM', status: 'Pending' },
            { id: 3, name: 'Mid Term Exam', date: '15 Jun 2015', startTime: '12:00 PM', endTime: '03:00 PM', status: 'Scheduled' },
            { id: 4, name: 'Final Term Exam', date: '22 Jun 2015', startTime: '10:00 AM', endTime: '01:30 PM', status: 'Closed' },
            { id: 5, name: 'Mock Test', date: '28 Jun 2015', startTime: '11:00 AM', endTime: '01:00 PM', status: 'Active' },
            { id: 6, name: 'Quiz Exam', date: '03 Jul 2015', startTime: '02:00 PM', endTime: '02:30 PM', status: 'Pending' },
            { id: 7, name: 'Group Discussion', date: '08 Jul 2015', startTime: '03:30 PM', endTime: '05:00 PM', status: 'Scheduled' },
            { id: 8, name: 'Presentation', date: '12 Jul 2015', startTime: '09:30 AM', endTime: '10:30 AM', status: 'Active' },
            { id: 9, name: 'Lab Performance', date: '15 Jul 2015', startTime: '01:00 PM', endTime: '03:00 PM', status: 'Closed' },
            { id: 10, name: 'Project Demo', date: '20 Jul 2015', startTime: '02:00 PM', endTime: '04:00 PM', status: 'Upcoming' },
            { id: 11, name: 'Viva Exam', date: '25 Jul 2015', startTime: '11:00 AM', endTime: '12:00 PM', status: 'Active' },
            { id: 12, name: 'Science Fair', date: '30 Jul 2015', startTime: '09:00 AM', endTime: '05:00 PM', status: 'Scheduled' },
        ]);

        const getStatusClass = (status) => {
             switch (status) {
                case 'Active':
                    return 'bg-success-100 text-success-600';
                case 'Pending':
                    return 'bg-warning-100 text-warning-600';
                case 'Scheduled':
                     return 'bg-info-100 text-info-600';
                 case 'Closed':
                     return 'bg-danger-100 text-danger-600';
                 case 'Upcoming':
                     return 'bg-info-100 text-info-600';
                default:
                    return 'bg-secondary-100 text-secondary-600';
            }
        };

        const toggleAll = () => {
            if (selectAll.value) {
                selectedItems.value = exams.value.map(e => e.id);
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
                        columnDefs: [{ orderable: false, targets: [6] }] // Disable sorting on action column
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
            exams,
            selectAll,
            selectedItems,
            toggleAll,
            getStatusClass
        };
    }
}
</script>
