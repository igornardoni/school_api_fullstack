from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'escola',
    "corsheaders",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'setup.urls'

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

WSGI_APPLICATION = 'setup.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
MEDIA_URL = '/media/'


REST_FRAMEWORK = {
 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
 'DEFAULT_PERMISSIONS_CLASSES': [
     'rest_framework.permissions.IsAuthenticated',
     'rest_framework.permissions.DjangoModelPermissions'
 ],
 'DEFAULT_AUTHENTICATION_CLASSES': [
     'rest_framework.authentication.BasicAuthentication',
 ],
 'DEFAULT_THROTTLE_CLASSES': [
     'rest_framework.throttling.AnonRateThrottle',

 ],
 'DEFAULT_THROTTLE_RATES': {
     'anon': '50/day',
 },
 # 'DEFAULT_PARSER_CLASSES': [
 #        'rest_framework.parsers.JSONParser',
 #        'rest_framework_xml.parsers.XMLParser',
 #        'rest_framework_yaml.parsers.YAMLParser',
 #    ],
 # 'DEFAULT_RENDERER_CLASSES': [
 #        'rest_framework.renderers.JSONRenderer',
 #        'rest_framework_xml.renderers.XMLRenderer',
 #        'rest_framework_yaml.renderers.YAMLRenderer',
 #    ],
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379/1',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     }
# }

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

SESSION_CACHE_ALIAS = 'default'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


