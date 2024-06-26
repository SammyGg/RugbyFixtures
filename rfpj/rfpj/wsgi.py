"""
WSGI config for rfpj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

settings_module = 'rfpj.deployment_pr' if 'WEBSITE_HOSTNAME' in os.environ else 'rfpj.settings'
#settings_module = 'ggpj.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rfpj.settings')

application = get_wsgi_application()
