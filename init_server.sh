#!/usr/bin/env bash
# init-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (python manage.py createsuperuser --no-input)
fi
python manage.py collectstatic --noinput
python manage.py migrate
(gunicorn upload_site.wsgi --user www-data --bind 0.0.0.0:3010 --workers 3) &
nginx -g "daemon off;"