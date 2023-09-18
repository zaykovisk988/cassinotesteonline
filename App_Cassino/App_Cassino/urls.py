from django.contrib import admin
from django.urls import path
from MainGame import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('login/', views.login, name='login.html')
]

