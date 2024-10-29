#from videoflix.settings import CACHE_TTL

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
# # Create your views here.
# @cache_page(CACHE_TTL)
# def index(request):
#     return render(request, 'index.html')
import os
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import StreamingHttpResponse, Http404
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

def stream_video(request, video_id, resolution):
    resolutions = ['360p', '480p', '720p', '1080p']
    if resolution not in resolutions:
        raise Http404("Resolution not found")

    video_path = os.path.join(settings.MEDIA_ROOT, f"{video_id}_{resolution}.mp4")
    if not os.path.exists(video_path):
        raise Http404("Video not found", video)

    def file_iterator(file_name, chunk_size=8192):
        with open(file_name, "rb") as f:
            while (chunk := f.read(chunk_size)):
                yield chunk

    response = StreamingHttpResponse(file_iterator(video_path), content_type="video/mp4")
    response['Content-Disposition'] = f'inline; filename="{video_id}_{resolution}.mp4"'
    return response

@api_view(['GET'])
def video_overview(request):
    videos = Video.objects.all()
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)