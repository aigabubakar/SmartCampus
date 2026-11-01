<template>
  <div class="card radius-12 border-0 shadow-1 h-100">
    <div class="d-flex align-items-center flex-wrap gap-2 justify-content-between py-16 px-20 border-bottom border-neutral-200">
      <div>
        <h6 class="mb-0 fw-bold text-lg text-neutral-900">Dean's Honour Roll</h6>
        <span class="text-secondary-light text-xs">Top Valedictorian Candidates & First Class Scholars</span>
      </div>
      <span class="badge bg-primary-50 text-primary-600 border border-primary-subtle text-xs px-8 py-4 radius-6 fw-semibold">
        CGPA &gt; 4.85
      </span>
    </div>

    <div class="card-body p-20">
      <div class="d-flex flex-column gap-20">
        <div v-for="(student, index) in students" :key="index"
          class="d-flex align-items-center justify-content-between gap-12 pb-12 border-bottom border-neutral-100">
          <div class="d-flex align-items-center gap-12">
            <span class="w-40-px h-40-px rounded-circle bg-primary-50 text-primary-700 fw-bold d-flex justify-content-center align-items-center text-xs flex-shrink-0">
              #{{ index + 1 }}
            </span>
            <div>
              <h6 class="text-sm fw-bold text-neutral-900 mb-2">{{ student.name }}</h6>
              <span class="text-xs text-secondary-light">{{ student.program }} • {{ student.level }}</span>
            </div>
          </div>
          <div class="text-end">
            <span class="badge bg-success-subtle text-success-800 fw-bold text-xs px-8 py-4 radius-6 d-inline-block">
              {{ student.cgpa }}
            </span>
            <span class="text-xxs text-secondary-light d-block mt-2">Cumulative GPA</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TopStudent",
  data() {
    return {
      students: [
        {
          name: "Amina Bello",
          program: "B.Sc. Computer Science",
          level: "400 Level",
          cgpa: "4.98 / 5.00"
        },
        {
          name: "Tunde Adeyemi",
          program: "B.Eng. Electrical Eng.",
          level: "500 Level",
          cgpa: "4.94 / 5.00"
        },
        {
          name: "Chioma Nwachukwu",
          program: "LL.B. Faculty of Law",
          level: "500 Level",
          cgpa: "4.91 / 5.00"
        },
        {
          name: "Farouk Ibrahim",
          program: "MBBS Medicine & Surgery",
          level: "600 Level",
          cgpa: "Distinction"
        },
        {
          name: "Zainab Al-Mansoor",
          program: "B.Sc. Software Engineering",
          level: "300 Level",
          cgpa: "4.89 / 5.00"
        }
      ]
    };
  }
}
</script>
