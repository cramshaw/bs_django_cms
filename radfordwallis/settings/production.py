from radfordwallis.settings.base import *

DEBUG = False

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
