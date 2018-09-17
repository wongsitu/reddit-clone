from django.contrib import admin
from .models import UserProfileInfo, Post, Comment
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Post)
admin.site.register(Comment)

