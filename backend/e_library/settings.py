"""
SETTINGS for e_library project.
"""
from pathlib import Path
import os
import re

# backend/e_library.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'zx6n)1_o^4*&6ypp-*@h37wd%s+g02(j-g&%p(yzyajl9uu&tg'
DEBUG = int(os.getenv('DEBUG'))
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django Rest Framework
    'rest_framework',
    'django_filters',

    # corsheaders
    "corsheaders",
    # django extensions
    "django_extensions",

    # app for All E-library Funcation
    'emanagement', # User E-Management models, views
    'django_cleanup', # To cleanup the storage

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Simplified static file serving on heroku.
    # whitenoise for serve static file on producation
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:8080',
# )

ROOT_URLCONF = 'e_library.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', ],
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

WSGI_APPLICATION = 'e_library.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGE_COOKIE_NAME = 'library_language'

LOCALE_PATH = (
    BASE_DIR / 'locale',
)
AUTH_USER_MODEL = 'emanagement.User'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'api-root'
LOGOUT_REDIRECT_URL = 'api-root'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (BASE_DIR / "static",)


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStoraQueryParameterVersioningge'

# Simple JWT
SIMPLE_JWT = {
    'UPDATE_LAST_LOGIN': True,
    'AUTH_HEADER_TYPES': ('Bearer', 'shyamkumaryadav', 'sky', 'shyamkumar', 'shyam'),
}

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

OLD_PASSWORD_FIELD_ENABLED = True

# EMAIL On Console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

# Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 
# EMAIT_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 
# EMAIL_HOST_PASSWORD = 

CSRF_FAILURE_VIEW = 'emanagement.views.csrf'