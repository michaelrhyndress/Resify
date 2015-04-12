from django.forms import ModelForm
from django import forms
from ATS.models import Keyword
# from django.dispatch import receiver


class AddKeyword(ModelForm):
    word = forms.CharField()

    class Meta:
        model = Keyword
        fields = ['word']
                
                
    