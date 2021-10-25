from django.core.validators import RegexValidator
from django.db import models

from .constants import CURRENCY_REGEX


class CurrencyExchangeRate(models.Model):
    currency_from = models.CharField(
        validators=[
            RegexValidator(
                regex=CURRENCY_REGEX,
                message="Currency must be 3 uppercase letters long",
            ),
        ],
        max_length=3,
    )
    currency_to = models.CharField(
        validators=[
            RegexValidator(
                regex=CURRENCY_REGEX,
                message="Currency must be 3 uppercase letters long",
            ),
        ],
        max_length=3,
    )
    rate = models.DecimalField(
        max_digits=20,
        decimal_places=5,
        null=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
