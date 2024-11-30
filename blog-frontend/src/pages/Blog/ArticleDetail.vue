<template>
  <Navbar></Navbar>
  <div class="border rounded overflow-hidden mb-4 shadow-custom position-relative">
    <div class="d-flex justify-content-center align-items-center" style="height: 250px; overflow: hidden;">
      <img :src="article.cover" :alt="article.title" class="img-fluid rounded-top"
        style="width: 100%; height: 100%; object-fit: cover;">
    </div>
    <div class="p-4">
      <strong class="d-block mb-2 text-primary">{{ article.title }}</strong>
      <div class="mb-3" style="white-space: pre-line;">{{ article.content }}</div>
    </div>
    <div class="p-4">
      <h2>Comment</h2>
      <ul class="list-group text-left" style="margin-left: 0;">
        <li v-for="comment in comments" :key="comment.id" class="list-group-item">
          {{ comment.content }}
          <div class="comment-meta">
            {{ comment.user_name }} | {{ formatDate(comment.created_at) }}
          </div>
        </li>
      </ul>

      <!-- Add Comment Form -->
      <div class="mt-4">
        <h3>Add a Comment</h3>
        <form @submit.prevent="postComment">
          <div class="form-group">
            <textarea v-model="newComment" class="form-control" rows="3" placeholder="Write your comment..."
              required></textarea>
          </div>
          <button type="submit" class="btn btn-primary mt-2">Post Comment</button>
        </form>
      </div>
    </div>
  </div>


</template>

<script>
  import axios from 'axios';
  import Navbar from '../../components/Layout/Navbar.vue';
  export default {
    components: {
      Navbar
    },
    data() {
      return {
        article: {}, // Store article data
        newComment: "", // Two-way binding for new comment text
        comments: [],
        articleId: 0
      };
    },
    async created() {
      this.articleId = this.$route.params.id; // Get article ID from route
      try {
        const response = await axios.get(`http://127.0.0.1:5000/articles/${this.articleId}`);
        const comments = await axios.get(`http://127.0.0.1:5000/getComments/${this.articleId}`)
        this.comments = comments.data

        this.article = response.data; // Store article data
      } catch (error) {
        console.error('Error fetching article:', error);
      }
    },
    methods: {
      formatDate(dateString) {
        // Parse the date string
        const date = new Date(dateString);
        // Format as "YYYY-MM-DD HH:mm:ss"
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const hours = String(date.getHours()).padStart(2, '0');
        const minutes = String(date.getMinutes()).padStart(2, '0');
        const seconds = String(date.getSeconds()).padStart(2, '0');
        return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
      },
      async postComment() {
        const token = localStorage.getItem("access_token");
        if (!token) {
          alert("You must be logged in to post a comment.");
          return;
        }
        const articleId = this.$route.params.id; // Get the current article ID
        try {
          // Post the new comment to the API
          const response = await axios.post(`http://127.0.0.1:5000/addComments`, {
            content: this.newComment, // Send the comment content
            article_id: articleId
          }, {
            headers: {
              Authorization: `Bearer ${token}`, // Include JWT token
            },
          });
          const comments = await axios.get(`http://127.0.0.1:5000/getComments/${this.articleId}`)
          this.comments = comments.data
          // Clear the input field
          this.newComment = "";
        } catch (error) {
          console.error("Error posting comment:", error);
          alert("Failed to post comment. Please try again.");
        }
      }
    },
  };
</script>
<style>
  .comment-meta {
    text-align: right;
    margin-top: 8px;
    font-size: 0.9em;
    color: #6c757d;
  }

  textarea.form-control {
    resize: none;
    /* Prevent manual resizing */
  }

  button.btn {
    width: 100%;
    /* Optional: Make the button full-width for mobile responsiveness */
  }
</style>