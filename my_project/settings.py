"""
Django settings for my_project project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import dj_database_url
from pathlib import Path
import os
from decouple import config



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY =  config('SECRET_KEY')
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]


# for online purposes
# DEBUG = os.environ.get('DEBUG','False').lower() == 'true' 
# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOST').split('')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'django.contrib.gis',

    'app_accounts',

    'app_notary',
    'app_notary_ver2',
    'app_forms',

    'app_import',
    'app_cairo',
    
    'app_htmx',
    'crispy_forms',
    'import_export',
    'crispy_bootstrap5',
    'widget_tweaks', # pip install django-widget-tweaks
    "django_htmx", #python -m pip install django-htmx

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     #other installs   
     "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = 'my_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [
          os.path.join(BASE_DIR,"templates")
                 ],
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

WSGI_APPLICATION = 'my_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },

    #      'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     # 'ENGINE':'django.contrib.gis.db.backends.postgis',

    #     'NAME':     config('DB_NAME'),
    #     'USER':     config('DB_USER'),
    #     'PASSWORD': config('DB_PASSWORD'),
    #     'HOST': config('DB_HOST'),
    # },
}

DATABASES={
  "default":dj_database_url.parse(os.environ.get("DATABASE_URL"))
  
}

# database_url = os.environ.get('DATABASE_URL')
# DATABASES['default']= dj_database_url.parse('database_url')


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

# crispy
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = '/assets/'
STATIC_ROOT = BASE_DIR/'static'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR,'assets'),
)


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MEDIA FILES CONFIG
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'


EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =   os.environ.get('EMAIL_PASSWORD')

# '''email setting  '''
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT', cast=int)
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD =   config('EMAIL_PASSWORD')


EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL =   os.environ.get('DEFAULT_FROM_EMAIL')
# DEFAULT_FROM_EMAIL=config('DEFAULT_FROM_EMAIL')



# EMAIL_BACKEND = config('EMAIL_BACKEND')
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
# GOOGLE_API_KEY=config('GOOGLE_API_KEY')

INTERNAL_IPS=[
  '127.0.0.1',

]


# os.environ['PATH'] = os.path.join(BASE_DIR, 'project_env\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
# os.environ['PROJ_LIB'] = os.path.join(BASE_DIR, 'project_env\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']

GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, 'project_env\Lib\site-packages\osgeo\gdal304.dll')