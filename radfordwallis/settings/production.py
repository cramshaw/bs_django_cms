from radfordwallis.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'radfordwallis',
        'USER': 'rwuser',
        'PASSWORD': os.getenv('DB_PASS'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
