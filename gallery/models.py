from django.db import models


class Photography(models.Model):

    CATEGORY_OPTIONS = [
        ("NEBULA", "Nebula"),
        ("STAR", "Star"),
        ("GALAXY", "Galaxy"),
        ("PLANET", "Planet")
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(
        max_length=50, choices=CATEGORY_OPTIONS, default="")
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Photography | Name: {self.name}"
