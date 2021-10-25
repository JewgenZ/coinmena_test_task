from asgiref.sync import async_to_sync

from config.celery import app

from .services import ExchangeRatesService


@app.task
def update_exchange_rates():
    return async_to_sync(ExchangeRatesService.update_exchange_rates)()
