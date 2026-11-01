<template>
  <div class="modal fade" id="exampleModalDelete" tabindex="-1" aria-hidden="true" ref="deleteModal">
    <div class="modal-dialog modal-sm modal-dialog modal-dialog-centered max-w-340-px">
      <div class="modal-content radius-16 bg-base">
        <div class="modal-body pt-32 px-36 pb-24 text-center">
          <span class="mb-16 fs-1 line-height-1 text-danger">
            <iconify-icon icon="fluent:delete-24-regular" class="menu-icon"></iconify-icon>
          </span>
          <h6 class="text-lg fw-semibold text-primary-light mb-0">Are you sure you want to delete this currency?</h6>
          <div class="d-flex align-items-center justify-content-center gap-3 mt-24">
            <button type="button" class="flex-grow-1 border border-danger-600 bg-hover-danger-200 text-danger-600 text-md px-24 py-11 radius-8" data-bs-dismiss="modal">
              Cancel
            </button>
            <button type="button" class="flex-grow-1 btn btn-primary-600 border border-primary-600 text-md px-16 py-12 radius-8" @click="confirmDelete">
              Yes, Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "DeleteCurrencyModal",
  emits: ['confirm-delete'],
  methods: {
    confirmDelete() {
      // In a real implementation, you'd hide the modal programmatically here or rely on data-bs-dismiss
      // For now, let's emit the event and assume the parent handles the actual deletion logic
       // and potentially closing the modal if controlled via JS.
       // Since it depends on bootstrap's JS, we might need to manually hide it if we want to be clean.
      this.$emit('confirm-delete');
      
      // Optional: Close modal using bootstrap API if needed, or rely on the user clicking cancel/clicking away for now.
      // But typically "Yes" should close it too.
      // const modalEl = document.getElementById('exampleModalDelete');
       // const modal = bootstrap.Modal.getInstance(modalEl);
       // if (modal) modal.hide();
    }
  }
}
</script>
