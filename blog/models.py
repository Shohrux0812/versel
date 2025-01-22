from django.db import models

# Blog post modelini yaratish
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Media content (media fayllar) modelini yaratish
class MediaContent(models.Model):
    CATEGORY_CHOICES = [
        ('lecture', 'Maruza'),
        ('practice', 'Amaliy ish'),
        ('lab', 'Laboratoriya'),
        ('other', 'Boshqalar'),
    ]
    title = models.CharField(max_length=255)  # Fayl nomi
    file = models.FileField(upload_to='uploads/')  # Fayl yuklanadigan joy
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Yuklangan sana
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return self.title
