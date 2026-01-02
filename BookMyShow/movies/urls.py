
from django.contrib import admin
from django.urls import path
from .views import movie_detail,movies_view

urlpatterns = [
   
    path("",movies_view,name='movies'),
    path("<int:id>/",movie_detail,name='movie_detail')
]    
