from django.conf.urls.defaults import *
from jombis.views import *
from jombis.usuarios.views import *
from jombis.settings import *
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User

admin.autodiscover()
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
        url(r'^ruser/$', registrarUsuario),
        url(r'^ruser/([a-z]{1,10})/$', registrarUsuario),
        url(r'^admin/', include(admin.site.urls)),
	    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'e:/jombis/static/'}),
	    url(r'^login/$', autenticarUsuario),
        url(r'^logout/$',logoutView),
        url(r'^comments/', include('comments.urls')),
	    url(r'^avatar/', include('avatar.urls')),
        url(r'^fotos/', include('fotos.urls')),
	    url(r'perfil/', perfil),
        url(r'^([A-Za-z]{1,15})/$', perfil),
	    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}), 
        url(r'^$', inicio),


    # Examples:
    # url(r'^$', 'jombis.views.home', name='home'),
    # url(r'^jombis/', include('jombis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
