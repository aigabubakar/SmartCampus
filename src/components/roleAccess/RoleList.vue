<template>
  <div class="d-flex flex-column gap-24">
    <!-- Super Admin Root Ownership Banner -->
    <div class="card border-0 shadow-sm radius-12 p-20 bg-primary-50 border-start border-primary-600 border-4">
      <div class="d-flex flex-wrap align-items-center justify-content-between gap-16">
        <div class="d-flex align-items-center gap-14">
          <div class="w-48-px h-48-px rounded-12 bg-primary-600 text-white d-flex align-items-center justify-content-center shadow-sm flex-shrink-0">
            <i class="ri-shield-keyhole-line text-2xl"></i>
          </div>
          <div>
            <div class="d-flex align-items-center gap-8 mb-4">
              <h6 class="fw-bold text-primary-light mb-0">Platform Developer & Managed Services Authority</h6>
              <span class="badge bg-danger-600 text-white text-xxs px-8 py-3 rounded-pill fw-semibold">
                ROOT PRIVILEGES
              </span>
            </div>
            <p class="text-xs text-neutral-600 mb-0">
              As the developer/operator, you hold absolute authority over system health, AI keys, and license governance. You can delegate scoped operational administrative rights to university staff below.
            </p>
          </div>
        </div>

        <div class="d-flex align-items-center gap-12">
          <div class="text-end d-none d-sm-block">
            <span class="text-xxs text-neutral-500 d-block">ACTIVE OPERATOR IDENTITY</span>
            <span class="text-xs fw-bold text-primary-light">{{ authStore.currentUser?.name }} ({{ authStore.currentUser?.role }})</span>
          </div>
          <span class="badge bg-success-50 text-success-700 border border-success-200 px-10 py-6 rounded-8 text-xs fw-medium d-flex align-items-center gap-6">
            <span class="w-6-px h-6-px rounded-circle bg-success-main"></span>
            License: Active
          </span>
        </div>
      </div>
    </div>

    <!-- Administrator Directory Card -->
    <div class="card h-100 border-0 shadow-sm radius-12 overflow-hidden">
      <!-- Table Filter Bar -->
      <div class="card-header bg-base border-bottom py-16 px-20 d-flex flex-wrap align-items-center justify-content-between gap-16">
        <div class="d-flex flex-wrap align-items-center gap-12">
          <div class="navbar-search m-0 position-relative">
            <span class="position-absolute start-0 top-50 translate-middle-y ps-12 text-neutral-400">
              <i class="ri-search-line"></i>
            </span>
            <input
              type="text"
              class="form-control text-xs ps-36 py-8 radius-8 border-neutral-300"
              placeholder="Search by name, email, or staff ID..."
              v-model="searchQuery"
            />
          </div>

          <!-- Status Filter Tabs -->
          <div class="btn-group btn-group-sm p-2 bg-neutral-100 rounded-8">
            <button
              type="button"
              class="btn btn-xs text-xxs fw-semibold px-10 py-4 rounded-6 border-0"
              :class="statusFilter === 'all' ? 'bg-white text-primary-600 shadow-sm' : 'text-neutral-600'"
              @click="statusFilter = 'all'"
            >
              All ({{ allAdmins.length }})
            </button>
            <button
              type="button"
              class="btn btn-xs text-xxs fw-semibold px-10 py-4 rounded-6 border-0"
              :class="statusFilter === 'active' ? 'bg-white text-success-700 shadow-sm' : 'text-neutral-600'"
              @click="statusFilter = 'active'"
            >
              Active ({{ activeAdminsCount }})
            </button>
            <button
              type="button"
              class="btn btn-xs text-xxs fw-semibold px-10 py-4 rounded-6 border-0"
              :class="statusFilter === 'suspended' ? 'bg-white text-danger-600 shadow-sm' : 'text-neutral-600'"
              @click="statusFilter = 'suspended'"
            >
              Suspended ({{ suspendedAdminsCount }})
            </button>
          </div>
        </div>

        <div class="d-flex align-items-center gap-8 text-xs text-secondary-light">
          <span class="text-neutral-500">Showing <strong>{{ filteredAdmins.length }}</strong> administrators</span>
        </div>
      </div>

      <!-- Table Body -->
      <div class="table-responsive">
        <table class="table bordered-table mb-0 align-middle">
          <thead class="table-light">
            <tr>
              <th scope="col" class="text-xs fw-bold text-neutral-600 ps-20">Administrator Profile</th>
              <th scope="col" class="text-xs fw-bold text-neutral-600">Administrative Tier</th>
              <th scope="col" class="text-xs fw-bold text-neutral-600">Operational Scope</th>
              <th scope="col" class="text-xs fw-bold text-neutral-600">Permissions</th>
              <th scope="col" class="text-xs fw-bold text-neutral-600">Status</th>
              <th scope="col" class="text-xs fw-bold text-neutral-600 text-end pe-20">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="admin in filteredAdmins" :key="admin.id" class="transition-all hover-bg-neutral-50">
              
              <!-- Profile Info -->
              <td class="ps-20 py-14">
                <div class="d-flex align-items-center gap-12">
                  <div class="position-relative">
                    <img :src="admin.avatar" alt="Avatar" class="w-40-px h-40-px rounded-circle object-fit-cover border">
                    <span v-if="admin.isRoot" class="position-absolute bottom-0 end-0 w-12-px h-12-px rounded-circle bg-danger-600 border border-white" title="Root Account"></span>
                  </div>
                  <div>
                    <div class="d-flex align-items-center gap-6">
                      <h6 class="text-xs fw-bold text-primary-light mb-0">{{ admin.name }}</h6>
                      <span v-if="admin.isRoot" class="badge bg-danger-50 text-danger-700 border border-danger-200 text-xxs px-6 py-1 rounded">
                        Developer Root
                      </span>
                    </div>
                    <span class="text-xxs text-secondary-light d-block">{{ admin.email }}</span>
                    <span class="text-xxs font-monospace text-neutral-400">{{ admin.staffId }} • {{ admin.department }}</span>
                  </div>
                </div>
              </td>

              <!-- Tier -->
              <td>
                <span v-if="admin.isRoot" class="badge bg-purple-50 text-purple-700 border border-purple-200 text-xs px-10 py-5 rounded-pill fw-semibold d-inline-flex align-items-center gap-4">
                  <i class="ri-crown-line text-xs"></i> Super Admin
                </span>
                <span v-else class="badge bg-blue-50 text-blue-700 border border-blue-200 text-xs px-10 py-5 rounded-pill fw-semibold d-inline-flex align-items-center gap-4">
                  <i class="ri-user-star-line text-xs"></i> University Admin
                </span>
              </td>

              <!-- Operational Scope -->
              <td>
                <span class="text-xs fw-semibold text-neutral-800 d-block">{{ admin.scope }}</span>
                <span class="text-xxs text-secondary-light">Created: {{ admin.dateCreated }}</span>
              </td>

              <!-- Permissions Badges -->
              <td>
                <div class="d-flex flex-wrap gap-4 max-w-260-px">
                  <span
                    v-for="(perm, pIdx) in (admin.permissions || []).slice(0, 3)"
                    :key="pIdx"
                    class="badge bg-neutral-100 text-neutral-700 text-xxs px-6 py-2 rounded font-monospace"
                  >
                    {{ perm.replace('_', ' ') }}
                  </span>
                  <span v-if="admin.permissions && admin.permissions.length > 3" class="badge bg-neutral-200 text-neutral-600 text-xxs px-4 py-2 rounded">
                    +{{ admin.permissions.length - 3 }} more
                  </span>
                </div>
              </td>

              <!-- Status -->
              <td>
                <span v-if="admin.status === 'Active'" class="badge bg-success-50 text-success-700 border border-success-200 text-xxs px-8 py-4 rounded-pill fw-semibold d-inline-flex align-items-center gap-4">
                  <span class="w-6-px h-6-px rounded-circle bg-success-main"></span>
                  Active
                </span>
                <span v-else class="badge bg-danger-50 text-danger-700 border border-danger-200 text-xxs px-8 py-4 rounded-pill fw-semibold d-inline-flex align-items-center gap-4">
                  <span class="w-6-px h-6-px rounded-circle bg-danger-main"></span>
                  Suspended
                </span>
              </td>

              <!-- Actions Dropdown -->
              <td class="text-end pe-20">
                <div class="dropdown d-inline-block">
                  <button type="button" class="btn btn-sm btn-outline-neutral-300 text-neutral-600 py-4 px-8 rounded-6 text-xs" data-bs-toggle="dropdown" aria-expanded="false">
                    <i class="ri-more-2-fill"></i>
                  </button>
                  <ul class="dropdown-menu dropdown-menu-end border shadow-sm p-8 text-xs">
                    <li>
                      <button
                        type="button"
                        class="dropdown-item py-6 px-12 rounded text-neutral-700 d-flex align-items-center gap-8"
                        @click="$emit('edit-role', admin)"
                      >
                        <i class="ri-edit-line text-sm text-primary-600"></i>
                        <span>Edit Scope & Permissions</span>
                      </button>
                    </li>
                    <li v-if="!admin.isRoot">
                      <button
                        type="button"
                        class="dropdown-item py-6 px-12 rounded text-neutral-700 d-flex align-items-center gap-8"
                        @click="toggleStatus(admin)"
                      >
                        <i :class="admin.status === 'Active' ? 'ri-pause-circle-line text-warning-main' : 'ri-play-circle-line text-success-main'" class="text-sm"></i>
                        <span>{{ admin.status === 'Active' ? 'Suspend Access' : 'Reactivate Admin' }}</span>
                      </button>
                    </li>
                    <li v-if="!admin.isRoot"><hr class="dropdown-divider my-4"></li>
                    <li v-if="!admin.isRoot">
                      <button
                        type="button"
                        class="dropdown-item py-6 px-12 rounded text-danger-600 hover-bg-danger-50 d-flex align-items-center gap-8"
                        @click="confirmDelete(admin)"
                      >
                        <i class="ri-delete-bin-line text-sm"></i>
                        <span>Revoke Admin Access</span>
                      </button>
                    </li>
                    <li v-if="admin.isRoot">
                      <span class="dropdown-item py-6 px-12 text-neutral-400 text-xxs font-italic">
                        <i class="ri-lock-line"></i> Root Protected
                      </span>
                    </li>
                  </ul>
                </div>
              </td>

            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth.js';
import { useToastStore } from '@/stores/toast.js';

export default {
  name: "RoleList",
  emits: ['edit-role'],
  setup() {
    const authStore = useAuthStore();
    const toastStore = useToastStore();
    const searchQuery = ref('');
    const statusFilter = ref('all');

    onMounted(async () => {
      try {
        await authStore.fetchAdmins();
      } catch (err) {
        console.warn("Could not sync live admin accounts, using store defaults:", err);
      }
    });

    const allAdmins = computed(() => authStore.allAdmins || []);

    const activeAdminsCount = computed(() => allAdmins.value.filter(a => a.status === 'Active').length);
    const suspendedAdminsCount = computed(() => allAdmins.value.filter(a => a.status === 'Suspended').length);

    const filteredAdmins = computed(() => {
      return allAdmins.value.filter(admin => {
        const matchesSearch =
          admin.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          admin.email.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          (admin.staffId && admin.staffId.toLowerCase().includes(searchQuery.value.toLowerCase())) ||
          (admin.department && admin.department.toLowerCase().includes(searchQuery.value.toLowerCase()));

        const matchesStatus =
          statusFilter.value === 'all' ||
          admin.status.toLowerCase() === statusFilter.value.toLowerCase();

        return matchesSearch && matchesStatus;
      });
    });

    const toggleStatus = (admin) => {
      try {
        const targetStatus = admin.status === 'Active' ? 'Suspended' : 'Active';
        authStore.toggleAdminStatus(admin.id);
        toastStore.info(
          `Staff member ${admin.name} status updated to ${targetStatus}.`,
          'Status Updated'
        );
      } catch (err) {
        toastStore.error(err.message, 'Action Failed');
      }
    };

    const confirmDelete = (admin) => {
      if (confirm(`Revoke all administrative access for ${admin.name} (${admin.staffId})?`)) {
        try {
          const name = admin.name;
          const staffId = admin.staffId;
          authStore.deleteAdminUser(admin.id);
          toastStore.warning(
            `Administrative credentials and access for ${name} (${staffId}) have been revoked.`,
            'Administrator Removed'
          );
        } catch (err) {
          toastStore.error(err.message, 'Action Failed');
        }
      }
    };

    return {
      authStore,
      searchQuery,
      statusFilter,
      allAdmins,
      activeAdminsCount,
      suspendedAdminsCount,
      filteredAdmins,
      toggleStatus,
      confirmDelete,
    };
  },
};
</script>

<style scoped>
.text-xxs {
  font-size: 0.6875rem;
}
.max-w-260-px {
  max-width: 260px;
}
</style>
