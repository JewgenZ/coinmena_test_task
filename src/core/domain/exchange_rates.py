from decimal import Decimal

from pydantic import BaseModel, Field, constr

from ..constants import CURRENCY_REGEX


class CurrencyExchangeRateDTO(BaseModel):
    currency_from: constr(regex=CURRENCY_REGEX) = Field(alias="1. From_Currency Code")
    currency_to: constr(regex=CURRENCY_REGEX) = Field(alias="3. To_Currency Code")
    rate: Decimal = Field(alias="5. Exchange Rate")

    class Config:
        allow_population_by_field_name = True
