from django.urls import path

from base.views import (
    ManufacturerList,
    ManufacturerDetailView,
    ScaleList,
    ScaleModelList,
    ScaleModelDetailView,
    homepage,
)

app_name = 'base'

urlpatterns = [
    path("", homepage),
    path('manufacturer/', ManufacturerList.as_view(), name="manufacturer-index"),
    path('manufacturer/<int:pk>/', ManufacturerDetailView.as_view(), name="manufacturer-detail"),
    path('scale/', ScaleList.as_view(), name="scale-index"),
    path('scalemodel/', ScaleModelList.as_view(), name="scalemodel-index"),
    path('scalemodel/<int:pk>/', ScaleModelDetailView.as_view(), name="scalemodel-detail"),
]
