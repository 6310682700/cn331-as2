<<<<<<< HEAD
from enum import unique
=======
from ast import ClassDef
from platform import mac_ver
from pyexpat import model
from tkinter import CASCADE
>>>>>>> 805505f26bebf9e4cf09e4cc3710865e50dbb88d
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

<<<<<<< HEAD
class Course(models.Model):
    Subject = models.CharField(max_length=99)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.Subject} ({self.capacity})"
    
class Student(models.Model):
    courses = models.ManyToManyField(Course, blank=True, through='Enroll')
    Student_Users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Student_Users}"

class Enroll(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['student', 'course']]

=======
class Class(models.Model):
    Subject = models.CharField(max_length=99)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.Subject} ({self.capacity})"
    
class Student(models.Model):
    enroll = models.ManyToManyField(User, related_name="Student", blank=True)
    Student_Users = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"({self.enroll}) {self.Student_Users}"
>>>>>>> 805505f26bebf9e4cf09e4cc3710865e50dbb88d
