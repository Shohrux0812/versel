from django.contrib import admin
from .models import Blog, MediaContent

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(MediaContent)
class MediaContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'file')
    search_fields = ('title',)
