from django.db import models

# Create your models here.

class Menu(models.Model):
    """
    Stores the menu information for the menu page.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class EventMenus(models.Model):
    """
    Stores the event menus information for the menu page.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title