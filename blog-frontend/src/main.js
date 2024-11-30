import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'; // Import router
import './index.css'; // Import TailwindCSS
import 'bootstrap/dist/css/bootstrap.min.css'; 
import 'bootstrap'; 

createApp(App).use(router).mount('#app');
