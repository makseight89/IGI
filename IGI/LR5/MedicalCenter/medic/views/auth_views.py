from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from .utils.date_utils import get_user_time


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    return render(request, "auth/logout.html")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # New users are not immediately active
            user.save()
            # Send email/SMS to user for account activation
            return redirect("email_sent")
    else:
        form = CustomUserCreationForm()
    return render(request, "auth/register.html", {"form": form})


@login_required
def profile_view(request):
    user = request.user
    user_time_data = get_user_time()
    context = {"user": user, "user_time_data": user_time_data}
    return render(request, "auth/profile.html", context)
