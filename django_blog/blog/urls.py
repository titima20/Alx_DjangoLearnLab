from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]
