from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    StudentUser = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    StudentCode = models.CharField(max_length=10, null=False, blank=False)
    StudentYear = models.IntegerField(null=True, blank=True)
    StudentSem = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.StudentUser.first_name

class Class(models.Model):
    ClassCode = models.CharField(max_length=10, primary_key=True)
    ClassName = models.CharField(max_length=100, null=False, blank=False)
    ClassYear = models.CharField(max_length=100, null=True, blank=True)
    ClassSem = models.CharField(max_length=100, null=True, blank=True)
    ClassCapacity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.ClassCode

class Enroll(models.Model):
    EnrollUser = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    EnrollClass = models.ForeignKey(Class, on_delete=models.CASCADE, null=False, blank=False)