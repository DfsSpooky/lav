# settings.py

import os
from pathlib import Path
from dotenv import load_dotenv

# ATENCIÓN: Se añade la carga de variables de entorno desde un archivo .env
# Esto debe estar al principio para que las variables estén disponibles.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))


# ATENCIÓN: La SECRET_KEY se obtiene de forma segura desde las variables de entorno.
# El valor original se deja como respaldo solo para desarrollo si el .env no existe.
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')

# ATENCIÓN: DEBUG debe ser False en producción. Se controla con una variable de entorno.
DEBUG = os.getenv('DJANGO_DEBUG', 'False').lower() in ['true', '1', 't']

# ATENCIÓN: Añade la IP de tu servidor y tu dominio a las hosts permitidos.
# Se controla con una variable de entorno que puede contener una lista separada por comas.
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'django_select2',  # Añadido para Select2
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

ROOT_URLCONF = 'laundry_app.urls'

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

WSGI_APPLICATION = 'laundry_app.wsgi.application'


# ATENCIÓN: Configuración de la Base de Datos para PostgreSQL en producción.
# Las credenciales se leen de forma segura desde las variables de entorno.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'), # 'db' es el nombre del servicio en docker-compose
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Directorio donde el servidor de desarrollo busca archivos estáticos.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# ATENCIÓN: Directorio donde 'collectstatic' reunirá todos los archivos estáticos para producción.
# Nginx servirá los archivos desde este directorio.
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Media files (Archivos subidos por el usuario)
MEDIA_URL = '/media/'

# ATENCIÓN: Directorio para los archivos subidos por los usuarios en producción.
# Se alinea con el volumen de Docker definido en docker-compose.yml.
MEDIA_ROOT = BASE_DIR / 'mediafiles'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'

# Configuración para django-select2
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'select2': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'select2',
    }
}
SELECT2_CACHE_BACKEND = 'select2'