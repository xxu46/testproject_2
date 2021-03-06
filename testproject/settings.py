"""
Django settings for testproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ec2xxu@gmail.com'
EMAIL_HOST_PASSWORD = ''



DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_TO_EMAIL = 'xxu46@illinois.edu'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIRECTORY = os.getcwd()

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR + STATIC_URL

ROOT_PATH = os.path.dirname(__file__)
STATICFILES_DIRS = [os.path.join(ROOT_PATH, 'static')]



STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


import os

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING':True,
        'TIMEOUT': 60 * 5,
    },
}
HAYSTACK_DEFAULT_OPERATOR = 'OR'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10

USE_TZ = True

#os.environ['TZ'] = 'Asia/Shanghai'
os.environ['TZ'] = 'America/Chicago'

# HAYSTACK_CONNECTIONS = {
#
#
#     'default': {
#         'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#         'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#     },
# }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+)j3mi=n3qgtbg2tc!p1fs86)la691t7va_-h(u)9ilqg==x*0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Added.
    'haystack',

    'task',
)
#
#
# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.contrib.auth.context_processors.auth",
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     "django.core.context_processors.static",
#     "django.core.context_processors.tz",
#     "django.contrib.messages.context_processors.messages",
#     #"context_processors.my_processor",
#     'django.core.context_processors.request', #activar las variables de session alojadas en el request
#     )
# #
# #
# #
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'django.core.context_processors.debug',
#     'django.core.context_processors.i18n',
#     'django.core.context_processors.media',
#     'django.contrib.messages.context_processors.messages',
#     #'context_processors.admin_media_prefix',
#     'django.core.context_processors.static',
#     'django.core.context_processors.request',
#    # 'context_processors.site',
# )
#
#
#
TEMPLATE_CONTEXT_PROCESSORS =("django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
'django.core.context_processors.request',)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testproject.urls'

WSGI_APPLICATION = 'testproject.wsgi.application'

#
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR,  'templates/task'),
)

#Xiaomin add following codes
# from sys import path
# c = os.getcwd()
# os.chdir(str(c)+'/superqq')
# d = os.getcwd()
# path.append(d)
# os.chdir(c)
# d = os.getcwd()
# os.environ['SCRAPY_SETTINGS_MODULE'] = 'superqq.settings'
