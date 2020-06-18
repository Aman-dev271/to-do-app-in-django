from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.messages import add_message, get_messages
from django.contrib import messages
from django.contrib.auth import authenticate, login as authorize, logout as dauth

# Create your views here.
def login(request):
    if (request.method == 'POST'):
        form = AuthenticationForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password=password)
        if user is None:
            messages.info(request,"The username and password doesn't match")
            return redirect('/user/login')
        else:
            authorize(request, user)
            return redirect('/user/profile')
            


    else:
        if(request.user.is_authenticated):
            return redirect('/user/profile/')

        form =  AuthenticationForm()
    return render(request, 'login.html', {'titile':'titale login page','form':form})
def register(request):
    form =UserCreationForm()
  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User is successfully Registered ')
            return redirect('/user/login')

    return render(request, 'register.html', {'titile':'title of Register page ', 'form':form})


def logout(request):
    if request.user.is_authenticated:
        dauth(request)
        messages.info(request, 'You are successfully logged Out')
    return redirect('/user/login')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'title':'title of profile page'})
    else:
        messages.info(request, 'You need to login first with valid account')
        return redirect('/user/login/')