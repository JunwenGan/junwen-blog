<template>
    <div>
      <h1>Blog Articles</h1>
      <ul>
        <li v-for="article in articles" :key="article.id">
          <router-link :to="`/article/${article.id}`">
            {{ article.title }}
          </router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
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
  