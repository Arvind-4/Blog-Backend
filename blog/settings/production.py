from blog.env import config
from blog.settings.base import *

MEDIA_URL = "/media/"

STATIC_ROOT = BASE_DIR / "static-cdn-local"
MEDIA_ROOT = BASE_DIR / "media-cdn-local"

DEBUG = config("DJANGO_DEBUG", cast=bool)
SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str)
ADMIN_URL = config("DJANGO_ADMIN_URL", cast=str)


CORS_ALLOWED_ORIGINS = []
CORS_ALLOWED_ORIGINS.extend(
    config(
        "DJANGO_CORS_ALLOWED_ORIGINS", cast=lambda v: [s.strip() for s in v.split(",")]
    )
)


ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    config("DJANGO_ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")])
)

from blog.db import *  # noqa

DJANGO_LIVE = config("DJANGO_LIVE", cast=bool)
if DJANGO_LIVE:
    from blog.https import *  # noqa
