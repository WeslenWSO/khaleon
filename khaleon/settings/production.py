from .base import *  # noqa: F403

DEBUG = False

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Render define RENDER_EXTERNAL_HOSTNAME automaticamente
render_hostname = env("RENDER_EXTERNAL_HOSTNAME", default=None)
if render_hostname:
    ALLOWED_HOSTS = list(set(ALLOWED_HOSTS + [render_hostname, ".onrender.com"]))
    CSRF_TRUSTED_ORIGINS = [f"https://{render_hostname}"]
else:
    CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])
