from django.db import models
from theaters.models import Theater,Seat
from django.contrib.auth.models import User
from movies.models import Movies
from Show.models import Show

class Bookings(models.Model):
    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('confirmed', 'Confirmed'),
    ('cancelled', 'Cancelled'),
]

    user =  models.ForeignKey(User,on_delete=models.CASCADE)
    total_tickets =  models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    show  = models.ForeignKey(Show,on_delete=models.CASCADE)
    #status = models.CharField(max_length=50, choices=STATUS_CHOICES,default=None)
    #seats = models.ForeignKey(Seat,on_delete=models.CASCADE,default=None)
    
    

