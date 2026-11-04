<template>
  <div class="card h-100 shadow-1 radius-16 border-0">
    <div class="card-body p-0 d-flex flex-column">
      <div
        class="d-flex flex-wrap align-items-center justify-content-between px-20 py-16 border-bottom border-neutral-200">
        <div>
          <h6 class="text-lg mb-0 fw-bold text-neutral-900">Academic Calendar</h6>
          <span class="text-secondary-light text-xs">Semester Schedule & Key Milestones</span>
        </div>
      </div>
      <div class="p-20 flex-grow-1 d-flex flex-column justify-content-center">
        <div class="calendar style-big">
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
            <div v-for="(day, index) in days" :key="index" 
            :class="{ 'current-date': day.isCurrent }"
            :data-date="day.dateString"
            >{{ day.number }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Calendar2",
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
        const currentDate = new Date(this.year, this.month, i);
        const isCurrent = (
          i === today.getDate() &&
          this.month === today.getMonth() &&
          this.year === today.getFullYear()
        );
        this.days.push({ 
            number: i, 
            isCurrent,
            dateString: currentDate.toDateString()
        });
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

.days div:hover:not(.current-date):not(:empty) {
  background-color: var(--neutral-200);
  color: var(--primary-600);
}

.current-date {
  background-color: var(--primary-600);
  color: white;
  border-radius: 50%;
}
</style>
