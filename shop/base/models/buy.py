from django.db import models

from base.models import User
from base.models import ScaleModel


class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    model = models.ForeignKey(ScaleModel, on_delete=models.PROTECT)
    buy_time = models.DateTimeField(auto_now_add=True)
