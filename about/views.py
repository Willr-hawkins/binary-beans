from django.shortcuts import render
from django.views import generic
from .models import About


# Create your views here.
def about_store(request):

    about = About.objects.all().first()

    return render(
        request,
        "about.html",
        {
            "about": about,
        }
    )
