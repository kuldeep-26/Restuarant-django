from django.contrib import admin
from .models import (GalleryImage, ContactMessage, Review, )

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'is_featured', 'is_active', 'created_at',)
    list_filter = ('category', 'is_featured', 'is_active',)
    search_fields = ('title',)
    list_editable = ('is_featured', 'is_active', )

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'subject', 'is_read', 'created_at', )
    list_filter = ('is_read', 'created_at', )
    search_fields = ('name', 'email', 'subject', 'message', )
    list_editable = ('is_read', )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'rating', 'is_approved', 'is_featured', 'created_at', )
    list_filter = ('rating', 'is_approved', 'is_featured', )
    search_fields = ('name', 'comment', )
    list_editable = ('is_approved', 'is_featured', )