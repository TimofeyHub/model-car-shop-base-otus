from django.db import models

from myauth.models import MyUser
from base.models import ScaleModel


class Buy(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    model = models.ForeignKey(ScaleModel, on_delete=models.PROTECT)
    buy_time = models.DateTimeField(auto_now_add=True)
