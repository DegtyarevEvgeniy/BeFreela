# -*- coding: utf-8 -*-

import os, sys
from django.core.wsgi import get_wsgi_application

#sys.path.insert(0, '/home/d/degtyarev/befreela/public_html/BeFreela/bizopt')
#sys.path.insert(1, '/home/d/degtyarev/befreela/public_html/venv_django/lib/python3.8/site-packages')

sys.path.insert(0, '/var/www/u1788843/data/www/befreela.ru/BeFreela/bizopt')
sys.path.insert(1, '/var/www/u1788843/data/djangovenv/lib/python3.10/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'bizopt.settings'


application = get_wsgi_application()