# from django.shortcuts import render, redirect 
# from pytube import *


# defining function 
# def youtube(request): 

# 	# checking whether request.method is post or not 
# 	if request.method == 'POST': 
		
# 		# getting link from frontend 
# 		link = request.POST['link'] 
# 		video = YouTube(link) 

# 		# setting video resolution 
# 		stream = video.streams.get_lowest_resolution() 
		
# 		# downloads video 
# 		stream.download() 

# 		# returning HTML page 
# 		return render(request, 'dashboard/dashboard.html') 
# 	return render(request, 'dashboard/dashboard.html')

""" added feature to download video"""
import os
from pytube import YouTube
from django.http import FileResponse
from django.shortcuts import render
from django.conf import settings

def download_video(request):
    video_url = request.GET.get('url')
    if not video_url:
        return render(request, 'dashboard/dashboard.html', {'error': 'Please provide a valid YouTube URL.'})

    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        video_file_path = stream.download(output_path=settings.MEDIA_ROOT)
        video_file_name = os.path.basename(video_file_path)

        response = FileResponse(open(video_file_path, 'rb'), as_attachment=True, filename=video_file_name)

        # Add attribute to response for cleanup in middleware
        response.cleanup_file = video_file_path

        return response

    except Exception as e:
        return render(request, 'dashboard/dashboard.html', {'error': str(e)})

