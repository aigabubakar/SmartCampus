<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
      <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-add-sidebar="openAddSidebar" />

        <div class="mt-24">
          <NoticeBoardTable @edit-notice="openEditSidebar" />
        </div>
      </div>

      <Footer />
    </main>

    <!-- ================= Add Notice Drawer ================= -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isAddSidebarOpen }">
      <div class="px-24 py-16 border-bottom border-neutral-200 d-flex align-items-center justify-content-between gap-20 bg-neutral-50">
        <div>
          <h5 class="text-md fw-bold text-neutral-900 mb-0">Publish Institutional Notice</h5>
          <span class="text-secondary-light text-xs">Broadcast official circulars across the campus community</span>
        </div>
        <button type="button" class="btn-close" @click="closeSidebar"></button>
      </div>

      <form @submit.prevent="submitAddNotice" class="d-flex flex-column p-24">
        <div class="row g-3">
          
          <div class="col-12">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Circular Subject / Title *</label>
            <input 
              type="text" 
              class="form-control text-sm radius-8" 
              placeholder="e.g. Senate Ratification of Harmattan Examination Timetable" 
              v-model="addForm.title" 
              required
            >
          </div>

          <div class="col-sm-6">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Issuing Authority / Department *</label>
            <select class="form-select text-sm radius-8" v-model="addForm.sender" required>
              <option value="Office of the Registrar">Office of the Registrar</option>
              <option value="Academic Planning Directorate">Academic Planning Directorate</option>
              <option value="University Bursary">University Bursary</option>
              <option value="Dean of Student Affairs">Dean of Student Affairs</option>
              <option value="Examinations & Records Board">Examinations & Records Board</option>
              <option value="Directorate of Research">Directorate of Research</option>
              <option value="Vice Chancellor's Office">Vice Chancellor's Office</option>
            </select>
          </div>

          <div class="col-sm-6">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Target Audience *</label>
            <select class="form-select text-sm radius-8" v-model="addForm.audience" required>
              <option value="all">All Campus Community</option>
              <option value="students">Students Only</option>
              <option value="faculty">Academic Faculty Only</option>
              <option value="guardians">Parents & Guardians Only</option>
            </select>
          </div>

          <div class="col-sm-6">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Priority Level *</label>
            <select class="form-select text-sm radius-8" v-model="addForm.priority" required>
              <option value="General">General Circular</option>
              <option value="Important">Important Announcement</option>
              <option value="Urgent">Urgent Senate Notice</option>
              <option value="Event">Academic Event / Conference</option>
            </select>
          </div>

          <div class="col-sm-6">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Dispatch Date</label>
            <input type="date" class="form-control text-sm radius-8" v-model="addForm.date_raw">
          </div>

          <div class="col-12">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Circular Description / Content *</label>
            <textarea 
              class="form-control text-sm radius-8" 
              rows="5" 
              placeholder="Full text of the circular, regulations, deadlines, and instructions..." 
              v-model="addForm.description"
              required
            ></textarea>
          </div>

          <div class="col-12 pt-16 border-top border-neutral-200 d-flex justify-content-end gap-12">
            <button type="button" class="btn btn-outline-neutral-300 btn-sm radius-8 px-16 py-8 text-xs fw-semibold" @click="closeSidebar">
              Cancel
            </button>
            <button type="submit" class="btn btn-primary-600 btn-sm radius-8 px-20 py-8 text-xs fw-bold text-white shadow-sm">
              Publish Circular
            </button>
          </div>

        </div>
      </form>
    </div>

    <!-- ================= Edit Notice Drawer ================= -->
    <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isEditSidebarOpen }">
      <div class="px-24 py-16 border-bottom border-neutral-200 d-flex align-items-center justify-content-between gap-20 bg-neutral-50">
        <div>
          <h5 class="text-md fw-bold text-neutral-900 mb-0">Edit Circular Details</h5>
          <span class="text-secondary-light text-xs">Update published notice content or priority</span>
        </div>
        <button type="button" class="btn-close" @click="closeSidebar"></button>
      </div>

      <form @submit.prevent="submitEditNotice" class="d-flex flex-column p-24">
        <div class="row g-3">
          
          <div class="col-12">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Circular Subject / Title *</label>
            <input 
              type="text" 
              class="form-control text-sm radius-8" 
              v-model="editForm.title" 
              required
            >
          </div>

          <div class="col-sm-6">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Issuing Authority / Department *</label>
            <input 
              type="text" 
              class="form-control text-sm radius-8" 
              v-model="editForm.sender" 
              required
            >
          </div>

          <div class="col-sm-6">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Target Audience *</label>
            <select class="form-select text-sm radius-8" v-model="editForm.audience" required>
              <option value="all">All Campus Community</option>
              <option value="students">Students Only</option>
              <option value="faculty">Academic Faculty Only</option>
              <option value="guardians">Parents & Guardians Only</option>
            </select>
          </div>

          <div class="col-sm-6">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Priority Level *</label>
            <select class="form-select text-sm radius-8" v-model="editForm.priority" required>
              <option value="General">General Circular</option>
              <option value="Important">Important Announcement</option>
              <option value="Urgent">Urgent Senate Notice</option>
              <option value="Event">Academic Event / Conference</option>
            </select>
          </div>

          <div class="col-12">
            <label class="text-xs fw-semibold text-neutral-800 d-block mb-6">Circular Content *</label>
            <textarea 
              class="form-control text-sm radius-8" 
              rows="5" 
              v-model="editForm.description"
              required
            ></textarea>
          </div>

          <div class="col-12 pt-16 border-top border-neutral-200 d-flex justify-content-end gap-12">
            <button type="button" class="btn btn-outline-neutral-300 btn-sm radius-8 px-16 py-8 text-xs fw-semibold" @click="closeSidebar">
              Cancel
            </button>
            <button type="submit" class="btn btn-primary-600 btn-sm radius-8 px-20 py-8 text-xs fw-bold text-white shadow-sm">
              Save Changes
            </button>
          </div>

        </div>
      </form>
    </div>

    <!-- Backdrop Overlay -->
    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active': isSidebarOpen }" @click="closeSidebar"></div>

  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useNoticeStore } from '@/stores/notices.js';
import { useToastStore } from '@/stores/toast.js';

import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import Breadcrumb from '@/components/noticeBoard/Breadcrumb.vue';
import NoticeBoardTable from '@/components/noticeBoard/NoticeBoardTable.vue';

export default {
  name: "NoticeBoard",
  components: {
    Sidebar,
    Navbar,
    Footer,
    Breadcrumb,
    NoticeBoardTable
  },
  setup() {
    const noticeStore = useNoticeStore();
    const toastStore = useToastStore();

    const isAddSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);

    const addForm = ref({
      title: '',
      sender: 'Office of the Registrar',
      audience: 'all',
      priority: 'General',
      date_raw: new Date().toISOString().split('T')[0],
      description: ''
    });

    const editForm = ref({
      id: null,
      title: '',
      sender: '',
      audience: 'all',
      priority: 'General',
      description: ''
    });

    const isSidebarOpen = computed(() => isAddSidebarOpen.value || isEditSidebarOpen.value);

    const openAddSidebar = () => {
      addForm.value = {
        title: '',
        sender: 'Office of the Registrar',
        audience: 'all',
        priority: 'General',
        date_raw: new Date().toISOString().split('T')[0],
        description: ''
      };
      isAddSidebarOpen.value = true;
    };

    const openEditSidebar = (notice) => {
      editForm.value = {
        id: notice.id,
        title: notice.title,
        sender: notice.sender,
        audience: notice.audience,
        priority: notice.priority,
        description: notice.description
      };
      isEditSidebarOpen.value = true;
    };

    const closeSidebar = () => {
      isAddSidebarOpen.value = false;
      isEditSidebarOpen.value = false;
    };

    const submitAddNotice = () => {
      const title = addForm.value.title;
      noticeStore.addNotice({
        title: addForm.value.title,
        sender: addForm.value.sender,
        audience: addForm.value.audience,
        priority: addForm.value.priority,
        date_raw: addForm.value.date_raw,
        description: addForm.value.description
      });
      toastStore.success(`"${title}" has been successfully broadcast to the campus community.`, 'Circular Published');
      closeSidebar();
    };

    const submitEditNotice = () => {
      if (editForm.value.id) {
        noticeStore.updateNotice(editForm.value.id, {
          title: editForm.value.title,
          sender: editForm.value.sender,
          audience: editForm.value.audience,
          priority: editForm.value.priority,
          description: editForm.value.description
        });
        toastStore.success(`Changes to circular "${editForm.value.title}" have been saved.`, 'Circular Updated');
      }
      closeSidebar();
    };

    return {
      isAddSidebarOpen,
      isEditSidebarOpen,
      isSidebarOpen,
      addForm,
      editForm,
      openAddSidebar,
      openEditSidebar,
      closeSidebar,
      submitAddNotice,
      submitEditNotice
    };
  }
}
</script>

<style scoped>
.my-sidebar.active,
.edit-sidebar.active {
  transform: translateX(0);
}

.overlay.active {
  visibility: visible;
  opacity: 1;
}
</style>
