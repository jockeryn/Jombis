from django.forms import ModelForm
from jombis.fotos import models

class AlbumForm(ModelForm):
    class Meta:
        model = models.Album

class FotoForm(ModelForm):
    class Meta:
        model = models.Foto