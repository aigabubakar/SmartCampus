<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb @open-add-sidebar="openAddSidebar" />

        <div class="mt-24">
          <ExpenseListTable @edit-item="openEditSidebar" />
        </div>
      </div>

      <Footer />
    </main>

    <ThemeCustomizer />

    <!-- Add Expense Sidebar -->
    <div class="my-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isAddSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Add Expense</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleAddSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-12">
            <div class="">
              <label for="expenseName" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Expense Name</label>
              <input type="text" class="form-control" id="expenseName" placeholder="Enter Expense Name" v-model="addForm.name">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="expenseHead" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Expense Head</label>
              <select id="expenseHead" class="form-control form-select" v-model="addForm.expenseHead">
                <option value="" selected disabled>Select an expense head</option>
                <option value="Salary Payment">Salary Payment</option>
                <option value="Utility Bills">Utility Bills</option>
                <option value="Maintenance">Maintenance</option>
                <option value="Stationery">Stationery</option>
                <option value="Transport">Transport</option>
                <option value="Laboratory">Laboratory</option>
                <option value="Sports Equipment">Sports Equipment</option>
                <option value="Library Books">Library Books</option>
                <option value="Technology">Technology</option>
                <option value="Event Expenses">Event Expenses</option>
                <option value="Marketing">Marketing</option>
                <option value="Miscellaneous">Miscellaneous</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="amount" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Amount</label>
              <input type="text" class="form-control" id="amount" placeholder="Enter Amount" v-model="addForm.amount">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="date" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Date</label>
              <input type="date" class="form-control" id="date" v-model="addForm.date">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="paymentType" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Payment Type</label>
              <select id="paymentType" class="form-control form-select" v-model="addForm.paymentType">
                <option value="" selected disabled>Select payment type</option>
                <option value="Cash">Cash</option>
                <option value="Online">Online</option>
                <option value="Bank Transfer">Bank Transfer</option>
                <option value="Cheque">Cheque</option>
              </select>
            </div>
          </div>
          <div class="col-sm-12">
            <div class="">
              <label for="description" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Description</label>
              <textarea class="form-control" id="description" placeholder="Enter Description" v-model="addForm.description"></textarea>
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

    <!-- Edit Expense Sidebar -->
    <div class="edit-sidebar bg-white position-fixed end-0 top-0 h-100vh overflow-y-auto z-99 max-w-700-px w-100 translate-x-full duration-300" :class="{ 'active': isEditSidebarOpen }">
      <div class="px-20 py-12 border-bottom d-flex align-items-center justify-content-between gap-20">
        <h5 class="text-lg mb-0">Edit Expense</h5>
        <button type="button" class="text-danger-600 text-lg d-flex" @click="closeSidebar">
          <i class="ri-close-large-line"></i>
        </button>
      </div>
      <form @submit.prevent="handleEditSubmit" class="d-flex flex-column p-20">
        <div class="row g-3">
          <div class="col-sm-12">
            <div class="">
              <label for="expenseNameEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Expense Name</label>
              <input type="text" class="form-control" id="expenseNameEdit" placeholder="Enter Expense Name" v-model="editForm.name">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="expenseHeadEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Expense Head</label>
              <select id="expenseHeadEdit" class="form-control form-select" v-model="editForm.expenseHead">
                <option value="" selected disabled>Select an expense head</option>
                <option value="Salary Payment">Salary Payment</option>
                <option value="Utility Bills">Utility Bills</option>
                <option value="Maintenance">Maintenance</option>
                <option value="Stationery">Stationery</option>
                <option value="Transport">Transport</option>
                <option value="Laboratory">Laboratory</option>
                <option value="Sports Equipment">Sports Equipment</option>
                <option value="Library Books">Library Books</option>
                <option value="Technology">Technology</option>
                <option value="Event Expenses">Event Expenses</option>
                <option value="Marketing">Marketing</option>
                <option value="Miscellaneous">Miscellaneous</option>
              </select>
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="amountEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Amount</label>
              <input type="text" class="form-control" id="amountEdit" placeholder="Enter Amount" v-model="editForm.amount">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="dateEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Date</label>
              <input type="date" class="form-control" id="dateEdit" v-model="editForm.date">
            </div>
          </div>
          <div class="col-sm-6">
            <div class="">
              <label for="paymentTypeEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Payment Type</label>
              <select id="paymentTypeEdit" class="form-control form-select" v-model="editForm.paymentType">
                <option value="" selected disabled>Select payment type</option>
                <option value="Cash">Cash</option>
                <option value="Online">Online</option>
                <option value="Bank Transfer">Bank Transfer</option>
                <option value="Cheque">Cheque</option>
              </select>
            </div>
          </div>
          <div class="col-sm-12">
            <div class="">
              <label for="descriptionEdit" class="text-sm fw-semibold text-primary-light d-inline-block mb-8">Description</label>
              <textarea class="form-control" id="descriptionEdit" placeholder="Enter Description" v-model="editForm.description"></textarea>
            </div>
          </div>
          <div class="col-12">
            <div class="d-flex align-items-center justify-content-center gap-3 mt-8">
              <button type="reset" class="border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-50 py-11 radius-8" @click="closeSidebar">
                Cancel
              </button>
              <button type="submit" class="btn btn-primary-600 border border-primary-600 text-md px-28 py-12 radius-8 max-w-156-px w-100">
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
import Breadcrumb from '@/components/accounts/expenseList/Breadcrumb.vue';
import ExpenseListTable from '@/components/accounts/expenseList/ExpenseListTable.vue';

export default {
  name: "ExpenseList",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    ExpenseListTable
  },
  setup() {
    const isAddSidebarOpen = ref(false);
    const isEditSidebarOpen = ref(false);

    const addForm = ref({
      name: '',
      expenseHead: '',
      amount: '',
      date: '',
      paymentType: '',
      description: ''
    });

    const editForm = ref({
      id: null,
      name: '',
      expenseHead: '',
      amount: '',
      date: '',
      paymentType: '',
      description: ''
    });

    const isSidebarOpen = computed(() => isAddSidebarOpen.value || isEditSidebarOpen.value);

    const openAddSidebar = () => {
      isAddSidebarOpen.value = true;
    };

    const openEditSidebar = (item) => {
      editForm.value = { ...item };
      isEditSidebarOpen.value = true;
    };

    const closeSidebar = () => {
      isAddSidebarOpen.value = false;
      isEditSidebarOpen.value = false;
    };

    const handleAddSubmit = () => {
      console.log('Add Expense:', addForm.value);
      // Here you would typically make an API call to add the expense
      closeSidebar();
    };

    const handleEditSubmit = () => {
      console.log('Edit Expense:', editForm.value);
      // Here you would typically make an API call to update the expense
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
