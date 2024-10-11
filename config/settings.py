

from pathlib import Path
from datetime import timedelta
import cloudinary, cloudinary.uploader
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(m*#e0fjcj1))gg$gx_ox3&m^q^zx_95-m@r2dy-t^i8)wbp)j'

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
    'corsheaders',     
    'simplejwt',
    'core.user',
    'core.perfil',
    'core.project',
    'core.proposal',
    'core.report',
    'core.service',
    'core.ads',
    'reportlab',
    'cloudinary',
    'requests',
    'uploader',
    'transformers',
    'tensorflow',
    'torch',
    'keras',
    'langdetect',
    'sentencepiece',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template/html')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    }


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

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework_simplejwt.authentication.JWTAuthentication',
#    ),
#    'DEFAULT_PERMISSION_CLASSES': (
#        'rest_framework.permissions.IsAuthenticated',
#    ),
#
#}

#SIMPLE_JWT = {
#    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
#    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#    'AUTH_HEADER_TYPES': ('Bearer',),
#}

#REST_FRAMEWORK = {
#    "DEFAULT_AUTHENTICATION_CLASSES": ("core.authentication.TokenAuthentication",), # Autenticação no passage.id
#    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated"), # Permissão total para usuários autenticados
#}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
    "http://localhost:5173",
]

cl = cloudinary.config(
    cloud_name='dm2odcrnf',
    api_key='392291948516824',
    api_secret='8L8ApfYnDq6_YiXSd4lAgDmZGnI'
)


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "martinsbarroskaua85@gmail.com"
EMAIL_HOST_PASSWORD = "hlgx xdmn prhf areg"

PASSAGE_APP_ID = 'RqVDnxkssH8vwNCSKmmCIl1b'
PASSAGE_API_KEY = 'LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JSUJDZ0tDQVFFQTRGdTBYWFRXd1pXbkdWcTRMT0VRZXhZbjZHUDJNWnJsbzVSdFNLZHNsOXBIMEQvYllWanMKTWhoMWtQT3lPRGsrcjBxQ2Iwd3h6ZzlmYnNYb1kzWXgwUmR6NzBXckFybFRHc2JnV0l1V2lwOHhDem9wREZoWApKTkhDRENqZWFkSkpKY2l1QVgyVmdTMm4zc2thNnVWZ1I3QzNjUU5wK0FnRWpKMEEwUXAzZFBGc2RDdkFtbXpDCkVqWVg3UVdHSVBia0tCSUR3b1JKYk1CdXhkdlZTUitHYUU5cXFPS3VOSlF1Z3Q3Q1hXbnpGMEJxa2NlWjVSVmgKdXozRlJndHZjREpXVWNFcGgwTktVYjJsWGM1bmdDUTBrVEw0QXhKUzZyVmxzS3BxNXdnd2xPbFN1VFB6RlJENApZV1pncGNhL0tyNlc1Nks1ZmRTdFJrc2txUDhGRlY0UTdRSURBUUFCCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0K'
AUTH_USER_MODEL = 'user.User'
