from .base import *
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    "debug_toolbar",
    # "django-extensions",
]

MIDDLEWARE +=[
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] 

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

GRAPH_MODELS ={
'all_applications': True,
'graph_models': True,
}

'''
DATABASES = {
    'default': {
        'ENGINE'  : 'django.db.backends.mysql',
        'NAME'    : env('DB_NAME'),
        'HOST'    : '127.0.0.1',
        'USER'    : env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'PORT'    : '3306',
        'OPTIONS' : {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
'''
# DATABASES = {
#     'default': {
#         'ENGINE'  : 'django.db.backends.mysql',
#         'NAME'    : 'bajaw',
#         'HOST'    : '127.0.0.1',
#         'USER'    : 'root',
#         'PASSWORD': '',
#         'PORT'    : '3306',
#         'OPTIONS' : {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'music.db'),
    }
}

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'static_cdn')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')