from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!


# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.messages",
    
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "social_auth"

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "allauth.account.middleware.AccountMiddleware",

    

]

ROOT_URLCONF = "chatbotcerebro.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "chatbotcerebro.wsgi.application"



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "es"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/





# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'chat_interface'


ACCOUNT_AUTHENTICATION_METHOD = "email" # Permite autenticación vía usuario o correo
ACCOUNT_EMAIL_REQUIRED = True # Obliga a los usuarios a proporcionar un correo electrónico
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Hace obligatoria la verificación del correo
ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # Confirma el correo electrónico cuando el usuario accede al enlace de confirmación
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False  # Evita el inicio de sesión automático tras la confirmación del correo


#Configuración de envío de correos electrónicos simulados por consola
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Configuración de envío de correos electrónicos con SendGrid
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'  # Este es el nombre de usuario estándar para SendGrid
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')  # Utilizar variable de entorno
DEFAULT_FROM_EMAIL = 'horacio.colina@hotmail.com' # Correo electrónico por defecto para enviar correos electrónicos



EMAIL_CONFIRMATION_EXPIRE_DAYS = 2 # Configuración para que el token de confirmación de email expire en 2 días

#COnfiguración base de endpoint de la API de langchain, variable de entorno en desarrollo de .env y docker de docker-compose.yml

