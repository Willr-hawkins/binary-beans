from .models import BookingRequest
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ('customer_name', 'customer_email', 'booking_date',)