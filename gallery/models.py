from django.db import models
from datetime import datetime


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
    photo = models.ImageField(upload_to="photos/%Y/%M/%d/", blank=True)
    published = models.BooleanField(default=False)
    photo_date = models.DateTimeField(default=datetime.now(), blank=False)

    def __str__(self):
        return self.name
