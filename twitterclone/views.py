from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import MeepForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms




# Create your views here.


def home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                meep = form.save(commit=False)
                meep.user = request.user
                meep.save()
                messages.success(request, ("Yout meep has been posted!"))
                return redirect('home') 
        
        meeps = Meep.objects.all().order_by("-created_at")
        return render(request, 'home.html', {'meeps':meeps, 'form':form})
    else:
        meeps = Meep.objects.all().order_by("-created_at")
        return render(request, 'home.html', {'meeps':meeps})

def profile_list(request): 
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)   
        return render(request, 'profile_list.html', {"profiles":profiles})
    
    else:
        messages.success(request, ("You have to log in"))
        return render(request, 'home.html', {})



def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        meeps = Meep.objects.filter(user_id=pk)
        

        # POST form method
        if request.method == "POST":
            # Get current user
            current_user_profile = request.user.profile
            # Ger from data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action  == "unfollow":
                current_user_profile.follows.remove(profile)
            else:
                current_user_profile.follows.add(profile)
            # Save the changes
            current_user_profile.save()

        return render(request, 'profile.html', {'profile':profile, 'meeps':meeps})
    else:
        messages.success(request, ("You have to log in"))
        return redirect(home)
    
    
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been loged in"))
            return redirect(home)
    else:
        messages.success(request, ("Error, Please try again!"))
        return render(request, 'login.html', {})   
    return render(request, 'login.html', {})



    
def logout_user(request):
    return render(logout_user, 'logout_user.html', {})



def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name =  form.cleaned_data['first_name']
            # second_name =  form.cleaned_data['second_name']
            # email =  form.cleaned_data['email']
            # Login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been signed up!!!"))
            return redirect('home')
    return render(request, 'register.html', {'form':form})
