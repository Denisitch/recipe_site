from django.shortcuts import render, redirect
from django.views.generic import DetailView

from apps.users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages

from apps.users.models import User


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect("home")
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы успешно авторизовались")
            return redirect("home")
        else:
            messages.error(request, "Ошибка авторизации")
    else:
        form = UserLoginForm
    return render(request, "users/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


class UserView(DetailView):
    model = User
    template_name = "users/user.html"
    context_object_name = "item_user"
