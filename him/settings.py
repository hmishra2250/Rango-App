"""
Django settings for him project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

"""BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print __file__
print os.path.dirname(__file__)
print os.path.dirname(os.path.dirname(__file__))"""
print os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))       #Added for dynamic path

TEMPLATE_PATH = os.path.join(BASE_DIR,'templates')

STATIC_PATH = os.path.join(BASE_DIR,'static')   # Added for static files

STATICFILES_DIRS = (                #added for static files as well
    STATIC_PATH,
    )

"""TEMPLATE_DIRS = (            #This is deprecated ij django 1.8  .... put this in TEMPLATE dict !
    TEMPLATE_PATH,

    )"""

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')     ##added for absolute path of media directory
LOGIN_URL = '/rango/login/'     ##page to redirect for login
SESSION_EXPIRE_AT_BROWSER_CLOSE = True          ##browser length cookies !!
## SESSION_EXPIRE_AT_BROWSER_CLOSE = False
## SESSION_COOKIE_AGE = 60   ##above 2 for persistent cookis ... age in seconds !!
REGISTRATION_OPEN = True        ##If true, users can register !
ACCOUNT_ACTIVATION_DAYS = 7     ##one week activation window
REGISTRATION_AUTO_LOGIN = True  ##Automatic login 
LOGIN_REDIRECT_URL = '/rango/'
LOGIN_URL = '/accounts/login/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j*xf9)gbr!w3b+9kwch_wg*!9x%lz%fszkqje8(mo&2$!)^vf$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',
    'registration',  ## For django Redux-registration
    'bootstrap_toolkit'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'him.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'him.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
