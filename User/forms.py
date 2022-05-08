from dataclasses import field
import email
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')
