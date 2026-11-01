import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router.js'

// Modern ESM runtime dependencies
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'iconify-icon'
import ApexCharts from 'apexcharts'
import flatpickr from 'flatpickr'

// Global bindings for embedded chart / picker components
window.ApexCharts = ApexCharts
window.flatpickr = flatpickr

// Stylesheets
import 'remixicon/fonts/remixicon.css'
import './assets/css/lib/bootstrap.min.css'
import './assets/css/lib/apexcharts.css'
import './assets/css/lib/dataTables.min.css'
import './assets/css/lib/flatpickr.min.css'
import './assets/css/lib/full-calendar.css'
import './assets/css/lib/calendar.css'
import './assets/css/style.css'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)
app.mount('#app')
