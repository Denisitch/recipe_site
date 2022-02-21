from django.urls import path

from apps.recipes.views import (
    RecipesView,
    RecipeDetail,
)

urlpatterns = [
    path("", RecipesView.as_view(), name="home"),
    path("recipe/<int:pk>", RecipeDetail.as_view(), name="detail"),
]
