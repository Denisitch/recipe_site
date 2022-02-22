from django.shortcuts import render, redirect
from django.views.generic import DetailView

from apps.users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib import messages

from apps.users.models import User


def register(request):
    """
    User registration view
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)
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
    """
    User authorization view
    """
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
    """
    User logout view
    """
    logout(request)
    return redirect("login")


class UserView(DetailView):
    """
    User Detail View
    """

    model = User
    template_name = "users/user.html"
    context_object_name = "item_user"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context["title"] = "Пользователь"

        user = User.objects.get(pk=self.kwargs["pk"])
        context["recipe_list"] = user.authors.all()
        return context


def not_author(request):
    """
    View if the user is not the author
    """
    return render(request, "users/not_author.html")
