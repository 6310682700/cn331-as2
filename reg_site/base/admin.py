from calendar import c
from turtle import st
from django.contrib import admin
from .models import Student, Class

# Register your models here.

admin.site.register(Student)
admin.site.register(Class)
