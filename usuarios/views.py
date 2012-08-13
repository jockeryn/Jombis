from django.shortcuts import *
from django.utils import simplejson
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.template import RequestContext
from django.contrib.auth.models import User
from jombis.usuarios.forms import *
from django.core import validators
import datetime, random, sha
from django.core.mail import send_mail
from usuarios.models import UserPerfil
from django.contrib.auth.decorators import *
from jombis.views import getU
from django.contrib.auth import authenticate, login, logout
# Create your views here.
# VISTAS
def registrarUsuario(request, task=''):
    redirects = 0
    err=""
    if task == "":
       if request.method == 'POST': # If the form has been submitted...
          user = User.objects.create_user(
          request.POST['username'],
          request.POST['email'],
          request.POST['password'])
          user.first_name = request.POST['first_name']
          user.last_name = request.POST['last_name']
          user.is_active = 0
          user.save()
          salt = sha.new(str(random.random())).hexdigest()[:5]
          activation_keys = sha.new(salt+request.POST['username']).hexdigest()
          key_expiress = datetime.datetime.today() + datetime.timedelta(2)
          p = UserPerfil(user_id=user.id, genero=request.POST['genero'], activation_key=activation_keys, key_expires=key_expiress)
          p.save()
          redirects = 1
    elif task=="chkusr":
         if request.is_ajax():
            err=_('usuario ya existe singup')
            try:
                User.objects.get(username=request.POST['username'])
            except User.DoesNotExist:
                   err=""
    elif task=="chkemail":
         if request.is_ajax():
            err = _('correo ya existe singup')
            try:
                User.objects.get(email=request.POST['email'])
            except User.DoesNotExist:
                   err=""
    if redirects == 1:
       	return render_to_response('default.html',
	{'message': _("mensaje bienvenida post registro")},
	context_instance=RequestContext(request))
    else:
         return HttpResponse(err)

def autenticarUsuario(request):
    if request.method == 'POST':
       usernamel = request.POST['username']
       password = request.POST['password']
       try:
           user = User.objects.get(email=usernamel)
           usernamel = user.username
       except User.DoesNotExist:
              usernamel = request.POST['username']
       user = authenticate(username=usernamel, password=password)
       if user is not None:
          if user.is_active:
             try:
                 user.get_profile()
             except:
                    p = UserPerfil(user_id=user.id, genero='', activation_key='', key_expires=datetime.datetime.today(), nacimiento=datetime.datetime.today(), )
                    p.save()
             login(request, user)
             return redirect('/')
          else:
               return render_to_response('default.html',
	       {'message': _("esta cuenta no ha sido desactivada.")},
	       context_instance=RequestContext(request))
       else:
             return render_to_response('loginFrm.html', {'message': _('Los datos que ingresaste con coinsiden con ninguna cuenta en jombis.')}, context_instance=RequestContext(request))
    else:
         return render_to_response('loginFrm.html', context_instance=RequestContext(request))

def logoutView(request):
  logout(request)
  return HttpResponseRedirect('/')

@login_required
def landing(request):
    return render_to_response('portada.html',
    {'message': _("Bienvenidos a Jombis"),
    },
    context_instance=RequestContext(request))

@login_required
def perfil(request, usern=""):
  avatars, userv = getU(request, usern)
  return render_to_response('landing.html',locals(),context_instance=RequestContext(request))
