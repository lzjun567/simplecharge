import os

import sys

path = '/srv/www'

if path not in sys.path:
    sys.path.append('/srv/www')
sys.path.append('/srv/www/simplecharge')

os.environ['DJANGO_SETTINGS_MODULE'] = 'simplecharge.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
