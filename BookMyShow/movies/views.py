from django.shortcuts import render,redirect
from django.urls import reverse
from django.http  import HttpResponse,JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Movies
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.timezone import now
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser,IsAuthenticated


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def movies_view(request):

    if request.method == 'GET':
        # cache_key = "movies:list"
        # cached_response = cache.get(cache_key)
        

        # if cached_response:
        #     return JsonResponse({'data' :cached_response},safe=False)
        movies = Movies.objects.all()
        print(movies)
        result = []
        for movie in movies:              
            result.append({
                    "id" : movie.id,
                    "title" : movie.title,
                    "description" : movie.description,
                    "poster" : request.build_absolute_uri(movie.poster.url) if movie.poster else None,
                    "release_date" : movie.release_date,
                    "rating": movie.rating,
                    "language" : movie.language,
                    "duration" : movie.duration
            })
        # cache.set(cache_key,result,300)
    
        
        return JsonResponse({"data" : result,"time":now() } )
    
    elif request.method == 'POST':    
            if not request.user.is_staff:
                return JsonResponse({"message" : "You don't have access to ADD movies"})        
            title = request.POST.get("title")
            description = request.POST.get('description')
            release_date = request.POST.get("release_date")
            rating = request.POST.get("rating")
            language = request.POST.get("language")
            duration = request.POST.get("duration")
            poster = request.FILES.get('poster')   
            poster = poster if poster else None                
            movie = Movies(title = title,description = description, release_date = release_date,poster = poster, rating = rating, duration = duration,language = language)
            movie.save()
            return JsonResponse({'message':"Movie Added"},status = 200)
    
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def movie_detail(request,id):
    if request.method == 'GET':
        try :
            movie = Movies.objects.get(id = id)
        except: return JsonResponse({"Error" : f"Image with  id : {id} doesn't exist"})
        
        data = {
        "id": movie.id,
        "title": movie.title,
        "description": movie.description,
        "release_date": movie.release_date,
        "poster": request.build_absolute_uri(movie.poster.url)
    }
        return  render(request,'./app/home.html',{"data" : data } )#JsonResponse({'message': data},status = 200)
    
    elif request.method == 'PUT':
            if not request.user.is_staff:
                return JsonResponse({"message" : "You don't have access to update movies"})
            try:
                data = json.loads(request.body)
                title = data.get("title")
                description = data.get('description')
                release_date = data.get("release_date")
            except:
                  return JsonResponse({'error':"Invalid"},status = 401)
            movie = Movies.objects.filter(id = id).update(title = title,description = description , release_date = release_date)
            return JsonResponse({'message':  "updated"},status = 200)
    
    elif request.method == 'PATCH':
        if not request.user.is_staff:
            return JsonResponse({"message" : "You don't have access to update movies"})
        try:
            data = json.loads(request.body)
            title = data.get("title")
            description = data.get('description')
            release_date = data.get("release_date")
        except:
                return JsonResponse({'error':"Invalid"},status = 401)
        movie = Movies.objects.filter(id = id).update(title = title,description = description , release_date = release_date)
        return JsonResponse({'message':  "updated"},status = 200)
    
    elif request.method == "DELETE":
          if not request.user.is_staff:
            return JsonResponse({"message" : "You don't have access to delete movies"})
          movie = Movies.objects.filter(id=id).values().first()
          Movies.objects.filter(id=id).delete()
          return JsonResponse({"message" : movie})


