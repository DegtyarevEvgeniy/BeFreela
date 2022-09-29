# -*- coding: utf-8 -*-

import os, sys
from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/home/d/degtyarev/seller.befreela/public_html/BeFreela/partner')
sys.path.insert(1, '/home/d/degtyarev/seller.befreela/public_html/venv_django/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'partner.settings'


application = get_wsgi_application()