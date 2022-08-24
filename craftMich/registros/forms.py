from dataclasses import fields
from socket import fromshare
from django import forms
from .models import Opinion

from django.forms import ModelForm, ClearableFileInput




class OpinionForm(forms.ModelForm):
    class Meta:
        model=Opinion
        fields=['usuario','comentario']