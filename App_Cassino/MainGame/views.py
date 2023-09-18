from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def login(request):
    return render(request, 'login.html')