from .base import * #noqa
from .base import env

ADMINS = [("Eribert Marquez","eriker1997@gmail.com")]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="F5EWAwZfpodPzQWXVa_DYAqJDS-qdyTR3cnk7XIp0Kqdj7UqJXY"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO add domain names of the production server
CSRF_TRUSTED_ORIGIN = []