<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path
from MainGame import views

urlpatterns = [
    path('index', include('index.urls')),