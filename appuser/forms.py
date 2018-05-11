from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class registerform(UserCreationForm):
    Email = forms.EmailField()
    class Meta:
        model = User
        # the 3 fields essential for user registration
        fields = ['username', 'Email', 'password1', 'password2']
