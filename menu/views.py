from django.shortcuts import render
from django.views import generic
from .models import Menu

# Create your views here.
def menu_list(request):

    menu = menu = Menu.objects.all().first()

    return render(
        request,
        "menu/menu.html",
        {
            "menu": menu,
        }
    )