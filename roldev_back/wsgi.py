"""
WSGI config for roldev_back project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roldev_back.settings')
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
load_dotenv(os.path.join(SITE_ROOT, '.env'))

application = get_wsgi_application()
