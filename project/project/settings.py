"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from .mconfig import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

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

    # D1.3 add flatpages
    'django.contrib.sites',
    'django.contrib.flatpages',
    # D1.4 add flatpages
    'fpages',
    # D2.4
    'simpleapp',
    'accounts',
    'django_filters',

    # D5
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',

    # D6.5. Выполнение задач по расписанию
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # D1.3 add flatpages
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # D1.3 add flatpages
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # D6.3 # `allauth` обязательно нужен этот процессор
                'django.template.context_processors.request',
            ],
        },
    },
]

# D5
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend', ]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'UTC'  # UTC+8 - Hongkong

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# LOGIN_URL = ''  # страница входа
LOGIN_REDIRECT_URL = "/portal"  # LOGOUT_REDIRECT_URL = "/accounts/login"
# LOGOUT_REDIRECT_URL = '/accounts/login'
LOGOUT_REDIRECT_URL = "/portal"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# D1.5 bootstrap
STATICFILES_DIRS = [BASE_DIR / "static"]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = config['ACCOUNT_EMAIL_VERIFICATION']  # проверяет наличие реальных почтовых ящиков!
print('ACCOUNT_EMAIL_VERIFICATION = ', ACCOUNT_EMAIL_VERIFICATION)# (пароль для сайта любой!)
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # не проверяет наличие реальных почтовых ящиков
# Кроме этого значения, переменная может принимать и два других:
# mandatory — не пускать пользователя на сайт до момента подтверждения почты;
# optional — сообщение о подтверждении будет отправлено, но пользователь может залогиниться без подтверждения почты.
ACCOUNT_CONFIRM_EMAIL_ON_GET = True     # позволит избежать дополнительного входа и активирует аккаунт сразу,
                                        # как только мы перейдём по ссылке.
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3  # Количество неудачных попыток входа в систему. 'None' - отключить ограничение.
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400  # секунд запрета на вход посте N неудачных попыток.
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS хранит количество дней, когда доступна ссылка на подтверждение регистрации.
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

# D6.2
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # значение по умолчанию (реальная отправка писем)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # вывод отправляемого в консоль (Terminal
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
<<<<<<< HEAD
EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = config['EMAIL_USE_TLS']
EMAIL_USE_SSL = config['EMAIL_USE_SSL']
=======
EMAIL_HOST_USER = "Rassven@yandex.ru"
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
>>>>>>> origin/main
EMAIL_SUBJECT_PREFIX = 'News portal: '  # EMAIL_SUBJECT_PREFIX = '[Django]'  # Префикс темы письма (managers & admins).
DEFAULT_FROM_EMAIL = config['DEFAULT_FROM_EMAIL']  # Будет отображаться в поле «отправитель» у получателя письма.
SERVER_EMAIL = config['SERVER_EMAIL']
MANAGERS = (config['MANAGERS'],)  # Не те менеджеры, что созданы под Админкой.
ADMINS = (config['ADMINS'],)

