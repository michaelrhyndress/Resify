from django.db import models
from django.utils import timezone

from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

    
class UserManager(BaseUserManager):
    def create_user(self, email, accept_terms, first_name, last_name, password=None):#date_of_birth
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            accept_terms=accept_terms,
            first_name=first_name,
            last_name=last_name,
            # date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, accept_terms, first_name, last_name, password): #date_of_birth
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            accept_terms=accept_terms,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name=models.CharField(blank=True, max_length=35, default="")
    last_name=models.CharField(blank=True, max_length=35, default="")
    # date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)
    can_contact = models.BooleanField(default=True)
    accept_terms = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    passed_setup = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True, default=timezone.now())
    modified_date = models.DateField(auto_now=True, default=timezone.now())
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'accept_terms']#date_of_birth

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + " " +self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

        
@python_2_unicode_compatible
class Tag(models.Model):
    ''' Purpose is still up in the air... Maybe connect to Categories? '''
    name=models.CharField(max_length=50, unique=True)
    class Meta:
        verbose_name='tag'
        verbose_name_plural='tags'
        ordering = ['name']
    
    def __str__(self):
        return self.name
  
class Template(models.Model):
    template_name=models.CharField(max_length=50, unique=True, default="Template0")
    readable_name=models.CharField(max_length=50, default="", blank=True)
    is_public_template = models.BooleanField(default=False)
    class Meta:
        verbose_name='template'
        verbose_name_plural='templates'
        ordering = ['template_name']
    def __str__(self):
        return self.template_name
        
class User_Template(models.Model):
    user=models.OneToOneField(User)
    template_name=models.ForeignKey(Template)
    class Meta:
        verbose_name='user template'
        verbose_name_plural='user templates'
        ordering = ['user']
    def __str__(self):
        return self.user.email
    
class UserProfile(models.Model):
    user=models.OneToOneField(User)
    profession=models.CharField(max_length=50, blank=True, default="")
    handle=models.SlugField(max_length=25, blank=True, default="", unique=True)
    phone_number = models.CharField(max_length=30, blank=True, default="")
    statement = models.TextField(blank=True, default="")
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
        return self.user.email
        
class SocialMedia(models.Model):
    user=models.OneToOneField(User)
    facebook=models.URLField(max_length=200, blank=True, default="")
    twitter=models.URLField(max_length=200, blank=True, default="")
    gplus = models.URLField(max_length=200, blank=True, default="")
    linkedIn = models.URLField(max_length=200, blank=True, default="")
    class Meta:
        verbose_name='social media'
        verbose_name_plural='social media'
        ordering = ['user']
    def __str__(self):
        return self.user.email

class Job_History(models.Model):
    user = models.ForeignKey(User)
    position=models.CharField(max_length=50, blank=True, default="")
    company=models.CharField(max_length=50, blank=True, default="")
    job_from_date=models.CharField(max_length=4, blank=True, default="")
    job_to_date=models.CharField(max_length=7, blank=True, default="")
    job_about=models.TextField(blank=True, default="")
    class Meta:
        verbose_name='job history'
        verbose_name_plural='job history'
        ordering = ['-job_from_date']
    def __str__(self):
        return self.position
        
        
# class Skills(models.Model):
#     name=models.CharField(max_length=30, blank=True, unique=True, default="")
#     # percentage=models.PositiveSmallIntegerField(max_length=100)
#     class Meta:
#         verbose_name='skill'
#         verbose_name_plural='skills'
#         ordering = ['name']
#     def __str__(self):
#         return self.name
    
class User_Skills(models.Model):
    user = models.ForeignKey(User)
    skill = models.CharField(max_length=30, default="New Record")
    percentage=models.PositiveSmallIntegerField(max_length=100, default=0)
    class Meta:
        verbose_name='user skill'
        verbose_name_plural='user skills'
        ordering = ['-percentage']
    def __str__(self):
        return self.user.email
        
    
class Education_History(models.Model):
    user = models.ForeignKey(User)
    school=models.CharField(max_length=50, blank=True, default="")
    Status_Choices= (
        ('', ''),
        ('Graduated', 'Graduated'),
        ('Attending', 'Attending')
    )
    status = models.CharField(max_length=9, choices=Status_Choices, blank=True)
    Education_from_date=models.CharField(blank=True, max_length=4, default="")
    Education_to_date=models.CharField(blank=True, max_length=7, default="")
    degree=models.CharField(blank=True, max_length=100, default="")
    about=models.TextField(blank=True, default="")
    class Meta:
        verbose_name='education history'
        verbose_name_plural='education history'
        ordering = ['-Education_from_date']
    def __str__(self):
        return self.school
        
class Accomplishments(models.Model):
    user = models.ForeignKey(User)
    title=models.CharField(blank=True, max_length=50, default="")
    Accomplishment_from_date=models.CharField(blank=True, max_length=4, default="")
    Accomplishment_to_date=models.CharField(blank=True, max_length=7, default="")
    about=models.TextField(blank=True, default="")
    class Meta:
        verbose_name='accomplishment'
        verbose_name_plural='accomplishments'
        ordering = ['-Accomplishment_from_date']
    def __str__(self):
        return self.user.email
