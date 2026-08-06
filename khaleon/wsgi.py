"""
WSGI config for khaleon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "khaleon.settings.production")

from khaleon.render_boot import run_render_boot

run_render_boot()

application = get_wsgi_application()
