from django.urls import path

from apps.users.views import register, user_login, user_logout, UserView

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("<int:pk>", UserView.as_view(), name="user"),
]
