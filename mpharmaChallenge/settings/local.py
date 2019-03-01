from mpharmaChallenge.settings.base import *

DEBUG = True

INSTALLED_APPS += [
    
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}