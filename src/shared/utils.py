import re


class ConnectionStringDoesNotMatch(ValueError):
    """Raises if connection string doesn't match regex pattern"""


class ConnectionStringContainsInvalidEngine(ValueError):
    """Raises if connection string contains invalid database engine"""


db_regex = (
    r"^(?P<db_engine>.*):\/{2}"
    r"((?P<db_username>[^:]*):(?P<db_password>[^@]*)@"
    r"(?P<db_hostname>[^:/]*)(:(?P<db_port>\d+))?\/)?(?P<db_name>.*)$"
)

DJANGO_DB_ENGINES = {
    "postgresql": "django.db.backends.postgresql",
    "postgis": "django.contrib.gis.db.backends.postgis",
    "sqlite3": "django.db.backends.sqlite3",
}


def get_db_config_from_connection_string(connection_string: str) -> dict:
    try:
        match = re.search(db_regex, connection_string)
        print(connection_string)
        return {
            "ENGINE": DJANGO_DB_ENGINES[match.group("db_engine")],
            "NAME": match.group("db_name"),
            "USER": match.group("db_username"),
            "PASSWORD": match.group("db_password"),
            "HOST": match.group("db_hostname"),
            "PORT": match.group("db_port"),
        }
    except AttributeError:
        raise ConnectionStringDoesNotMatch(
            f'Database connection string "{connection_string}" does not match with expected regex.'
        )
    except KeyError:
        raise ConnectionStringContainsInvalidEngine(
            f'Database connection string "{connection_string}" '
            f'includes unexpected db_engine: "{match.group("db_engine")}".'
        )
