from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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

