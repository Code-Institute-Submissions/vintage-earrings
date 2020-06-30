"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import logging.config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import pika

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY', 'my_fancy_key')

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')

HOST = os.environ.get('HOST', 'http://localhost:3000')

STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

# RabbitMQ URL

CLOUDAMQP_URL = os.environ.get("CLOUDAMQP_URL")

# VINTAGE_EARRINGS_INDEX_URL

VINTAGE_EARRINGS_INDEX_URL = os.environ.get('VINTAGE_EARRINGS_INDEX_URL', 'http://localhost:3000')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if ENVIRONMENT != 'dev':
    DEBUG = False
    SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = [
    'vintage-earrings.herokuapp.com',
    "127.0.0.1",
    "localhost"
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'authentication',
    'django_extensions',
    'product',
    'basket',
    'order',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vintage_earrings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vintage_earrings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if "DATABASE_URL" in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", '')
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", '')

S3_USE_SIGV4 = True
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_STATIC_BUCKET_NAME = "vintage-earrings-static"

AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

STATIC_URL = "https://%s.s3.amazonaws.com/" % AWS_STATIC_BUCKET_NAME
STATICFILES_STORAGE = "static.storage.StaticS3Storage"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

logging.config.dictConfig(LOGGING)

try:
    from .developer_settings import *
except:
    pass
