<template>
  <div class="card h-100 shadow-1 radius-16 border-0">
    <div class="card-body p-0 dataTable-wrapper">
      
      <!-- Top Bar: Filters, Search, and Audience Tabs -->
      <div class="p-20 border-bottom border-neutral-200">
        <div class="d-flex align-items-center justify-content-between flex-wrap gap-16">
          
          <!-- Audience Filters -->
          <div class="d-flex align-items-center gap-8 flex-wrap">
            <button 
              type="button" 
              class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
              :class="activeFilter === 'all' ? 'btn-primary-600 text-white' : 'btn-outline-neutral-300 text-secondary-light'"
              @click="activeFilter = 'all'"
            >
              All Circulars ({{ notices.length }})
            </button>
            <button 
              type="button" 
              class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
              :class="activeFilter === 'students' ? 'btn-primary-600 text-white' : 'btn-outline-neutral-300 text-secondary-light'"
              @click="activeFilter = 'students'"
            >
              Student Bulletins ({{ countAudience('students') }})
            </button>
            <button 
              type="button" 
              class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
              :class="activeFilter === 'faculty' ? 'btn-primary-600 text-white' : 'btn-outline-neutral-300 text-secondary-light'"
              @click="activeFilter = 'faculty'"
            >
              Faculty & Senate ({{ countAudience('faculty') }})
            </button>
            <button 
              type="button" 
              class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
              :class="activeFilter === 'guardians' ? 'btn-primary-600 text-white' : 'btn-outline-neutral-300 text-secondary-light'"
              @click="activeFilter = 'guardians'"
            >
              Parents & Guardians ({{ countAudience('guardians') }})
            </button>
            <button 
              type="button" 
              class="btn btn-sm radius-8 px-14 py-6 fw-semibold"
              :class="activeFilter === 'urgent' ? 'btn-danger-600 text-white' : 'btn-outline-neutral-300 text-secondary-light'"
              @click="activeFilter = 'urgent'"
            >
              Urgent Priority ({{ countUrgent }})
            </button>
          </div>

          <!-- Search Input -->
          <div class="position-relative" style="min-width: 260px;">
            <input 
              type="text" 
              class="form-control radius-8 py-6 ps-36 pe-16 text-sm" 
              placeholder="Search circulars, department, keywords..."
              v-model="searchQuery"
            >
            <iconify-icon icon="ion:search-outline" class="position-absolute top-50 start-0 translate-middle-y ms-12 text-secondary-light"></iconify-icon>
          </div>

        </div>
      </div>

      <!-- Table of Notices -->
      <div class="table-responsive">
        <table class="table bordered-table mb-0 align-middle text-sm">
          <thead class="bg-neutral-50 text-secondary-light fw-semibold text-xs text-uppercase">
            <tr>
              <th scope="col" class="py-12 px-16">Date</th>
              <th scope="col" class="py-12 px-16">Issuing Authority</th>
              <th scope="col" class="py-12 px-16">Circular Subject & Details</th>
              <th scope="col" class="py-12 px-16 text-center">Audience</th>
              <th scope="col" class="py-12 px-16 text-center">Priority</th>
              <th scope="col" class="py-12 px-16 text-end" v-if="canManageNotices">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="notice in filteredNotices" :key="notice.id">
              
              <!-- Date -->
              <td class="py-12 px-16 text-nowrap">
                <div class="d-flex align-items-center gap-6">
                  <iconify-icon icon="solar:calendar-linear" class="text-secondary-light text-base"></iconify-icon>
                  <span class="fw-medium text-neutral-800 text-xs">{{ notice.date }}</span>
                </div>
              </td>

              <!-- Issuing Department -->
              <td class="py-12 px-16 text-nowrap">
                <span class="badge radius-6 text-xs px-8 py-4 fw-semibold" :class="notice.senderColor || 'bg-primary-50 text-primary-600'">
                  {{ notice.sender }}
                </span>
              </td>

              <!-- Subject & Excerpt -->
              <td class="py-12 px-16">
                <h6 class="text-sm fw-bold text-neutral-900 mb-2">{{ notice.title }}</h6>
                <p class="text-secondary-light text-xs mb-0 line-clamp-2">{{ notice.description }}</p>
              </td>

              <!-- Target Audience -->
              <td class="py-12 px-16 text-center text-nowrap">
                <span 
                  class="badge radius-pill px-10 py-4 text-xs fw-semibold text-capitalize"
                  :class="getAudienceBadgeClass(notice.audience)"
                >
                  {{ notice.audience === 'all' ? 'All Campus' : notice.audience }}
                </span>
              </td>

              <!-- Priority -->
              <td class="py-12 px-16 text-center text-nowrap">
                <span class="badge radius-6 px-8 py-4 text-xs fw-bold" :class="notice.priorityClass">
                  {{ notice.priority }}
                </span>
              </td>

              <!-- Actions (Admin Only) -->
              <td class="py-12 px-16 text-end text-nowrap" v-if="canManageNotices">
                <div class="dropdown d-inline-block">
                  <button type="button" class="btn btn-sm btn-outline-neutral-300 radius-8 px-8 py-4 text-xs" data-bs-toggle="dropdown" aria-expanded="false">
                    <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end border p-8 radius-8 shadow-sm text-xs">
                    <li>
                      <button type="button" class="dropdown-item rounded py-6 px-12 text-primary-600 d-flex align-items-center gap-6" @click="$emit('edit-notice', notice)">
                        <i class="ri-edit-2-line"></i> Edit Circular
                      </button>
                    </li>
                    <li>
                      <button type="button" class="dropdown-item rounded py-6 px-12 text-danger-600 d-flex align-items-center gap-6" @click="handleDelete(notice.id)">
                        <i class="ri-delete-bin-6-line"></i> Revoke Notice
                      </button>
                    </li>
                  </ul>
                </div>
              </td>

            </tr>
            <tr v-if="filteredNotices.length === 0">
              <td colspan="6" class="text-center py-40 text-secondary-light">
                <iconify-icon icon="solar:notes-bold-duotone" class="text-4xl text-neutral-300 d-block mx-auto mb-8"></iconify-icon>
                <p class="text-sm mb-0">No circulars match the selected filter or search term.</p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useNoticeStore } from '@/stores/notices.js';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: "NoticeBoardTable",
  emits: ['edit-notice'],
  setup(props, { emit }) {
    const noticeStore = useNoticeStore();
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const activeFilter = ref('all');
    const searchQuery = ref('');

    const notices = computed(() => {
      return canManageNotices.value ? noticeStore.allNotices : noticeStore.noticesForCurrentUser;
    });
    const canManageNotices = computed(() => authStore.isAdmin || authStore.isSuperAdmin);

    const countAudience = (aud) => {
      return notices.value.filter(n => n.audience === 'all' || n.audience === aud).length;
    };

    const countUrgent = computed(() => {
      return notices.value.filter(n => n.priority === 'Urgent').length;
    });

    const filteredNotices = computed(() => {
      return notices.value.filter(notice => {
        // Audience filter
        let matchesAudience = true;
        if (activeFilter.value === 'students') {
          matchesAudience = notice.audience === 'all' || notice.audience === 'students';
        } else if (activeFilter.value === 'faculty') {
          matchesAudience = notice.audience === 'all' || notice.audience === 'faculty';
        } else if (activeFilter.value === 'guardians') {
          matchesAudience = notice.audience === 'all' || notice.audience === 'guardians';
        } else if (activeFilter.value === 'urgent') {
          matchesAudience = notice.priority === 'Urgent';
        }

        // Search query
        const query = searchQuery.value.toLowerCase().trim();
        const matchesSearch = !query || 
          notice.title.toLowerCase().includes(query) ||
          notice.description.toLowerCase().includes(query) ||
          notice.sender.toLowerCase().includes(query);

        return matchesAudience && matchesSearch;
      });
    });

    const getAudienceBadgeClass = (aud) => {
      switch (aud) {
        case 'students':
          return 'bg-blue-50 text-blue-700 border border-blue-subtle';
        case 'faculty':
          return 'bg-purple-50 text-purple-700 border border-purple-subtle';
        case 'guardians':
          return 'bg-warning-50 text-warning-800 border border-warning-subtle';
        case 'all':
        default:
          return 'bg-success-50 text-success-700 border border-success-subtle';
      }
    };

    const handleDelete = (id) => {
      const noticeToRevoke = notices.value.find(n => n.id === id);
      const title = noticeToRevoke ? noticeToRevoke.title : 'Circular';
      if (confirm('Are you sure you want to revoke this notice from the campus board?')) {
        noticeStore.deleteNotice(id);
        toastStore.warning(`"${title}" has been revoked from the campus notice board.`, 'Circular Revoked');
      }
    };

    return {
      activeFilter,
      searchQuery,
      notices,
      filteredNotices,
      canManageNotices,
      countAudience,
      countUrgent,
      getAudienceBadgeClass,
      handleDelete
    };
  }
}
</script>
