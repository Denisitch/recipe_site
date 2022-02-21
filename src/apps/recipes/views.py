from django.views.generic import (
    ListView,
    DetailView,
)
from apps.recipes.models import Recipe, Ingredient


class RecipesView(ListView):
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
    model = Recipe
    template_name = "recipes/detail.html"
    context_object_name = "item_recipe"
