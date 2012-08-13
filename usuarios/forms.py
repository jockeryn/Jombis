from django import forms
class registroUsuario(forms.Form):
      username   = forms.CharField(max_length=20)
      first_name   = forms.CharField(max_length=50)
      last_name   = forms.CharField(max_length=50)
      email   = forms.EmailField(max_length=50)
      password = forms.CharField(max_length=25)