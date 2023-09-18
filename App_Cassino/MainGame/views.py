from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request):
    return HttpResponse, ('index.html')


def login(request):
    return HttpRequest, ('login.html')
