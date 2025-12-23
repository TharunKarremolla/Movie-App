from django.db import models
from movies.models import Movies
from theaters.models import Screen,Theater

# Create your models here.
class Show(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
  #  screen = models.ForeignKey(Screen,on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE)
    price = models.IntegerField()
    start_time = models.TimeField()