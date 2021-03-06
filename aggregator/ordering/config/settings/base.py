"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import pathlib
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = pathlib.Path(__file__).resolve(strict=True)
ROOT_DIR = BASE_DIR.parent.parent.parent
APPS_DIR = ROOT_DIR / 'ordering'

env = environ.Env()
env.read_env(str(ROOT_DIR / '.envs' / '.local'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET')
API_KEY = env('API_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders'
]

LOCAL_APPS = [

]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR / 'templates')
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {

    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


# External Services
PRODUCT_SERVICE = {
    'url': env('PRODUCT_SERVICE_URL'),
    'api': {
        'CREATE': env('PRODUCT_CREATE_API', default=None),
        'UPDATE': env('PRODUCT_UPDATE_API', default=None),
        'DETAIL': env('PRODUCT_DETAIL_API', default=None),
        'DELETE': env('PRODUCT_DELETE_API', default=None),
        'LIST': env('PRODUCT_LIST_API', default=None)
    }
}

ORDER_SERVICE = {
    'url': env('ORDER_SERVICE_URL'),
    'api': {
        'CREATE': env('ORDER_CREATE_API', default=None),
        'UPDATE': env('ORDER_UPDATE_API', default=None),
        'DETAIL': env('ORDER_DETAIL_API', default=None),
        'DELETE': env('ORDER_DELETE_API', default=None),
        'LIST': env('ORDER_LIST_API', default=None)
    }
}

PAYMENT_SERVICE = {
    'url': env('PAYMENT_SERVICE_URL'),
    'api': {
        'CREATE': env('PAYMENT_CREATE_API', default=None),
        'UPDATE': env('PAYMENT_UPDATE_API', default=None),
        'DETAIL': env('PAYMENT_DETAIL_API', default=None),
        'DELETE': env('PAYMENT_DELETE_API', default=None),
        'LIST': env('PAYMENT_LIST_API', default=None)
    }
}

CART_SERVICE = {
    'url': env('CART_SERVICE_URL'),
    'api': {
        'UPDATE': env('CART_UPDATE_API', default=None),
        'DETAIL': env('CART_DETAIL_API', default=None),
        'DELETE': env('CART_DELETE_API', default=None),
    }
}