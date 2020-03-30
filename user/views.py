from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm, PasswordChangeForm
from proje.views import get_cart_item, set_cart_item


def register(request):
    set_cart_item(0)
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username=username)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)

        return redirect("home")
    context = {
        "form": form
    }
    return render(request, "forms/register.html", context)


def loginUser(request):
    set_cart_item(0)
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, "forms/login.html", context)

        login(request, user)
        return redirect("home")
    return render(request, "forms/login.html", context)


def logoutUser(request):
    set_cart_item(0)
    logout(request)
    return redirect("home")


def profile(request, username):
    return render(request, "profile.html", {'cart_item': get_cart_item()})