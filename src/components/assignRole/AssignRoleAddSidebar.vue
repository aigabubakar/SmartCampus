<template>
    <!-- Add sidebar start -->
    <div
        class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300 active-translate-0">
        <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
            <h5 class="text-lg mb-0">Assign Role</h5>
            <button type="button" class="close-my-sidebar text-danger-600 text-lg d-flex">
                <i class="ri-close-large-line"></i>
            </button>
        </div>
        <form action="#" class="d-flex flex-column p-20">
            <div class="row g-3">
                <div class="col-sm-12">
                    <div class="">
                        <label for="roleName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Role Name
                        </label>
                        <input type="text" class="form-control" id="roleName" placeholder="Enter Role Name">
                    </div>
                </div>
                <div class="col-sm-12">
                    <div class="">
                        <label for="featuresSelect" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Features
                        </label>
                        <select id="featuresSelect" class="form-control form-select">
                            <option value="Select a Class" disabled>Select a Class</option>
                            <option value="User Management">User Management</option>
                            <option value="System Settings">System Settings</option>
                            <option value="Notifications">Notifications</option>
                            <option value="Payroll">Payroll</option>
                        </select>
                    </div>
                </div>
                <div class="col-12">
                    <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
                        <button type="reset"
                            class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8">
                            Cancel
                        </button>
                        <button type="submit"
                            class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
                            Save
                        </button>
                    </div>
                </div>
            </div>
        </form>
    </div>
    <!-- Add sidebar end -->
</template>

<script>
export default {
    name: "AssignRoleAddSidebar"
}
</script>
