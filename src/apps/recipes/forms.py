from django import forms
from apps.recipes.models import Recipe, Ingredient


class RecipesForm(forms.ModelForm):
    """
    Form for creating recipes
    """

    new_ingredients = forms.CharField(
        label="Добавьте ингредиенты так, чтобы каждый новый ингредиент отделялся знаком + от последующего",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Соль+Сахар+Перец и тд..."}
        ),
    )
    ingredient = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Recipe
        fields = (
            "title",
            "instruction",
            "ingredient",
            "new_ingredients",
            "image",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "instruction": forms.Textarea(attrs={"class": "form-control"}),
        }
