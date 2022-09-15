from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('Regist', views.Regist, name='Regist'),
    path('Remove',views.Remove,name='Remove'),
]