from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'blog'  # Explicitly specify the app_label

    def __str__(self):
        return self.title
