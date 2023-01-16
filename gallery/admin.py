from django.contrib import admin
from .models import Photography


class getPhotographs(admin.ModelAdmin):
    list_display = ("id", "name", "caption")
    list_display_links = ("name",)
    search_fields = ("name", )


admin.site.register(Photography, getPhotographs)
