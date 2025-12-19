from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100,null=False,blank=False)
    description = models.CharField(max_length=200,null=False,blank=False)
    release_date = models.DateField(null=True)
    poster = models.ImageField(upload_to='posters/',blank=True)

    def __str__(self):
        return self.title
    