from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'input', 'placeholder':'Enter Username'}))

  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'Enter Password'}))