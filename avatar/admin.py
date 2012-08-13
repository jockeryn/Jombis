from django.contrib import admin
from jombis.avatar.models import Avatar

class avatarAdmin(admin.ModelAdmin):
      list_display = ('user',)
      list_select_related = (True)
      select_related = ('user')
admin.site.register(Avatar, avatarAdmin)