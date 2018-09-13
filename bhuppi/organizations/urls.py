from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^create', views.create, name='create'),
    url(r'(?P<id>[0-9]+)',views.read, name='read')
]
