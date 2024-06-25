from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import generic
from .models import Events, BookingRequest
from .forms import BookingForm


# Create your views here.
def about_events(request):

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.customer_name = request.user
            booking.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Booking Request recieved! Awaiting approval."
            )

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


def edit_booking(request, booking_id):
    booking = get_object_or_404(
        BookingRequest,
        id=booking_id,
        customer_name=request.user
        )

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking request updated successfully!")
            return redirect('events')

    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        'events/edit_booking.html',
        {'form': form, 'booking': booking}
    )


def delete_booking(request, booking_id):
    booking = get_object_or_404(
        BookingRequest,
        id=booking_id,
        customer_name=request.user
    )

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking request deleted successfully!")
        return redirect('events')

    return render(request, 'events/delete_booking.html', {'booking': booking})
