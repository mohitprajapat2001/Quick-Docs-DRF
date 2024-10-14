from pathlib import Path
from utils.constants import Settings
from os.path import join

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# ------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# ------------------------------------------------
SECRET_KEY = Settings.SECRET_KEY.value


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "quick_docs",
    "drf_spectacular",
    "quick_docs_drf",
    "rest_framework",
    "rest_framework_extensions",
    "rest_framework_nested",
]
# Middlewares
# ------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = Settings.ROOT_URLCONF.value

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(BASE_DIR, Settings.TEMPLATES.value)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = Settings.WSGI_APPLICATION.value


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / Settings.DATABASE_NAME.value,
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = Settings.LANGUAGE_CODE.value

TIME_ZONE = Settings.TIME_ZONE.value

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [join(BASE_DIR, Settings.STATICFILES_DIRS.value)]
STATIC_ROOT = join(BASE_DIR, Settings.STATIC_ROOT.value)

# Media files (Images, Videos, etc.)
# ------------------------------------------------
MEDIA_URL = Settings.MEDIA_URL.value
MEDIA_ROOT = join(BASE_DIR, Settings.MEDIA_ROOT.value)


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = Settings.DEFAULT_AUTO_FIELD.value


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_RATES": {"anon": "100/day", "user": "1000/day"},
}

# Quick Docs DRF Configuration
QUICK_DOCS_DRF = {
    "TITLE": "Quick Docs DRF",
    "DESCRIPTION": "Quick Docs DRF is a simple and easy-to-use documentation generator for Django REST Framework.",
    "VERSION": "1.0.0",
    "AUTHOR": "Mohit Prajapat",
    "AUTHOR_EMAIL": "mohit.prajapat@trootech.com",
    "API_URL": "/api/",
    "BASE_URL": "quick_docs.urls",
    "BASE_ROUTER_NAME": "quick_docs.urls.router",
    "VIEWSET_LISTS": [
        "quick_docs.views.BlogViewSet",
        "quick_docs.views.UserViewSet",
        "quick_docs.views.NewUserViewSet",
    ],
    # "TEMPLATE_STYLE": "tailwind",
    "SOCIAL_MEDIA": {
        "FACEBOOK": "itsmohit.codes",
        "INSTAGRAM": "itsmohit.codes",
        "GITHUB": "mohit-trootech",
        "LINKEDIN": "mohitprajapat2001",
        "X": "itsmohit.codes",
    },
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Your Project API",
    "DESCRIPTION": "Your project description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
