from django.contrib import admin
from django.urls import path, include
from . import views
from students import views
urlpatterns = [
    path('',views.home, name="index"),
    path('index',views.home, name="index"),
    path('signup',views.signup, name="signup"),
    path('nav',views.nav, name="nav"),
    path('signin',views.signin, name="signin"),
    path('signout',views.signout, name="signout"),
    path('students_detail',views.students_detail, name="students_detail"),
    path('enroll/', views.enroll, name='enroll'),
    path('delete/', views.delete, name='delete'),
    path('editprofile/', views.editprofile, name='editprofile')
]