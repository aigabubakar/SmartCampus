<template>
  <div class="shadow-1 radius-12 bg-base h-100 overflow-hidden">
    <div class="card-header border-bottom bg-base py-16 px-24 d-flex align-items-center justify-content-between">
      <h6 class="text-lg fw-semibold mb-0">Class Routine </h6>
    </div>
    <div class="card-body p-20 d-flex flex-column gap-20">
      <div class="overflow-x-auto d-flex scroll-sm pb-8">
        <!-- Monday -->
        <div class="d-flex gap-16 flex-shrink-0 flex-grow-1">
          <div class="flex-grow-1">
            <h6 class="text-md mb-8">Monday</h6>
            <div class="d-flex flex-column gap-16">
              <div class="border radius-8 overflow-hidden" v-for="(cls, index) in mondayClasses" :key="index">
                <h6 class="text-sm fw-semibold py-10 px-16 text-center mb-0"
                    :class="cls.headerClass">
                  Class: {{ cls.className }}
                </h6>
                <div class="px-10 py-16 d-flex flex-column gap-10">
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-book-open-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="w-64-px flex-shrink-0"> Subject </span>
                      <span class="flex-grow-1">: {{ cls.subject }}</span>
                    </div>
                  </div>
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-building-4-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="w-64-px flex-shrink-0"> Room No </span>
                      <span class="flex-grow-1">: {{ cls.room }}</span>
                    </div>
                  </div>
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-time-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="flex-grow-1">{{ cls.time }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Tuesday -->
          <div class="flex-grow-1">
            <h6 class="text-md mb-8">Tuesday</h6>
            <div class="d-flex flex-column gap-16">
              <div class="border radius-8 overflow-hidden" v-for="(cls, index) in tuesdayClasses" :key="index">
                <h6 class="text-sm fw-semibold py-10 px-16 text-center mb-0"
                    :class="cls.headerClass">
                  Class: {{ cls.className }}
                </h6>
                <div class="px-10 py-16 d-flex flex-column gap-10">
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-book-open-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="w-64-px flex-shrink-0"> Subject </span>
                      <span class="flex-grow-1">: {{ cls.subject }}</span>
                    </div>
                  </div>
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-building-4-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="w-64-px flex-shrink-0"> Room No </span>
                      <span class="flex-grow-1">: {{ cls.room }}</span>
                    </div>
                  </div>
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-time-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="flex-grow-1">{{ cls.time }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Wednesday -->
           <div class="flex-grow-1">
            <h6 class="text-md mb-8">Wednesday</h6>
            <div class="d-flex flex-column gap-16">
              <div class="border radius-8 overflow-hidden" v-for="(cls, index) in wednesdayClasses" :key="index">
                <h6 class="text-sm fw-semibold py-10 px-16 text-center mb-0"
                    :class="cls.headerClass">
                  Class: {{ cls.className }}
                </h6>
                <div class="px-10 py-16 d-flex flex-column gap-10">
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-book-open-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="w-64-px flex-shrink-0"> Subject </span>
                      <span class="flex-grow-1">: {{ cls.subject }}</span>
                    </div>
                  </div>
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-building-4-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="w-64-px flex-shrink-0"> Room No </span>
                      <span class="flex-grow-1">: {{ cls.room }}</span>
                    </div>
                  </div>
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-time-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="flex-grow-1">{{ cls.time }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
           <!-- Thursday -->
           <div class="flex-grow-1">
            <h6 class="text-md mb-8">Thursday</h6>
            <div class="d-flex flex-column gap-16">
              <div class="border radius-8 overflow-hidden" v-for="(cls, index) in thursdayClasses" :key="index">
                <h6 class="text-sm fw-semibold py-10 px-16 text-center mb-0"
                    :class="cls.headerClass">
                  Class: {{ cls.className }}
                </h6>
                <div class="px-10 py-16 d-flex flex-column gap-10">
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-book-open-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="w-64-px flex-shrink-0"> Subject </span>
                      <span class="flex-grow-1">: {{ cls.subject }}</span>
                    </div>
                  </div>
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-building-4-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="w-64-px flex-shrink-0"> Room No </span>
                      <span class="flex-grow-1">: {{ cls.room }}</span>
                    </div>
                  </div>
                  <div class="d-flex align-items-center gap-8">
                    <span class="d-flex line-height-1 text-secondary-light text-lg">
                      <i class="ri-time-line"></i>
                    </span>
                    <div class="text-primary-light text-sm d-flex">
                      <span class="flex-grow-1">{{ cls.time }}</span>
                    </div>
                  </div>
                </div>
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
  name: "ClassRoutineTab",
  setup() {
    // Sample data to make it cleaner than raw HTML repetition
    const createClass = (className, subject, room, time, colorClass) => ({
      className, subject, room, time, headerClass: `bg-${colorClass}-100 text-${colorClass}-600`
    });

    const mondayClasses = [
      createClass("1 (A)", "Math", "16", "09:00 AM - 09:45 AM", "warning"),
      createClass("2 (B)", "English", "10", "09:50 AM - 10:35 AM", "info"),
      createClass("3 (A)", "Science", "22", "10:40 AM - 11:25 AM", "success"),
      createClass("4 (C)", "History", "8", "11:30 AM - 12:15 PM", "danger"),
      createClass("5 (B)", "CSE", "25", "12:20 PM - 01:05 PM", "primary"),
    ];
    
     const tuesdayClasses = [
      createClass("1 (A)", "Math", "16", "09:00 AM - 09:45 AM", "warning"),
      createClass("2 (B)", "English", "10", "09:50 AM - 10:35 AM", "info"),
      createClass("3 (A)", "Science", "22", "10:40 AM - 11:25 AM", "success"),
      createClass("4 (C)", "History", "8", "11:30 AM - 12:15 PM", "danger"),
      createClass("5 (B)", "CSE", "25", "12:20 PM - 01:05 PM", "primary"),
    ];

     const wednesdayClasses = [
      createClass("1 (A)", "Math", "16", "09:00 AM - 09:45 AM", "warning"),
      createClass("2 (B)", "English", "10", "09:50 AM - 10:35 AM", "info"),
      createClass("3 (A)", "Science", "22", "10:40 AM - 11:25 AM", "success"),
      createClass("4 (C)", "History", "8", "11:30 AM - 12:15 PM", "danger"),
      createClass("5 (B)", "CSE", "25", "12:20 PM - 01:05 PM", "primary"),
    ];

     const thursdayClasses = [
      createClass("1 (A)", "Math", "16", "09:00 AM - 09:45 AM", "warning"),
      createClass("2 (B)", "English", "10", "09:50 AM - 10:35 AM", "info"),
      createClass("3 (A)", "Science", "22", "10:40 AM - 11:25 AM", "success"),
      createClass("4 (C)", "History", "8", "11:30 AM - 12:15 PM", "danger"),
      createClass("5 (B)", "CSE", "25", "12:20 PM - 01:05 PM", "primary"),
    ];

    return {
      mondayClasses,
      tuesdayClasses,
      wednesdayClasses,
      thursdayClasses
    }
  }
}
</script>
