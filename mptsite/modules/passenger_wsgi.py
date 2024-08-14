# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2520250/data/www/code-future-python.ru/server')
sys.path.insert(1, '/var/www/u2520250/data/djangoenv/lib/python3.9.0/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()