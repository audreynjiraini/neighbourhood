from django.shortcuts import render, redirect
from .models import *
from .forms import *
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
    
    return render(request, 'index.html', {"posts": posts, "profile": profile, "businesses": businesses, "neighbourhood": neighbourhood})


@login_required(login_url='/accounts/login')
def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        
        profile = Profile.objects.get(user = request.user)
        search_term = request.GET.get("business")
        searched_businesses = Business.objects.filter(neighbourhood = profile.neighbourhood, name__icontains = search_term)
        
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "businesses": searched_businesss})

    else:
        message = "You haven't searched for any business"
        
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login')
def business(request):
    
    profile = Profile.objects.get(user = request.user)
    businesses = Business.objects.filter(neighbourhood = profile.neighbourhood)
        
    return render(request, 'business.html', {"businesses": businesses})


@login_required(login_url='/accounts/login')
def new_business(request):
    
    profile = Profile.objects.get(user = request.user)
    
    if request.method == 'POST':
        
        form = BusinessForm(request.POST)
        
        if form.is_valid():
            
            business = form.save(commit = False)
            business.user = profile
            business.neighbourhood = profile.neighbourhood
            business.save()
            
        return redirect('business')
    
    else:
        
        form = BusinessForm()
        
    return render(request, 'new_business.html', {'form': form})


@login_required(login_url='/accounts/login')
def post(request, id):
    
    post = Post.objects.get(id = id)
    
    return render(request, 'post.html', {"post": post})


@login_required(login_url='/accounts/login')
def new_post(request):
    
    profile = Profile.objects.get(user = request.user)
    
    if request.method == 'POST':
        
        form = PostForm(request.POST)
        
        if form.is_valid():
            
            post = form.save(commit = False)
            post.user = request.user
            post.neighbourhood = profile.neighbourhood
            post.save()
            
        return redirect('index')
    
    else:
        
        form = PostForm()
        
    return render(request, 'new_post.html', {"profile": profile, "form": form})


@login_required(login_url='/accounts/login')
def profile(request, username):
    
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    businesses = Business.objects.filter(user = profile)
    
    return render(request, 'profile.html', {"profile": profile, "businesses": businesses})


@login_required(login_url='/accounts/login')
def edit_profile(request,username):
    
    profile = Profile.objects.get(user = request.user)
    
    if request.method == 'POST':
        
        form = ProfileForm(request.POST, instance = profile)
        
        if form.is_valid():
            
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            
        return redirect('profile', username = request.user)
    
    else:
        
        if Profile.objects.filter(user = request.user):
            
            profile = Profile.objects.get(user = request.user)
            form = ProfileForm(instance = profile)
            
        else:
            form = ProfileForm()
   
    return render(request, 'edit_profile.html', {"form":form})