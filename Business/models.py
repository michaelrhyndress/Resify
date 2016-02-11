from uuid import uuid1
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from localflavor.us.models import USStateField
from localflavor.us.us_states import STATE_CHOICES
from Registration.models import User
from json import loads
import urllib2
from urllib import quote

class BusinessGroup(models.Model):
    #AIzaSyDZk31ooSQwpdxYExUASXHv3OmKQtpn_Iw
    # Add Logo
    # uuid = uuid1().hex
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.EmailField(
        verbose_name='Owner',
        max_length=255,
    )
    name = models.CharField(verbose_name='Business name',blank=False, max_length=255)
    corporation = models.CharField(verbose_name='Corporation', max_length=100, blank=True)
    departement = models.CharField(verbose_name='Departement', max_length=50, blank=True)
    phone_number = models.CharField(verbose_name='Phone number',max_length=30, blank=True)
    description = models.TextField(verbose_name='Description',default="Description Not Available")
    website = models.URLField(verbose_name='Website',blank=True)
    #Location info
    building = models.CharField(verbose_name='Building', max_length=20, blank=True)
    floor = models.CharField(verbose_name='Floor', max_length=20, blank=True)
    door = models.CharField(verbose_name='Door', max_length=20, blank=True)
    number = models.CharField(verbose_name='Number', max_length=30, blank=True)
    street_line1 = models.CharField(verbose_name='Address 1', max_length=100)
    street_line2 = models.CharField(verbose_name='Address 2', max_length=100, blank=True)
    city = models.CharField(verbose_name='City', max_length=100)  # Bentley
    state = USStateField(verbose_name='State',choices=STATE_CHOICES)
    country = models.CharField(verbose_name='Country', max_length=100, default="USA") # US
    postal_box = models.CharField(verbose_name='Postal box', max_length=20, blank=True)
    zipcode = models.CharField(verbose_name='ZIP code', max_length=5)
    
    # gmaps = GoogleMaps(api_key)
    # address = 'Constitution Ave NW & 10th St NW, Washington, DC'
    # lat, lng = gmaps.address_to_latlng(address)
    # print lat, lng
    # When this saves get lat and long
    lat = models.FloatField(verbose_name='Latitude', blank=True, null=True)
    lon = models.FloatField(verbose_name='Longitude', blank=True, null=True)

    #Account control
    members = models.ManyToManyField(User, blank=True, related_name='Members')
    banned = models.ManyToManyField(User, blank=True, related_name='Banned')
    subscribed = models.ManyToManyField(User, blank=True, related_name='Subscribed')
    
    #Times
    created_date = models.DateField(verbose_name='Date created', auto_now_add=True, default=timezone.now())
    deleted_date = models.DateField(verbose_name='Date deleted', blank=True, null=True)
    
    #boolean
    is_active = models.BooleanField(verbose_name='Is active', default=True)
    is_locked = models.BooleanField(verbose_name='Is locked', default=False) #In case of report
    
    def __str__(self):
        return '%s' % " ".join((self.name, self.corporation, self.departement)).encode('utf-8').strip()
        
    def save(self, *args, **kw):
        if self.pk is not None: # update on save and fields changed
            orig = BusinessGroup.objects.get(pk=self.pk)
            changed_street = (orig.street_line1 != self.street_line1)
            changed_city = (orig.city != self.city)
            changed_state = (orig.state != self.state)
            changed_zip = (orig.zipcode != self.zipcode)
            if changed_street or changed_city or changed_state or changed_zip:
                address="%s,%s,%s %s" % (self.street_line1, self.city, self.state, self.zipcode)
                url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % quote(address)
                response = urllib2.urlopen(url)
                jsongeocode = response.read()
                parsed_data=loads(jsongeocode)
                if parsed_data['status'] == "OK":
                    self.lat = parsed_data['results'][0]['geometry']['location']['lat']
                    self.lon = parsed_data['results'][0]['geometry']['location']['lng']
        else: # first save
            address="%s,%s,%s %s" % (self.street_line1, self.city, self.state, self.zipcode)
            url="https://maps.googleapis.com/maps/api/geocode/json?address=%s" % quote(address)
            response = urllib2.urlopen(url)
            jsongeocode = response.read()
            parsed_data=loads(jsongeocode)
            if parsed_data['status'] == "OK":
                self.lat = parsed_data['results'][0]['geometry']['location']['lat']
                self.lon = parsed_data['results'][0]['geometry']['location']['lng']
            
                
        super(BusinessGroup, self).save(*args, **kw)