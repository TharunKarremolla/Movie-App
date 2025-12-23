
from django.contrib import admin
from django.urls import path
from .views import index,show_times

urlpatterns = [
   

    path("index/",index,name='index_view'),
    path("",show_times,name='show_times'),
    path("<int:movie_id>/<int:theater_id>",show_times,name='show_times')
]    
