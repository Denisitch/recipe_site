from django.shortcuts import render, redirect
from apps.users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages


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
