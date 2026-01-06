from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Show
from django.contrib.auth.decorators import login_required
import json

@login_required
def movies_by_theater(request,id):
    

    if request.method == "GET":
        
        # show = Show.objects.filter(movie=id).first()
        # title = show.movie.title
        
        shows = Show.objects.select_related('theater','movie').filter(movie=id).order_by('start_time')

        if not shows.exists():
            return JsonResponse({'timings': {}, 'title': None})
        title = shows.first().movie.title
        result = []
        timings = {}
        for show in shows:
            theater_name = show.theater.name
            if  theater_name not in timings:
                timings[theater_name]= []
            timings[theater_name].append({'id' : show.id, 'time' : show.start_time.strftime("%H:%M") ,"price" : show.price})
       
        
        return JsonResponse({'timings' : timings, 'title' : title})
    
    
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

