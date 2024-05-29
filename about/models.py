from django.db import models

# Create your models here.

class About(models.Model):
    """
    Stores the about information for the home page.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title