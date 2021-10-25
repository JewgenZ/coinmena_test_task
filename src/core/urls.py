from django.urls import re_path

from .api import currency_exchange_retrieve

app_name = "core"

urlpatterns = [
    re_path(
        r"quotes/?$",
        currency_exchange_retrieve,
        name="currency_exchange_retrieve",
    )
]
