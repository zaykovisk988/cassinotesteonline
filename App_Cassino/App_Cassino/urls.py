from django.contrib import admin
from django.urls import path
from App_Cassino import views

urlpatterns = [
    path('', views.login.html, name='login'),
]