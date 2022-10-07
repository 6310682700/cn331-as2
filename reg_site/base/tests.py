from django.test import TestCase, client
from .models import Course, Student , Enroll
from django.urls import reverse 
from django.db.models import Max
from django.contrib.auth.models import User

class testModel(TestCase):

    def setUp(self):
        User.objects.create(username = "non")
        Course.objects.create(Subject="AA",Subject_name = "A", Year = 1 ,Semester = 1, capacity = 1, status = True )
        Course.objects.create(Subject="BB",Subject_name = "B", Year = 1 ,Semester = 1, capacity = 0, status = True )

        Student.objects.create(
            Student_Users = User.objects.first()
        )

        Enroll.objects.create(
            student = Student.objects.first() , course= Course.objects.first()
        )

    def test_capacity_availible(self):
        course = Course.objects.first()
        self.assertEqual(course.capacity, 1)
        

    def test_capacity_non_availible(self):
        course = Course.objects.get(pk = 2)
        self.assertEqual(course.capacity, 0)
        
    
        