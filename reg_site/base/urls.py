from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
<<<<<<< HEAD
    path('logout', views.logout_view, name='logout'),    
    path('enroll', views.enroll, name='enroll'),
=======
    path('logout', views.logout_view, name='logout'),
    path('regist', views.regist, name='regist'),
    path('remove',views.remove,name='remove'),
>>>>>>> 805505f26bebf9e4cf09e4cc3710865e50dbb88d
]