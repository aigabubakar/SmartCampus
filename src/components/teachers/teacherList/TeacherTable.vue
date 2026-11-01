<template>
    <div class="card h-100">
        <div class="card-body p-0 dataTable-wrapper">

            <div
                class="d-flex align-items-center justify-content-between flex-wrap gap-16 px-20 py-12 border-bottom border-neutral-200">
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
                            <div
                                class="d-flex align-items-center justify-content-between border-bottom py-8 px-16">
                                <span class="fw-semibold text-lg text-primary-light">Filter</span>
                                <button type="button">
                                    <i class="ri-close-large-line"></i>
                                </button>
                            </div>

                            <form action="#" class="p-16">
                                <div class="row g-3">
                                    <div class="col-12">
                                        <label for="subject"
                                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Gender</label>
                                        <select id="subject" class="form-control form-select">
                                            <option value="Select" disabled selected>Select Subject</option>
                                            <option value="Match">Match</option>
                                            <option value="English">English</option>
                                            <option value="Bangla">Bangla</option>
                                            <option value="Economics">Economics</option>
                                            <option value="Physics">Physics</option>
                                        </select>
                                    </div>
                                    <div class="col-12">
                                        <label for="status"
                                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
                                        <select id="status" class="form-control form-select">
                                            <option value="Select" disabled selected>Select Status</option>
                                            <option value="Active">Active</option>
                                            <option value="Inactive">Inactive</option>
                                        </select>
                                    </div>
                                    <div class="col-6">
                                        <button type="reset"
                                            class="btn btn-danger-200 text-danger-600 w-100">Reset</button>
                                    </div>
                                    <div class="col-6">
                                        <button type="submit" class="btn btn-primary-600 w-100">Apply</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
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
                <table class="table bordered-table mb-0 data-table" id="dataTable" data-page-length='10'>
                    <thead>
                        <tr>
                            <th scope="col">
                                <div class="form-check style-check d-flex align-items-center">
                                    <input class="form-check-input" type="checkbox" id="selectAll">
                                    <label class="form-check-label" for="selectAll">
                                        S.L
                                    </label>
                                </div>
                            </th>
                            <th scope="col">Staff ID</th>
                            <th scope="col">Faculty Member</th>
                            <th scope="col">Department & Specialization</th>
                            <th scope="col">Assigned Courses</th>
                            <th scope="col">Official Email</th>
                            <th scope="col">Office Location</th>
                            <th scope="col">Qualification</th>
                            <th scope="col">Status</th>
                            <th scope="col">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(teacher, index) in teachers" :key="index">
                            <td>
                                <div class="form-check style-check d-flex align-items-center">
                                    <input class="form-check-input" type="checkbox" :id="'check' + index">
                                    <label class="form-check-label" :for="'check' + index">
                                        {{ index + 1 < 10 ? '0' + (index + 1) : index + 1 }}
                                    </label>
                                </div>
                            </td>
                            <td><span class="text-primary-600">{{ teacher.id }}</span></td>
                            <td>
                                <div class="d-flex align-items-center">
                                    <img :src="teacher.image"
                                        alt="Teacher Image" class="flex-shrink-0 me-12 radius-8">
                                    <div class="">
                                        <h6 class="text-md mb-0 fw-medium flex-grow-1">{{ teacher.name }}</h6>
                                    </div>
                                </div>
                            </td>
                            <td>{{ teacher.subject }}</td>
                            <td>{{ teacher.class }}</td>
                            <td>{{ teacher.email }}</td>
                            <td>{{ teacher.phone }}</td>
                            <td>{{ teacher.joinDate }}</td>
                            <td>
                                <span :class="getStatusClass(teacher.status)">{{ teacher.status }}</span>
                            </td>
                            <td>
                                <div class="btn-group">
                                    <button type="button" class="text-primary-light text-xl"
                                        data-bs-toggle="dropdown" data-bs-display="static"
                                        aria-expanded="false">
                                        <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                                    </button>
                                    <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                                        <li>
                                            <router-link to="/teacher-details"
                                                class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6">
                                                <i class="ri-user-3-line"></i>
                                                View Faculty Profile
                                            </router-link>
                                        </li>
                                        <li>
                                            <router-link to="/edit-teacher"
                                                class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6">
                                                <i class="ri-edit-2-line"></i>
                                                Edit
                                            </router-link>
                                        </li>
                                        <li>
                                            <button
                                                class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                                                type="button">
                                                <i class="ri-error-warning-line"></i>
                                                Inactive
                                            </button>
                                        </li>
                                        <li>
                                            <button class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6" data-bs-toggle="modal" data-bs-target="#exampleModalDelete"><i class="ri-delete-bin-6-line"></i>Delete</button>
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
</template>

<script>
import { onMounted, ref, nextTick } from 'vue';
import { lecturersApi } from '@/services/api.js';

// Import images
import img1 from '@/assets/images/thumbs/teacher-avatar-img1.png';
import img2 from '@/assets/images/thumbs/teacher-avatar-img2.png';
import img3 from '@/assets/images/thumbs/teacher-avatar-img3.png';
import img4 from '@/assets/images/thumbs/teacher-avatar-img4.png';
import img5 from '@/assets/images/thumbs/teacher-avatar-img5.png';
import img6 from '@/assets/images/thumbs/teacher-avatar-img6.png';
import img7 from '@/assets/images/thumbs/teacher-avatar-img7.png';
import img8 from '@/assets/images/thumbs/teacher-avatar-img8.png';
import img9 from '@/assets/images/thumbs/teacher-avatar-img9.png';

export default {
    name: "TeacherTable",
    setup() {
        const imageList = [img1, img2, img3, img4, img5, img6, img7, img8, img9];

        const defaultLecturers = [
            {
                id: 'STAFF-FAC-104',
                name: 'Prof. Alex Finch',
                image: img1,
                subject: 'Department of Computer Science',
                class: 'CSC 301, SEN 305',
                email: 'alex.finch@smartcampus.edu',
                phone: 'Science Complex, Block B, Room 201',
                joinDate: 'Ph.D. Distributed Systems',
                status: 'Active'
            },
            {
                id: 'STAFF-FAC-105',
                name: 'Dr. Angela Davis',
                image: img3,
                subject: 'Department of Computer Science',
                class: 'CSC 303, AI 401',
                email: 'angela.davis@smartcampus.edu',
                phone: 'Computing Center, Wing A, Room 104',
                joinDate: 'Ph.D. Artificial Intelligence',
                status: 'Active'
            },
            {
                id: 'STAFF-FAC-106',
                name: 'Engr. Marcus Vance',
                image: img2,
                subject: 'Department of Software Engineering',
                class: 'SEN 301, CSC 202',
                email: 'marcus.vance@smartcampus.edu',
                phone: 'Engineering Complex, Office 312',
                joinDate: 'M.Sc. Software Architecture',
                status: 'Active'
            }
        ];

        const teachers = ref(defaultLecturers);
        const isLoading = ref(false);

        const getStatusClass = (status) => {
            return status === 'Active'
                ? 'bg-success-100 text-success-600 px-24 py-4 radius-4 fw-medium text-sm'
                : 'bg-danger-100 text-danger-600 px-24 py-4 radius-4 fw-medium text-sm';
        };

        const mapApiLecturer = (l, idx) => ({
            id: l.staffId || l.userId || `STAFF-FAC-${idx + 101}`,
            name: l.rank ? `${l.rank} ${l.name}` : l.name,
            image: imageList[idx % imageList.length],
            subject: l.department || 'Department of Computer Science',
            class: (l.assignedCourses && l.assignedCourses.length > 0) ? l.assignedCourses.join(', ') : 'CSC 301, CSC 303',
            email: l.email || `${l.name.toLowerCase().replace(/[^a-z]/g, '.')}@smartcampus.edu`,
            phone: l.officeLocation || 'Science Complex, Block B, Room 201',
            joinDate: l.highestQualification || 'Ph.D.',
            status: 'Active'
        });

        const initDataTable = () => {
            if (typeof $ !== 'undefined') {
                $('.data-table').each(function () {
                    const $table = $(this);
                    if ($table.hasClass('dataTable-initialized')) return;

                    let tableInstance;
                    if ($.fn.DataTable) {
                        tableInstance = $table.DataTable({
                            pageLength: 10,
                            columnDefs: [{ orderable: false, targets: [0, 8] }]
                        });
                        $table.addClass('dataTable-initialized');
                    }

                    if (tableInstance) {
                        $table.closest('.dataTable-wrapper').find('.dt-search .dt-input').on('keyup', function () {
                            tableInstance.search(this.value).draw();
                        });

                        $table.closest('.dataTable-wrapper').find('.dt-length .dt-input').on('change', function () {
                            const value = $(this).val();
                            tableInstance.page.len(value).draw();
                        });
                    }
                });
            }
        };

        onMounted(async () => {
            isLoading.value = true;
            try {
                const records = await lecturersApi.listLecturers();
                if (Array.isArray(records) && records.length > 0) {
                    teachers.value = records.map(mapApiLecturer);
                }
            } catch (err) {
                console.warn("Using fallback academic faculty directory:", err);
            } finally {
                isLoading.value = false;
                await nextTick();
                initDataTable();
            }
        });

        return {
            teachers,
            isLoading,
            getStatusClass
        };
    }
}
</script>
