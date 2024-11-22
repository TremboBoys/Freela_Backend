

from pathlib import Path
from datetime import timedelta
#import cloudinary, cloudinary.uploader


import os
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(m*#e0fjcj1))gg$gx_ox3&m^q^zx_95-m@r2dy-t^i8)wbp)j'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']

DEBUG = True
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
    'core.pay',
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
    'keras',
    'langdetect',
    'sentencepiece',
    'django_filters',
    'cloudinary_storage',
    
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
    'whitenoise.middleware.WhiteNoiseMiddleware'
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
    'default': dj_database_url.config(
        default='postgresql://hackathon_k28t_user:N9FeBvPjSnde453f8FpWM0fP0caB2pb7@dpg-csrpe6bv2p9s73bg0c2g-a.ohio-postgres.render.com/hackathon_k28t',
        conn_max_age=600,
        ssl_require=True
    )
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

CORS_ALLOW_ALL_ORIGINS = True

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

REST_FRAMEWORK = {
#    "DEFAULT_AUTHENTICATION_CLASSES": ("core.authentication.TokenAuthentication",), # Autenticação no passage.id
#    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated"), # Permissão total para usuários autenticados
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  
    "http://localhost:5173",
]

#CLOUDINARY_STORAGE = {
#    "CLOUD_NAME": 'dm2odcrnf',
#    "API_KEY": '392291948516824',
#    "API_SECRET": '8L8ApfYnDq6_YiXSd4lAgDmZGnI'
#}
MEDIA_ENDPOINT = "/media/"
CLOUDINARY_URL = 'https://console.cloudinary.com/pm/c-8f6c5d0d412fd7c17a48c2d9174667/media-explorer'
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "images")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "martinsbarroskaua85@gmail.com"
EMAIL_HOST_PASSWORD = "hlgx xdmn prhf areg"

APPEND_SLASH = False

MEDIA_URL = '/media/'
