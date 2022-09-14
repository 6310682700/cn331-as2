from audioop import reverse
from cgitb import html
from email import message
from http.client import HTTPResponse
import imp
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from base import models
from base.models import Class
from base.models import Student

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'users/index.html',{
        "Class" : Class.objects.all() 
        })
    

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))            
        else:
            return render(request, 'users/login.html', {
                'message': 'Invalid credentials.'
                })
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message': 'You have logged out.'
    })

def Regist(request, Username):
    if request.method == "POST":
        Student = Student.objects.get(pk = name)
        Student = Student.objects.get(pk=int(request.POST["Student"]))
        Student.Classs.add(Class)
        return HttpResponseRedirect("Class", args=(Student.name,))

