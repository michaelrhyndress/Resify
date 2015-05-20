from django.contrib.auth.decorators import login_required
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User as django_User
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.template import RequestContext, Template, Context
from django.utils.timezone import now
from django.db.models import get_model

from Registration.forms import AuthenticationForm, RegistrationForm, UserForm
from Registration.models import Job_History, User, Education_History, Skills, User_Skills, SocialMedia
from Registration.models import Accomplishments, Template, UserProfile, User_Template, Tag
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
        if request.user.is_authenticated():
            return Homepage.as_view()(self.request)
        form = AuthenticationForm()
        return render_to_response('login.html', {
        'form': form,
    }, context_instance=RequestContext(request))
    
    
    
class Registration(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return Homepage.as_view()(self.request)
        form = RegistrationForm()
        return render_to_response('registration.html', {
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
                    return HttpResponseRedirect("/")
        #NOT VALID, SEND ERROR TO PAGE
        return render_to_response('registration.html', {
            'form': form,
        }, context_instance=RequestContext(request))

# class Recover(View):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated():
#             return Homepage.as_view()(self.request)
#         form = RecoverForm()
#         return render_to_response('recover.html', {
#                 'form': form,
#             }, context_instance=RequestContext(request))
#
#     def post(self, request, *args, **kwargs):
#         form = RecoverForm(data=request.POST)
#         if form.is_valid():
#             #CREATE RANDOM Send MAIL
#             return HttpResponseRedirect("passwordChange")
#         #NOT VALID, SEND ERROR TO PAGE
#         return render_to_response('registration.html', {
#             'form': form,
#         }, context_instance=RequestContext(request))
        
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
        #if logged in
        if request.user.is_authenticated():
            #Check if it is the right user
            if s_user.email == request.user.email:
                #render Resume
                return render(request, template, c)
        
        # Check if page is private
        if not s_user.is_public or not s_user.is_active:
            return render(request, 'private.html')
        
        #render Resume
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
            YEAR_CHOICES = []
            template_list = list(Template.objects.all())
        
            for r in xrange((now().year), 1979, -1):
                YEAR_CHOICES.append(r)
                
            if(request.user.passed_setup is False):
                #USER SETUP     
            
                c = {
                    'year_choices' : YEAR_CHOICES,
                    'template_list' : template_list,
                }
                return render(request, 'setup.html', c)#Setup form
            else: #User passed Setup
                s_user = get_object_or_404(User, email=request.user.email)
                job_list = list(Job_History.objects.filter(user__email=s_user.email))
                education_list = list(Education_History.objects.filter(user__email=s_user.email))
                skill_list = list(User_Skills.objects.filter(user__email=s_user.email))
                accomplishments_list =list(Accomplishments.objects.filter(user__email=s_user.email))
                socialMedia_list =list(SocialMedia.objects.filter(user__email=s_user.email))
                tag_list=list(Tag.objects.all())
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
                    'year_choices' : YEAR_CHOICES,
                    'template_list' : template_list,
                    'tag_list': tag_list,
                }
                return render(request, 'editResume.html', c)
                
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
                return render(request, 'setup.html', c)
        else:
            return redirect('/')
        
def checkURL(request):
    if request.user.is_authenticated():
        if request.is_ajax():
            handle = request.POST.get('handle', False)
            if handle:
                count = User.objects.filter(userprofile__handle=handle).count()
                if count != 0:
                    res = "1" #If it exists
                else:
                    res = "0" #If it DOES NOT exist
                return HttpResponse(res)
            else:
                return HttpResponse("")
        else:
            return HttpResponse("Failed")
            
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
        
def saveResume(request):
    if request.user.is_authenticated():
        if request.is_ajax():
            key = request.POST.get('key', None)
            value = request.POST.get('value', None)
            group = request.POST.get('sub', None) #sub key (ex. education -> school name)
            pk = request.POST.get('pk', None)
            option = request.POST.get('option', None)
            isSet=0

            print "Fieldname: " + key
            print "Content: " + value
            print "Group: " + group
            print "ID: " + pk
            print "Action: " + option 
            
            if group == "None":
                if key == "first_name":
                    if option == "update":
                        request.user.first_name=value
                        request.user.save()
                        isSet=-1
                        return HttpResponse(isSet)
    
                if key == "last_name":
                    if option == "update":
                        request.user.last_name=value
                        request.user.save()
                        isSet=-1
                        return HttpResponse(isSet)
        
                if key == "is_public":
                    if option == "update":
                        if value == "true":
                            request.user.is_public=True
                        else:
                            request.user.is_public=False
                        request.user.save()
                        isSet=-1
                        return HttpResponse(isSet)
                    
                #Template        
                if key == "template" and value:
                    template = User_Template.objects.get(user=request.user)
                    if option == "update":
                        TemplateObj = Template.objects.get(template_name=value)
                        template.template_name=TemplateObj
                        template.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
                #Profile    
                if key == "handle":
                    profile = UserProfile.objects.get(user=request.user)
                    if option == "update":
                        profile.handle=slugify(value)
                        profile.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
                    
                if key == "profession":
                    profile = UserProfile.objects.get(user=request.user)
                    if option == "update":
                        profile.profession=value
                        profile.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
                if key == "phone_number":
                    profile = UserProfile.objects.get(user=request.user)
                    if option == "update":
                        profile.phone_number=value
                        profile.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
                if key == "personal": #Statement
                    profile = UserProfile.objects.get(user=request.user)
                    if option == "update":
                        profile.statement=value
                        profile.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
                if key == "tags":
                    profile = UserProfile.objects.get(user=request.user)
                    if option == "add":
                        obj, created = Tag.objects.get_or_create(name=value.title())
                        # print profile.tags.filter(name=value).exists()
                        if value == "" or profile.tags.filter(name=value).exists():
                            return HttpResponse(isSet)
                        profile.tags.add(obj) #Add obj to profile
                        profile.save()
                        # obj = profile.tags.get(name=value) #get instance of saved object for id
                        isSet = obj.id
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
                    if option == "delete":
                        obj = profile.tags.get(pk=pk)
                        profile.tags.remove(obj)
                        profile.save()
                        request.user.modified_date=now()
                        request.user.save()
                        isSet=-1
                        return HttpResponse(isSet)
                        
                #SocialMedia
                if key == "facebook":
                    media = SocialMedia.objects.get(user=request.user)
                    if option == "update":
                        media.facebook=value
                        media.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
                if key == "twitter":
                    media = SocialMedia.objects.get(user=request.user)
                    if option == "update":
                        media.twitter=value
                        media.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
                if key == "gplus":
                    media = SocialMedia.objects.get(user=request.user)
                    if option == "update":
                        media.gplus=value
                        media.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
                if key == "linkedIn":
                    media = SocialMedia.objects.get(user=request.user)
                    if option == "update":
                        media.linkedIn=value
                        media.save()
                        isSet=-1
                        request.user.modified_date=now()
                        request.user.save()
                        return HttpResponse(isSet)
            
            # accordian groups            
            if group == "education":
                model = Education_History

            elif group == "experience":
                model = Job_History
                    
            elif group == "accomplishments":
                model = Accomplishments
                if key == "accomplishments_about": # Name override
                    key = "about"
                    
            elif group == "skills":
                model = User_Skills
                #override, add skill if doesn't exist. Link or remove.
                    
            else:
                return HttpResponse(isSet)
                    
            group_set = set(["education", "experience", "accomplishments", "skills"])
            
            if group in group_set:        
                #ambiguous options on these groups
                if option == "add":
                    obj = model.objects.create(user=request.user)
                    isSet = obj.id
                    request.user.modified_date=now()
                    request.user.save()
                    return HttpResponse(isSet)
            
                if option == "delete":
                    obj = model.objects.get(pk=pk, user=request.user)
                    obj.delete()
                    request.user.modified_date=now()
                    request.user.save()
                    isSet=-1
                    return HttpResponse(isSet)
                    
                if option == "update":
                    #do things to obj fields
                    obj = model.objects.get(pk=pk, user=request.user)
                    setattr(obj, key, value)
                    obj.save()
                    isSet=-1
                    request.user.modified_date=now()
                    request.user.save()
                    return HttpResponse(isSet)

        return HttpResponse(isSet)
        
    else: #Not Authenticated!!
        return HttpResponse(isSet) 
             
        
def slugify(s):
    """
    Simplifies ugly strings into something URL-friendly.

    """
    s = s.lower()
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '')
    s = re.sub('\W', '', s)
    s = s.replace('_', '')
    s = re.sub('\s+', ' ', s)
    s = s.strip()

 
    return s   
            
            