from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    user = request.user
    
    try:
        profile = Profile.objects.get(user = user)
        
    except:
        profile = Profile.objects.create(user = user, name = user.username)
        profile.save()
        
    posts = Post.objects.filter(neighbourhood = profile.neighbourhood)
    businesses = Business.objects.filter(neighbourhood = profile.neighbourhood)
    neighbourhood = profile.neighbourhood
    
    return render(request, 'index.html', {"posts": posts, "businesses": businesses, "neighbourhood": neighbourhood})