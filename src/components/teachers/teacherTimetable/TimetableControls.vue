<template>
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
                <input type="text" class="item-search-input dt-input bg-transparent radius-4" name="search"
                    placeholder="Search...">
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
    </div>
</template>

<script>
export default {
    name: "TimetableControls"
}
</script>
