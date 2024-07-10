"""
WSGI config for signup_form project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "signup_form.settings")

application = get_wsgi_application()
