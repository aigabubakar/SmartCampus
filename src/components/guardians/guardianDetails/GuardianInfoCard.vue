<template>
    <div class="card h-100">
        <div class="card-body p-24">
            <div class="d-flex gap-32 flex-md-row flex-column">
                <div class="max-w-300-px w-100 text-center">
                    <figure class="mb-24 w-120-px h-120-px mx-auto rounded-circle overflow-hidden">
                        <img :src="guardian.image" alt="guardian Image" class="w-100 h-100 object-fit-cover">
                    </figure>
                    <h2 class="h6 text-primary-light mb-8 fw-semibold">{{ guardian.name }}</h2>
                    <p class="mb-0">ID: <span class="text-primary-600 fw-semibold"> {{ guardian.id }}</span>
                    </p>
                    <div class="mt-20 d-flex gap-16 w-100">
                        <router-link to="/edit-guardian"
                            class="btn btn-primary-600 border fw-medium border-primary-600 text-md d-flex justify-content-center align-items-center gap-8 flex-grow-1 px-12 py-8 radius-8">
                            <span class="d-flex text-lg">
                                <i class="ri-edit-line"></i>
                            </span>
                            Edit
                        </router-link>
                    </div>
                </div>
                <div class="">
                    <span class="h-100 w-1-px bg-neutral-200"></span>
                </div>
                <div class="flex-grow-1">
                    <div class="pb-16 border-bottom d-flex align-items-center justify-content-between gap-20">
                        <h3 class="h6 text-primary-light text-lg mb-0 fw-semibold">Personal Info</h3>
                    </div>
                    <div class="mt-16 d-flex flex-column gap-20">
                        <div class="d-flex gap-4">
                            <span class="fw-semibold text-sm text-primary-light w-110-px">Guardians Type</span>
                            <span class="fw-normal text-sm text-secondary-light">: {{ guardian.type }}</span>
                        </div>
                        <div class="d-flex gap-4">
                            <span class="fw-semibold text-sm text-primary-light w-110-px">Phone Number</span>
                            <span class="fw-normal text-sm text-secondary-light">: {{ guardian.phone }}</span>
                        </div>
                        <div class="d-flex gap-4">
                            <span class="fw-semibold text-sm text-primary-light w-110-px">Occupation</span>
                            <span class="fw-normal text-sm text-secondary-light">: {{ guardian.occupation }}</span>
                        </div>
                        <div class="d-flex gap-4">
                            <span class="fw-semibold text-sm text-primary-light w-110-px">Address</span>
                            <span class="fw-normal text-sm text-secondary-light">: {{ guardian.address }}</span>
                        </div>
                        <div class="d-flex gap-4">
                            <span class="fw-semibold text-sm text-primary-light w-110-px">Join Date</span>
                            <span class="fw-normal text-sm text-secondary-light">: {{ guardian.joinDate }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "GuardianInfoCard",
    props: {
        guardian: {
            type: Object,
            required: true
        }
    }
}
</script>
