from django.shortcuts import render,redirect
from django.urls import reverse
from django.http  import HttpResponse,JsonResponse
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@ensure_csrf_cookie
def home(request):       
        return HttpResponse("hello")


def logout_user(request):
      logout(request)
      return redirect("home")


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
            is_staff = data.get('is_staff')

            user = User.objects.create_user(username=username,password=password,email=email,is_staff = is_staff)

            user.save()
            return JsonResponse({"message" : f"Created User {user.username}"})

       
        return HttpResponse("hello woel")
