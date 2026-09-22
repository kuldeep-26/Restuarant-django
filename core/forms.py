from django import forms
from .models import (ContactMessage, Review, )
from datetime import date

class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message...','rows': 6}),
        }

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review

        fields = ['name', 'rating', 'comment', ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'rating': forms.Select(),
            'comment': forms.Textarea(attrs={'placeholder': 'Share your experience...', 'rows': 5}),
        }
