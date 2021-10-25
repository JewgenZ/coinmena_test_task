from os import getenv, path
from pathlib import Path

from shared.utils import get_db_config_from_connection_string

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-g4zwl3_znj2vosbj1kj2e%#=$n#o6@%u2$s)+_92$mw4wp=ejs",
)

DEBUG = getenv("DJANGO_DEBUG", False)

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_beat",
    # Local apps
    "core.apps.CoreConfig",
    "shared.apps.SharedConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
DATABASES = {
    "default": get_db_config_from_connection_string(
        connection_string=getenv("DATABASE_URL")
    ),
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = "/static/"
STATICFILES_DIR = [
    path.join(BASE_DIR, "static"),
]
STATIC_ROOT = path.join(path.dirname(BASE_DIR), "static-cdn-local")


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CELERY_BROKER_URL = getenv("CELERY_BROKER_URL")
CELERY_WORKERS = int(getenv("CELERY_WORKERS", "10"))

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

CELERY_TIMEZONE = "Europe/Kiev"

CELERY_DEFAULT_QUEUE = "celery"
CELERY_QUEUE_NAME = CELERY_DEFAULT_QUEUE
CELERY_TASK_CREATE_MISSING_QUEUES = False

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_BEAT_SCHEDULE = {
    "udpate_exchange_rates": {
        "task": "core.tasks.update_exchange_rates",
        "schedule": 3600.0,
    },
}

ALPHAVANTAGE_BASE_URL = getenv(
    "ALPHAVANTAGE_BASE_URL",
    "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=",
)
ALPHAVANTAGE_API_KEY = getenv("ALPHAVANTAGE_API_KEY")
