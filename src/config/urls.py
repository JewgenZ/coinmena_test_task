from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path("^admin/", admin.site.urls),
    re_path(r"^api/v1/", include("core.urls")),
]
