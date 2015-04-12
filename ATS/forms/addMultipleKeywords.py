from django import forms
from ATS.forms import AddKeyword

class AddMultipleKeywords(forms.Form):
    text_area = forms.CharField(label='Enter keywords with commas to seperate', widget=forms.Textarea)