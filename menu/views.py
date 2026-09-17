from django.shortcuts import render
from .models import Category, MenuItem

def menu_list(request):

    categories = Category.objects.filter(is_active=True)

    menu_items = MenuItem.objects.filter(is_available=True).select_related('category')

    return render(request, 'menu/menu.html', {'categories': categories, 'menu_items': menu_items,})