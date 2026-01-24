from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model): 
    title = models.CharField(max_length=75)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title