<template>
  <div class="card h-100">
    <div class="card-body">
      <div class="p-20">
        <div class="calendar">
          <div class="calendar__header">
            <button type="button" class="calendar__arrow left" @click="prevMonth">
              <i class="ri-arrow-left-s-line"></i>
            </button>
            <p class="display text-md text-secondary-light fw-semibold mb-0">{{ currentMonthYear }}</p>
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
            <div 
                v-for="(day, index) in days" 
                :key="index" 
                class="calendar__day" 
                :class="{ 'today': isToday(day) }"
            >
                {{ day ? day.getDate() : '' }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';

export default {
  name: "Calendar5",
  setup() {
    const currentDate = ref(new Date());

    const currentMonthYear = computed(() => {
      return currentDate.value.toLocaleString('default', { month: 'long', year: 'numeric' });
    });

    const days = computed(() => {
      const year = currentDate.value.getFullYear();
      const month = currentDate.value.getMonth();
      const firstDayOfMonth = new Date(year, month, 1).getDay();
      const daysInMonth = new Date(year, month + 1, 0).getDate();
      
      const daysArray = [];
      
      // Empty slots for days before the 1st of the month
      for (let i = 0; i < firstDayOfMonth; i++) {
        daysArray.push(null);
      }
      
      // Days of the month
      for (let i = 1; i <= daysInMonth; i++) {
        daysArray.push(new Date(year, month, i));
      }
      
      return daysArray;
    });

    const prevMonth = () => {
      currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() - 1, 1);
    };

    const nextMonth = () => {
      currentDate.value = new Date(currentDate.value.getFullYear(), currentDate.value.getMonth() + 1, 1);
    };

    const isToday = (date) => {
        if (!date) return false;
        const today = new Date();
        return date.getDate() === today.getDate() &&
               date.getMonth() === today.getMonth() &&
               date.getFullYear() === today.getFullYear();
    };

    return {
      currentMonthYear,
      days,
      prevMonth,
      nextMonth,
      isToday
    };
  }
}
</script>

<style scoped>
.calendar__day {
    width: 100%;
    text-align: center;
    padding: 10px 0;
    cursor: pointer;
    font-size: 14px;
    color: #6c757d; 
}
.calendar__day:hover {
    background-color: #f8f9fa;
    border-radius: 50%;
    color: #0d6efd;
}
.calendar__day.today {
    background-color: #0d6efd;
    color: white;
    border-radius: 50%;
}
.days {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 5px;
}
</style>
