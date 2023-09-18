from django.shortcuts import render

def index(request):
    return render (request, 'cassino_online/index.html')
