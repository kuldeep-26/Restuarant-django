from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def reservation(request):

    if request.method == 'POST':
        form = ReservationForm(request.POST)

        if form.is_valid():
            reservation = form.save()

            email_body = render_to_string('reservations/reservation_confirmation.txt', {'reservation': reservation,})

            html_body = render_to_string('reservations/reservation_confirmation.html', {'reservation': reservation,})

            email = EmailMultiAlternatives(
            subject='Reservation Request Received - Brew & Bite',
            body=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[reservation.email],
            )

            email.attach_alternative(html_body, 'text/html')

            email.send()

            restaurant_email_body = render_to_string('reservations/new_reservation.html', {'reservation': reservation,})

            restaurant_email = EmailMultiAlternatives(
            subject='New Reservation - Brew & Bite',
            body=(
            f"New reservation from {reservation.name}. "
            f"{reservation.date} at {reservation.time} "
            f"for {reservation.guests} guests."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.RESTAURANT_EMAIL],
            )

            restaurant_email.attach_alternative(restaurant_email_body, 'text/html')

            restaurant_email.send()

            messages.success(request, "Your table reservation request has been submitted successfully.")

            return redirect('reservation_success', confirmation_token=reservation.confirmation_token)
    
    else:
        form = ReservationForm()

    return render(request, 'reservations/reservation.html', {'form': form})


def reservation_success(request, confirmation_token):

    reservation = get_object_or_404(
        Reservation,
        confirmation_token=confirmation_token
    )

    return render(request,'reservations/reservation_success.html',{'reservation': reservation})