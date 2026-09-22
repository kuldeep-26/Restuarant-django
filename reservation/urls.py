from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation, name='reservation'),
    path(
        'reservation/success/<uuid:confirmation_token>/',
        views.reservation_success,
        name='reservation_success'
    ),
]