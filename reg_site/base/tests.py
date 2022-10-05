from django.test import TestCase, client
from .models import Course, Student , Enroll
from django.urls import reverse 
from django.db.models import Max
from django.contrib.auth.models import User

class testModel(TestCase):

    def setUp(self):
        user = User.objects.create("non")
        course1 = Course.objects.create(Subject="AA",Subject_name = "A", Year = 1 ,Semester = 1, capacity = 1, status = True )
        course2 = Course.objects.create(Subject="BB",Subject_name = "B", Year = 1 ,Semester = 1, capacity = 1, status = True )

        student = Student.objects.create(
            Student_Users = user
        )

        enroll = Enroll.objects.create(
            Student = user , course= "course1"
        )

    def test_index_status(self):
        c = client()
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_registration(self):
        student = Student.objects.create("non")
        s = User.objects.first()
        s.capacity = 1
        s.save()

        c = client()
        response = c.get(reverse('users:enroll'))
        self.assertEqual(response.context['users'].count(), 1)

    def test_regist_page(self):
        c = client()
        response = c.get(reverse('users:enroll'))
        self.assertEqual(response.status_code, 200)