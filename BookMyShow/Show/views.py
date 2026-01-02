from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Show
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
import json


def movies_by_theater(request,id):
    

    if request.method == "GET":
        # print(request.)
        
        shows = list(Show.objects.filter(movie=id).values())
        
        return JsonResponse({"shows": shows})
    
    
    elif request.method == 'POST':    
            if not request.user.is_staff:
                return JsonResponse({"message" : "You don't have access to ADD Shows"})   
            movie_id = request.GET.get('movie')
            theater_id = request.GET.get('theater')
            data = json.loads(request.body)  
            price = data.get('price')
            start_time = data.get('start_time')
            
            show = Show(price = price, start_time = start_time, movie_id = movie_id,theater_id = theater_id)
            show.save()
            return JsonResponse({'message':"New Shows Created"},status = 200)

