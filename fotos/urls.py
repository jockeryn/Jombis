from django.conf.urls.defaults import patterns, url
from jombis.fotos.views import *

urlpatterns = patterns('fotos.views',		
    url(r'^addAlbum/$', addAlbum),
    url(r'^([A-Za-z]{1,15})/$', viewFotos),
    url(r'^$', viewFotos),
    url(r'^addFotos/([\d]{1,10})/$', addFotos),
    url(r'^album/([\d]{1,10})/$', viewAlbum),
    url(r'^album/([\d]{1,10})/$', viewAlbum),
    url(r'^album/([\d]{1,10})/([\d]{1,10})/$', viewFoto),
       
)
