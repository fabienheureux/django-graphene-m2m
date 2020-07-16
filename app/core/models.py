from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=255)
    photos = models.ManyToManyField(
        "core.Image",
        related_name="related_properties",
        blank=True,
        verbose_name="Photos",
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    url = models.CharField(max_length=255)
    def __str__(self):
        return self.url
