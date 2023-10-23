from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=320)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username
