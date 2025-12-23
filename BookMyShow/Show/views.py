from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Show
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
import json

@csrf_exempt
def index(request):
    return HttpResponse("shows")

@csrf_exempt
def show_times(request,movie_id=None,theater_id=None):

    if request.method == "GET":
        shows = list(Show.objects.all().values())
        
        return JsonResponse({"shows": shows})
    
    
    elif request.method == 'POST':    
            if not request.user.is_staff:
                return JsonResponse({"message" : "You don't have access to ADD Shows"})     
            data = json.loads(request.body)  
            price = data.get('price')
            start_time = data.get('start_time')
            
            show = Show(price = price, start_time = start_time, movie_id = movie_id,theater_id = theater_id)
            show.save()
            return JsonResponse({'message':"New Bookings Created"},status = 200)

