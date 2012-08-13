from django.contrib import admin
from jombis.fotos.models import *

class galeriaAdmin(admin.ModelAdmin):
      list_display = ('usuario', 'nombre', )
      list_select_related = (True)
admin.site.register(Album, galeriaAdmin)

class fotoAdmin(admin.ModelAdmin):
      list_display = ('album','title','is_cover_photo',)
      list_select_related = (True)
admin.site.register(Foto,fotoAdmin)