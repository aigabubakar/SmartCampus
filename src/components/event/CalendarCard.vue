<template>
  <div class="card h-100 p-0">
    <div class="card-body p-24">
      <div id='wrap'>
        <div id='calendar'></div>
        <div style='clear:both'></div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted } from 'vue';

export default {
  name: "CalendarCard",
  setup() {
    onMounted(() => {
      // Initialize FullCalendar
      // Assuming user has FullCalendar assets available globally or integrated via package
      // The provided HTML referenced 'assets/js/full-calendar.js'
      // Ideally we should import specific library but for now we follow the structure
      // If FullCalendar is globally available via script tag in index.html
      if (typeof FullCalendar !== 'undefined') {
          // Logic to init calendar
          var calendarEl = document.getElementById('calendar');
          var calendar = new FullCalendar.Calendar(calendarEl, {
            initialView: 'dayGridMonth',
            headerToolbar: {
              left: 'prev,next today',
              center: 'title',
              right: 'dayGridMonth,timeGridWeek,timeGridDay'
            }
          });
          calendar.render();
      }
    });
  }
}
</script>
