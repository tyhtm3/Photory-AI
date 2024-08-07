"""
Django settings for photory project.

Generated by 'django-admin startproject' using Django 2.1.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import datetime
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j2h#co&lv7af2!$b%r4^p!p-w+=nf(i!1r#65*@^o=_$b91_nd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','k3a205.p.ssafy.io','localhost:8000']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django extensions
    'django_extensions',
    
    # rest_auth + allauth
    'rest_auth', # login,logout
    'django.contrib.sites',
    'allauth', # signup
    'allauth.account',  # signup
    'allauth.socialaccount',
    'rest_auth.registration',  # signup

    # include the providers you want to enable:
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    #DRF
    'rest_framework',
    'rest_framework.authtoken',
    #cors
    'corsheaders',

    #My apps
    'storys',
    'accounts',
    'board',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'photory.urls'

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

WSGI_APPLICATION = 'photory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#Custom User settings
AUTH_USER_MODEL = 'accounts.User'
REST_AUTH_REGISTER_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer',
    'REGISTER_SERIALIZER': 'accounts.serializers.RegistrationSerializer',
}

# custom user detail 가져오기
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer',
}

ACCOUNT_ADAPTER = 'accounts.adapter.CustomAccountAdapter'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None  # 사용자 지정 모델에 username 필드가 없을 경우
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_USE_JWT = True
ACCOUNT_LOGOUT_ON_GET = True

# django sites app setting  
SITE_ID =1

# DRF auth settings
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.TokenAuthentication',

#     ]
# }
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_PAGINATION_CLASS': 'apps.core.pagination.StandardResultsSetPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}

# JWT
REST_USE_JWT = True
ACCOUNT_LOGOUT_ON_GET = True


JWT_AUTH = {
   'JWT_SECRET_KEY' : SECRET_KEY,
   'JWT_ALGORITHM' : 'HS256',
   'JWT_EXPIRATION_DELTA' : datetime.timedelta(seconds=86400),
   'JWT_ALLOW_REFRESH' : False,
   'JWT_REFRESH_EXPIRATION_DELTA' : datetime.timedelta(days=7),
}


# CORS Allow
CORS_ORIGIN_ALLOW_ALL = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# allauth d
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # <- 디폴트 모델 백엔드
    'allauth.account.auth_backends.AuthenticationBackend', # <- 추가
)

# Django Extensions
SHELL_PLUS = "ipython"


# 이미지 업로드 설정
MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')