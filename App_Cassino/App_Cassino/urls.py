
from django.contrib import admin
from django.urls import include, path
from MainGame import views

urlpatterns = [
    path('index/', views.index, name='index'),
]
# sss5
