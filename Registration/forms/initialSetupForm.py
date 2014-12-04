from django.forms import ModelForm
from django import forms
from Registration.models import User, UserProfile, Job_History
from Registration.models import Education_History, Accomplishments, SocialMedia, User_Template


class UserForm(ModelForm):    
    class Meta:
        model = User
        # fields = ['email', 'first_name', 'last_name', 'passed_setup']
        exclude = ("passed_setup",)
        

class UserProfileForm(ModelForm):    
    class Meta:
        model = UserProfile
        exclude = ("user", "tags",)

class JobHistoryForm(ModelForm):    
    class Meta:
        model = Job_History
        # fields = ['position', 'company', 'job_from_date', 'job_to_date', 'job_about']
        exclude = ("user",)
    
        
class EducationHistoryForm(ModelForm):    
    class Meta:
        model = Education_History
        # fields = ['school', 'status', 'Education_from_date', 'Education_to_date', 'degree', 'about']
        exclude = ("user",)
        
        
class AccomplishmentForm(ModelForm):    
    class Meta:
        model = Accomplishments
        # fields = ['title', 'Accomplishment_from_date', 'Accomplishment_to_date', 'about']
        exclude = ("user",)

        
class SocialMediaForm(ModelForm):    
    class Meta:
        model = SocialMedia
        # fields = ['facebook', 'twitter', 'gplus']
        exclude = ("user",)

class UserTemplateForm(ModelForm):    
    class Meta:
        model = User_Template
        exclude = ("user", "template_name",)
        
        