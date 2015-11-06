# -*- coding: utf-8 -*-
# pylint: disable=unused-wildcard-import, wildcard-import
from __future__ import unicode_literals
# IMPORTANT NOTE!  YOU MAY NEED TO REFERENCE THIS ON A PYWINTYPES MSSQL ERROR:
# http://stackoverflow.com/a/7766757
import datetime
import os
import platform
import sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DEBUG = False
TEMPLATE_DEBUG = DEBUG
FORCE_ALL_EMAILS_TO_ADMIN = True
ALLOWED_HOSTS = []

ADMINS = ()

MANAGERS = ADMINS

DATABASE_ROUTERS = ['web__django.db_routers.MyAppRouter']
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Denver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'static\\user\\'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/static/user/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    "C:/Users/rr013615/Desktop/repo_checkouts/firestorm/static",
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "static",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a-#%ligo%gasdfmp;e1zk$+s)bk7b61dct5_+fylzz+5h'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'webpages._SiteWide.logging_middleware.LoggingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'web__django.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'web__django.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "templates",
)

INSTALLED_APPS = (
    # 3rd Party
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'sekizai',

    # Site-Specific
    'webpages._SiteWide',
    'webpages.kiosk',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },#'file': {'level': 'DEBUG','class': 'logging.FileHandler','filename': 'log_%s.txt' % datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f'),'formatter': 'verbose',},
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },# '': {'handlers': ['file'],'level': 'DEBUG','propagate': True,},
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}

LOGIN_URL = '/accounts/login'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
)

EMAIL_HOST = ''
SMTP_USER = None
SMTP_PASS = None
TEST_RUNNER = 'discover_runner.DiscoverRunner'

DEV_SERVICE_TAGS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'firestorm.db',
    }
}

try:
    from .base_local import *
except ImportError:
    pass

SETTINGS = "web__django.settings.settings_prod"
DEV_MACHINE = False
if platform.uname()[1].upper() in DEV_SERVICE_TAGS:
    if 'site:prod' in sys.argv:
        DEV_MACHINE = False
    else:
        DEV_MACHINE = True
        SETTINGS = "web__django.settings.settings_dev"
