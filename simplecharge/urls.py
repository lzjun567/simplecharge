from django.conf.urls import patterns, include, url
from django.conf import settings
from charge.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplecharge.views.home', name='home'),
    # url(r'^simplecharge/', include('simplecharge.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',index),
    url(r'^$',home),
    url(r'^index/stat/$',stat),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
)
