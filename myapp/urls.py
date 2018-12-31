from django.urls import path
from . import views
from . views import (PostListView,
PostDetailView,
PostCreateView,
PostUpdateView,
PostDeleteView,
UserPostListView
)

urlpatterns = [
    path(r'', PostListView.as_view(), name='index'),
    path(r'user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path(r'about/', views.about, name='about'),
    path(r'post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path(r'post/new/', PostCreateView.as_view(), name='post-create'),
    path(r'post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path(r'post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]