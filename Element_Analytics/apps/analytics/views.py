from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def file_home(request):
    return HttpResponse("Hello")
