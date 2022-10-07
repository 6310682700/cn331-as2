from ast import arg
from django.test import TestCase, Client
from .models import Course, Student , Enroll
from django.urls import reverse 
from django.db.models import Max
from django.contrib.auth.models import User

class testView(TestCase):

    def setUp(self):
        User.objects.create(username = "non", password = "idkanything")
        Course.objects.create(Subject="AA",Subject_name = "A", Year = 1 ,Semester = 1, capacity = 1, status = True )
        Course.objects.create(Subject="BB",Subject_name = "B", Year = 1 ,Semester = 1, capacity = 0, status = True )

        Student.objects.create(Student_Users = User.objects.first())

        Enroll.objects.create(student = Student.objects.first() , course = Course.objects.first())

    def test_login(self):
        self.client = Client()
        response = self.client.post(reverse('login'), {"username": "non", "password": "idkanything"})
        self.assertEqual(response.status_code, 200)
        

    def test_logout(self):
        self.client = Client()
        response = self.client.post(reverse('login'), {"username": "non", "password": "idkanything"})
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        
    
    def test_regist(self):
        sub = Course.objects.first()
        s = Student.objects.first()

        c = Client()
        c.post(reverse('enrollment' , args=[s.id]), { 'student_id' : s.id, 'Subject': sub.id, } ,)
        self.assertEqual(Course.objects.get(Subject= sub.Subject).capacity, 0)
        

    def test_remove(self):
        sub = Course.objects.get(pk= 2)
        s = Student.objects.first()

        c = Client()
        c.post(reverse('remove_enroll' , args=[s.id]), { 'student_id' : s.id, 'Subject': sub.id,  } ,)
        self.assertEqual(Course.objects.get(Subject= sub.Subject).capacity, 1)


    def test_search(self):
        s = Student.objects.first()
        c = Course.objects.first()
        self.client.force_login(s.Student_Users)
        find = self.client.post(reverse('search', args=[s.id]), {"search" : 'CN331'}).context['courses']
        self.assertEqual(find[0].Subject, c.Subject )








