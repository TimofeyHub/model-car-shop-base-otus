from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Scale(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value


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

    def __str__(self):
        return self.name
