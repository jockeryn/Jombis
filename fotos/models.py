#!/usr/bin/py
# -*- coding: utf-8 -*-
import datetime, os, sys
try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps

from django.core.files import File
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.hashcompat import md5_constructor
import unicodedata
from jombis.settings import DOMINIO
def emptext(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def avatar_file_path(instance, filename):
      try:
            username = instance.user.username
      except:
            username = 'jocky'
      return  os.sep.join(['fotos', username, md5_constructor(os.path.splitext(unicodedata.normalize ('NFKD',filename).encode('ASCII','ignore'))[0]).hexdigest()+os.path.splitext(filename)[1]])

def get(instance, filename=""):
      try:
            username = instance.user.username
      except:
            username = 'jocky'
      return  username

      

def seekuser(instance,filename):
      
      try:
            username = instance.user.username
      except:
            username = 'jocky'
      return  os.sep.join(['fotos', username, imagename+'tmb'+ext])

# Create your models here.
class Album(models.Model):
      usuario = models.ForeignKey(User)
      nombre = models.CharField(max_length=128)
      summary = models.TextField()
      date_created = models.DateTimeField(auto_now_add=True)
      date_modified = models.DateTimeField(auto_now=True)
      slug = models.SlugField()
    
      def __unicode__(self):
            return self.nombre
      
      def get_cover_photo(self):
            if self.foto_set.filter(is_cover_photo=True).count() > 0:
                  return self.foto_set.filter(is_cover_photo=True)[0]
            elif self.foto_set.all().count() > 0:
                  return self.foto_set.all()[0]
            else:
                  return 'imagenes/defaultCoverFoto.jpg'
      def contarFotos(self):
            return self.foto_set.count()

      def get_absolute_url(self):
            return '%sfotos/album/%s' %  (settings.DOMINIO, self.id)

      

          
class Foto(models.Model):
      album = models.ForeignKey(Album)
      title = models.CharField(max_length=250,
            help_text='Maximum 250 characters.')
      summary = models.TextField(blank=True,
            help_text='An optional summary.')
      summary_html = models.TextField(editable=False, blank=True)
      date = models.DateTimeField(default=datetime.datetime.now)
      image = models.ImageField(upload_to=avatar_file_path,
            help_text='Maximum resolution 800x600. Larger images will be resized.')
      thumb = models.ImageField(upload_to=avatar_file_path, editable=False)
      is_cover_photo = models.BooleanField()
      slug = models.SlugField()

            
      class Meta:
            ordering = ['-date']

      def __unicode__(self):
            return str(self.thumb)

      def get_image_filename(self):
            return avatar_file_path 

      def save(self, force_insert=False, force_update=False):
            import md5
            if self.is_cover_photo:
                  other_cover_photo = Foto.objects.filter(album=self.album).filter(is_cover_photo = True)
                  for photo in other_cover_photo:
                        photo.is_cover_photo = False
                        photo.save()
            if self.summary:
                  self.summary_html = self.summary
            super(Foto, self).save(force_insert, force_update)
            if self.image and not self.thumb:
                  # Set the thumbnail size and maximum size.
                  t_size = 150, 150
                  max_size = 750, 500
                  # Open the image that was uploaded.
                  im = Image.open(settings.MEDIA_ROOT + str(self.image))
                  if im.mode not in ("L", "RGB"):
                        im = im.convert("RGB")
                  # Compare the image size against the maximum size. If it is greater, the image will be resized.
                  if im.size > max_size:
                        # Using 'thumbnail', instead of 'resize', keeps the aspect ratio of the image.
                        im.thumbnail(max_size, Image.ANTIALIAS)
                        im.save(settings.MEDIA_ROOT + str(self.image))
                  # Create the thumbnail and save the path to the database.
                  im = ImageOps.fit(im, t_size, Image.ANTIALIAS)
                  im.save(settings.MEDIA_ROOT + os.path.splitext(str(self.image))[0] + "_tmb" + os.path.splitext(str(self.image))[1], "JPEG")
                  self.thumb = os.path.splitext(str(self.image))[0] +"_tmb" + os.path.splitext(str(self.image))[1]
                  super(Foto, self).save(force_insert, force_update)
      def get_absolute_url(self):
            return '%sfotos/album/%s/%s' %  (settings.DOMINIO, self.album.id, self.id)     

      def delete(self):
            filename = self.get_image_filename()
            try:
                  os.remove(self.get_medium_filename())
                  os.remove(self.get_small_filename())
            except:
                  pass
            super(Foto, self).delete()

      
          
