from .base import *

import os
import django_heroku
import dj_database_url

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

MEDIA_URL = '/media-url/'

MEDIA_ROOT = BASE_DIR / 'media'

SECRET_KEY = str(os.environ.get('SECRET_KEY'))

ADMIN_URL = str(os.environ.get('ADMIN_URL'))

DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

django_heroku.settings(locals())