from .base import *

SECRET_KEY = 'django-insecure-w95w!ge72_p!(^!pnxh#94y3yfk9=6f3%escg4i7t1iz*uztf0'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}