import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Liv.settings')

application = get_wsgi_application()

#gunicorn Liv.wsgi:application --bind 0.0.0.0:$PORT
