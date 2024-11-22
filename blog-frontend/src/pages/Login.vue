<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="login">
        <label>
          Username:
          <input type="text" v-model="username" />
        </label>
        <label>
          Password:
          <input type="password" v-model="password" />
        </label>
        <button type="submit">Login</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: null,
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/token/', {
            username: this.username,
            password: this.password,
          });
          const token = response.data.access; // Save access token
          localStorage.setItem('token', token); // Store token in localStorage
          this.$router.push('/'); // Redirect to home page
        } catch (error) {
          this.error = 'Invalid username or password';
        }
      },
    },
  };
  </script>
  