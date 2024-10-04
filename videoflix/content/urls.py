from django.urls import path
from .views import stream_video, video_overview

urlpatterns = [
    path('stream/<str:video_id>/<str:resolution>/', stream_video, name='stream_video'),
    path('videos/', video_overview, name='video_overview')
]