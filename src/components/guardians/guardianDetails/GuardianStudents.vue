<template>
    <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
        <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
            <h6 class="text-lg fw-semibold mb-0">Profile Detail</h6>
        </div>
        <div class="card-body p-0">
            <div class="">
                <div v-for="(student, index) in students" :key="index" class="bg-hover-neutral-50 p-20">
                    <div class="row g-4">
                        <div class="col-sm-4">
                            <div class="d-flex align-items-center gap-12">
                                <figure class="w-48-px h-48-px rounded-circle overflow-hidden mb-0">
                                    <img :src="student.image" alt="Student Image"
                                        class="flex-shrink-0 w-100 h-100 object-fit-cover">
                                </figure>
                                <div class="">
                                    <h6 class="text-md mb-2 fw-medium flex-grow-1">{{ student.name }}</h6>
                                    <span class="">{{ student.relation }}</span>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="">
                                <h6 class="text-md mb-2 fw-medium flex-grow-1">Class</h6>
                                <span class="">{{ student.phone }}</span> <!-- Note: The original HTML had phone number under Class, keeping it consistent or fix? Original label says Class but value looks like phone. I will stick to structure but maybe label is wrong in original. Let's assume the value is what we want to show. -->
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="">
                                <h6 class="text-md mb-2 fw-medium flex-grow-1">Roll No</h6>
                                <span class="">{{ student.email }}</span> <!-- Similarly, label Roll No but value is email. Keeping consistency with original HTML content structure. -->
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "GuardianStudents",
    props: {
        students: {
            type: Array,
            required: true,
            default: () => []
        }
    }
}
</script>
