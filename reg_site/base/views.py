from audioop import reverse
from cgitb import html
from email import message
from http.client import HTTPResponse
from re import sub
import re
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Course, Student, Enroll



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

# load enroll.html and package

def enroll(request, student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    student = Student.objects.get(Student_Users_id=request.user.id)                         # User's student object
    course = Course.objects.all()                                                           # All courses
    if student.courses.all() != None:                                           
        enroll = Enroll.objects.filter(student_id=student.id)                               # Filter to only User's enroll
        unenroll = Course.objects.exclude(id__in=enroll.all().values_list('course_id'))     # Filter to only Course that didn't enroll by user
    return render(request, 'users/enroll.html', {
        "courses": course,
        "unenroll": unenroll,
        "enroll": student.courses.all(),
        "subjects": student,
    })

def search(request, student_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    student = Student.objects.get(Student_Users_id=request.user.id)                         # User's student object
    course = Course.objects.all()                                                           # All courses
    if student.courses != None:
        enroll = Enroll.objects.filter(student_id=student.id)                               # Filter to only User's enroll
        unenroll = Course.objects.exclude(id__in=enroll.all().values_list('course_id'))     # Filter to only Course that didn't enroll by user
        unenroll_search = unenroll.filter(Subject__icontains=request.POST["search"])        # Search the course that user didn't enroll
    return render(request, 'users/enroll.html', {
        "courses": course,
        "unenroll": unenroll_search,
        "enroll": student.courses.all(),
        "subjects": student,
    })

def enrollment(request, student_id):
    course = Course.objects.get(id=request.POST["Subject"])                                 # Get input from form
    student = Student.objects.get(Student_Users_id=student_id)
    Course.objects.filter(id=request.POST["Subject"]).update(capacity=course.capacity - 1)  # Subtract 1 the capacity from the selected course
    student.courses.add(course)
    return HttpResponseRedirect(reverse("enroll", args=(request.user.id,)))

def remove_enroll(request, student_id):
    course = Course.objects.get(id=request.POST["Subject"])                                 # Get input from form
    student = Student.objects.get(Student_Users_id=student_id)
    Course.objects.filter(id=request.POST["Subject"]).update(capacity=course.capacity + 1)  # Add 1 the capacity from the selected course
    student.courses.remove(course)
    return HttpResponseRedirect(reverse("enroll", args=(request.user.id,)))

