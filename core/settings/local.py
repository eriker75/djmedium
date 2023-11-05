from .base import * #noqa
from .base import env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="F5EWAwZfpodPzQWXVa_DYAqJDS-qdyTR3cnk7XIp0Kqdj7UqJXY"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGIN = ["http://localhost:8080"]