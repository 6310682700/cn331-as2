from ast import ClassDef
from platform import mac_ver
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Class(models.Model):
    Subject = models.CharField(max_length=99)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.Subject} ({self.capacity})"

class Student(models.Model):
    enroll = models.ForeignKey(Class,on_delete=models.CASCADE)
    Student_Users = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.enroll}) {self.Student_Users}"


     