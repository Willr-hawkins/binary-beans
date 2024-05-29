from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about_binary_beans(request):
    return HttpResponse('Hello coffee lovers!')