from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Location(models.Model):
    
    name = models.CharField(max_length = 30)

    def __str__(self):
        
        return self.name
    
    
    
class Neighbourhood(models.Model):
    
    name = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants = models.IntegerField(null=True, default=0)
    
    
    def __str__(self):
        
        return self.name