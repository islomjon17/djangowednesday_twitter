from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def profile_list(request): 
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)   
        return render(request, 'profile_list.html', {"profiles":profiles})
    
    else:
        messages.success(request, ("You have to log in"))
        return render(request, 'home.html', {})