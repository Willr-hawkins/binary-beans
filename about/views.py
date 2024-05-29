from django.shortcuts import render
from django.views import generic
from .models import About

# Create your views here.
def about_store(request):
    return render(request,"about.html")
