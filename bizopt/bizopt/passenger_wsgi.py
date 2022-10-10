# -*- coding: utf-8 -*-

import os, sys
from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
<<<<<<< HEAD
sys.path.insert(0, '/home/d/degtyarev/befreela/public_html/BeFreela/bizopt')
=======
sys.path.insert(0, '/home/d/degtyarev/befreela/public_html/bizopt')
>>>>>>> 0b07ab1 (optimised for beget)
=======
sys.path.insert(0, '/home/d/degtyarev/befreela/public_html/bizopt')
>>>>>>> 0b07ab1 (optimised for beget)
sys.path.insert(1, '/home/d/degtyarev/befreela/public_html/venv_django/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bizopt.settings'


application = get_wsgi_application()