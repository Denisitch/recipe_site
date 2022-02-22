from django.db import models
from django.urls import reverse
from apps.users.models import User


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        abstract = True


class Recipe(TimeStampMixin):
    title = models.CharField("Название рецепта", max_length=150)
    instruction = models.TextField("Инструкция приготовления")
    ingredient = models.ManyToManyField(
        "Ingredient", verbose_name="Ингредиент", related_name="ingredient"
    )
    image = models.ImageField(
        upload_to="images/recipes", blank=True, verbose_name="Изображение"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Автор рецепта",
        related_name="authors",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ["-created_at"]


class Ingredient(models.Model):
    title = models.CharField("Ингредиент", unique=True, max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ingredient", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        ordering = ["title"]
