from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

from django.conf import settings
from django.db import models
from models import SampleType


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']



class multiSample(forms.Form):
    samples = forms.IntegerField()
    #for type in SampleType.objects.all():

    #wipes = forms.IntegerField()
    #swabs = forms.IntegerField()
    #air = forms.IntegerField()
    #pos = forms.IntegerField(label="positive control")
    #neg = forms.IntegerField(label= "negative control")


