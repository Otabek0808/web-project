"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# from ckeditor_uploader.fields import RichTextUploadingField # ckeditor
# from ckeditor_demo.settings import STATICFILES_STORAGE
from django.contrib.staticfiles.storage import StaticFilesStorage
from django.utils.translation import gettext_lazy as _ # tarjima fayli uchun
from django.conf.global_settings import MEDIA_URL, STATICFILES_DIRS, STATIC_ROOT
from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True  # Ishlatilayotgan muhitda True bo'lishi kerak
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']  # O'zingizning domeningizni qo'shing

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # 'ckeditor',
    # 'ckeditor_uploader',
    'tinymce',
    'crispy_forms',
    'crispy_bootstrap5',
    'crispy_bootstrap4',

    'accounts',
    'pages',
    'articles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # O'z shablonlaringiz joylashgan joy
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
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default" : env.dj_db_url('DATABASE_URL')
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

USE_L10N = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGES = [
    ('uz', _('O\'zbekcha')),
    ('en', _('English')),
    ('ru', _('Русский')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static",  ]# O'zgartiring yoki to'g'ri yo'lni ko'rsating
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'

# EMAIL BACKEND
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Bootstrap 4 ni tanlang
CRISPY_TEMPLATE_PACK = 'bootstrap5'  # Bootstrap 4 ni tanlang
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

# MEDIA     
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CKEDITORS CONFIG

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Full',
#     },
# }
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline', 'Strike'],
#             ['NumberedList', 'BulletedList'],
#             ['Link', 'Unlink', 'Image', 'Table'],
#             ['Source'],
#         ],
#         'width': '100%',
#     },
# }

# CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_RESTRICT_BY_USER = True
# CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
# CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'