import { defineStore } from 'pinia';

export const useToastStore = defineStore('toast', {
  state: () => ({
    toasts: []
  }),

  actions: {
    show({ message, title = '', type = 'success', duration = 4000, icon = null }) {
      const id = `toast_${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;

      // Default icons based on toast type
      const defaultIcons = {
        success: 'solar:check-circle-bold',
        error: 'solar:danger-triangle-bold',
        warning: 'solar:shield-warning-bold',
        info: 'solar:info-circle-bold'
      };

      // Default titles if not provided
      const defaultTitles = {
        success: 'Action Completed',
        error: 'Action Failed',
        warning: 'Attention Required',
        info: 'System Dispatch'
      };

      const newToast = {
        id,
        title: title || defaultTitles[type] || 'Notice',
        message,
        type: ['success', 'error', 'warning', 'info'].includes(type) ? type : 'info',
        duration,
        icon: icon || defaultIcons[type] || defaultIcons.info,
        progress: 100,
        paused: false,
        timer: null,
        startTime: Date.now(),
        remainingTime: duration
      };

      this.toasts.push(newToast);

      if (duration > 0) {
        newToast.timer = setTimeout(() => {
          this.remove(id);
        }, duration);
      }

      return id;
    },

    success(message, title = 'Action Succeeded', duration = 4000) {
      return this.show({ message, title, type: 'success', duration });
    },

    error(message, title = 'Action Failed', duration = 5000) {
      return this.show({ message, title, type: 'error', duration });
    },

    warning(message, title = 'Attention Required', duration = 4500) {
      return this.show({ message, title, type: 'warning', duration });
    },

    info(message, title = 'Campus Notice', duration = 4000) {
      return this.show({ message, title, type: 'info', duration });
    },

    remove(id) {
      const index = this.toasts.findIndex(t => t.id === id);
      if (index !== -1) {
        if (this.toasts[index].timer) {
          clearTimeout(this.toasts[index].timer);
        }
        this.toasts.splice(index, 1);
      }
    },

    clear() {
      this.toasts.forEach(t => {
        if (t.timer) clearTimeout(t.timer);
      });
      this.toasts = [];
    }
  }
});
