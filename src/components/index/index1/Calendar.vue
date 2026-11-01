<template>
  <div class="card h-100">
    <div class="card-body p-0">
      <div
        class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <h6 class="text-lg mb-0">Calendar</h6>
      </div>

      <div class="p-20">
        <div class="calendar">
          <div class="calendar__header">
            <button type="button" class="calendar__arrow left" @click="prevMonth">
              <i class="ri-arrow-left-s-line"></i>
            </button>
            <p class="display text-md text-secondary-light fw-semibold mb-0">{{ formattedDate }}</p>
            <button type="button" class="calendar__arrow right" @click="nextMonth">
              <i class="ri-arrow-right-s-line"></i>
            </button>
          </div>

          <div class="calendar__week week">
            <div class="calendar__week-text">Su</div>
            <div class="calendar__week-text">Mo</div>
            <div class="calendar__week-text">Tu</div>
            <div class="calendar__week-text">We</div>
            <div class="calendar__week-text">Th</div>
            <div class="calendar__week-text">Fr</div>
            <div class="calendar__week-text">Sa</div>
          </div>
          <div class="days">
            <div v-for="(day, index) in days" :key="index" :class="{ 'current-date': day.isCurrent }">{{ day.number }}</div>
          </div>
        </div>
      </div>

      <div class="ps-20 pt-20 pb-20 border-top border-neutral-200">
        <h6 class="text-lg mb-20">Upcoming Events</h6>
        <div class="pe-20 d-flex flex-column gap-32 overflow-y-auto max-h-500-px scroll-sm">
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-purple-600">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-lg fw-normal mb-0">09:00 - 09:45</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">AM</span>
              </div>
              <p class="text-secondary-light mt-4 mb-2 text-sm">Marketing Strategy Kickoff</p>
              <p class="text-xs text-secondary-light mb-0">Lead by <a href="javascript:void(0)"
                  class="text-primary-600 hover-underline">Robert Fox</a></p>
            </div>
            <div>
              <a href="javascript:void(0)"
                class="py-6 px-16 radius-4 bg-neutral-100 text-secondary-light fw-semibold bg-hover-primary-600 hover-text-white">View</a>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-warning-600">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-lg fw-normal mb-0">11:15 - 12:00</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">AM</span>
              </div>
              <p class="text-secondary-light mt-4 mb-2 text-sm">Product Design Brainstorm</p>
              <p class="text-xs text-secondary-light mb-0">Lead by <a href="javascript:void(0)"
                  class="text-primary-600 hover-underline">Leslie Alexander</a></p>
            </div>
            <div>
              <a href="javascript:void(0)"
                class="py-6 px-16 radius-4 bg-neutral-100 text-secondary-light fw-semibold bg-hover-primary-600 hover-text-white">View</a>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-blue-600">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-lg fw-normal mb-0">02:00 - 03:00</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">PM</span>
              </div>
              <p class="text-secondary-light mt-4 mb-2 text-sm">Client Feedback Review</p>
              <p class="text-xs text-secondary-light mb-0">Lead by <a href="javascript:void(0)"
                  class="text-primary-600 hover-underline">Courtney Henry</a></p>
            </div>
            <div>
              <a href="javascript:void(0)"
                class="py-6 px-16 radius-4 bg-neutral-100 text-secondary-light fw-semibold bg-hover-primary-600 hover-text-white">View</a>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-success-600">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-lg fw-normal mb-0">04:15 - 05:00</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">PM</span>
              </div>
              <p class="text-secondary-light mt-4 mb-2 text-sm">Sprint Planning & Task Allocation</p>
              <p class="text-xs text-secondary-light mb-0">Lead by <a href="javascript:void(0)"
                  class="text-primary-600 hover-underline">Eleanor Pena</a></p>
            </div>
            <div>
              <a href="javascript:void(0)"
                class="py-6 px-16 radius-4 bg-neutral-100 text-secondary-light fw-semibold bg-hover-primary-600 hover-text-white">View</a>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-primary-600">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-lg fw-normal mb-0">01:15 - 02:00</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">PM</span>
              </div>
              <p class="text-secondary-light mt-4 mb-2 text-sm">Client Feedback Review</p>
              <p class="text-xs text-secondary-light mb-0">Lead by <a href="javascript:void(0)"
                  class="text-primary-600 hover-underline">John</a></p>
            </div>
            <div>
              <a href="javascript:void(0)"
                class="py-6 px-16 radius-4 bg-neutral-100 text-secondary-light fw-semibold bg-hover-primary-600 hover-text-white">View</a>
            </div>
          </div>
          <div class="d-flex align-items-center justify-content-between gap-16">
            <div class="ps-10 border-start-width-3-px border-warning-600">
              <div class="d-flex align-items-end gap-6">
                <h6 class="text-lg fw-normal mb-0">11:15 - 12:00</h6>
                <span class="text-xs text-secondary-light line-height-1 mb-2">AM</span>
              </div>
              <p class="text-secondary-light mt-4 mb-2 text-sm">Product Design Brainstorm</p>
              <p class="text-xs text-secondary-light mb-0">Lead by <a href="javascript:void(0)"
                  class="text-primary-600 hover-underline">Leslie Alexander</a></p>
            </div>
            <div>
              <a href="javascript:void(0)"
                class="py-6 px-16 radius-4 bg-neutral-100 text-secondary-light fw-semibold bg-hover-primary-600 hover-text-white">View</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Calendar",
  data() {
    return {
      date: new Date(),
      days: []
    }
  },
  computed: {
    formattedDate() {
      return this.date.toLocaleString("en-US", {
        month: "long",
        year: "numeric"
      });
    },
    year() {
      return this.date.getFullYear();
    },
    month() {
      return this.date.getMonth();
    }
  },
  methods: {
    generateDays() {
      const firstDay = new Date(this.year, this.month, 1);
      const lastDay = new Date(this.year, this.month + 1, 0);
      const firstDayIndex = firstDay.getDay(); // 0-6
      const numberOfDays = lastDay.getDate();

      this.days = [];
      
      // Empty slots for previous month days
      for (let x = 0; x < firstDayIndex; x++) {
        this.days.push({ number: '', isCurrent: false });
      }

      const today = new Date();
      
      for (let i = 1; i <= numberOfDays; i++) {
        const isCurrent = (
          i === today.getDate() &&
          this.month === today.getMonth() &&
          this.year === today.getFullYear()
        );
        this.days.push({ number: i, isCurrent });
      }
    },
    prevMonth() {
      this.date = new Date(this.year, this.month - 1, 1);
      this.generateDays();
    },
    nextMonth() {
      this.date = new Date(this.year, this.month + 1, 1);
      this.generateDays();
    }
  },
  mounted() {
    this.generateDays();
  }
}
</script>

<style scoped>
.calendar__week,
.days {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  text-align: center;
  justify-items: center;
  align-items: center;
}

.days div {
  width: 35px;
  height: 35px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  cursor: pointer;
  border-radius: 50%;
  margin: 5px 0;
}

.days div:hover:not(.current-date) {
  background-color: var(--neutral-200);
  color: var(--primary-600);
}

.current-date {
  background-color: var(--primary-600);
  color: white;
  border-radius: 50%;
}
</style>
