<template>
  <div class="card radius-12 border-0">
    <div
      class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-12 px-20 border-bottom border-neutral-200">
      <h6 class="mb-2 fw-bold text-lg">Recent Enrolled Courses</h6>
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
    <div class="card-body p-0">
      <div class="table-responsive scroll-sm">
        <table class="table bordered-table mb-0 rounded-0 border-0">
          <thead>
            <tr>
              <th scope="col" class="bg-neutral-100 rounded-0">Invoice</th>
              <th scope="col" class="bg-neutral-100 rounded-0">Student</th>
              <th scope="col" class="bg-neutral-100 rounded-0">Courses Name</th>
              <th scope="col" class="bg-neutral-100 rounded-0">Amount</th>
              <th scope="col" class="bg-neutral-100 rounded-0">Payment By</th>
              <th scope="col" class="bg-neutral-100 rounded-0">Date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(course, index) in courses" :key="index">
              <td>{{ course.invoice }}</td>
              <td>{{ course.student }}</td>
              <td>{{ course.courseName }}</td>
              <td>{{ course.amount }}</td>
              <td>{{ course.paymentBy }}</td>
              <td>{{ course.date }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "RecentEnrolledCourses",
  setup() {
    const courses = [
      { invoice: "#829776", student: "John Doe", courseName: "Scorm drawing course", amount: "$29.00", paymentBy: "PayPal", date: "04 Feb, 2025" },
      { invoice: "#829777", student: "Emily Carter", courseName: "Advanced UI/UX Design", amount: "$49.00", paymentBy: "Stripe", date: "06 Feb, 2025" },
      { invoice: "#829778", student: "Michael Smith", courseName: "Full-Stack Development", amount: "$79.00", paymentBy: "MasterCard", date: "08 Feb, 2025" },
      { invoice: "#829779", student: "Sarah Johnson", courseName: "Digital Marketing Pro", amount: "$39.00", paymentBy: "Visa", date: "10 Feb, 2025" },
      { invoice: "#829780", student: "David Wilson", courseName: "Laravel API Development", amount: "$59.00", paymentBy: "PayPal", date: "12 Feb, 2025" },
    ];

    return {
      courses
    };
  }
}
</script>
