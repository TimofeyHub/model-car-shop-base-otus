from django.urls import path

from base.views import (
    ManufacturerList,
    ManufacturerDetailView,
    ManufacturerCreate,
    ScaleList,
    ScaleCreate,
    ScaleModelList,
    ScaleModelDetailView,
    ScaleModelCreate,
    homepage,
)

app_name = 'base'

urlpatterns = [
    path("", homepage),
    path('manufacturer/', ManufacturerList.as_view(), name="manufacturer-index"),
    path('manufacturer/<int:pk>/', ManufacturerDetailView.as_view(), name="manufacturer-detail"),
    path('manufacturer/create/', ManufacturerCreate.as_view(), name="manufacturer-create"),

    path('scale/', ScaleList.as_view(), name="scale-index"),
    path('scale/create/', ScaleCreate.as_view(), name="scale-create"),

    path('scalemodel/', ScaleModelList.as_view(), name="scalemodel-index"),
    path('scalemodel/<int:pk>/', ScaleModelDetailView.as_view(), name="scalemodel-detail"),
    path('scalemodel/create/', ScaleModelCreate.as_view(), name="scalemodel-create"),
]
