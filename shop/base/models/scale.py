from django.db import models


class Scale(models.Model):
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value
