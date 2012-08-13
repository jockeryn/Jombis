from django.contrib import admin
from jombis.usuarios.models import usuario

     admin.site.register(usuario, AuthorAdmin)