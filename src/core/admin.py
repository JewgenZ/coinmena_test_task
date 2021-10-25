from django.contrib import admin

from .models import CurrencyExchangeRate


@admin.register(CurrencyExchangeRate)
class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    pass
