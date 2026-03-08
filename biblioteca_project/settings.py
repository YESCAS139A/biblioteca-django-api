import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# CARGAR VARIABLES DE ENTORNO
# ==============================
# Esto busca el archivo .env en la raíz de tu proyecto
load_dotenv(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Lee la clave del .env, si no la encuentra usa la que tenías por defecto
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-ax!&u#e9@3*tj^&#5)sglnd%&^q92zh56rfjw^9lk!u*%2b90p')

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
    'django_extensions',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party apps
    'rest_framework',
    'corsheaders',
    'django_filters',
    'oauth2_provider', # Django OAuth Toolkit
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    # Tu aplicación
    'libros',
]

MIDDLEWARE = [
    'django.contrib.sites.middleware.CurrentSiteMiddleware', # Opcional pero recomendado para sites
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # CORS siempre arriba de CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'biblioteca_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'biblioteca_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'biblioteca_uni4',
        'USER': 'root',
        'PASSWORD': os.getenv('DB_PASSWORD', '123456'),  # ← Lee del .env, o usa '123456' por defecto
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'latin1',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
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


# ==============================
# CONFIGURACIÓN DE IDIOMA Y ZONA HORARIA
# ==============================
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Hermosillo'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==============================
# CONFIGURACIÓN DE CORS
# ==============================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
CORS_ALLOW_CREDENTIALS = True


# ==============================
# CONFIGURACIÓN DE REST FRAMEWORK
# ==============================
REST_FRAMEWORK = {
    # AUTENTICACIÓN: Qué métodos acepta tu API
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT (Token moderno)
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # Para OAuth 2.0
        'rest_framework.authentication.TokenAuthentication',          # Token tradicional
        'rest_framework.authentication.SessionAuthentication',        # Sesión (para admin)
    ],
    
    # PERMISOS: Qué pueden hacer los usuarios
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    
    # PAGINACIÓN: Cuántos resultados por página
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    
    # FILTROS: Permitir búsquedas y ordenamiento
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}


# =======================
# SIMPLE JWT CONFIG
# =======================
SIMPLE_JWT = {
    # ⏱️ DURACIÓN DE TOKENS
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),    # Token de acceso válido 1 hora
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),    # Token de refresco válido 7 días
    
    # 🔄 ROTACIÓN DE TOKENS (Seguridad extra)
    'ROTATE_REFRESH_TOKENS': True,                  # Genera nuevo refresh al refrescar
    'BLACKLIST_AFTER_ROTATION': True,               # Invalida el refresh anterior
    'UPDATE_LAST_LOGIN': True,                      # Actualiza last_login del usuario
    
    # 🔐 ALGORITMO Y CLAVE DE FIRMA
    'ALGORITHM': 'HS256',                           # HMAC SHA-256 (más común)
    'SIGNING_KEY': SECRET_KEY,                      # Usa la SECRET_KEY de Django
    'VERIFYING_KEY': None,                          # Solo para algoritmos asimétricos (RSA)
    
    # 📋 CONFIGURACIÓN DE HEADERS
    'AUTH_HEADER_TYPES': ('Bearer',),               # Tipo: "Authorization: Bearer TOKEN"
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',       # Nombre del header
    
    # 👤 CLAIMS DEL USUARIO
    'USER_ID_FIELD': 'id',                          # Campo del modelo User para ID
    'USER_ID_CLAIM': 'user_id',                     # Nombre del claim en el payload
    
    # 🎫 CONFIGURACIÓN DEL TOKEN
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',               # Claim que identifica tipo de token
    'JTI_CLAIM': 'jti',                             # JWT ID (identificador único)
}


# =======================
# SITE CONFIGURATION
# =======================
SITE_ID = 1


# =======================
# AUTHENTICATION BACKENDS
# =======================
AUTHENTICATION_BACKENDS = [
    # Backend por defecto de Django (username/password)
    'django.contrib.auth.backends.ModelBackend',
    
    # Backend de allauth para OAuth social
    'allauth.account.auth_backends.AuthenticationBackend',
]


# =======================
# DJANGO ALLAUTH CONFIG
# =======================

# Configuración de cuentas
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False  # Solo email para login social
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # Para desarrollo: 'mandatory' en producción
ACCOUNT_EMAIL_MAX_LENGTH = 190

# Configuración de login social
SOCIALACCOUNT_AUTO_SIGNUP = True  # Crear usuario automáticamente
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'  # No verificar email en OAuth

# Proveedores OAuth configurados (Leyendo del .env)
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': os.getenv('GOOGLE_CLIENT_ID', ''),     # ← AHORA LEE DEL .ENV
            'secret': os.getenv('GOOGLE_CLIENT_SECRET', ''),    # ← AHORA LEE DEL .ENV
            'key': ''
        }
    }
}

# =======================
# REDIRECCIONES DE LOGIN (¡AGREGADO!)
# =======================
LOGIN_REDIRECT_URL = '/'           # A dónde ir tras login exitoso
LOGOUT_REDIRECT_URL = '/'          # A dónde ir tras logout
SOCIALACCOUNT_LOGIN_ON_GET = True  # Para evitar el prompt doble de Google

# =======================
# OAUTH 2.0 PROVIDER SETTINGS (FUSIONADO Y CORREGIDO)
# =======================
OAUTH2_PROVIDER = {
    # Tiempo de vida de los tokens
    'ACCESS_TOKEN_EXPIRE_SECONDS': 3600,        # 1 hora
    'REFRESH_TOKEN_EXPIRE_SECONDS': 86400 * 7,  # 7 días
    
    # Scopes disponibles
    'SCOPES': {
        'read': 'Acceso de lectura',
        'write': 'Acceso de escritura',
    },
    
    # Modelos de tokens
    'ACCESS_TOKEN_MODEL': 'oauth2_provider.AccessToken',
    'APPLICATION_MODEL': 'oauth2_provider.Application',
    'REFRESH_TOKEN_MODEL': 'oauth2_provider.RefreshToken',
    'ID_TOKEN_MODEL': 'oauth2_provider.IDToken',
}