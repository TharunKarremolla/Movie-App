from django.db import models

# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    location = models.CharField(max_length=100,null=True)
    # screens = models.IntegerField(default=None)
    capacity = models.IntegerField(default=None)
    

    def __str__(self):
        return self.title
    

class Screen(models.Model):
    screen_number = models.IntegerField()
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE)
    total_seats = models.IntegerField()


class Seat(models.Model):
    seat_number = models.IntegerField()
    Screen = models.ForeignKey(Screen,on_delete=models.CASCADE)
    seat_type = models.CharField()