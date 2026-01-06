
from django.contrib import admin
from django.urls import path
from .views import home, register_user ,login_user,logout_user
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView )

urlpatterns = [
   
    path("",home,name="home"),
    path("register/",register_user),
    path("login/",login_user),
    path("logout/",logout_user),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]    
