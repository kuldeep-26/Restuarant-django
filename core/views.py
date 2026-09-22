from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Avg, Count
from menu.models import MenuItem
from .models import (GalleryImage, Review)
from .forms import (ContactMessageForm, ReviewForm, )

def home(request):

    featured_items = MenuItem.objects.filter(is_available=True, is_popular=True)[:3]

    featured_reviews = Review.objects.filter(is_approved=True, is_featured=True)[:3]

    review_stats = Review.objects.filter(
        is_approved=True
    ).aggregate(
        average_rating=Avg('rating'),
        total_reviews=Count('id'),
    )

    return render(
        request,
        'core/home.html',
        {
            'featured_items': featured_items,
            'featured_reviews': featured_reviews,
            'review_stats': review_stats,
        }
    )

def about(request):
    
    return render(request, 'core/about.html')

def gallery(request):

    gallery_images = GalleryImage.objects.filter(is_active=True)
    return render(request, 'core/gallery.html', {'gallery_images': gallery_images})

def contact(request):

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been sent successfully! "
                "We'll get back to you soon."
            )
            return redirect('contact')
    else:
        form = ContactMessageForm()
    return render(request, 'core/contact.html', {'form': form})

def reviews(request):

    reviews = Review.objects.filter(is_approved=True)
    review_stats = reviews.aggregate(average_rating=Avg('rating'), total_reviews=Count('id'),)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for sharing your experience! "
                "Your review will appear after approval."
            )
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'core/reviews.html', {'reviews': reviews, 'form': form, 'review_stats': review_stats,})
