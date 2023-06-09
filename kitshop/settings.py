"""
Django settings for kitshop project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import requests
import base64
import json

CURRENT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^-c3ih&=nwhj5qj82rxu4zpq!2@=a6!i+)m@kl70r*p7f&#t1u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#change to true before deploying into production
ENABLE_SSL = False

AUTHNET_POST_URL = 'test.authorize.net'
AUTHNET_POST_PATH = '/gateway/transact.dll'
AUTHNET_LOGIN = ''
AUTHNET_KEY = ''

#Lipa na Mpesa credentials
MPESA_CONSUMER_KEY = "YOUR CONSUMER KEY"
MPESA_CUNSUMER_SECRET = "YOUR CONSUMER SECRET"
MPESA_API_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
MPESA_SHORTCODE = "YOUR LIPA NA MPESA SHORTCODE"
MPESA_PASSKEY = "YOUR LIPA NA MPESA PASSKEY"
CALLBACK_URL = "https://your_callbackurl.com"

#Used for search purposes i.e num of results per page
PRODUCTS_PER_PAGE = 12
PRODUCTS_PER_ROW = 4



ALLOWED_HOSTS = []

SESSION_COOKIE_AGE = 60 * 60 * 24 * 90



# Application definition

INSTALLED_APPS = [
    'preview.apps.PreviewConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'catalog.apps.CatalogConfig',
    'utils.apps.UtilsConfig',
    'cart.apps.CartConfig',
    'checkout.apps.CheckoutConfig',
    'accounts.apps.AccountsConfig',
    'search.apps.SearchConfig',
    'stats.apps.StatsConfig',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'crispy_forms',
    'crispy_bootstrap5',
    'dblog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',


]

ROOT_URLCONF = 'kitshop.urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(CURRENT_PATH,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.kitshop',
            ],
        },
    },
]

WSGI_APPLICATION = 'kitshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'kitshop',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'DESKTOP-9LJEFGO\SQLEXPRESS',
        'OPTIONS': {'driver':'ODBC Driver 17 for SQL Server', },

    }
}
DATABASE_CONNECTION_POOLING = False


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SITE_NAME = 'Kitshop'
META_KEYWORDS = 'kitshop,sports, sports kits,kits,Games,Games kits, Jezis, games equipment,football,netball'
META_DESCIPTION = 'Kitshop is an online supplier of all sports equipmets and instruments for many games'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(CURRENT_PATH,'static'),]
MEDIA_ROOT = os.path.join(CURRENT_PATH, 'static')

# = '/static/'
LOGIN_REDIRECT_URL = '/accounts/my_account/'
AUTH_PROFILE_MODULE = 'accounts.userprofile'

CRISPY_ALLOWED_TEMPLATE_PACKS ='bootstrap5'
CRISPY_TEMPLATE_PACK ='bootstrap5'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
