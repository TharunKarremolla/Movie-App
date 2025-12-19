
from django.contrib import admin
from django.urls import path
from .views import home ,theater_view,theater_details

urlpatterns = [
   

    path("",theater_view,name='theater_view'),
    path("<int:id>",theater_details,name='theater_details')
]    
