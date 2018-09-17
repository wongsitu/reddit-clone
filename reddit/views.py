from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserProfileInfoForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

# Create your views here.

# --------------VIEWS-----------------

def index(request):
    posts = Post.objects.all()
    return render(request, 'reddit/index.html', {'posts': posts})

# --------------POSTS-----------------

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.all()
    return render(request,'reddit/post_detail.html', {'post': post ,'comment': comments})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            if 'pictures' in request.FILES:
                post.picture = request.FILES['pictures']
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'reddit/post_form.html', {'form': form})

# --------------COMMENTS-----------------

@login_required
def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'reddit/comment_form.html', {'form': form})

@login_required
def comment_edit(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'reddit/comment_form.html', {'form': form})

@login_required
def comment_detail(request,pk):
    comment = Comment.objects.get(id=pk)
    return render(request,'reddit/comment_detail.html', {'comment': comment })

@login_required
def comment_delete(request, id):
    Comment.objects.get(id=id).delete()
    return redirect('index')

# ----------AUTHENTICATION--------------

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'reddit/registration.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'reddit/login.html', {})