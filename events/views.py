from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from .models import Events, BookingRequest
from .forms import BookingForm

# Create your views here.
def about_events(request):

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.add_message(request, messages.SUCCESS, "Private event booking request received! I plan to respond within 2 working days.")

    events = events = Events.objects.all().first()
    booking_form = BookingForm()
    bookings = BookingRequest.objects.all()
    

    return render(
        request,
        "events/events.html",
        {
            "events": events,
            "booking_form": booking_form,
            "bookings": bookings,
        }
    )
