from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User Model Administration
    """

    list_display = ("username", "email", "get_photo")
    list_display_links = ("username",)
    readonly_fields = ("get_photo",)

    def get_photo(self, obj):
        try:
            return mark_safe(f'<img src={obj.photo.url} width="50" height="50"')
        except:
            pass

    get_photo.short_description = "Фото"
