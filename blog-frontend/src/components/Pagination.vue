<template>
    <nav aria-label="Page navigation">
      <ul class="pagination justify-content-center">
        <!-- Previous Button -->
        <li
          class="page-item"
          :class="{ disabled: currentPage === 1 }"
        >
          <button
            class="page-link"
            @click="changePage(currentPage - 1)"
            :disabled="currentPage === 1"
          >
            Previous
          </button>
        </li>
  
        <!-- Page Numbers -->
        <li
          v-for="page in pages"
          :key="page"
          class="page-item"
          :class="{ active: currentPage === page }"
        >
          <button
            class="page-link"
            @click="changePage(page)"
          >
            {{ page }}
          </button>
        </li>
  
        <!-- Next Button -->
        <li
          class="page-item"
          :class="{ disabled: currentPage === totalPages }"
        >
          <button
            class="page-link"
            @click="changePage(currentPage + 1)"
            :disabled="currentPage === totalPages"
          >
            Next
          </button>
        </li>
      </ul>
    </nav>
  </template>
  
  <script>
  export default {
    name: "Pagination",
    props: {
      totalPages: { type: Number, required: true },
      currentPage: { type: Number, required: true },
    },
    computed: {
      pages() {
        const pages = [];
        for (let i = 1; i <= this.totalPages; i++) {
          pages.push(i);
        }
        return pages;
      },
    },
    methods: {
      changePage(page) {
        if (page >= 1 && page <= this.totalPages) {
          this.$emit("change", page); // Emit the new page number to the parent
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .page-item.disabled .page-link {
    pointer-events: none;
    color: #6c757d;
  }
  .page-item.active .page-link {
    background-color: #007bff;
    border-color: #007bff;
    color: white;
  }
  </style>
  