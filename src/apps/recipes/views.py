from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from apps.recipes.forms import RecipesForm
from apps.recipes.models import Recipe, Ingredient
from apps.recipes.utils import UserRuleMixin


class RecipesView(ListView):
    """
    List of recipes with search and filtering by ingredients
    """

    model = Recipe
    template_name = "recipes/index.html"
    context_object_name = "recipes"
    paginate_by = 4

    def get_queryset(self):
        recipe = self.request.GET.get("recipe")
        ingredients = self.request.GET.get("ingredient")
        recipes_list = Recipe.objects.all()
        if recipe:
            recipes_list = recipes_list.filter(title__icontains=recipe)
        if ingredients:
            recipes_list = recipes_list.filter(
                ingredient__title__icontains=ingredients
            ).distinct()
        return recipes_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RecipesView, self).get_context_data(**kwargs)
        context["title"] = "Главная страница"
        context["ingredients_list"] = Ingredient.objects.all().order_by("title")
        context["recipes_list"] = self.get_queryset
        return context


class RecipeDetail(DetailView):
    """
    Recipe Detail View
    """

    model = Recipe
    template_name = "recipes/detail.html"
    context_object_name = "item_recipe"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RecipeDetail, self).get_context_data(**kwargs)
        context["rule"] = "Только для зарегистрированных"
        return context


class CreateRecipe(LoginRequiredMixin, CreateView):
    """
    Recipe Create View
    """

    model = Recipe
    template_name = "add_recipe.html"
    form_class = RecipesForm
    success_url = reverse_lazy("home")


class UpdateRecipe(UserRuleMixin, UpdateView):
    """
    Recipe Update View
    """

    model = Recipe
    template_name = "recipes/edit_recipe.html"
    fields = ["title", "instruction", "ingredient"]
    context_object_name = "item_recipe"


class DeleteRecipe(UserRuleMixin, DeleteView):
    """
    Recipe Delete View
    """

    model = Recipe
    template_name = "recipes/delete_recipe.html"
    context_object_name = "item_recipe"
    success_url = reverse_lazy("home")
