import os

from settings.base import *


DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# POSTGRESQL DEFINITIONS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', None),
        'USER': os.environ.get('DB_USER', None),
        'PASSWORD': os.environ.get('DB_PASS', None),
        'HOST': os.environ.get('DB_HOST', None),
        'PORT': os.environ.get('DB_PORT', None),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s: %(lineno)s %(message)s]",
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },

    'handlers': {
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, '../app.log'),
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'verbose',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['log_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['null', ],
        },
        'app': {
            'handlers': ['log_file'],
            'level': 'DEBUG',
        },
    }
}