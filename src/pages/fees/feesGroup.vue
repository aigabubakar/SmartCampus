<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="isAddSidebarOpen = true" />
      <div class="mt-24">
         <FeesGroupTable @edit="openEditSidebar" @delete="openDeleteModal" />
      </div>
    </div>
    <Footer />
  </main>
  
  <AddFeesGroupSidebar :isOpen="isAddSidebarOpen" @close="isAddSidebarOpen = false" @save="handleAdd" />
  <EditFeesGroupSidebar :isOpen="isEditSidebarOpen" :feesGroup="selectedFeesGroup" @close="isEditSidebarOpen = false" @update="handleUpdate" />
  <DeleteFeesGroupModal @delete="handleDelete" />
  <ThemeCustomizer />
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/fees/feesGroup/Breadcrumb.vue';
import FeesGroupTable from '@/components/fees/feesGroup/FeesGroupTable.vue';
import AddFeesGroupSidebar from '@/components/fees/feesGroup/AddFeesGroupSidebar.vue';
import EditFeesGroupSidebar from '@/components/fees/feesGroup/EditFeesGroupSidebar.vue';
import DeleteFeesGroupModal from '@/components/fees/feesGroup/DeleteFeesGroupModal.vue';

export default {
  name: "FeesGroupList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    FeesGroupTable,
    AddFeesGroupSidebar,
    EditFeesGroupSidebar,
    DeleteFeesGroupModal
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const isEditSidebarOpen = ref(false);
      const selectedFeesGroup = ref(null);
      const itemToDelete = ref(null);

      const openEditSidebar = (item) => {
          selectedFeesGroup.value = item;
          isEditSidebarOpen.value = true;
      };

      const openDeleteModal = (item) => {
          itemToDelete.value = item;
          const modalElement = document.getElementById('deleteFeesGroupModal');
          if (modalElement && window.bootstrap) {
              const modal = window.bootstrap.Modal.getInstance(modalElement) || new window.bootstrap.Modal(modalElement);
              modal.show();
          }
      };

      const handleAdd = (newItem) => {
          console.log('Add new item:', newItem);
          // In a real app, you would add this to the list
      };

      const handleUpdate = (updatedItem) => {
          console.log('Update item:', updatedItem);
          // In a real app, you would update the list
      };

      const handleDelete = () => {
          console.log('Delete item:', itemToDelete.value);
          // In a real app, you would remove from the list
      };

      return {
          isAddSidebarOpen,
          isEditSidebarOpen,
          selectedFeesGroup,
          openEditSidebar,
          openDeleteModal,
          handleAdd,
          handleUpdate,
          handleDelete
      };
  }
}
</script>
