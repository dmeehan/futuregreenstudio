from __future__ import absolute_import, unicode_literals

import os

from .base import *

DEBUG = False

#==============================================================================
# Site
#==============================================================================
ALLOWED_HOSTS = ['futuregreenstudio.com', 'www.futuregreenstudio.com', 'futuregreenstudio.opalstacked.com',  'smtp.webfaction.com']

BASE_URL = 'http://futuregreenstudio.com'

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '87hq#$x_zu_=r)polio0q1y*$ii2z4wt82cqpx=167wt4lsa83$')


#==============================================================================
# Email
#==============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.webfaction.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = 'futuregreen'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = '587'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_USE_TLS = 'True'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = 'Future Green Studio'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'admin@futuregreenstudio.com'

DEFAULT_FROM_EMAIL = 'Future Green Studio <info@futuregreenstudio.com>'

#==============================================================================
#  Databases
#==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', ''),
        'USER': os.environ.get('DJANGO_DB_USER', ''),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '',
    }
}


#==============================================================================
# Caching
#==============================================================================

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:63008',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

try:
    from .local import *
except ImportError:
    pass
