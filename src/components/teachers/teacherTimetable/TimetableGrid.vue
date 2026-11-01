<template>
  <div class="card-body p-20 d-flex flex-column gap-20">
    <div class="overflow-x-auto d-flex scroll-sm pb-8">
      <div class="d-flex gap-16 flex-shrink-0 flex-grow-1">
        
        <div class="flex-grow-1" v-for="(daySchedule, dayName) in timetable" :key="dayName">
          <h6 class="text-md mb-8">{{ dayName }}</h6>
          <div class="d-flex flex-column gap-16">
            <div 
              class="attendance-card border radius-8 overflow-hidden" 
              v-for="(cls, index) in daySchedule" 
              :key="index"
            >
              <template v-if="cls.isHoliday">
                    <h6 class="text-sm bg-warning-100 text-warning-600 fw-semibold py-10 px-16 text-center mb-0 card-title">
                        Holiday
                    </h6>
              </template>
              <template v-else>
                <h6 class="text-sm fw-semibold py-10 px-16 text-center mb-0 card-title"
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
              </template>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TimetableGrid",
  setup() {
    // Helper to create class objects easily with consistent styling
    // Colors: warning, info, success, danger, primary, purple (custom?), etc.
    const createClass = (className, subject, room, time, color) => ({
      className,
      subject,
      room,
      time,
      headerClass: `bg-${color}-100 text-${color}-600`
    });

    const defaultDay = [
      createClass("1 (A)", "Math", "16", "09:00 AM - 09:45 AM", "warning"),
      createClass("2 (B)", "English", "10", "09:50 AM - 10:35 AM", "info"),
      createClass("3 (A)", "Science", "22", "10:40 AM - 11:25 AM", "success"),
      createClass("4 (C)", "History", "8", "11:30 AM - 12:15 PM", "danger"),
      createClass("5 (B)", "CSE", "25", "12:20 PM - 01:05 PM", "primary"),
    ];

    const holidayDay = [
      { isHoliday: true }
    ];

    const timetable = {
      Monday: defaultDay,
      Tuesday: defaultDay, // Repeating for example as per HTML
      Wednesday: defaultDay,
      Thursday: defaultDay,
      Friday: defaultDay,
      Saturday: defaultDay,
      Sunday: holidayDay,
    };

    return {
      timetable
    }
  }
}
</script>
