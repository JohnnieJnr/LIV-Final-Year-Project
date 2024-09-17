"""
WSGI config for Liv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Liv.settings')

application = get_wsgi_application()

# gunicorn Liv.wsgi:application --bind 0.0.0.0:$PORT
