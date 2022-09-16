from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),    
    path('<int:student_id>/', views.enroll, name='enroll'),
    path('<int:student_id>/enrollment', views.enrollment, name='enrollment'),
    path('<int:student_id>/remove_enroll', views.remove_enroll, name='remove_enroll'),
]