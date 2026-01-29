
from django.contrib import admin
from django.urls import path
from .views import home, register_user,LogoutView
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView )

urlpatterns = [
   
    path("",home,name="home"),
    path("register/",register_user),
  
    path("logout/",LogoutView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]    
