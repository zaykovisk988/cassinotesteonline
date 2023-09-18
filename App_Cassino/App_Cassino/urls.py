from django.contrib import admin
from django.urls import path
from MainGame import views

urlpatterns = [
    path('', views.login, name='login'),
]
