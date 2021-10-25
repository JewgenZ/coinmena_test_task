from functools import wraps
from http import HTTPStatus

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .domain import AlphaVantageBadRequestError
from .services import ExchangeRatesService


def catch_alphavantage_errors(coro):
    @wraps(coro)
    async def wrapper(*args, **kwargs):
        try:
            return await coro(*args, **kwargs)
        except AlphaVantageBadRequestError as error:
            return JsonResponse(status=HTTPStatus.BAD_REQUEST, data=error.data)

    return wrapper


@catch_alphavantage_errors
@csrf_exempt
async def currency_exchange_retrieve(request):
    if request.method.lower() not in ("get", "post"):
        raise HTTPStatus.METHOD_NOT_ALLOWED

    if request.method == "GET":
        data = await ExchangeRatesService.get_last_exchange_rates()
    else:
        data = await ExchangeRatesService.get_fresh_exchange_rates()

    return JsonResponse(data)
