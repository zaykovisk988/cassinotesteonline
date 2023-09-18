
from django.urls import path
from MainGame import views

urlpatterns = [
    path('', views.index, name='index.html'),
]

