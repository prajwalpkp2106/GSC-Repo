from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError, send_mail
# Create your views here.
def home(request):
    return render(request,'index.html')


def send_email(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        msg = request.POST.get("msg", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone","")
        if name and msg and email and phone:
            try:
                message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}"
                send_mail(name, message, email, ["padoleprajwalextra@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("home")
        else:
            return HttpResponse("Make sure all fields are entered and valid.")
        
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('home')  # Redirect to the 'home' URL pattern
            
    return render(request, 'login.html')
def logout_page(request):
    logout(request)
    return redirect('home')

def register(request):
    
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        

        
        
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")
        
        return redirect('/register/')
        
    return render(request,'register.html')