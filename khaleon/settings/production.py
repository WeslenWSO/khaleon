from .base import *  # noqa: F403

DEBUG = False

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SITE_DOMAINS = ["khaleon.com.br", "www.khaleon.com.br"]
ALLOWED_HOSTS = list(set(ALLOWED_HOSTS + SITE_DOMAINS + [".onrender.com"]))

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=[
        "https://khaleon.com.br",
        "https://www.khaleon.com.br",
    ],
)

render_hostname = env("RENDER_EXTERNAL_HOSTNAME", default=None)
if render_hostname:
    ALLOWED_HOSTS.append(render_hostname)
    CSRF_TRUSTED_ORIGINS.append(f"https://{render_hostname}")

ALLOWED_HOSTS = list(set(ALLOWED_HOSTS))
CSRF_TRUSTED_ORIGINS = list(set(CSRF_TRUSTED_ORIGINS))

# Render: serve arquivos de static/ sem depender de collectstatic no build
WHITENOISE_USE_FINDERS = True
STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.StaticFilesStorage"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
