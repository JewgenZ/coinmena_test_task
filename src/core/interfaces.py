import httpx
from django.conf import settings

from .domain import AlphaVantageBadRequestError


class AlphaVantageInterface:
    SUCCESS_RESPONSE_TITLE = "Realtime Currency Exchange Rate"

    @classmethod
    async def fetch_exchange_rates(cls) -> dict:
        url = f"{settings.ALPHAVANTAGE_BASE_URL}{settings.ALPHAVANTAGE_API_KEY}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        data = response.json()

        if cls.SUCCESS_RESPONSE_TITLE not in data:
            raise AlphaVantageBadRequestError()

        return response.json()[cls.SUCCESS_RESPONSE_TITLE]
