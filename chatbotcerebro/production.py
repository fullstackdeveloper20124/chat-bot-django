from .base import *
import os
from dotenv import load_dotenv
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['botpoint.azurewebsites.net']

# Forzar el uso de HTTPS para las sesiones
SESSION_COOKIE_SECURE = True

# Forzar el uso de HTTPS para cookies CSRF
CSRF_COOKIE_SECURE = True

# Utilizado para redirigir todas las peticiones HTTP no seguras a HTTPS
SECURE_SSL_REDIRECT = True

# El encabezado `X-Forwarded-Proto` sea reconocido, muy útil si estás detrás de un proxy o balanceador de carga
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}

DEFAULT_FILE_STORAGE = 'chatbotcerebro.azure_storage.AzureMediaStorage'
STATICFILES_STORAGE = 'chatbotcerebro.azure_storage.AzureStaticStorage'

AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'