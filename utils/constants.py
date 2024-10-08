from dotenv import dotenv_values
from enum import Enum


# Settings Constants
# ------------------------------------------------
class Settings(Enum):
    config = dotenv_values(".env")
    SECRET_KEY = config.get("SECRET_KEY")
    ROOT_URLCONF = "quick_docs.urls"
    WSGI_APPLICATION = "quick_docs.wsgi.application"
    TEMPLATES = "templates/"
    STATIC = "static/"
    STATIC_ROOT = "assets/"
    STATICFILES_DIRS = "templates/static"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    USE_I18N = True
    USE_TZ = True
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    DEBUG = True
    ALLOWED_HOSTS = []
    DATABASE_NAME = "db.sqlite3"
