from . import views
from django.urls import path

urlpatterns = [
    path('', views.review_list, name="reviews"),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]