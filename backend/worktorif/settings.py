"""
Django settings for worktorif project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

import logging
# logging.basicConfig(level=logging.DEBUG)
import os
import platform
import stat
import atexit
from sshtunnel import SSHTunnelForwarder
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)k0@khml6ev4+!iq^wz$kin_c*nsoz9#vmi^^#v^w5=*o&=w-z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

SITE_ID=1

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    "rest_framework",
]

SOCIALACCOUNT_PROVIDERS ={
    "google":{
        "SCOPE":[
            "profile",
            "email"
        ],
        "AUTH_PARAMS":{"access_type": "online"}
    }
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'worktorif.urls'

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

WSGI_APPLICATION = 'worktorif.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Initialize environment variables
env = environ.Env()
# environ.Env.read_env()  # Reads the .env file

# Take environment variables from .env file
environ.Env.read_env(os.path.join(os.path.dirname(__file__), '.env'))  # Ensure this path is correct


# Setting up the SSH tunnel
SSH_ADDRESS = env('SSH_ADDRESS')
SSH_PORT = env.int('SSH_PORT')
SSH_USER = env('SSH_USER')
SSH_KEY = env('SSH_KEY')
SSH_PASSPHRASE = env('SSH_PASSPHRASE', default=None)

# Ensure the private key file exists and has correct permissions
if not os.path.isfile(SSH_KEY):
    raise ValueError(f"Private key file {SSH_KEY} does not exist")

# Check if the OS is not Windows, then check the permissions
if platform.system() != 'Windows':
    if os.stat(SSH_KEY).st_mode & 0o777 != 0o600:
        raise ValueError(f"Private key file {SSH_KEY} must have permissions 600")

# Create the SSH tunnel
tunnel = SSHTunnelForwarder(
    (SSH_ADDRESS, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_pkey=SSH_KEY,
    ssh_private_key_password=SSH_PASSPHRASE,
    remote_bind_address=('localhost', 3306),
    local_bind_address=('127.0.0.1', 3306)
)

tunnel.start()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': '127.0.0.1', 
        'PORT' : '3306',
    }
}

# Add a cleanup handler to stop the tunnel when the Django server stops
atexit.register(tunnel.stop)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
CORS_ALLOW_ALL_ORIGINS = True #fase development


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_BACKENDS = {
    "django.contrib.auth.backends.ModelBackend",
    "allauth.accounts.auth_backends.AuthentificationBackend"
}

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
