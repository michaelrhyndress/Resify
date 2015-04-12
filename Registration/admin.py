from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from Registration.models import User, UserProfile, Tag, Template, User_Template, Education_History
from Registration.models import Skills, User_Skills, Job_History, Accomplishments, SocialMedia

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'accept_terms',) #date_of_birth

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_public', 'can_contact', 'is_active', 'is_admin', 'accept_terms') #date_of_birth

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'last_name', 'last_login', 'is_public', 'can_contact' , 'is_admin', 'accept_terms',) #date_of_birth 
    list_filter = ('is_admin', 'is_public', 'accept_terms')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
        # ('Personal info', {'fields': ('date_of_birth',)}),
        ('Settings', {'fields': ('is_public', 'can_contact')}),
        ('Permissions', {'fields': ('is_admin', 'accept_terms', 'passed_setup',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'accept_terms',)} #'date_of_birth'
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    
class UserProfileAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

    
# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Tag)
admin.site.register(Template)
admin.site.register(Education_History)
admin.site.register(Job_History)
admin.site.register(Accomplishments)
admin.site.register(Skills)
admin.site.register(User_Skills)
admin.site.register(User_Template)
admin.site.register(SocialMedia)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)