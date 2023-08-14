import os
import sys
from datetime import timedelta, datetime

import django.conf.locale
from corsheaders.defaults import default_headers
from dotenv import dotenv_values

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'apps'))
ENV = dotenv_values(os.path.join(BASE_DIR, '../../.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '13scl_s5v&=r#wg4rjjx=qr19hnf^!=q3gs&gpw2*$tk^uj!nm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CURRENT_HOST = 'http://dicore.uz:5005'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third-party
    'drf_yasg',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'background_task',
    'debug_toolbar',
    'django_crontab',

    # custom apps
    'contacts',
    'files',
    'knowledge_base',
    # 'mailing',
    'service_desk',
    'shared',
    'task_manager',
    'users',
    'sla',
    'sales_bpm',
    'file_management'
]


MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'users.middleware.UserRequestSessionsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '')],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': ENV.get('DB_NAME', 'shar_dev_db'),
        'USER': ENV.get('DB_USER', 'zk_user'),
        'PASSWORD': ENV.get('DB_PASSWORD', 'Br3lgkmgte7377@'),
        'HOST': ENV.get('DB_HOST', '127.0.0.1'),
        'PORT': ENV.get('DB_PORT', '1111'),
    },
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'sharqdbtest',
    #     'USER': 'postgres',
    #     'PASSWORD': 'root',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # }
}

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
# REDIS_HOST = ENV.get('REDIS_HOST', 'localhost')
# REDIS_PORT = ENV.get('REDIS_PORT', '6379')
# REDIS_DB = int(ENV.get('REDIS_DB', 0))

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
    ('uz', 'Uzbek'),
)

EXTRA_LANG_INFO = {
    'uz': {
        'bidi': False,  # right-to-left
        'code': 'uz',
        'name': 'Uzbek',  # name in English
        'name_local': 'Uzbek',  # locale name
    },
}

django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

MODELTRANSLATION_LANGUAGES = ('ru', 'en', 'uz')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, os.environ.get('STATIC_PATH', '../static/'))
MEDIA_ROOT = os.path.join(BASE_DIR, os.environ.get('MEDIA_PATH', '../../media/'))

# Cross domain list

# CORS_ALLOWED_ORIGINS = [
#     "http://zk.leocrm.uz",
# ]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = default_headers + (
    'cache-control',
)

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'shared.rest_framework.permissions.CustomDjangoModelPermissions',
        # 'shared.rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'shared.rest_framework.paging.PageNumberPagination',
    'PAGE_SIZE': 10,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Swagger settings
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Type in the *\'Value\'* input box below: **\'Bearer &lt;JWT&gt;\'**, where JWT is the JSON web token you get back when logging in.'
        }
    },
    'DOC_EXPANSION': 'list',  # “none”, “list”, or “full”
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ENABLE_STACKTRACES = True

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

now = datetime.now()
MAILING_RESPONSE_PATH = BASE_DIR + '/../media/responses/' + str(now.date()) + '.txt'

CRONJOBS = [
    ('0 13,18,22 * * *', 'apps.service_desk.cron.report_daily_all_calls'),
    ('0 13,18,22 * * *', 'apps.service_desk.cron.report_daily_hourly'),
    ('0 13,18,22 * * *', 'apps.service_desk.cron.report_daily_by_products'),
    (
        '0 * * * *', 'sla.cron_jobs.synchron_feedback.synchronize_create',
        '>> ' + os.path.join(BASE_DIR, 'logs/test.log')),
    (
        '5 * * * *', 'sla.cron_jobs.synchron_feedback.synchronize_update',
        '>> ' + os.path.join(BASE_DIR, 'logs/test.log')),
]

SLA_SETTINGS = {
    "manager_url": "http://zk.leocrm.uz:82",
    "sla_project_id": os.environ.get("SLA_PROJECT_ID", 10),
}


#j3QQ4HHH7777@