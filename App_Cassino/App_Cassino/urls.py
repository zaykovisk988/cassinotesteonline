from django.contrib import admin
from django.urls import path
from MainGame import views

urlpatterns = [
    path('login/', views.login.html, name='login'),
]


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    
]
