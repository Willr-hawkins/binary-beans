from django.contrib import admin
from .models import Events, BookingRequest

# Register your models here.
admin.site.register(Events)
admin.site.register(BookingRequest)
