import os
import subprocess

def convert_480p(video_path):
    file_name, file_extension = os.path.splitext(video_path)
    new_video_path = file_name + '_480p' + file_extension
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(video_path, new_video_path)
    subprocess.run(cmd, shell=True)

def convert_720p(video_path):    
    file_name, file_extension = os.path.splitext(video_path)
    new_video_path = file_name + '_720p' + file_extension   
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(video_path, new_video_path)    
    run = subprocess.run(cmd, shell=True)