from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=99)
    surname = models.CharField(max_length=99)
    studentid = models.CharField(max_length=10)

    def __str__(self):
        return f"({self.name} ({self.surname} {self.studentid})"

class Class(models.Model):
    subject = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="Subject")
    capacity = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="capacity")

    def __str__(self):
        return f"{self.subject} ({self.capacity})"