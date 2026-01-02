
from django.contrib import admin
from django.urls import path
from .views import  bookings_view
urlpatterns = [
   
    path("",bookings_view,name="Bookings")
]    
