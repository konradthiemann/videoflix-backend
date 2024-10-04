from .helpers import convert_video_files, delete_file, delete_resolution_files 
from .models import Video, export_videos
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import django_rq

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
     if created:
        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(convert_video_files, instance.video_file.path)

@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if not instance.video_file:
        return

    file_path = instance.video_file.path
    if not delete_file(file_path):
        return

    delete_resolution_files(file_path)

@receiver(post_save, sender=Video)
def export_videos_post_save(sender, instance, **kwargs):
    export_videos()