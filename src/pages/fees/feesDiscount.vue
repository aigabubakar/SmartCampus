<template>
  <Sidebar />
  <main class="dashboard-main">
    <Navbar />
    <div class="dashboard-main-body">
      <Breadcrumb @openAddSidebar="isAddSidebarOpen = true" />
      <div class="mt-24">
         <FeesDiscountTable @edit="openEditSidebar" @delete="openDeleteModal" />
      </div>
    </div>
    <Footer />
  </main>
  
  <AddFeesDiscountSidebar :isOpen="isAddSidebarOpen" @close="isAddSidebarOpen = false" @save="handleAdd" />
  <EditFeesDiscountSidebar :isOpen="isEditSidebarOpen" :feesDiscount="selectedFeesDiscount" @close="isEditSidebarOpen = false" @update="handleUpdate" />
  <DeleteFeesDiscountModal @delete="handleDelete" />
  <ThemeCustomizer />
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/fees/feesDiscount/Breadcrumb.vue';
import FeesDiscountTable from '@/components/fees/feesDiscount/FeesDiscountTable.vue';
import AddFeesDiscountSidebar from '@/components/fees/feesDiscount/AddFeesDiscountSidebar.vue';
import EditFeesDiscountSidebar from '@/components/fees/feesDiscount/EditFeesDiscountSidebar.vue';
import DeleteFeesDiscountModal from '@/components/fees/feesDiscount/DeleteFeesDiscountModal.vue';

export default {
  name: "FeesDiscountList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    FeesDiscountTable,
    AddFeesDiscountSidebar,
    EditFeesDiscountSidebar,
    DeleteFeesDiscountModal
  },
  setup() {
      const isAddSidebarOpen = ref(false);
      const isEditSidebarOpen = ref(false);
      const selectedFeesDiscount = ref(null);
      const itemToDelete = ref(null);

      const openEditSidebar = (item) => {
          selectedFeesDiscount.value = item;
          isEditSidebarOpen.value = true;
      };

      const openDeleteModal = (item) => {
          itemToDelete.value = item;
          const modalElement = document.getElementById('deleteFeesDiscountModal');
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
          selectedFeesDiscount,
          openEditSidebar,
          openDeleteModal,
          handleAdd,
          handleUpdate,
          handleDelete
      };
  }
}
</script>
