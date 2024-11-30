<template>
    <div>
      <Navbar></Navbar>
      <!-- <h1 class="text-2xl font-bold">Blog Articles</h1>
      <p class="mt-2">This is a sample application using Vue 3 and TailwindCSS.</p> -->
      <ArticleIndex></ArticleIndex>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  import ArticleIndex from './Blog/ArticleIndex.vue';
  import Navbar from '../components/Layout/Navbar.vue';
  export default {
    components: {
      Navbar, 
      ArticleIndex
  },
    data() {
      return {
        articles: [], // Store articles
      };
    },
    async created() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/articles/'); // Fetch articles from API
        this.articles = response.data.results; // Store articles
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    },
  };
  </script>
  