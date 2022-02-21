from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    photo = models.ImageField(upload_to="images/users", blank=True, verbose_name="Фото")

    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.pk})
