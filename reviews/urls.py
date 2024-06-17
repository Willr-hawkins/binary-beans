from . import views
from django.urls import path

urlpatterns = [
    path('', views.review_list, name="reviews"),
]