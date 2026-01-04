from django.shortcuts import render,redirect
from django.urls import reverse
from django.http  import HttpResponse,JsonResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Bookings
from Show.models import Show

@login_required
def bookings_view(request):
    if request.method == 'GET':

        booking = Bookings.objects.select_related('show__movie').select_related('show__theater').filter(user_id = request.user.id)
      
        if not booking:
              return JsonResponse({"Error" : f"No Bookings are made"})
        data = []
        for item in booking:
            data.append({
                "booking_id" : item.id,
                "total_tickets" : item.total_tickets,
                'show' : item.show.start_time,
                'movie' : item.show.movie.title,
                "theater" : item.show.theater.name
            
            } )
        return JsonResponse({'message': data },status = 200)
    elif request.method == 'POST':    
            data = json.loads(request.body)  
            print(data)
            # user_id = request.user
            # total_tickets = data.get('total_tickets')
            # show = data.get('show')
            # booking = Bookings(show_id = show, user = user_id,total_tickets = total_tickets)
            # booking.save()
            # return JsonResponse({'message':"New Bookings Created",'id' : booking.id},status = 200)
    
    return JsonResponse({'message':"Invalid Method"})
    