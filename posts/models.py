from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length=75, blank=True, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title or f"Post by {self.author.username} on {self.date.strftime('%Y-%m-%d')}"


class PostImage(models.Model):
    """Store multiple images for a post"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='posts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['uploaded_at']
    
    def __str__(self):
        return f"Image for {self.post.title}"