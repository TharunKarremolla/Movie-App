
from django.contrib import admin
from django.urls import path
from .views import  bookings_view,Booking_details
urlpatterns = [
   
    path("",bookings_view,name="Bookings_view"),
  

    #path("details/",Booking_details,name='Booking_details'),
    # path("movies/<int:id>",movie_detail,name='movie_detail')
]    
