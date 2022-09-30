# -*- coding: utf-8 -*-
import os, sys
#sys.path.insert(0, '/var/www/u1788843/data/www/befreela.ru/bizopt')
sys.path.insert(0, '/var/www/u1788843/data/www/befreela.ru/BeFreela/bizopt')
sys.path.insert(1, '/var/www/u1788843/data/djangovenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bizopt.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
