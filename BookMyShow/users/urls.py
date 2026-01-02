
from django.contrib import admin
from django.urls import path
from .views import home, register_user ,login_user,logout_user

urlpatterns = [
   
    path("",home,name="home"),
    path("register/",register_user),
    path("login/",login_user),
    path("logout/",logout_user),

]    
