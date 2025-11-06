"""
WSGI config for Django_Projects project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# add /home/raqeebcoder to sys.path (so manage.py and project are found)
project_home = '/home/raqeebcoder'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# also add specific project dir
project_dir = '/home/raqeebcoder/Django_Projects'
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Projects.settings')

# Activate the virtualenv (if activate_this.py exists)
activate_this = '/home/raqeebcoder/Django_Env/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

