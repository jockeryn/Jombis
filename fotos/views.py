from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from jombis.fotos.forms import *
from jombis.fotos.models import *
from jombis.views import getU
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import defaultfilters

def getU(request, usern=''):
  if not usern:
    usern = request.user.username 
  userv = User.objects.get(username__exact = usern)
  avatars = userv.avatar_set.order_by("primary", "-date_uploaded")[:2]
  return avatars, userv

@login_required
def viewFotos(request, usern=''):
	avatars, userv = getU(request, usern)
	try:
		album = Album.objects.filter(usuario=userv.id)
	except:
		pass
	return render_to_response('fotos/viewFotos.html',locals(),context_instance=RequestContext(request))

@login_required
def addAlbum(request):
	if request.method == 'POST':
		form = AlbumForm(request.POST)
		p = Album(usuario_id = request.user.id, slug = defaultfilters.slugify(request.POST['nombre']), nombre = request.POST['nombre'], summary = request.POST['summary'])
		p.save()
		return HttpResponseRedirect('/fotos/addFotos/%s' % p.id)
	else:
		form = AlbumForm()
		avatars, userv = getU(request)
		return render_to_response('fotos/addAlbum.html',locals(),context_instance=RequestContext(request))

@login_required
def addFotos(request, album=""):
	if request.method == 'POST':
		form = FotoForm(request.POST)
		for f in request.FILES.getlist(u'image[]'):
			f = Foto(album_id='1', title=str(f), image = f, slug = defaultfilters.slugify(f))
			f.save()
		return HttpResponseRedirect('/fotos/album/%s' % album)
	else:
		form = FotoForm()
		avatars, userv = getU(request)
		return render_to_response('fotos/addFotos.html', locals(),context_instance=RequestContext(request))

@login_required
def viewAlbum(request,album):
	avatars, userv = getU(request)
	fotos, album = Foto.objects.filter(album=album), Album.objects.get(id=album)
	return render_to_response('fotos/viewAlbum.html', locals(),context_instance=RequestContext(request))


def viewFoto(request, album, foto):
	avatars, userv = getU(request)
	fotos, foto, album =  Foto.objects.filter(album=album), Foto.objects.get(pk=foto), Album.objects.get(id=album)
	return render_to_response('fotos/viewFoto.html', locals(),context_instance=RequestContext(request))



	