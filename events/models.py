from django.db import models
from django.contrib.auth.models import User


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
    Stores a single request for a private event realted to :model:`auth.User
    """
    customer_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer'
    )
    customer_email = models.EmailField()
    booking_date = models.DateField()
    event_title = models.CharField(max_length=300)
    event_description = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Private event booking request from {self.customer_name}"