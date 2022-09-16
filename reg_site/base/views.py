from audioop import reverse
from cgitb import html
from email import message
from http.client import HTTPResponse
from re import sub
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Course, Student, Enroll


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    student = Student.objects.get(Student_Users_id=request.user.id)
    return render(request, 'users/index.html', {
        "courses": student.courses.all()
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


def enroll(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    student = Student.objects.get(Student_Users_id=request.user.id)
    course = Course.objects.all()
    return render(request, 'users/enroll.html', {
        "courses": course,
        "subjects": student,
    })


def enrollment(request, coures):
    if request.method == "POST":
        course = Course.objects.get(id=coures)
        student = Student.objects.get(Student_Users_id=request.user.id)
        student.course.add(course)
        return HttpResponseRedirect("index.html")
