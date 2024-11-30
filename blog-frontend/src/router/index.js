import { createRouter, createWebHistory } from 'vue-router';

// Define routes
const routes = [
  { path: '/', component: () => import('../pages/Home.vue') }, // Home page
  { path: '/article/:id', component: () => import('../pages/Blog/ArticleDetail.vue') }, // Article detail page
  { path: '/login', component: () => import('../pages/Login.vue') }, // Login page
];

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
