from django.db import models

from base.models import Manufacturer
from base.models import Scale


class ScaleModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        null=True,
    )
    scale = models.ForeignKey(
        Scale,
        on_delete=models.PROTECT
    )
    description = models.TextField(null=False, blank=True)

    price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
