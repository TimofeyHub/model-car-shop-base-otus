from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.name
