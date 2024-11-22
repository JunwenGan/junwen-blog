from django.urls import path  # Import Django's URL module
from .views import (          # Import views
    ArticleListCreateView,
    ArticleRetrieveUpdateDestroyView,
    CommentListCreateView,
    UserRegisterView
)


urlpatterns = [
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),  # API for listing and creating articles
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),  # API for retrieving, updating, and deleting a single article
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),  # API for listing and creating comments
    path('register/', UserRegisterView.as_view(), name='user-register'),
]
