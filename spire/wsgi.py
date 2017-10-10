"""
WSGI config for spire project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from configurations.wsgi import get_wsgi_application

from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spire.settings')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prompt.settings")
#os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')


application = DjangoWhiteNoise(get_wsgi_application())




# application = get_wsgi_application()

# python manage.py runserver --settings=mysite.settings --configuration=Dev