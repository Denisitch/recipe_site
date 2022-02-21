from django.urls import path

from apps.recipes.views import (
    RecipesView,
    RecipeDetail,
    CreateRecipe,
    UpdateRecipe,
    DeleteRecipe,
)

urlpatterns = [
    path("", RecipesView.as_view(), name="home"),
    path("recipe/<int:pk>", RecipeDetail.as_view(), name="detail"),
    path("recipe/add_recipe/", CreateRecipe.as_view(), name="add_recipe"),
    path("recipe/edit_recipe/<int:pk>/", UpdateRecipe.as_view(), name="edit_recipe"),
    path(
        "recipe/delete_recipe/<int:pk>/", DeleteRecipe.as_view(), name="delete_recipe"
    ),
]
