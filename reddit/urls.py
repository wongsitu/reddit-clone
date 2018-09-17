from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/<int:pk>', views.post_detail, name="post_detail"),
    path('posts/new', views.post_create, name="post_create"),
    path('posts/<int:pk>/comments/new', views.comment_create, name="comment_create"),
    path('comments/<int:pk>',views.comment_detail, name="comment_detail"),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name="user_login"),
    path('logout', views.user_logout, name='logout'),
    path('comments/<int:id>/delete', views.comment_delete, name='comment_delete'),
    path('comments/<int:id>/edit', views.comment_edit, name='comment_edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)