from django.forms import ModelForm
from django import forms
from Registration.models import User

class RecoverForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']
    
    def clean(self):
        cleaned_data = super(RecoverForm, self).clean()
        if 'email' in self.cleaned_data: 
            if not User.objects.filter(email=self.cleaned_data['email']):
                raise forms.ValidationError(("There is no account associated with that email."), code="doesntExist")
        
        return self.cleaned_data         
                
                
                
                
                
                
    