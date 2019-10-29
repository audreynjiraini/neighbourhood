from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
       
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['neighbourhood', 'user']
        
        
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = []
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'neighbourhood']