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



class Profile(models.Model):
    
    name = models.CharField(max_length = 30)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        
        return self.name
    
    
    
class Business(models.Model):
    
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    description = models.TextField(null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)


    def __str__(self):
        
        return self.name
 
    
    
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        
        return self.title