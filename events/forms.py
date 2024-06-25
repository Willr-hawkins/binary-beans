from .models import BookingRequest, EventMenus
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        model = BookingRequest
        fields = (
            'customer_email',
            'booking_date',
            'event_title',
            'event_description',
            'menu',
        )
        widgets = {'booking_date': DateInput, }
