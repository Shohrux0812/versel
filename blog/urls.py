from django.urls import path
from .views import BlogListCreateView, BlogDetailView, MediaContentListCreateView, MediaContentDetailView

urlpatterns = [
    path('blog/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('media/', MediaContentListCreateView.as_view(), name='media-list-create'),
    path('media/<int:pk>/', MediaContentDetailView.as_view(), name='media-detail'),
]
