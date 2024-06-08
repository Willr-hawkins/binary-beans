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


class BookingRequest(models.Model):
    """
    Stores a single request for a private event
    """
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Private event booking request from {self.customer_name}"