from django.forms import ModelForm
from django import forms
from Registration.models import User
# from django.dispatch import receiver


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2', 'accept_terms']
        #'is_public', 'can_contact'
        
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if not self.cleaned_data['first_name']:
            raise forms.ValidationError(("No name, no service!"), code="noName")
        
        if not self.cleaned_data['last_name']:
            raise forms.ValidationError(("First and Last name are required"), code="noFullName")
        
        if 'email' in self.cleaned_data: 
            if User.objects.filter(email=self.cleaned_data['email']):
                raise forms.ValidationError(("That Email address is already in use."), code="usedEmail")
            
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError(("Passwords do not match."), code="invalidPass")
        
        if not self.cleaned_data['accept_terms']:
            raise forms.ValidationError(("You must accept the terms and conditions"), code="noTerms")
            
        return self.cleaned_data
        
    def save(self, commit=True, user=None):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user                
    