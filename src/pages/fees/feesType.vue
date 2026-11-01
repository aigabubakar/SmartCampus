<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="isAddSidebarOpen = true" />
      <div class="mt-24">
         <FeesTypeTable @edit="openEditSidebar" @delete="openDeleteModal" />
      </div>
    </div>
    <Footer />
  </main>
  
  <AddFeesTypeSidebar :isOpen="isAddSidebarOpen" @close="isAddSidebarOpen = false" @save="handleAdd" />
  <EditFeesTypeSidebar :isOpen="isEditSidebarOpen" :feesType="selectedFeesType" @close="isEditSidebarOpen = false" @update="handleUpdate" />
  <DeleteFeesTypeModal @delete="handleDelete" />
  <ThemeCustomizer />
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/fees/feesType/Breadcrumb.vue';
import FeesTypeTable from '@/components/fees/feesType/FeesTypeTable.vue';
import AddFeesTypeSidebar from '@/components/fees/feesType/AddFeesTypeSidebar.vue';
import EditFeesTypeSidebar from '@/components/fees/feesType/EditFeesTypeSidebar.vue';
import DeleteFeesTypeModal from '@/components/fees/feesType/DeleteFeesTypeModal.vue';

export default {
  name: "FeesTypeList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    FeesTypeTable,
    AddFeesTypeSidebar,
    EditFeesTypeSidebar,
    DeleteFeesTypeModal
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const isEditSidebarOpen = ref(false);
      const selectedFeesType = ref(null);
      const itemToDelete = ref(null);

      const openEditSidebar = (item) => {
          selectedFeesType.value = item;
          isEditSidebarOpen.value = true;
      };

      const openDeleteModal = (item) => {
          itemToDelete.value = item;
          const modalElement = document.getElementById('deleteFeesTypeModal');
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
          selectedFeesType,
          openEditSidebar,
          openDeleteModal,
          handleAdd,
          handleUpdate,
          handleDelete
      };
  }
}
</script>
