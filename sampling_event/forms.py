from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

from django.conf import settings
from django.db import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']