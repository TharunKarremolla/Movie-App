
from django.contrib import admin
from django.urls import path
from .views import movies_by_theater

urlpatterns = [
    path("movies/<int:id>/theaters/",movies_by_theater,name='movies_by_theater'),
    # path("<int:movie_id>/<int:theater_id>",show_times,name='show_times')
]    
