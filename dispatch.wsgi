import os, sys
sys.path.append("/home1/songzhen/public_html/spiritwine");
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['PYTHON_EGG_CACHE'] = '/home1/songzhen/.python_egg_cache'
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)