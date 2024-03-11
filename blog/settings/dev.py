from blog.env import config
from blog.settings.base import *


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

BASE_URL = "http://127.0.0.1:8000"

MEDIA_URL = "/media/"

STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / "static-cdn-local"
MEDIA_ROOT = BASE_DIR / "media-cdn-local"

SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str, default="Sample-key-1234")

ADMIN_URL = "admin"

DEBUG = config("DJANGO_DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = ["*"]

APPEND_SLASH = True

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Blog API',
    'DESCRIPTION': 'API for the blog app',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,
}

from blog.db import *  # noqa
