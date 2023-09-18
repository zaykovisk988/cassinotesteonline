
from django.urls import path
from MainGame import views

urlpatterns = [
    path('index/', views.index, name='index'),
]

