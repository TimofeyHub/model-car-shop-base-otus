from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('', include('base.urls', namespace='base')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
