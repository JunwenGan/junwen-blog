<template>
    <div class="row container-fluid" >
        <div class="col-md-12">
            <h3 class="pb-4 mb-4 font-italic border-bottom">
                Dendi Blog
            </h3>
        </div>
        <div class="col-sm-12 col-md-12 row mt-2">
            <div class="col-md-12">
                <ArticleCard v-for="article in articles" :key="article.id" :article="article" />
            </div>
        </div>
        <!-- Pagination Component -->
        <Pagination :pagination="pagination" :totalPages="totalPages" :currentPage="currentPage" :endpoint="endpoint"
            @change="fetchPage" />
    </div>
</template>

<script>
import ArticleCard from "../../components/ArticleCard.vue";
import axios from "axios";
import Pagination from "../../components/Pagination.vue";

export default {
    name: "ArticlesIndex",
    components: {
        ArticleCard,
        Pagination,
    },
    data() {
        return {
            endpoint: "http://127.0.0.1:5000/articles", // Base API endpoint with Flask server
            articles: [],
            pagination: {
                next: null,
                previous: null,
            },
            totalPages: 1, // Total number of pages
            currentPage: 1, // Current page number
            pageSize: 5, // Number of articles per page
        };
    },
    async created() {
        // Fetch the first page on component mount
        this.fetchPage(1);
    },
    methods: {
        async fetchPage(page) {
            const url = this.buildUrl(page)
            if (typeof url !== "string") {
                console.error("Invalid URL emitted:", url);
                return;
            }

            console.log("Fetching page with URL:", url); // Log the valid emitted URL

            try {
                const response = await axios.get(url);
                this.articles = response.data.articles; // Assume API returns articles list in `articles`
                this.pagination = response.data.pagination; // Assume API returns pagination details
                this.totalPages = this.pagination.total_pages; // Update total pages
                this.currentPage = this.pagination.current_page; // Update current page
                console.log("Articles fetched successfully:", this.articles);
            } catch (error) {
                console.error("Error fetching articles:", error);
            }
        },
        buildUrl(page) {
            // Construct the API URL with page and limit parameters
            return `${this.endpoint}?page=${page}&limit=${this.pageSize}`;
        },
        
    },
};
</script>


<style scoped>
    /* Add styles if needed */
</style>