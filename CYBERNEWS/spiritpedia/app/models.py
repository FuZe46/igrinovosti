from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', blank=True)  # Поле для хранения фотографии

    def str(self):
        return self.title