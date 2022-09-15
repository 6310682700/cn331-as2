from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('regist', views.regist, name='regist'),
    path('remove',views.remove,name='remove'),
]