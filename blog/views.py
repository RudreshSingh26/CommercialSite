from django.http import HttpResponse
from django.shortcuts import render
# python manage.py runserver

def index(request):
    return render(request,'blog/index.html')



