<template>
  <div class="d-flex align-items-center justify-content-center vh-100 bg-light">
    <div class="card shadow p-4" style="width: 350px;">
      <h2 class="text-center mb-4">Login</h2>
      <form @submit.prevent="login">
        <!-- Username Input -->
        <div class="form-group mb-3">
          <label for="username" class="form-label">Username</label>
          <input
            type="text"
            id="username"
            class="form-control"
            v-model="username"
            placeholder="Enter your username"
            required
          />
        </div>

        <!-- Password Input -->
        <div class="form-group mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            id="password"
            class="form-control"
            v-model="password"
            placeholder="Enter your password"
            required
          />
        </div>

        <!-- Error Message -->
        <div v-if="error" class="alert alert-danger text-center mb-3">
          {{ error }}
        </div>

        <!-- Submit Button -->
        <button type="submit" class="btn btn-primary w-100">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post("http://127.0.0.1:5000/login", {
          username: this.username,
          password: this.password,
        });
        const token = response.data.access; // Save access token
        localStorage.setItem("session_token", token); // Store token in localStorage
        this.$router.push("/"); // Redirect to home page
      } catch (error) {
        this.error = "Invalid username or password";
      }
    },
  },
};
</script>

<style scoped>
body {
  margin: 0;
  font-family: Arial, sans-serif;
}
</style>
