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

                            <form action="#" class="p-16">
                                <div class="row g-3">
                                    <div class="col-12">
                                        <label for="subject"
                                            class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Gender</label>
                                        <select id="subject" class="form-control form-select">
                                            <option value="Select">Select Subject</option>
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
                                            <option value="Select">Select Status</option>
                                            <option value="Active">Active</option>
                                            <option value="Inactive">Inactive</option>
                                        </select>
                                    </div>
                                    <div class="col-6">
                                        <button type="reset" class="btn btn-danger-200 text-danger-600 w-100">Reset</button>
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
                <div class="table-responsive">
                    <table class="table bordered-table mb-0 data-table" id="dataTable" data-page-length='10'>
                        <thead>
                            <tr>
                                <th scope="col">
                                    <div class="form-check style-check d-flex align-items-center">
                                        <input class="form-check-input" type="checkbox">
                                        <label class="form-check-label">S.L</label>
                                    </div>
                                </th>
                                <th scope="col">ID</th>
                                <th scope="col">Name</th>
                                <th scope="col">Child</th>
                                <th scope="col">Email</th>
                                <th scope="col">Phone Number</th>
                                <th scope="col">Join Date</th>
                                <th scope="col">Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(guardian, index) in guardians" :key="index">
                                <td>
                                    <div class="form-check style-check d-flex align-items-center">
                                        <input class="form-check-input" type="checkbox">
                                        <label class="form-check-label">{{ index + 1 }}</label>
                                    </div>
                                </td>
                                <td><span class="text-primary-600">{{ guardian.id }}</span></td>
                                <td>
                                    <div class="d-flex align-items-center">
                                        <img :src="guardian.avatar" :alt="guardian.name"
                                            class="flex-shrink-0 me-12 radius-8">
                                        <div>
                                            <h6 class="text-md mb-0 fw-medium flex-grow-1 text-secondary-light">{{
                                                guardian.name }}</h6>
                                        </div>
                                    </div>
                                </td>
                                <td>
                                    <div class="d-flex align-items-center">
                                        <img :src="guardian.childAvatar" :alt="guardian.childName"
                                            class="flex-shrink-0 me-12 radius-8">
                                        <div>
                                            <h6 class="text-md mb-0 fw-medium flex-grow-1 text-secondary-light">{{
                                                guardian.childName }}</h6>
                                            <span class="text-secondary-light text-sm">Class: {{ guardian.childClass
                                                }}</span>
                                        </div>
                                    </div>
                                </td>
                                <td>{{ guardian.email }}</td>
                                <td>{{ guardian.phone }}</td>
                                <td>{{ guardian.joinDate }}</td>
                                <td>
                                    <div class="dropdown">
                                        <button type="button" class="text-primary-light text-xl"
                                            data-bs-toggle="dropdown" aria-expanded="false">
                                            <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                                        </button>
                                        <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                                            <li><router-link to="/guardian-details"
                                                    class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"><i
                                                        class="ri-user-3-line"></i>View Guardian</router-link></li>
                                            <li><router-link to="/edit-guardian"
                                                    class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"><i
                                                        class="ri-edit-2-line"></i>Edit</router-link></li>
                                            <li><router-link to="/login"
                                                    class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"><i
                                                        class="ri-login-box-line"></i>Login</router-link></li>
                                            <li><button
                                                    class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                                                    data-bs-toggle="modal" data-bs-target="#exampleModalDelete"><i
                                                        class="ri-delete-bin-6-line"></i>Delete</button></li>
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
                    <h6 class="text-lg fw-semibold text-primary-light mb-0">Are your sure you want to Delete this guardian?</h6>
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
import { onMounted, ref } from 'vue';

// Import images (assuming they are in src/assets/images)
import teacherAvatar1 from '@/assets/images/thumbs/teacher-avatar-img1.png';
import teacherAvatar2 from '@/assets/images/thumbs/teacher-avatar-img2.png';
import teacherAvatar3 from '@/assets/images/thumbs/teacher-avatar-img3.png';
import teacherAvatar4 from '@/assets/images/thumbs/teacher-avatar-img4.png';
import teacherAvatar5 from '@/assets/images/thumbs/teacher-avatar-img5.png';
import teacherAvatar6 from '@/assets/images/thumbs/teacher-avatar-img6.png';
import teacherAvatar7 from '@/assets/images/thumbs/teacher-avatar-img7.png';
import teacherAvatar8 from '@/assets/images/thumbs/teacher-avatar-img8.png';

import studentAvatar1 from '@/assets/images/thumbs/avatar-img1.png';
import studentAvatar2 from '@/assets/images/thumbs/avatar-img2.png';
import studentAvatar3 from '@/assets/images/thumbs/avatar-img3.png';
import studentAvatar4 from '@/assets/images/thumbs/avatar-img4.png';
import studentAvatar5 from '@/assets/images/thumbs/avatar-img5.png';
import studentAvatar6 from '@/assets/images/thumbs/avatar-img6.png';
import studentAvatar7 from '@/assets/images/thumbs/avatar-img7.png';
import studentAvatar8 from '@/assets/images/thumbs/avatar-img8.png';

export default {
    name: "GuardianTable",
    setup() {
        const guardians = ref([
            { id: 'AD52365', name: 'Marvin McKinney', avatar: teacherAvatar1, childName: 'Darlene Robertson', childAvatar: studentAvatar1, childClass: '1 (A)', email: 'chinthaka@hotmail.com', phone: '209.555.0104', joinDate: '05 May 2012' },
            { id: 'AD65412', name: 'Esther Howard', avatar: teacherAvatar2, childName: 'Jane Cooper', childAvatar: studentAvatar2, childClass: '2 (B)', email: 'esther@example.com', phone: '305.442.0899', joinDate: '10 Feb 2014' },
            { id: 'AD76548', name: 'Cody Fisher', avatar: teacherAvatar3, childName: 'Robert Fox', childAvatar: studentAvatar3, childClass: '3 (A)', email: 'codyf@example.com', phone: '312.900.0981', joinDate: '08 Mar 2016' },
            { id: 'AD33221', name: 'Jenny Wilson', avatar: teacherAvatar4, childName: 'Albert Flores', childAvatar: studentAvatar4, childClass: '4 (B)', email: 'jenny@example.com', phone: '404.788.1120', joinDate: '15 Aug 2017' },
            { id: 'AD77231', name: 'Theresa Webb', avatar: teacherAvatar5, childName: 'Leslie Alexander', childAvatar: studentAvatar5, childClass: '5 (A)', email: 'theresa.webb@example.com', phone: '213.987.7770', joinDate: '22 Sep 2018' },
            { id: 'AD52366', name: 'John Smith', avatar: teacherAvatar2, childName: 'Kathryn Murphy', childAvatar: studentAvatar2, childClass: '2 (B)', email: 'kathryn.murphy@example.com', phone: '208.555.1122', joinDate: '12 Jan 2013' },
            { id: 'AD52367', name: 'Theresa Webb', avatar: teacherAvatar3, childName: 'Guy Hawkins', childAvatar: studentAvatar3, childClass: '3 (C)', email: 'guy.hawkins@example.com', phone: '203.555.2145', joinDate: '27 Mar 2014' },
            { id: 'AD52368', name: 'Courtney Henry', avatar: teacherAvatar4, childName: 'Eleanor Pena', childAvatar: studentAvatar4, childClass: '4 (A)', email: 'eleanor.pena@example.com', phone: '210.555.1098', joinDate: '08 Sep 2014' },
            { id: 'AD52369', name: 'Albert Flores', avatar: teacherAvatar5, childName: 'Jenny Wilson', childAvatar: studentAvatar5, childClass: '5 (B)', email: 'jenny.wilson@example.com', phone: '212.555.3223', joinDate: '11 Nov 2015' },
            { id: 'AD52370', name: 'Jerome Bell', avatar: teacherAvatar6, childName: 'Esther Howard', childAvatar: studentAvatar6, childClass: '6 (A)', email: 'esther.howard@example.com', phone: '210.555.7766', joinDate: '22 Feb 2016' },
            { id: 'AD52371', name: 'Devon Lane', avatar: teacherAvatar7, childName: 'Robert Fox', childAvatar: studentAvatar7, childClass: '7 (C)', email: 'robert.fox@example.com', phone: '202.555.8974', joinDate: '10 Jul 2017' },
            { id: 'AD52372', name: 'Floyd Miles', avatar: teacherAvatar8, childName: 'Leslie Alexander', childAvatar: studentAvatar8, childClass: '8 (A)', email: 'leslie.alexander@example.com', phone: '205.555.6742', joinDate: '21 Oct 2018' },
        ]);

        onMounted(() => {
            // Data Table initialization
            if (typeof $ !== 'undefined') {
                $('.data-table').each(function () {
                    const $table = $(this);
                    
                    if ($table.hasClass('dataTable-initialized')) return;

                    let tableInstance;
                    if ($.fn.DataTable) {
                        tableInstance = $table.DataTable({
                            pageLength: 10,
                            columnDefs: [{ orderable: false, targets: [7] }] // Disable sorting action columns
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
        });

        return {
            guardians,
        };
    }
}
</script>
