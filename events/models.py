from django.db import models

# Create your models here.

class Events(models.Model):
    """
    Stores the events information for the events page.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title