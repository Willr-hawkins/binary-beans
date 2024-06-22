from django.test import TestCase
from .forms import BookingForm

class TestBookingForm(TestCase):

    def test_form_is_valid(self):
        """
        Test the form is valid.
        """
        booking_form = BookingForm({
            'customer_email': 'test@gmail.com',
            'booking_date': '2024-06-08',
            'event_title': 'Test Event',
            'event_description': 'This is a test event',
        })
        self.assertTrue(booking_form.is_valid(), msg='Form is not valid')

    def test_customer_email_is_required(self):
        """
        Test for the cutomer_email field.
        """
        booking_form = BookingForm({
            'customer_email': '',
            'booking_date': '2024-06-08',
            'event_title': 'Test Event',
            'event_description': 'This is a test event',
        })
        self.assertFalse(booking_form.is_valid(), msg='No customer email was provided')

    def test_booking_date_is_required(self):
        """
        Test for the booking_date field.
        """
        booking_form = BookingForm({
            'customer_email': 'test@gmail.com',
            'booking_date': ' ',
            'event_title': 'Test Event',
            'event_description': 'This is a test event',
        })
        self.assertFalse(booking_form.is_valid(), msg='No booking date was provided')

    def test_event_title_is_required(self):
        """
        Test for the event_title field.
        """
        booking_form = BookingForm({
            'customer_email': 'test@gmail.com',
            'booking_date': '2024-06-08',
            'event_title': ' ',
            'event_description': 'This is a test event',
        })
        self.assertFalse(booking_form.is_valid(), msg='No event title was provided')

    def test_event_description_is_required(self):
        """
        Test for the event_description field.
        """
        booking_form = BookingForm({
            'customer_email': 'test@gmail.com',
            'booking_date': '2024-06-08',
            'event_title': 'Test Event',
            'event_description': '',
        })
        self.assertFalse(booking_form.is_valid(), msg='No event description was provided')