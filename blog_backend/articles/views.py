from rest_framework import generics, permissions
from .models import Article, Comment  # Import models
from .serializers import ArticleSerializer, CommentSerializer  # Import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny, IsAdminUser

# List and create articles
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()  # Fetch all articles from the database
    serializer_class = ArticleSerializer  # Use the Article serializer
    # permission_classes = [IsAuthenticated]

# Retrieve, update, and delete a single article
class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()  # Fetch all articles from the database
    serializer_class = ArticleSerializer  # Use the Article serializer

# List and create comments
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()  # Fetch all comments from the database
    serializer_class = CommentSerializer  # Use the Comment serializer
    permission_classes = [IsAuthenticated]
    
    # def get_queryset(self):
    #     return super().get_queryset()
    # def get_permissions(self):

    #     self.permission_classes = [AllowAny]
    #     if self.request.method == 'POST':
    #         self.permission_classes = [IsAuthenticated]
    #     return super().get_permissions()


    def get_serializer_context(self):

        # Provide the request to the serializer context
        return {'request': self.request}

# User Registration API
class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
