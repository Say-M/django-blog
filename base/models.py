from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    featured_image = models.ImageField(upload_to='./assets/images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    comment = models.TextField(max_length=5000)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='followed_user')
    created_at = models.DateTimeField(auto_now_add=True, null=True)