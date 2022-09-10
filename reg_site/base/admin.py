from calendar import c
from turtle import st
from django.contrib import admin
from .models import Student, Class, Enroll

# Register your models here.

admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Enroll)