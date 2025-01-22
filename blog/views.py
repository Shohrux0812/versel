from rest_framework import generics
from .models import Blog, MediaContent
from .serializers import BlogSerializer, MediaContentSerializer

# Blog postlarini olish va yaratish
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Blog postini olish va o'chirish
class BlogDetailView(generics.RetrieveDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Media contentlarini olish va yaratish
class MediaContentListCreateView(generics.ListCreateAPIView):
    queryset = MediaContent.objects.all()
    serializer_class = MediaContentSerializer
    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return MediaContent.objects.filter(category=category)
        return MediaContent.objects.all()
    
# Media contentini olish va o'chirish
class MediaContentDetailView(generics.RetrieveDestroyAPIView):
    queryset = MediaContent.objects.all()
    serializer_class = MediaContentSerializer
