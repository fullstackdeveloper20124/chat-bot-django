from dotenv import load_dotenv
from .base import *


SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure-k+*^hb$cm^)tnf!s&8&r_041)&*36l6xs)$jvl=u6!xyh$yk6rqis8')
ALLOWED_HOSTS = ['django', 'localhost', '127.0.0.1', '[::1]']


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
