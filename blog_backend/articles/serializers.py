from rest_framework import serializers  # Import Django REST Framework serializers
from .models import Article, Comment    # Import Article and Comment models
from django.contrib.auth.models import User

# Serializer for comments
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)  # Read-only field for username

    class Meta:
        model = Comment
        fields = ['id', 'content', 'article', 'user', 'created_at']

    def get_user(self, obj):
        return obj.user.username  # Return the username of the user

    def create(self, validated_data):
        request = self.context.get('request')  # Get the request object from the context
        user = request.user  # Get the currently authenticated user
        return Comment.objects.create(user=user, **validated_data)  # Associate comment with user

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