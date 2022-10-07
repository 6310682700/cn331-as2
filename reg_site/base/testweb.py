from django.test import TestCase, Client
from .models import Course, Student , Enroll
from django.urls import reverse 
from django.db.models import Max
from django.contrib.auth.models import User

class testWeb(TestCase):

    def setUp(self):
        User.objects.create(username = "non")
        Course.objects.create(Subject="AA",Subject_name = "A", Year = 1 ,Semester = 1, capacity = 1, status = True )
        Course.objects.create(Subject="BB",Subject_name = "B", Year = 1 ,Semester = 1, capacity = 0, status = True )

        Student.objects.create(Student_Users = User.objects.first())

        Enroll.objects.create(student = Student.objects.first() , course = Course.objects.first())

    def test_index_status(self):
        c = Client()
        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 302)
        
    

    def test_regist_page(self):
        c = Client()
        student = Student.objects.first()
        response = c.get(reverse('enroll', args=(student.pk,)))
        self.assertEqual(response.status_code, 302)
        

    def test_login_status(self):
        c = Client()
        response = c.get(reverse('login'))
        self.assertEqual(response.status_code, 200)    


        