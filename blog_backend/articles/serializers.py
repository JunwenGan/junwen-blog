from rest_framework import serializers  # Import Django REST Framework serializers
from .models import Article, Comment    # Import Article and Comment models
from django.contrib.auth.models import User

# Serializer for comments
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment  # Specify the Comment model
        fields = '__all__'  # Serialize all fields in the Comment model

# Serializer for articles
class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Serialize related comments (read-only)

    class Meta:
        model = Article  # Specify the Article model
        fields = '__all__'  # Serialize all fields in the Article model

# User Registration Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    # Custom create method to hash the password
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']  
        )
        return user