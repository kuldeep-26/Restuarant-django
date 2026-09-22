from django import forms
from datetime import date, time
from django.db.models import Sum
from .models import Reservation

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation

        fields = ['name', 'email', 'phone', 'date', 'time', 'guests', 'special_request',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'autocomplete': 'name',}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'autocomplete': 'email',}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number', 'autocomplete': 'tel',}),
            'date': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat(),}),
            'time': forms.TimeInput(attrs={'type': 'time',}),
            'guests': forms.NumberInput(attrs={'min': 1, 'max': 20, 'placeholder': 'Number of Guests',}),
            'special_request': forms.Textarea(attrs={'placeholder': 'Any special requests? (Optional)', 'rows': 5,}),
        }

    def clean_date(self):
        
        reservation_date = self.cleaned_data.get('date')
        if reservation_date and reservation_date < date.today():
            raise forms.ValidationError("Please select today or a future date.")
        return reservation_date


    def clean_guests(self):

        guests = self.cleaned_data.get('guests')
        if guests is None:
            return guests

        if guests < 1:
            raise forms.ValidationError("There must be at least 1 guest.")

        if guests > 20:
            raise forms.ValidationError("Reservations are limited to 20 guests.")

        return guests


    def clean_time(self):

        reservation_time = self.cleaned_data.get('time')

        if not reservation_time:
            return reservation_time

        opening_time = time(11, 0)
        closing_time = time(22, 0)

        if not opening_time <= reservation_time <= closing_time:
            raise forms.ValidationError("Reservations are available between 11:00 AM and 10:00 PM.")

        return reservation_time


    def clean(self):

        cleaned_data = super().clean()

        reservation_date = cleaned_data.get('date')
        reservation_time = cleaned_data.get('time')
        guests = cleaned_data.get('guests')

        if not reservation_date or not reservation_time or not guests:
            return cleaned_data

        MAX_SLOT_CAPACITY = 20

        existing_guests = Reservation.objects.filter(
            date=reservation_date,
            time=reservation_time,
            status__in=['pending', 'confirmed'],
        ).aggregate(
            total_guests=Sum('guests')
        )['total_guests'] or 0

        if existing_guests + guests > MAX_SLOT_CAPACITY:

            raise forms.ValidationError(
                "Sorry, this time slot is currently full. "
                "Please choose another time."
            )

        return cleaned_data