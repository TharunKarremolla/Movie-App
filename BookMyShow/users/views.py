from django.shortcuts import render,redirect
from django.urls import reverse
from django.http  import HttpResponse,JsonResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie,csrf_exempt
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

@ensure_csrf_cookie
def home(request):       
        return JsonResponse({"csrftoken" : 'get_token(request)' })


def logout_user(request):
    if request.user.id:
            
        logout(request)
        return JsonResponse({"Message" : 'User Logged Out' })
    return JsonResponse({"Message" : 'User Already Logged Out' })


def login_user(request):
        if request.method == "POST":
            try:
                data = json.loads(request.body)
                username = data.get("username")
                password = data.get('password')
                
            except:
                  return JsonResponse({'error':"Invalid"},status = 401)

            user = authenticate(username = username,password= password)

            if user is None:
                   return JsonResponse({'error':"User doesn't exist"},status = 401)
            login(request,user)
            return JsonResponse({'message':"User Logged In"},status = 200)
        return JsonResponse({'error':"User is not Logged In"},status = 401)        
       

def register_user(request):
        if request.method == "POST":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get('password')
            email = data.get('email')
            

            user = User.objects.create_user(username=username,password=password,email=email)

            user.save()
            return JsonResponse({"message" : f"Created User {user.username}"})

       
        return HttpResponse("Invalid HTTP method")
