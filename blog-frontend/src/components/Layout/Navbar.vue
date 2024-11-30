<template>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <router-link class="navbar-brand" to="/">DENDI Blog</router-link>

            <div>
                <span v-if="!session_token" @click="login" class="btn btn-outline-primary btn-sm mx-1">Login</span>
                <span v-else @click="logout" class="btn btn-outline-danger btn-sm mx-1">Logout</span>
            </div>
            <!-- <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor03" aria-controls="navbarColor03" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button> -->

            <!-- <div class="collapse navbar-collapse" id="navbarColor03">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="postsDropdownLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Posts
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <router-link class="dropdown-item" :to="{ name: 'posts.index' }">Latest posts</router-link>
                            <router-link class="dropdown-item" :to="{ name: 'posts.index', query: { popular: '1'} }">Popular posts</router-link>
                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="categoriesDropdownLink" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Categories
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                            <router-link class="dropdown-item" :key="category.id" v-for="category in categories"
                                :to="{name: 'categories.index', params: { category: category.slug } }"
                            >{{ category.name }}</router-link>
                        </div>
                    </li>
                </ul>
                <PostSearch/>
            </div> -->
        </div>
    </nav>
    <!-- End navbar -->
</template>

<script>
    //  import PostSearch from "../../../components/PostSearch";
    export default {
        name: "Navbar",
        data() {
            return {
                session_token: localStorage.getItem('session_token')
            };
        },
        methods: {
            logout() {
                // Clear token from localStorage
                localStorage.removeItem("session_token");

                // Update the component's session_token state
                this.session_token = null;

                // Optionally redirect to the login page or home
                this.$router.push("/");
            },
            login() {
                this.$router.push("/login");
            }
        },
        components: {},
        computed: {

        }
    }
</script>

<style scoped>

</style>