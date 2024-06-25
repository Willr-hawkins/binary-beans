from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_events, name='events'),
    path(
        'booking/edit/<int:booking_id>/',
        views.edit_booking,
        name='edit_booking'
    ),
    path(
        'booking/delete/<int:booking_id>/',
        views.delete_booking,
        name='delete_booking'
    ),
]
