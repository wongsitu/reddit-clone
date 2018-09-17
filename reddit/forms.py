from django import forms
from .models import UserProfileInfo, Post, Comment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','picture','content')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)