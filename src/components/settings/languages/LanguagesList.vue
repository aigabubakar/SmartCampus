<template>
  <div class="mt-24">
    <div class="card h-100">
      <div class="card-body p-0 dataTable-wrapper">
        <div class="d-flex align-items-center justify-content-between flex-wrap gap-16 px-20 py-12 border-bottom border-neutral-200">
          <div class="d-flex flex-wrap align-items-center gap-16">
            <div class="dropdown">
              <button type="button" class="px-12 py-5-px border border-neutral-300 radius-8 d-flex align-items-center gap-20 " data-bs-toggle="dropdown" aria-expanded="false">
                <span class="d-flex align-items-center gap-1 text-secondary-light text-sm">
                  <i class="ri-file-upload-line text-md line-height-1"></i>
                  Export
                </span>
                <span class="">
                  <i class="ri-arrow-down-s-line"></i>
                </span>
              </button>
              <ul class="dropdown-menu p-12 border bg-base shadow">
                <li>
                  <button type="button" class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10">
                    <i class="ri-file-3-line"></i>
                    PDF
                  </button>
                </li>
                <li>
                  <button type="button" class="dropdown-item px-16 py-8 rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-10">
                    <i class="ri-file-excel-line"></i>
                    Excel
                  </button>
                </li>
              </ul>
            </div>
            <form class="navbar-search dt-search m-0" @submit.prevent>
              <input type="text" class="dt-input bg-transparent radius-4" aria-controls="dataTable" name="search" placeholder="Search...">
              <iconify-icon icon="ion:search-outline" class="icon"></iconify-icon>
            </form>
          </div>
          <div class="d-flex align-items-center gap-8 text-secondary-light">
            <span class="">Rows per page:</span>
            <div class="dt-length">
              <select name="dataTable_length" aria-controls="dataTable" class="dt-input form-control form-select">
                <option value="5">5</option>
                <option value="10">10</option>
                <option value="25">25</option>
                <option value="50">50</option>
                <option value="100">100</option>
              </select>
            </div>
          </div>
        </div>

        <div class="p-0">
          <div class="table-responsive">
            <table class="table bordered-table mb-0 data-table" id="dataTableLanguages">
              <thead>
                <tr>
                  <th scope="col">
                    <div class="form-check style-check d-flex align-items-center">
                      <input class="form-check-input" type="checkbox" @change="toggleAll">
                      <label class="form-check-label">S.L</label>
                    </div>
                  </th>
                  <th scope="col">Name</th>
                  <th scope="col">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(language, index) in languages" :key="index">
                  <td>
                    <div class="form-check style-check d-flex align-items-center">
                      <input class="form-check-input" type="checkbox" v-model="language.selected">
                      <label class="form-check-label">{{ String(index + 1).padStart(2, '0') }}</label>
                    </div>
                  </td>
                  <td>{{ language.name }}</td>
                  <td>
                    <div class="btn-group">
                      <button type="button" class="text-primary-light text-xl" data-bs-toggle="dropdown" data-bs-display="static" aria-expanded="false">
                        <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
                      </button>
                      <ul class="dropdown-menu dropdown-menu-lg-end border p-12">
                        <li>
                          <button type="button" class="edit-sidebar-btn dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6" @click="$emit('edit-language', language)">
                            <i class="ri-edit-2-line"></i>Edit
                          </button>
                        </li>
                        <li>
                          <button class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2 py-6" type="button" @click="$emit('delete-language', language)">
                            <i class="ri-delete-bin-6-line"></i>Delete
                          </button>
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
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from 'vue';

export default {
  name: "LanguagesList",
  emits: ['edit-language', 'delete-language'],
  setup(props, { emit }) {
    const languages = ref([
      { name: 'English(Default)', selected: false },
      { name: 'Spanish', selected: false },
      { name: 'French', selected: false },
      { name: 'German', selected: false },
      { name: 'Chinese', selected: false },
      { name: 'Japanese', selected: false },
      { name: 'Korean', selected: false },
      { name: 'Arabic', selected: false },
      { name: 'Hindi', selected: false },
      { name: 'Portuguese', selected: false },
      { name: 'Russian', selected: false },
      { name: 'Italian', selected: false }
    ]);

    const toggleAll = () => {
      const allSelected = languages.value.every(language => language.selected);
      languages.value.forEach(language => {
        language.selected = !allSelected;
      });
    };

    onMounted(async () => {
      await nextTick();
      if (typeof $ !== 'undefined' && $.fn.DataTable) {
        $('.data-table').each(function () {
          const $table = $(this);

          if ($table.hasClass('dataTable-initialized')) return;

          let tableInstance = $table.DataTable({
            pageLength: 10,
            columnDefs: [{ orderable: false, targets: [0, 2] }]
          });

          $table.addClass('dataTable-initialized');

          $table.closest('.dataTable-wrapper').find('.dt-search .dt-input').on('keyup', function () {
            tableInstance.search(this.value).draw();
          });

          $table.closest('.dataTable-wrapper').find('.dt-length .dt-input').on('change', function () {
            const value = $(this).val();
            tableInstance.page.len(value).draw();
          });
        });
      }
    });

    return {
      languages,
      toggleAll
    };
  }
}
</script>
