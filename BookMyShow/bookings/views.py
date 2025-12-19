from django.shortcuts import render,redirect
from django.urls import reverse
from django.http  import HttpResponse,JsonResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Bookings



@ensure_csrf_cookie
@csrf_exempt
def bookings_view(request):
    if request.method == 'GET':

        booking = Bookings.objects.filter(user_id = 2).select_related("movie").select_related('theater')

        if not booking:
              return JsonResponse({"Error" : f"No Bookings are made"})

        data = {
             "booking_id" : booking.id,
             "movie_title" : booking.movie.title,
             "Theater Name" : booking.theater.name,
             "Location" : booking.theater.location
        }

    
        return JsonResponse({'message': data },status = 200)


            

    if request.method == 'POST':    
            data = json.loads(request.body)  
            theater_id = data.get("theater")
            movie_id = data.get('movie')
            user_id = data.get("user")
            total_tickets = data.get('total_tickets')                   
            booking = Bookings(theater_id = theater_id,movie_id = movie_id, user_id = user_id,total_tickets = total_tickets)
            booking.save()
            return JsonResponse({'message':"New Bookings Created"},status = 200)
    
# @login_required
# @ensure_csrf_cookie
@csrf_exempt
def Booking_details(request):
    if request.method == 'GET':
        try :
            theater = Bookings.objects.filter(user_id = request.user.id).values().first()
            return JsonResponse({'message': theater },status = 200)

        except: 
             return JsonResponse({"Error" : f"No Bookings are made"})

#         return JsonResponse({'message': theater },status = 200)
    
#     elif request.method == 'PUT':
#             if not request.user.is_staff:
#                 return JsonResponse({"message" : "Audience cannot ADD Theaters"})
#             try:
#                 data = json.loads(request.body)
#                 name = data.get("name")
#                 location = data.get('location')
#                 screens = data.get("screens")
#                 capacity = data.get("capacity")
#             except:
#                   return JsonResponse({'error':"Invalid"},status = 401)
#             theater = Bookings.objects.filter(id = id).update(name = name,location = location, screens = screens,capacity = capacity)
#             return JsonResponse({'message':  "updated"},status = 200)
    
#     elif request.method == "DELETE":
#           if not request.user.is_staff:
#             return JsonResponse({"message" : "Audience cannot ADD Theaters"})
#           theater = Bookings.objects.filter(id=id).values().first()
#           if not Bookings:
#                return JsonResponse({"Error" : "Bookings doesnt exist with the given id"},status=400)
#           Bookings.objects.filter(id=id).delete()
#           return JsonResponse({"Deleted" : theater})
