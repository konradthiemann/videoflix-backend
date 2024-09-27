from django.urls import path
from .views import stream_video 

urlpatterns = [
    path('stream/<str:video_id>/<str:resolution>/', stream_video, name='stream_video'),
]