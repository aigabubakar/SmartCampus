<template>
  <div class="card radius-12 border-0">
    <div
      class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-12 px-20 border-bottom border-neutral-200">
      <h6 class="mb-2 fw-bold text-lg">Top Instructor</h6>
      <div class="dropdown">
        <button type="button" data-bs-toggle="dropdown" aria-expanded="false">
          <iconify-icon icon="entypo:dots-three-vertical" class="icon text-secondary-light"></iconify-icon>
        </button>
        <ul class="dropdown-menu p-12 border bg-base shadow">
          <li>
            <button type="button"
              class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10"
              data-bs-toggle="modal" data-bs-target="#exampleModalView">
              <iconify-icon icon="hugeicons:view" class="icon text-lg line-height-1"></iconify-icon>
              View
            </button>
          </li>
          <li>
            <button type="button"
              class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10"
              data-bs-toggle="modal" data-bs-target="#exampleModalEdit">
              <iconify-icon icon="lucide:edit" class="icon text-lg line-height-1"></iconify-icon>
              Edit
            </button>
          </li>
          <li>
            <button type="button"
              class="delete-item dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-danger-100 text-hover-danger-600 d-flex align-items-center gap-10"
              data-bs-toggle="modal" data-bs-target="#exampleModalDelete">
              <iconify-icon icon="fluent:delete-24-regular" class="icon text-lg line-height-1"></iconify-icon>
              Delete
            </button>
          </li>
        </ul>
      </div>
    </div>
    <div class="card-body d-flex flex-column gap-20">
      <div v-for="(instructor, index) in instructors" :key="index" class="d-flex align-items-center justify-content-between gap-3">
        <div class="d-flex align-items-center">
          <img :src="instructor.image" alt="Image"
            class="w-40-px h-40-px radius-4 flex-shrink-0 me-12 overflow-hidden">
          <div class="flex-grow-1">
            <h6 class="text-md mb-0 fw-medium">{{ instructor.name }}</h6>
            <span class="text-sm text-secondary-light fw-medium">Agent ID: {{ instructor.id }}</span>
          </div>
        </div>
        <div class="">
          <div class="d-flex align-items-center gap-6 mb-1">
            <span v-for="i in 5" :key="i" class="text-lg text-warning-600 d-flex line-height-1"><i
                class="ri-star-fill"></i></span>
          </div>
          <span class="text-primary-light text-sm d-block text-end">{{ instructor.reviews }} Reviews</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopInstructor",
  setup() {
    const instructors = [
      { name: "Dianne Russell", id: "36254", image: "/assets/images/users/user1.png", reviews: 25 },
      { name: "Wade Warren", id: "36254", image: "/assets/images/users/user2.png", reviews: 25 },
      { name: "Albert Flores", id: "36254", image: "/assets/images/users/user3.png", reviews: 25 },
      { name: "Bessie Cooper", id: "36254", image: "/assets/images/users/user4.png", reviews: 25 },
      { name: "Arlene McCoy", id: "36254", image: "/assets/images/users/user5.png", reviews: 25 },
    ];

    return {
      instructors
    };
  }
}
</script>
