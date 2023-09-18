
from django.contrib import admin
from django.urls import include, path
from MainGame import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
# 22
