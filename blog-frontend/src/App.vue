<template>
  <!-- <Navbar /> -->
  <router-view /> <!-- Render the current route's component -->
</template>

<script>
import Navbar from './components/Layout/Navbar.vue';
export default {
  name: 'App',
  components: {
    Navbar
  }
};
</script>

<style>
/* You can style the root component here */
</style>
