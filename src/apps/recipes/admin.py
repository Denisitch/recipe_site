from django.contrib import admin
from django.utils.safestring import mark_safe
from apps.recipes.models import Recipe, Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "instruction",
        "user",
        "created_at",
        "updated_at",
        "get_image",
    )
    list_display_links = (
        "id",
        "title",
        "user",
    )
    search_fields = ("title", "instruction")
    list_filter = ("created_at", "ingredient")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')

    get_image.short_description = "Изображение"


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)
