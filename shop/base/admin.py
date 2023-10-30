from django.contrib import admin

from base.models import Scale, Manufacturer, ScaleModel, Buy
from myauth.models import MyUser


@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    list_display = "pk", "value"


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = "pk", "name"


@admin.register(ScaleModel)
class ScaleModelAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "price", "manufacturer", "scale", "description"
    list_display_links = "pk", "name"


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = "pk", "username", "full_name", "email", "phone_number"


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = "user", "model", "buy_time"
    list_display_links = "user", "model",
