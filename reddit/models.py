from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    picture = models.FileField(upload_to='pictures',blank=True)
    content = models.TextField(blank=True)
    site_url = models.URLField(blank=True)
    vote_total = models.SmallIntegerField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
            return self.title

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    vote_total = models.SmallIntegerField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
            return self.user