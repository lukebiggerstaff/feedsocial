import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Environment = {
    'DJANGO_DEBUG' : bool(int(os.environ.get("DJANGO_DEBUG"))),
    'DJANGO_SECRET' : os.environ.get("DJANGO_SECRET"),
    'DJANGO_DB_NAME' : os.environ.get("DJANGO_DB_NAME"),
    'DJANGO_DB_USER' : os.environ.get("DJANGO_DB_USER"),
    'DJANGO_DB_PASSWORD' : os.environ.get("DJANGO_DB_PASSWORD"),
    'DJANGO_DB_HOST' : os.environ.get("DJANGO_DB_HOST"),
    'DJANGO_DB_PORT' : os.environ.get("DJANGO_DB_PORT"),
    'DJANGO_SITENAME' : os.environ.get("DJANGO_SITENAME"),
}


DEBUG = Environment["DJANGO_DEBUG"]

SECRET_KEY = Environment["DJANGO_SECRET"]

ALLOWED_HOSTS = ["*" if Environment["DJANGO_DEBUG"] else Environment["DJANGO_SITENAME"]]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': Environment['DJANGO_DB_NAME'],
        'USER': Environment['DJANGO_DB_USER'],
        'PASSWORD': Environment['DJANGO_DB_PASSWORD'],
        'HOST': Environment['DJANGO_DB_HOST'],
        'PORT': Environment['DJANGO_DB_PORT'],
    }
}



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feed',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'feedsocial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'feedsocial.wsgi.application'



AUTH_USER_MODEL = 'accounts.FeedSocialUser'

LOGIN_REDIRECT_URL = 'feed'

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
