<template>
    <div>
      <h1>{{ article.title }}</h1>
      <p>{{ article.content }}</p>
      <h2>Comments</h2>
      <ul>
        <li v-for="comment in article.comments" :key="comment.id">
          {{ comment.content }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        article: {}, // Store article data
      };
    },
    async created() {
      const articleId = this.$route.params.id; // Get article ID from route
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/articles/${articleId}/`);
        this.article = response.data; // Store article data
      } catch (error) {
        console.error('Error fetching article:', error);
      }
    },
  };
  </script>
  