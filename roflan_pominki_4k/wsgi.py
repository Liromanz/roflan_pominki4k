import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roflan_pominki_4k.settings')

application = get_wsgi_application()
