from django.shortcuts import render,redirect
from django.urls import reverse
from django.http  import HttpResponse,JsonResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from  .models import Theater

@ensure_csrf_cookie
def home(request):       
        return HttpResponse("hello")


@ensure_csrf_cookie
def theater_view(request):
    if request.method == 'GET':
          theaters = list(Theater.objects.all().values())
          print(theaters)
          return JsonResponse({"message" : theaters})

    elif request.method == 'POST':    
            if not request.user.is_staff:
                return JsonResponse({"message" : "Audience cannot ADD Theaters"})      
            data = json.loads(request.body)  
            name = data.get("name")
            location = data.get('location')
            screens = data.get("screens")
            capacity = data.get('capacity')                   
            theater = Theater(name = name,location = location, screens = screens,capacity = capacity)
            theater.save()
            return JsonResponse({'message':"New Theater Created"},status = 200)
    
@login_required
@ensure_csrf_cookie
def theater_details(request,id):
    if request.method == 'GET':
        try :
            theater = Theater.objects.filter(id = id).values().first()

        except: 
             return JsonResponse({"Error" : f"Theater with  id : {id} doesn't exist"})

        return JsonResponse({'message': theater },status = 200)
    
    elif request.method == 'PUT':
            if not request.user.is_staff:
                return JsonResponse({"message" : "Audience cannot ADD Theaters"})
            try:
                data = json.loads(request.body)
                name = data.get("name")
                location = data.get('location')
                screens = data.get("screens")
                capacity = data.get("capacity")
            except:
                  return JsonResponse({'error':"Invalid"},status = 401)
            theater = Theater.objects.filter(id = id).update(name = name,location = location, screens = screens,capacity = capacity)
            return JsonResponse({'message':  "updated"},status = 200)
    
    elif request.method == "DELETE":
          if not request.user.is_staff:
            return JsonResponse({"message" : "Audience cannot ADD Theaters"})
          theater = Theater.objects.filter(id=id).values().first()
          if not theater:
               return JsonResponse({"Error" : "Theater doesnt exist with the given id"},status=400)
          Theater.objects.filter(id=id).delete()
          return JsonResponse({"Deleted" : theater})


