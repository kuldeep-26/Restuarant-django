from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, f"Welcome to Restuarant, {user.username}! Your account has been created.")
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(
        request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):

    if request.method == 'POST':

        user = request.user
        user.first_name = request.POST.get('first_name', '').strip()
        user.last_name = request.POST.get('last_name', '').strip()
        user.email = request.POST.get('email', '').strip()

        user.save()

        messages.success(request, "Your profile has been updated successfully.")
        return redirect('profile')

    return render(request, 'accounts/profile.html')