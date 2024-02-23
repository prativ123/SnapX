from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from blog.models import *
# Create your views here.

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        send_updates = request.POST.get('send_updates')

        # Perform basic validation
        if not (username and email and password):
            messages.error(request, 'Please provide all required information.')
            return redirect('register')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Optionally handle sending updates
        if send_updates:
            # Add logic here to handle sending updates
            pass

        # Optionally log in the user automatically
        # login(request, user)

        messages.success(request, 'Account created successfully.')
        return redirect('register')

    return render(request, 'blog/index.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # if user.is_staff:
            #     return redirect('/admins/dashboard')
            # else:
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'blog/index.html')

def logout_user(request):
    logout(request)
    return redirect('/')