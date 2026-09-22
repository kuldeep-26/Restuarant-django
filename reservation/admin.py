from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'date', 'time', 'guests', 'status', 'created_at', )
    list_filter = ('status', 'date', )
    search_fields = ('name', 'email', 'phone', )
    list_editable = ('status', )
    ordering = ('-date', '-time', )
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Customer Information', {'fields': ('name', 'email', 'phone',)}),
        ('Reservation Details', {'fields': ('date', 'time', 'guests', 'special_request',)}),
        ('Reservation Status', {'fields': ('status', 'created_at',)}),
    )