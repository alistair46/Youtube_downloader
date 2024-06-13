# from django.contrib import admin 
# from django.urls import path 
# from . import views 

# urlpatterns = [ 
# 	path('admin/', admin.site.urls), 
# 	path('youtube/', views.download_video, name='youtube'), 
#]
from django.urls import path
from .views import download_video

urlpatterns = [
    path('download/', download_video, name='download_video'),
]

