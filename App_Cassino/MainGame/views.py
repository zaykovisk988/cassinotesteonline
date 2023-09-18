from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import path


def index(request):
    return HttpResponse, ('index.html')


def login(request):
    return HttpRequest, ('login.html')
