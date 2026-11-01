<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-add-sidebar="openAddSidebar" />

        <div class="mt-24">
          <BooksTable @edit-book="openEditSidebar" />
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- Add Sidebar -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isAddSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add Book</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleAddSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-12">
            <div class="">
              <label for="bookName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Book Name</label>
              <input type="text" class="form-control" id="bookName" placeholder="Enter Book Name" v-model="addForm.bookName">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="publisher" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Publisher</label>
              <input type="text" class="form-control" id="publisher" placeholder="Enter Publisher" v-model="addForm.publisher">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="author" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Author</label>
              <input type="text" class="form-control" id="author" placeholder="Enter Author" v-model="addForm.author">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="number" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Number</label>
              <input type="number" class="form-control" id="number" placeholder="Enter Number" v-model="addForm.number">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="subject" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Subject</label>
              <input type="text" class="form-control" id="subject" placeholder="Enter Subject" v-model="addForm.subject">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="rackNo" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Rack No</label>
              <input type="text" class="form-control" id="rackNo" placeholder="Enter Rack No" v-model="addForm.rackNo">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="enterQty" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Qty</label>
              <input type="text" class="form-control" id="enterQty" placeholder="Enter Qty" v-model="addForm.qty">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="available" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Available</label>
              <input type="text" class="form-control" id="available" placeholder="Enter Available" v-model="addForm.available">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="price" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Price</label>
              <input type="text" class="form-control" id="price" placeholder="Enter Price" v-model="addForm.price">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="postDate" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Post Date</label>
              <input type="date" class="form-control" id="postDate" v-model="addForm.postDate">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="status" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
              <select id="status" class="form-control form-select" v-model="addForm.status">
                <option value="" selected disabled>Select Status</option>
                <option value="Active">Active</option>
                <option value="Inactive">Inactive</option>
              </select>
            </div>
          </div>
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
              <button type="reset" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="closeSidebar">
                Cancel
              </button>
              <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
                Save
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>

    <!-- Edit Sidebar -->
    <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isEditSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Book</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleEditSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-12">
            <div class="">
              <label for="bookNameEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Book Name</label>
              <input type="text" class="form-control" id="bookNameEdit" placeholder="Enter Book Name" v-model="editForm.bookName">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="publisherEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Publisher</label>
              <input type="text" class="form-control" id="publisherEdit" placeholder="Enter Publisher" v-model="editForm.publisher">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="authorEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Author</label>
              <input type="text" class="form-control" id="authorEdit" placeholder="Enter Author" v-model="editForm.author">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="numberEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Number</label>
              <input type="number" class="form-control" id="numberEdit" placeholder="Enter Number" v-model="editForm.number">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="subjectEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Subject</label>
              <input type="text" class="form-control" id="subjectEdit" placeholder="Enter Subject" v-model="editForm.subject">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="rackNoEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Rack No</label>
              <input type="text" class="form-control" id="rackNoEdit" placeholder="Enter Rack No" v-model="editForm.rackNo">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="enterQtyEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Qty</label>
              <input type="text" class="form-control" id="enterQtyEdit" placeholder="Enter Qty" v-model="editForm.qty">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="availableEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Available</label>
              <input type="text" class="form-control" id="availableEdit" placeholder="Enter Available" v-model="editForm.available">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="priceEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Price</label>
              <input type="text" class="form-control" id="priceEdit" placeholder="Enter Price" v-model="editForm.price">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="postDateEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Post Date</label>
              <input type="date" class="form-control" id="postDateEdit" v-model="editForm.postDate">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="statusEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Status</label>
              <select id="statusEdit" class="form-control form-select" v-model="editForm.status">
                <option value="" selected disabled>Select Status</option>
                <option value="Active">Active</option>
                <option value="Inactive">Inactive</option>
              </select>
            </div>
          </div>
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
              <button type="reset" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="closeSidebar">
                Cancel
              </button>
              <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8">
                Update
              </button>
            </div>
          </div>
        </div>
      </form>
    </div>

    <div class="overlay bg-black bg-opacity-50 w-100 h-100 position-fixed z-9 visibility-hidden opacity-0 duration-300" :class="{ 'active': isSidebarOpen }" @click="closeSidebar"></div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/library/booksList/Breadcrumb.vue';
import BooksTable from '@/components/library/booksList/BooksTable.vue';

export default {
  name: "BooksList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    BooksTable
  },
  setup() {
    const isAddSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);
    
    const addForm = ref({
      bookName: '',
      publisher: '',
      author: '',
      number: '',
      subject: '',
      rackNo: '',
      qty: '',
      available: '',
      price: '',
      postDate: '',
      status: ''
    });

    const editForm = ref({
      bookName: '',
      publisher: '',
      author: '',
      number: '',
      subject: '',
      rackNo: '',
      qty: '',
      available: '',
      price: '',
      postDate: '',
      status: ''
    });

    const isSidebarOpen = computed(() => isAddSidebarOpen.value || isEditSidebarOpen.value);

    const openAddSidebar = () => {
      isAddSidebarOpen.value = true;
    };

    const openEditSidebar = (book) => {
      editForm.value = { ...book };
      isEditSidebarOpen.value = true;
    };

    const closeSidebar = () => {
      isAddSidebarOpen.value = false;
      isEditSidebarOpen.value = false;
    };

    const handleAddSubmit = () => {
      console.log('Add Book:', addForm.value);
      // Here you would typically make an API call to add the book
      closeSidebar();
    };

    const handleEditSubmit = () => {
      console.log('Edit Book:', editForm.value);
      // Here you would typically make an API call to update the book
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
      handleAddSubmit,
      handleEditSubmit
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
