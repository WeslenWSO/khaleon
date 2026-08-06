#!/usr/bin/env bash
set -o errexit

export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-khaleon.settings.production}"

python manage.py migrate --noinput
python manage.py seed_demo
exec gunicorn khaleon.wsgi:application --bind "0.0.0.0:${PORT:-8000}"
