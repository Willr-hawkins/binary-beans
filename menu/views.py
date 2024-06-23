from django.shortcuts import render
from django.views import generic
from .models import Menu, EventMenus

# Create your views here.
def menu_list(request):

    menu = Menu.objects.all().first()
    event_menus = EventMenus.objects.all()

    return render(
        request,
        "menu/menu.html",
        {
            "menu": menu,
            "event_menus": event_menus,
        }
    )