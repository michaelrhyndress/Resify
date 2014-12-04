from django.forms import ModelForm
from django import forms
from Registration.models import User, UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2', 'accept_terms']
        #'is_public', 'can_contact'
        
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords do not match.")
        return self.cleaned_data
        
    def save(self, commit=True, user=None):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
        
    # @receiver(post_save, sender=User)
    # def create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)