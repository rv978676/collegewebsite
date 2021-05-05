from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('login/',views.Login,name="Login"),
    path('register/',views.Register,name="Register"),
    path('Exam/<int:id>/',views.Exam,name="Exam"),
    path('Subject/<int:id>/',views.Subject,name="Subject"),
    path('Department',views.Department,name="Department"),
    path('about',views.queries,name="about"),
    path('logout',views.logout,name="logout"),
]