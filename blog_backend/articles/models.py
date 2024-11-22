from django.db import models  # Import Django's model module

# Article model
class Article(models.Model):
    title = models.CharField(max_length=200)  # Article title, max length is 200 characters
    content = models.TextField()              # Article content with no length limit
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

    def __str__(self):
        return f"Comment on {self.article.title}"  # Return the associated article title for the comment
