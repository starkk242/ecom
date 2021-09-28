# Development settings

from .base import *

SECRET_KEY = 'f41z(gp#mm7ktjo1bfux-n*0!mlti$9d1@k_sws@&kl*@tfi21'

DEBUG = True
USE_TZ = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'limitless-fjord-13336.herokuapp.com','*']

DATABASES = {
    "default": {
        "ENGINE": os.environ.get(
            "SQL_ENGINE", "django.db.backends.postgresql"
        ),
        "NAME": os.environ.get("SQL_DATABASE", "antbhyvh"),
        "USER": os.environ.get("SQL_USER", "antbhyvh"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "vftQF6RW67gIRAKQlqXA-dJE-hsnxM4C"),
        "HOST": os.environ.get("SQL_HOST", "satao.db.elephantsql.com"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STRIPE_SECRET_KEY = 'YOUR_STRIPE_SECRET_KEY'
STRIPE_PUBLISHABLE_KEY = 'YOUR_STRIPE_PUBLISHABLE_KEY'
