from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myapp.models import Project, Donation
from users.models import Profile


@login_required
def view_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    projects = []
    donations = []
    return render(
        request,
        "users/view_profile.html",
        {
            "user": user,
            "profile": profile,
            "projects": projects,
            "donations": donations,
        },
    )


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("users/edit_profile.html")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "users/edit_profile.html", {"form": form})


@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("view_profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "users/edit_profile.html", {"profile": profile,"form":form})


@login_required
def delete_user(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("home")  # Redirect to home page after deletion
    return redirect("view_profile")


def redirect_view(request):

      return redirect("view_profile")