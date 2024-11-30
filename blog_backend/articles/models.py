from django.db import models  # Import Django's model module
from django.contrib.auth.models import User

# Article model
class Article(models.Model):
    title = models.CharField(max_length=200)  # Article title, max length is 200 characters
    content = models.TextField()              # Article content with no length limit
    category = models.CharField(max_length=100, default="Uncategorized")  # Article category, default is 'Uncategorized'
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)  # Article cover image, optional
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation timestamp
    updated_at = models.DateTimeField(auto_now=True)      # Automatically update the timestamp when modified

    def __str__(self):
        return self.title  # Return the article title when printing the object


# Comment model
class Comment(models.Model):
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE
    )  # Link the comment to an article; delete all comments when the article is deleted
    content = models.TextField()               # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the comment creation timestamp
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)  # Link to auth_user

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"  # Display username and partial content
