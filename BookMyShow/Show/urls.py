
from django.contrib import admin
from django.urls import path
from .views import show_times

urlpatterns = [
    path("",show_times,name='show_list'),
    path("<int:movie_id>/<int:theater_id>",show_times,name='show_times')
]    
