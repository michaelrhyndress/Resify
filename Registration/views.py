from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User as django_User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.template import RequestContext, Template, Context
from django.utils.timezone import now
from Registration.forms import AuthenticationForm, RegistrationForm, UserForm
from Registration.models import Job_History, User, Education_History, Skills, User_Skills, SocialMedia
from Registration.models import Accomplishments, Template
from Registration.forms import UserProfileForm, JobHistoryForm, EducationHistoryForm, AccomplishmentForm, SocialMediaForm, UserTemplateForm

import os, re, datetime

class Login(View):
    """
    Log in view
    """
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return HttpResponseRedirect("/")
        return render_to_response('login.html', {
            'form': form,
        }, context_instance=RequestContext(request))
    
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render_to_response('login.html', {
        'form': form,
    }, context_instance=RequestContext(request))
    
    
    
class Registration(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render_to_response('form.html', {
                'form': form,
            }, context_instance=RequestContext(request))
        
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    # return redirect(user.handle)
        return render_to_response('form.html', {
                    'form': form,
                }, context_instance=RequestContext(request))


class Resume(View):
    def get(self, request, handle):
        #get user
        s_user = get_object_or_404(User, userprofile__handle=handle)
        job_list = list(Job_History.objects.filter(user__email=s_user.email))
        education_list = list(Education_History.objects.filter(user__email=s_user.email))
        skill_list = list(User_Skills.objects.filter(user__email=s_user.email))
        accomplishments_list =list(Accomplishments.objects.filter(user__email=s_user.email))
        socialMedia_list =list(SocialMedia.objects.filter(user__email=s_user.email))
        #get user template
        template = str(s_user.user_template.template_name)
        template= os.path.join('Resumes',template,'index.html')
        
        #make context
        c = {
            's_user' : s_user,
            'job_list' : job_list,
            'education_list' : education_list,
            'parsed_phone_number' : re.sub(r'\W+', '', s_user.userprofile.phone_number),
            'skill_list' : skill_list,
            'accomp_list' : accomplishments_list,
            'social_list' : socialMedia_list,
        }
        
        if not s_user.is_public: # Check if page is private
            return render(request, 'private.html')
            
        return render(request, template, c)

        
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')
            
        return render(request, self.template_name, {'form': form})

class Homepage(View):
    def get(self, request, *args, **kwargs):
        # if user is logged in send them to logged in view
        if request.user.is_authenticated():
            if(request.user.passed_setup is False):
                #USER SETUP     
                YEAR_CHOICES = []
                template_list = list(Template.objects.all())
            
                for r in xrange((now().year), 1900, -1):
                    YEAR_CHOICES.append(r)
            
                c = {
                    'year_choices' : YEAR_CHOICES,
                    'template_list' : template_list,
                }
                return render(request, 'setup.html', c)#Setup form
            else:
                return render(request, 'editResume.html')
                
        # render homepage if not logged in
        else:
            return render(request, 'homepage.html')
        
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            all_valid = True
            #USER FORM
            user_instance = User.objects.get(email=request.user)
            user_instance.passed_setup = True
            #END USER FORM
            
            #PROFILE FORM
            profile_form = UserProfileForm(request.POST)
            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.user = User.objects.get(email=request.user)
            else:
                all_valid = False
            #END PROFILE FORM
            
            #JOB FORM
            job_form = JobHistoryForm(request.POST)
            if job_form.is_valid():
                job = job_form.save(commit=False)
                job.user = request.user
            else:
                all_valid = False
            #END JOB FORM
            
            #EDUCATION FORM
            education_form = EducationHistoryForm(request.POST)
            if education_form.is_valid():
                education = education_form.save(commit=False)
                education.user = request.user
            else:
                all_valid = False
            #END EDUCATION FORM
            
            #ACCOMPLISHMENT FORM
            accomplishment_form = AccomplishmentForm(request.POST)
            if accomplishment_form.is_valid():
                accomplishment = accomplishment_form.save(commit=False)
                accomplishment.user = request.user
            else:
                all_valid = False
            #END ACCOMPLISHMENT FORM
            
            #SOCIAL MEDIA FORM
            social_form = SocialMediaForm(request.POST)
            if social_form.is_valid():
                social = social_form.save(commit=False)
                social.user = request.user
            else:
                all_valid = False
            #SOCIAL MEDIA FORM
            
            #User Template FORM
            template_form = UserTemplateForm(request.POST)
            if template_form.is_valid():
                template = template_form.save(commit=False)
                template.user = request.user
                template.template_name = Template.objects.get(template_name=request.POST['template_name'])
            else:
                all_valid = False
            #User Template FORM
            
            
            if all_valid is True:
                profile.save() # save user profile form
                job.save() # save job form
                education.save() # save education form
                accomplishment.save() # save education form
                social.save() # save social media
                template.save() # save social media
                user_instance.save() #change setup to True
                return redirect('/')
                
            if all_valid is False:
                YEAR_CHOICES = []
                template_list = list(Template.objects.all())
            
                for r in xrange((now().year), 1900, -1):
                    YEAR_CHOICES.append(r)
            
                c = {
                    'year_choices' : YEAR_CHOICES,
                    'template_list' : template_list,
                    'profile_form' : profile_form,
                    'job_form' : job_form,
                    'education_form' : education_form,
                    'accomplishment_form' : accomplishment_form,
                    'social_form' : social_form,
                    'template_form' : template_form,
                }
                print(profile_form.errors)
                print(job_form.errors)
                print(education_form.errors)
                print(accomplishment_form.errors)
                print(social_form.errors)
                print(template_form.errors)
                return render(request, 'setup.html', c)
        else:
            return redirect('/')
        
        
def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('/')
    
def skipSetup(request):
     if request.user.is_authenticated():
         if(request.user.passed_tutorial):
             return redirect('/')
         else:
             request.user.passed_tutorial=True
             request.user.save()
             return redirect('/')
        
        