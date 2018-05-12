from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerform(UserCreationForm):
    Email = forms.EmailField()
    class Meta:
        model = User
        # the 3 fields essential for user registration
        fields = ['username', 'Email', 'password1', 'password2']

class loginform(forms.Form):
    Username = forms.CharField(max_length = 250, error_messages = {'required': 'Username must not be blank'})
    Password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
