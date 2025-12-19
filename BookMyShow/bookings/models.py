from django.db import models

# Create your models here.
from theaters.models import Theater
from django.contrib.auth.models import User
from movies.models import Movies

class Bookings(models.Model):
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    total_tickets =  models.IntegerField()

