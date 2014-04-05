# Django settings for freshmandebates project.
import os
import socket
#import envvars

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# check for production
#if socket.gethostname() == 'LAMP':
#    DATABASES = envvars.DATABASES
if False:
    print "What?"
else:
    DATABASES = {
        'default': {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': 'django.db.backends.sqlite3',
            # Or path to database file if using sqlite3.
            'NAME': 'dev.db',
            # The following settings are not used with sqlite3:
            'USER': '',
            'PASSWORD': '',
            # Empty for localhost through domain sockets or '127.0.0.1' for
            # localhost through TCP.
            'HOST': '',
            # Set to empty string for default.
            'PORT': '',
        }
    }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Vancouver'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

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
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_ROOT + "/freshmandebates/static/",
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '09-y+u=9v7s(3oak$dv@dlrmxw&3mbi%%7asq3m-0am08duk)7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'freshmandebates.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'freshmandebates.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_ROOT + "/freshmandebates/templates/"
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    # Admin
    'django.contrib.admin',
    'django.contrib.admindocs',
    # End of Admin
    'debates',
    #'debates.models.User',
    #'django_openid_auth',
    'social_auth',
    #'admin_import',
)

# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


#Google LogIn

# GAPPS_DOMAIN = 'mydomain.com'
# GAPPS_USERNAME = ''
# GAPPS_PASSWORD = ''

# Check for new groups, or only on initial user creation
GAPPS_ALWAY_ADD_GROUPS = False
AUTHENTICATION_BACKENDS = (
    #'social_auth.backends.google.GoogleOAuthBackend',
    #'social_auth.backends.CustomGoogleBackend.CustomGoogleBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend'
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/SplashPage'
LOGIN_ERROR_URL = '/login-error/'
LOGIN_URL = '/login/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/NewUserLogIn'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
SOCIAL_AUTH_UID_LENGTH = 222
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 135
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 125
LOGOUT_URL = '/logout/'
OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'



# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.contrib.auth.context_processors.auth',
#     'social_auth.context_processors.social_auth_by_type_backends',
#     'social_auth.context_processors.social_auth_backends',
#     'django.core.context_processors.static',
# )

SOCIAL_AUTH_DEFAULT_USERNAME = 'New_User'
SOCIAL_AUTH_UID_LENGTH = 222
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 135
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 125
SOCIAL_AUTH_ENABLED_BACKENDS = ('google')
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
#AUTH_USER_MODEL = 'debates.models.User'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details'
)

#project id = thinking-volt-426

GOOGLE_OAUTH2_CLIENT_ID = '1019514932196-nme23t11a8rvvrpmedmn5iii41119c0l.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = '2GT8H077O3u5-OHGS41x4uGS'

#End Google LogIn


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'dev_debug':{
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/Logs/debug.log'
        },
        'dev_info':{
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/Logs/info.log'
        },
        'dev_warning':{
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/Logs/warning.log'
        },
        'dev_error':{
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/Logs/error.log'
        },
        'dev_critical':{
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'filename': PROJECT_ROOT + '/Logs/critical.log'
        }

    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'logview.debugger': {
            'handlers': ['dev_debug'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'logview.info': {
            'handlers': ['dev_info'],
            'level': 'INFO',
            'propagate': True,
        },
        'logview.warning': {
            'handlers': ['dev_warning'],
            'level': 'WARNING',
            'propagate': True,
        },
        'logview.error': {
            'handlers': ['dev_error'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 'logview.critical': {
        #     'handlers': ['dev_critical'],r
        #     'level': 'CRITICAL',
        #     'propagate': True,
        # },
    }
}
