"""
Django settings for eureka project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import environ
from django.core.management.utils import get_random_secret_key

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    "authentication",
    "menus",
    "experience",
    "about",
    "blog",
    "courses",
    "home",
    "search",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django_extensions',
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "eureka.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

CSRF_TRUSTED_ORIGINS = ['https://eureka-production-6efb.up.railway.app', 'https://www.eurekadataacademy.com/', 'https://eurekadataacademy.com/']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')
CSRF_USE_SESSIONS = False
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_FRAME_DENY = True
SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_REFERRER_POLICY = 'same-origin'

WSGI_APPLICATION = "eureka.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }
DATABASES = {
    "default": dj_database_url.config(default='postgresql://postgres:qDeZYDXnjsGIKOhMQjofGqcPUwWPuiPS@monorail.proxy.rlwy.net:31039/railway', conn_max_age=1800),
}


AUTH_USER_MODEL = 'authentication.User'
WAGTAIL_USER_EDIT_FORM = 'authentication.forms.CustomUserEditForm'
WAGTAIL_USER_CREATION_FORM = 'authentication.forms.CustomUserCreationForm'
WAGTAIL_USER_CUSTOM_FIELDS = ['email', 'country', 'city', 'phone_number', 'region', 'residential_address', 'avatar']


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Default storage settings, with the staticfiles storage updated.
# See https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # ManifestStaticFilesStorage is recommended in production, to prevent
    # outdated JavaScript / CSS assets being served from cache
    # (e.g. after a Wagtail upgrade).
    # See https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}


# Wagtail settings

WAGTAIL_SITE_NAME = "eureka"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = ['csv', 'docx', 'key', 'odt', 'pdf', 'pptx', 'rtf', 'txt', 'xlsx', 'zip']
