<template>
    <div
        class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-custom h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static col-md-8">
            <strong class="d-inline-block mb-2 text-primary">{{ article.category }}</strong>
            <h3 class="mb-0">{{ article.title }}</h3>
            <div class="mb-1 text-muted">{{ article.created_at }}</div>
            <p class="card-text">{{ article.description}}</p>
            <!-- <div class="d-flex justify-content-between">
                <router-link
                    :to="{
                        name: 'posts.show',
                        params: {
                            category: post.category.slug,
                            slug: post.slug
                        }
                    }"
                    class="stretched-link"
                >Continue reading</router-link>
                <span> {{ article.visits_count }} views </span>
            </div> -->
            <div class="d-flex justify-content-between">
                <router-link :to="`/article/${article.id}`" class="stretched-link">
                    Continue reading
                </router-link>
                <!-- <NavigateButton  :to="`/article/${article.id}`" class="stretched-link" >
                    Continue reading
                </NavigateButton> -->
                <!-- <span> {{ article.visits_count }} views </span> -->
            </div>

        </div>
        <div class="col-auto d-none d-lg-block col-md-4">
            <div class="d-flex justify-content-center align-items-center" style="height: 100%;">
                <img :src="article.cover" :alt="article.title" class="img-fluid rounded"
                    style="max-width: 100%; height: auto; object-fit: cover;">
            </div>
        </div>
    </div>
</template>

<script>
    import NavigateButton from './NavigateButton.vue';
    export default {
        name: "Article",
        components: {
            NavigateButton
        },
        props: {
            article: {
                type: Object,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>