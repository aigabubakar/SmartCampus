<template>
    <div class="card h-100">
        <div class="card-body dataTable-wrapper p-0">
            <div
                class="d-flex flex-wrap align-items-center gap-16 px-20 py-12 border-bottom border-neutral-200">
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

            <div class="p-0">
                <table class="table data-table bordered-table mb-0" id="dataTable" data-page-length='10'>
                    <thead>
                        <tr>
                            <th scope="col">
                                <div class="form-check style-check d-flex align-items-center">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">
                                        S.L
                                    </label>
                                </div>
                            </th>
                            <th scope="col">Category Name</th>
                            <th scope="col">Status</th>
                            <th scope="col" class="text-center">Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(category, index) in categories" :key="index">
                            <td>
                                <div class="form-check style-check d-flex align-items-center">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">{{ index < 9 ? `0${index + 1}` : index + 1 }}</label>
                                </div>
                            </td>
                            <td><span class="">{{ category.name }}</span></td>
                            <td><span
                                    :class="category.statusClass" class="px-24 py-4 radius-4 fw-medium text-sm">{{ category.status }}</span>
                            </td>
                            <td class="text-center">
                                <div class="btn-group">
                                    <button type="button" class="text-primary-light text-xl"
                                        data-bs-toggle="dropdown" data-bs-display="static"
                                        aria-expanded="false">
                                        <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                                    </button>
                                    <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                                        <li>
                                            <button
                                                class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                                                type="button">
                                                <i class="ri-edit-2-line"></i>Edit
                                            </button>
                                        </li>
                                        <li>
                                            <button
                                                class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6"
                                                type="button">
                                                <i class="ri-delete-bin-6-line"></i>Delete
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
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
  name: "StudentCategoryTable",
  setup() {
    const categories = ref([
        { id: 1, name: "General", status: "Active", statusClass: "bg-success-100 text-success-600" },
        { id: 2, name: "Special", status: "Inactive", statusClass: "bg-danger-100 text-danger-600" },
        { id: 3, name: "Physically Challenged", status: "Active", statusClass: "bg-success-100 text-success-600" },
        { id: 4, name: "General", status: "Inactive", statusClass: "bg-danger-100 text-danger-600" },
        { id: 5, name: "Special", status: "Active", statusClass: "bg-success-100 text-success-600" },
        { id: 6, name: "Physically Challenged", status: "Inactive", statusClass: "bg-danger-100 text-danger-600" },
        { id: 7, name: "General", status: "Active", statusClass: "bg-success-100 text-success-600" },
        { id: 8, name: "Special", status: "Inactive", statusClass: "bg-danger-100 text-danger-600" },
        { id: 9, name: "Physically Challenged", status: "Active", statusClass: "bg-success-100 text-success-600" },
        { id: 10, name: "General", status: "Inactive", statusClass: "bg-danger-100 text-danger-600" },
    ]);

    onMounted(() => {
        // Data Table
        if (typeof $ !== 'undefined') {
            $('.data-table').each(function () {
                const $table = $(this);
                // Check if already initialized to prevent double init
                if ( $.fn.DataTable && !$.fn.DataTable.isDataTable(this) ) {
                     const tableInstance = $table.DataTable({
                        pageLength: 10,
                        columnDefs: [{ orderable: false, targets: [0, 3] }] // Disable sorting on checkbox and action
                     });

                     // Handle search input (inside same wrapper)
                     $table.closest('.dataTable-wrapper').find('.dt-search .dt-input').on('keyup', function () {
                        tableInstance.search(this.value).draw();
                     });

                     // Handle page length change (inside same wrapper)
                     $table.closest('.dataTable-wrapper').find('.dt-length .dt-input').on('change', function () {
                        const value = $(this).val();
                        tableInstance.page.len(value).draw();
                     });
                }
            });
        }
    });

    return {
        categories
    };
  }
}
</script>
