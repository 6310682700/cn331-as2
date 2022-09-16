from audioop import reverse
from cgitb import html
from email import message
from http.client import HTTPResponse
<<<<<<< HEAD
from re import sub
=======
import imp
from unicodedata import name
>>>>>>> 805505f26bebf9e4cf09e4cc3710865e50dbb88d
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from base import models
from base.models import Class
from base.models import Student

from .models import Course, Student, Enroll


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
<<<<<<< HEAD
    student = Student.objects.get(Student_Users_id=request.user.id)
    return render(request, 'users/index.html', {
        "courses": student.courses.all()
    })
=======
    return render(request, 'users/index.html',{
        "Class" : Class.objects.all() 
        })
>>>>>>> 805505f26bebf9e4cf09e4cc3710865e50dbb88d
    

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

<<<<<<< HEAD

def enroll(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    student = Student.objects.get(Student_Users_id=request.user.id)
    course = Course.objects.all()
    return render(request, 'users/enroll.html', {
        "courses": course,
        "subjects": student,
    })


def enroll(request, coures):
    if request.method == "POST":
        course = Course.objects.get(id=coures)
        student = Student.objects.get(Student_Users_id=request.user.id)
        student.course.add(course)
        return HttpResponseRedirect("index.html")
=======
def regist(request):
    if request.method == "POST":
        Enroll = Student.enroll.add(Class.Subject)
        Class.capacity = Class.capacity + 1
        return render(request, 'index.html', {
            "Enrollment" : Enroll
    })

def remove(request):
    if request.method == "POST":
        Enroll = Student.enroll.remove(Class.Subject)
        Class.capacity = Class.capacity - 1
        return render(request, 'index.html', {
            "Enrollemnt" : Enroll
    })


>>>>>>> 805505f26bebf9e4cf09e4cc3710865e50dbb88d
