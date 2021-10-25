from contextlib import suppress
from typing import Optional

from asgiref.sync import sync_to_async

from .domain import CurrencyExchangeRateDTO
from .interfaces import AlphaVantageInterface
from .models import CurrencyExchangeRate


class CurrencyExchangeRateCRUD:
    @staticmethod
    @sync_to_async
    def last() -> Optional[CurrencyExchangeRateDTO]:
        with suppress(CurrencyExchangeRate.DoesNotExist, AttributeError):
            instance = CurrencyExchangeRate.objects.last()
            return CurrencyExchangeRateDTO(**instance.__dict__)

    @staticmethod
    @sync_to_async
    def create(payload: CurrencyExchangeRateDTO) -> Optional[CurrencyExchangeRate]:
        return CurrencyExchangeRate.objects.create(**payload.dict())


class ExchangeRatesService:
    @classmethod
    async def fetch_exchange_rates_from_alpha_vantage(cls) -> CurrencyExchangeRateDTO:
        payload: dict = await AlphaVantageInterface.fetch_exchange_rates()
        return CurrencyExchangeRateDTO(**payload)

    @classmethod
    async def update_exchange_rates(cls) -> None:
        payload = await cls.fetch_exchange_rates_from_alpha_vantage()
        await CurrencyExchangeRateCRUD.create(payload)

    @classmethod
    async def get_last_exchange_rates(cls) -> dict:
        last_currency_exchange = await CurrencyExchangeRateCRUD.last()
        if not last_currency_exchange:
            await cls.update_exchange_rates()
            last_currency_exchange = await CurrencyExchangeRateCRUD.last()

        return last_currency_exchange.dict()

    @classmethod
    async def get_fresh_exchange_rates(cls) -> dict:
        await cls.update_exchange_rates()
        return await cls.get_last_exchange_rates()
