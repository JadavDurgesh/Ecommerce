from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yi8#@7!&g^z2u(0n0#+ze^we9az!f%78r&lokbvszbvw1&4j^p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','mysite.org']  # <-- Here


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'social_django',# <-- Here
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',# <-- Here
]

ROOT_URLCONF = 'jewelryproject.urls'

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

                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect', # <-- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'jewelryproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = { message_constants.DEBUG: 'debug',
                 message_constants.INFO: 'info',
                 message_constants.SUCCESS: 'success',
                 message_constants.WARNING: 'warning',
                 message_constants.ERROR: 'danger',}







EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'devansh3334@gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = 'kkzteitslxkudizs'


AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',    # <-- Here
    'social_core.backends.instagram.InstagramOAuth2',  # <-- Here
    'social_core.backends.google.GoogleOAuth2',        # <-- Here
    'social_core.backends.twitter.TwitterOAuth',       # <-- Here
    'social_core.backends.github.GithubOAuth2',        # <-- Here

    'django.contrib.auth.backends.ModelBackend',       # <-- Here
)

SOCIAL_AUTH_FACEBOOK_KEY = '4789104841217856'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '29396f826df08486c428c2d4c1137fe6 '  # App Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '850192774609-etc7i5h3fvq5gp80jr7hd3vii2sj2j6k.apps.googleusercontent.com'  # App ID
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'  # App Secret


LOGIN_REDIRECT_URL = '/'