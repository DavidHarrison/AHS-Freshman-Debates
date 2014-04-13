#!/usr/bin/env python2.7
#file: settings.py

# Django settings for debates project.
import os
import socket
#private environment variable, not pushed to Git
#import envvars

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# check for production
if socket.gethostname() == u'LAMP':
    pass
    #see envvar import
    #DATABASES = envvars.DATABASES
else:
    DATABASES = {
        u'default': {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            u'ENGINE': u'django.db.backends.sqlite3',
            # Or path to database file if using sqlite3.
            u'NAME': u'debates.db',
            # The following settings are not used with sqlite3:
            #'USER': '',
            #'PASSWORD': '',
            # Empty for localhost through domain sockets or '127.0.0.1' for
            # localhost through TCP.
            #'HOST': '',
            # Set to empty string for default.
            #'PORT': '',
        }
    }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = u'America/Vancouver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = u'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = u''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = u'/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = u''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = u'/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_ROOT + u"/debates/static/",
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    u'django.contrib.staticfiles.finders.FileSystemFinder',
    u'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = u'09-y+u=9v7s(3oak$dv@dlrmxw&3mbi%%7asq3m-0am08duk)7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    u'django.template.loaders.filesystem.Loader',
    u'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    u'django.middleware.common.CommonMiddleware',
    u'django.contrib.sessions.middleware.SessionMiddleware',
    u'django.middleware.csrf.CsrfViewMiddleware',
    u'django.contrib.auth.middleware.AuthenticationMiddleware',
    u'django.contrib.messages.middleware.MessageMiddleware',
    u'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = u'debates_site.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = u'debates_site.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_ROOT + u"/debates/templates/"
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    u'django.contrib.auth',
    u'django.contrib.contenttypes',
    u'django.contrib.sessions',
    u'django.contrib.sites',
    u'django.contrib.messages',
    u'django.contrib.staticfiles',
    u'django.contrib.formtools',
    # Admin
    u'django.contrib.admin',
    u'django.contrib.admindocs',
    # End of Admin
    u'debates',
    #'debates.models.User',
    #'django_openid_auth',
    u'social.apps.django_app.default',
    u'import_export',
)

# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


#Google LogIn

# GAPPS_DOMAIN = 'mydomain.com'
# GAPPS_USERNAME = ''
# GAPPS_PASSWORD = ''

# Check for new groups, or only on initial user creation
GAPPS_ALWAY_ADD_GROUPS = False
AUTHENTICATION_BACKENDS = (
    #'social.backends.google.GoogleOAuth',
    #'social.backends.CustomGoogleBackend.CustomGoogle',
    u'social.backends.google.GoogleOAuth2',
    # 'social.backends.google.Google'
    u'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = u'/splash'
LOGIN_ERROR_URL = u'/login-error/'
LOGIN_URL = u'/login/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = u'/new_user_login'
SOCIAL_AUTH_COMPLETE_URL_NAME  = u'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = u'socialauth_associate_complete'
SOCIAL_AUTH_UID_LENGTH = 222
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 135
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 125
LOGOUT_URL = u'/logout/'
OPENID_SSO_SERVER_URL = u'https://www.google.com/accounts/o8/id'



# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'social.context_processors.social_auth_by_type_backends',
#     'social.context_processors.social_auth_backends',
#     'django.core.context_processors.static',
# )

SOCIAL_AUTH_DEFAULT_USERNAME = u'New_User'
SOCIAL_AUTH_UID_LENGTH = 222
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 135
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 125
SOCIAL_AUTH_ENABLED_BACKENDS = (u'google')
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
#AUTH_USER_MODEL = 'debates.models.User'

SOCIAL_AUTH_PIPELINE = (
    u'social.backends.pipeline.social.social_auth_user',
    u'social.backends.pipeline.associate.associate_by_email',
    u'social.backends.pipeline.user.get_username',
    u'social.backends.pipeline.user.create_user',
    u'social.backends.pipeline.social.associate_user',
    u'social.backends.pipeline.social.load_extra_data',
    u'social.backends.pipeline.user.update_user_details'
)

#project id = thinking-volt-426

GOOGLE_OAUTH2_CLIENT_ID = u'1019514932196-nme23t11a8rvvrpmedmn5iii41119c0l.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = u'2GT8H077O3u5-OHGS41x4uGS'

#End Google LogIn


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    u'version': 1,
    u'disable_existing_loggers': False,
    u'filters': {
        u'require_debug_false': {
            u'()': u'django.utils.log.RequireDebugFalse'
        }
    },
    u'handlers': {
        u'mail_admins': {
            u'level': u'ERROR',
            u'filters': [u'require_debug_false'],
            u'class': u'django.utils.log.AdminEmailHandler'
        },
        u'dev_debug':{
            u'level': u'DEBUG',
            u'class': u'logging.FileHandler',
            u'filename': PROJECT_ROOT + u'/logs/debug.log'
        },
        u'dev_info':{
            u'level': u'INFO',
            u'class': u'logging.FileHandler',
            u'filename': PROJECT_ROOT + u'/logs/info.log'
        },
        u'dev_warning':{
            u'level': u'WARNING',
            u'class': u'logging.FileHandler',
            u'filename': PROJECT_ROOT + u'/logs/warning.log'
        },
        u'dev_error':{
            u'level': u'ERROR',
            u'class': u'logging.FileHandler',
            u'filename': PROJECT_ROOT + u'/logs/error.log'
        },
        u'dev_critical':{
            u'level': u'CRITICAL',
            u'class': u'logging.FileHandler',
            u'filename': PROJECT_ROOT + u'/logs/critical.log'
        }

    },
    u'loggers': {
        u'django.request': {
            u'handlers': [u'mail_admins'],
            u'level': u'ERROR',
            u'propagate': True,
        },
        u'logview.debugger': {
            u'handlers': [u'dev_debug'],
            u'level': u'DEBUG',
            u'propagate': True,
        },
        u'logview.info': {
            u'handlers': [u'dev_info'],
            u'level': u'INFO',
            u'propagate': True,
        },
        u'logview.warning': {
            u'handlers': [u'dev_warning'],
            u'level': u'WARNING',
            u'propagate': True,
        },
        u'logview.error': {
            u'handlers': [u'dev_error'],
            u'level': u'ERROR',
            u'propagate': True,
        },
        # 'logview.critical': {
        #     'handlers': ['dev_critical'],r
        #     'level': 'CRITICAL',
        #     'propagate': True,
        # },
    }
}
