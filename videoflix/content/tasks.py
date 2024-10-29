import os
import subprocess

def convert_360p(video_path, video_id):
    print('Converting video to 360p')
    file_name, file_extension = os.path.splitext(video_path)
    directory = os.path.dirname(video_path)
    new_video_path = os.path.join(directory, f'{video_id}_360p{file_extension}')
    print("video_path:", video_path)  # Debugging line
    print("file_name path:", file_name)  # Debugging line

    # Set resolution to 640x360 for 360p
    cmd = 'ffmpeg -y -i "{}" -s 640x360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(video_path, new_video_path)
    subprocess.run(cmd, shell=True)
    return new_video_path

def convert_480p(video_path, video_id):
    print('Converting video to 480p')
    file_name, file_extension = os.path.splitext(video_path)
    directory = os.path.dirname(video_path)
    new_video_path = os.path.join(directory, f'{video_id}_480p{file_extension}')

    # Set resolution to 854x480 for 480p
    cmd = 'ffmpeg -i "{}" -s 854x480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(video_path, new_video_path)
    subprocess.run(cmd, shell=True)
    return new_video_path

def convert_720p(video_path, video_id):    
    print('Converting video to 720p')
    file_name, file_extension = os.path.splitext(video_path)
    directory = os.path.dirname(video_path)
    new_video_path = os.path.join(directory, f'{video_id}_720p{file_extension}')

    # Set resolution to 1280x720 for 720p
    cmd = 'ffmpeg -i "{}" -s 1280x720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(video_path, new_video_path)
    subprocess.run(cmd, shell=True)
    return new_video_path

def convert_1080p(video_path, video_id):    
    print('Converting video to 1080p')
    file_name, file_extension = os.path.splitext(video_path)
    directory = os.path.dirname(video_path)
    new_video_path = os.path.join(directory, f'{video_id}_1080p{file_extension}')

    # Set resolution to 1920x1080 for 1080p
    cmd = 'ffmpeg -i "{}" -s 1920x1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(video_path, new_video_path)
    subprocess.run(cmd, shell=True)
    return new_video_path
