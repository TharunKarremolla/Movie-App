from django.shortcuts import render,redirect
from django.urls import reverse
from django.http  import HttpResponse,JsonResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Movies


@ensure_csrf_cookie
def movies_view(request):

    if request.method == 'GET':
          movies = Movies.objects.all()
          
          data = []
          for movie in movies:              
                data.append({
                      "id" : movie.id,
                      "title" : movie.title,
                      "description" : movie.description,
                      "poster" : request.build_absolute_uri(movie.poster.url) if movie.poster else None,
                      "release_date" : movie.release_date
                })
          return JsonResponse({"data" : data } )
    
    elif request.method == 'POST':    
            if not request.user.is_staff:
                return JsonResponse({"message" : "Audience cannot ADD movies"})        
            title = request.POST.get("title")
            description = request.POST.get('description')
            release_date = request.POST.get("release_date")
            poster = request.FILES.get('poster')                   
            movie = Movies(title = title,description = description, release_date = release_date,poster = poster)
            movie.save()
            return JsonResponse({'message':"Movie Added"},status = 200)
    
@login_required
@ensure_csrf_cookie
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
                return JsonResponse({"message" : "Audience cannot ADD movies"})
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
            return JsonResponse({"message" : "Audience cannot ADD movies"})
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
            return JsonResponse({"message" : "Audience cannot ADD movies"})
          movie = Movies.objects.filter(id=id).values().first()
          Movies.objects.filter(id=id).delete()
          return JsonResponse({"message" : movie})


