import random
from django.core.files import File
import os
from .models import Video
from .tasks import convert_360p ,convert_480p, convert_720p, convert_1080p

def convert_video_files(video_file_path):
    convert_360p(video_file_path)
    convert_480p(video_file_path)
    convert_720p(video_file_path)
    convert_1080p(video_file_path)

def delete_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        return True
    return False

def delete_resolution_files(file_path):
    resolutions = ['_360p', '_480p', '_720p', '_1080p']
    for resolution in resolutions:
        file_name, file_extension = os.path.splitext(file_path)
        file_to_delete = file_name + resolution + file_extension
        delete_file(file_to_delete)
