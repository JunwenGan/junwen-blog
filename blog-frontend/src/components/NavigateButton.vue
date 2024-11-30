<template>
    <button @click="navigate" class="btn btn-link stretched-link" >
      <slot></slot>
    </button>
  </template>
  
  <script>
  export default {
    name: 'NavigateButton',
    props: {
      to: {
        type: String,
        required: true,
      },
    },
    methods: {
      navigate() {
        this.$router.push(this.to); 
      },
    },
  };
  </script>
  
  <style scoped>

  </style>
  