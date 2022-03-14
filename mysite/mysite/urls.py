import os
from django.contrib import admin
# from django.conf.urls import url
from django.urls import include, path
from django.urls import re_path as url  # <-- Django 4 version of dango.conf.urls
from django.views.static import serve
from django.views.generic.base import TemplateView

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),                                                                                           
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),


]
