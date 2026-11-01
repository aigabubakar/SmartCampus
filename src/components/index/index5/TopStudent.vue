<template>
  <div class="card radius-12 border-0 h-100">
    <div
      class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-12 px-20 border-bottom border-neutral-200">
      <h6 class="mb-2 fw-bold text-lg">Top Student</h6>
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
    <div class="card-body">
      <div class="d-flex flex-column gap-20">
        <div v-for="(student, index) in students" :key="index" class="d-flex align-items-center justify-content-between gap-10">
          <div class="d-flex align-items-center gap-12">
            <span class="w-44-px h-44-px rounded-circle d-flex justify-content-center align-items-center">
              <img :src="student.image" class="w-44-px h-44-px object-fit-cover rounded-circle" alt="Icon">
            </span>
            <div class="">
              <h6 class="text-sm mb-2">{{ student.name }}</h6>
              <span class="text-xs text-secondary-light">Class: {{ student.class }}</span>
            </div>
          </div>
          <div class="d-flex align-items-center gap-8">
            <span class="text-sm text-secondary-light">Marks</span>
            <span class="text-primary-light text-sm d-block text-end">
              <svg class="radial-progress w-44-px" viewBox="0 0 80 80">
                <circle class="incomplete stroke-8-px opacity-02" :class="student.colorClass" cx="40" cy="40" r="35"></circle>
                <circle class="complete stroke-8-px" :class="student.colorClass" cx="40" cy="40" r="35"
                        :style="{ strokeDashoffset: calculateDashOffset(student.percentage) }"></circle>
                <text class="percentage fill-black" x="50%" y="57%" transform="matrix(0, 1, -1, 0, 80, 0)">{{ student.percentage }}</text>
              </svg>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopStudent",
  setup() {
    const students = [
      { name: "Brooklyn Simmons", class: "Six", image: "/assets/images/thumbs/avatar-img1.png", percentage: 20, colorClass: "stroke-blue" },
      { name: "Floyd Miles", class: "Seven", image: "/assets/images/thumbs/avatar-img2.png", percentage: 35, colorClass: "stroke-red" },
      { name: "Courtney Henry", class: "Eight", image: "/assets/images/thumbs/avatar-img2.png", percentage: 45, colorClass: "stroke-warning" },
      { name: "Kathryn Murphy", class: "Nine", image: "/assets/images/thumbs/avatar-img4.png", percentage: 65, colorClass: "stroke-green" },
      { name: "Annette Black", class: "Ten", image: "/assets/images/thumbs/avatar-img5.png", percentage: 65, colorClass: "stroke-blue" },
    ];

    const calculateDashOffset = (percentage) => {
      const radius = 35;
      const circumference = 2 * Math.PI * radius;
      return circumference - ((percentage * circumference) / 100);
    };

    return {
      students,
      calculateDashOffset
    };
  }
}
</script>

<style scoped>
/* Add necessary CSS for radial progress specifically if not global */
/* Assuming global CSS provides basic styles, but specific SVG attributes rely on specific classes */
/* The user provided HTML has classes like stroke-blue, stroke-red */
/* I will assume these classes set the stroke color. */

.radial-progress {
    transform: rotate(-90deg);
}

.radial-progress circle {
    fill: none;
    stroke-linecap: round;
}

.radial-progress .incomplete {
    opacity: 0.2;
}

/* Define stroke colors if not present in global CSS */
.stroke-blue { stroke: #487FFF; }
.stroke-red { stroke: #EF4444; }
.stroke-warning { stroke: #FF9F29; }
.stroke-green { stroke: #00B252; }

/* Text centering */
.percentage {
    font-size: 14px;
    font-weight: bold;
    text-anchor: middle;
}
</style>
