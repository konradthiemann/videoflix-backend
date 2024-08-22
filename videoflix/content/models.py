from django.db import models
import datetime

# Create your models here.
class Video(models.Model):
    # created_at = models.DateTimeField(default=date.today)
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(
        default=datetime.date.today
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos', null=True, blank=True)

    def __str__(self):
        return self.title