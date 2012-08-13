from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import *
from jombis.usuarios.forms import *
from avatar.models import Avatar
from django.core import validators


def getU(request, usern=''):
  if not usern:
    usern = request.user.username 
  userv = User.objects.get(username__exact = usern)
  avatars = userv.avatar_set.order_by("primary", "-date_uploaded")[:2]
  return avatars, userv

def inicio(request, usern=''):  
  if not request.user.is_authenticated():
    return render_to_response('portada.html', locals(), context_instance=RequestContext(request))
  else:
    avatars, userv = getU(request, usern)    
    return render_to_response('landing.html', locals(), context_instance=RequestContext(request))

def current_datetime(request,task=''):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})