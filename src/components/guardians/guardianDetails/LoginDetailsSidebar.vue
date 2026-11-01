<template>
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active-translate-0': isOpen }">
        <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
            <h5 class="text-lg mb-0">Login Details</h5>
            <button type="button" @click="$emit('close')" class="close-my-sidebar text-danger-600 text-lg d-flex">
                <i class="ri-close-large-line"></i>
            </button>
        </div>
        <form action="#" class="d-flex flex-column">
            <div class="p-20">
                <div class="d-flex align-items-center gap-20">
                    <figure class="w-72-px h-72-px rounded-circle overflow-hidden mb-0">
                        <img :src="guardian.image" alt="guardian Image" class="w-100 h-100 object-fit-cover">
                    </figure>
                    <div class="flex-grow-1">
                        <h2 class="text-xl text-primary-light mb-4">{{ guardian.name }}</h2>
                        <p class="mb-0">ID: <span class="text-primary-light fw-semibold">{{ guardian.id }}</span> </p>
                    </div>
                </div>
            </div>
            <div class="table-bottom-info-none">
                <table class="table bordered-table mb-0 table-heading-dark-mode w-100 data-table" id="loginDetailsTable">
                    <thead>
                        <tr>
                            <th scope="col" class="text-start">User Type</th>
                            <th scope="col" class="text-start">Email</th>
                            <th scope="col" class="text-start">Password</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="text-start">Guardian</td>
                            <td class="text-start">{{ guardian.email }}</td>
                            <td class="text-start">{{ guardian.password }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </form>
    </div>
    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active visibility-visible opacity-1': isOpen }" @click="$emit('close')"></div>
</template>

<script>
export default {
    name: "LoginDetailsSidebar",
    props: {
        isOpen: {
            type: Boolean,
            default: false
        },
        guardian: {
            type: Object,
            required: true
        }
    },
    emits: ['close']
}
</script>
