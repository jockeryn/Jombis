from django.contrib import admin
from jombis.usuarios.models import *

class perfilAdmin(admin.ModelAdmin):
      list_display = ('user', 'genero')
      list_select_related = (True)
      select_related = ('user')
admin.site.register(UserPerfil, perfilAdmin)

