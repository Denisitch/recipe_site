from django import forms
from apps.recipes.models import Recipe


class RecipesForm(forms.ModelForm):
    new_ingredients = forms.CharField(
        label="Добавьте ингредиенты так, чтобы каждый новый ингредиент отделялся знаком + от последующего",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Соль+Сахар+Перец и тд..."}
        ),
    )

    class Meta:
        model = Recipe
        fields = (
            "title",
            "instruction",
            "new_ingredients",
            "image",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "instruction": forms.Textarea(attrs={"class": "form-control"}),
        }
