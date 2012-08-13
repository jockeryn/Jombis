from django.db import models
from django.contrib.auth.models import User
from jombis.settings import *
from django.utils.translation import ugettext as _

GENEROS = (
        ('M', _('Masculino')),
        ('F', _('Femenino'))
          )

# Create your models here.
class UserPerfil(models.Model):
  user = models.OneToOneField(User)
  activation_key = models.CharField(max_length=40)
  key_expires = models.DateTimeField()
  genero = models.CharField(max_length=2, choices = GENEROS)
  nacimiento = models.DateField()
  webSite = models.URLField()
  intereses = models.TextField()
  def __unicode__(self):
    return self.user.username