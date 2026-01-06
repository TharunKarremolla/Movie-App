from django.db import models
from movies.models import Movies
from theaters.models import Screen,Theater

# Create your models here.
class Show(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
 
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE)
    price = models.IntegerField()
    start_time = models.TimeField()
    #name = models.CharField(default="name")
    show_date = models.DateField(auto_now_add=True,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Show"
    
    class Meta:
        db_table = "shows"